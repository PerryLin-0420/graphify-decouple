"""state_affinity — cross-language self/this-attribute usage analysis.

decouple.py's community-based grouping only sees the CALL graph (who calls
whom). Two methods can look unrelated there and still share a pile of the
same `self.` instance state — split them into separate classes and the
state has to go somewhere: a shared "context" object, a back-reference to
the original class, or duplicated fields. The split then doesn't reduce
coupling, it relocates it. This module answers the question the call graph
can't: how much INSTANCE STATE would two proposed groups actually share?

Approach: re-parse the god node's own source file directly with tree-sitter
(bypassing graphify's extraction pipeline and its cached graph entirely —
this needs exact per-method attribute access, which graphify's AST tier
does not record for any language; see decouple.py's module docstring) and
walk each method's body for `self`/`this`-style attribute access. Read vs.
write is NOT distinguished — "does this method touch this attribute" is
sufficient for a cohesion/overlap signal, and collapsing the distinction
avoids needing a verified assignment-LHS shape for every grammar (the part
most likely to be silently wrong).

Coverage: the 11 OOP languages graphify already ships tree-sitter grammars
for as mandatory dependencies (pyproject.toml) — every node type and field
name below was verified empirically against the installed grammars, not
guessed from documentation. Go is supported via per-method receiver name
resolution (`func (f *Foo) M()` — "f" is resolved fresh for each method,
there is no fixed keyword). C is explicitly NOT supported: a struct-pointer
parameter is not syntactically distinguishable from any other parameter, so
there is no reliable signal to key off without full type inference.
Anything else (source_file extension not in `EXT_LANG`) is also skipped.
Every caller-facing function returns `None` on any of this — a skip, never
a wrong-looking answer.
"""
from __future__ import annotations

import importlib
from pathlib import Path
from typing import Any

# ---- language detection -----------------------------------------------

EXT_LANG: dict[str, str] = {
    ".py": "python",
    ".js": "javascript", ".jsx": "javascript", ".mjs": "javascript", ".cjs": "javascript",
    ".ts": "typescript", ".mts": "typescript", ".cts": "typescript",
    ".tsx": "tsx",
    ".java": "java",
    ".cs": "csharp",
    ".rs": "rust",
    ".rb": "ruby", ".rake": "ruby",
    ".php": "php",
    ".swift": "swift",
    ".kt": "kotlin", ".kts": "kotlin",
    ".cpp": "cpp", ".cc": "cpp", ".cxx": "cpp", ".hpp": "cpp",
    ".go": "go",
}

# language -> (tree-sitter grammar module, attribute on it returning the
# Language capsule). Verified empirically: TypeScript/TSX and PHP are the
# only ones whose language function isn't plain "language".
_TS_LOADER: dict[str, tuple[str, str]] = {
    "python": ("tree_sitter_python", "language"),
    "javascript": ("tree_sitter_javascript", "language"),
    "typescript": ("tree_sitter_typescript", "language_typescript"),
    "tsx": ("tree_sitter_typescript", "language_tsx"),
    "java": ("tree_sitter_java", "language"),
    "csharp": ("tree_sitter_c_sharp", "language"),
    "rust": ("tree_sitter_rust", "language"),
    "ruby": ("tree_sitter_ruby", "language"),
    "php": ("tree_sitter_php", "language_php"),
    "swift": ("tree_sitter_swift", "language"),
    "kotlin": ("tree_sitter_kotlin", "language"),
    "cpp": ("tree_sitter_cpp", "language"),
    "go": ("tree_sitter_go", "language"),
}

_CLASS_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"class_definition"}),
    "javascript": frozenset({"class_declaration"}),
    "typescript": frozenset({"class_declaration"}),
    "tsx": frozenset({"class_declaration"}),
    "java": frozenset({"class_declaration"}),
    "csharp": frozenset({"class_declaration"}),
    "rust": frozenset({"impl_item"}),
    "ruby": frozenset({"class"}),
    "php": frozenset({"class_declaration"}),
    "swift": frozenset({"class_declaration"}),
    "kotlin": frozenset({"class_declaration"}),
    "cpp": frozenset({"class_specifier"}),
}

_FUNCTION_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"function_definition"}),
    "javascript": frozenset({"method_definition", "function_declaration"}),
    "typescript": frozenset({"method_definition", "function_declaration"}),
    "tsx": frozenset({"method_definition", "function_declaration"}),
    "java": frozenset({"method_declaration"}),
    "csharp": frozenset({"method_declaration"}),
    "rust": frozenset({"function_item"}),
    "ruby": frozenset({"method"}),
    "php": frozenset({"method_declaration"}),
    "swift": frozenset({"function_declaration"}),
    "kotlin": frozenset({"function_declaration"}),
    "cpp": frozenset({"function_definition"}),
    "go": frozenset({"method_declaration"}),
}

# Node types meaning "some kind of member/attribute access" per language.
_ACCESS_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"attribute"}),
    "javascript": frozenset({"member_expression"}),
    "typescript": frozenset({"member_expression"}),
    "tsx": frozenset({"member_expression"}),
    "java": frozenset({"field_access"}),
    "csharp": frozenset({"member_access_expression"}),
    "rust": frozenset({"field_expression"}),
    "ruby": frozenset({"instance_variable"}),
    "php": frozenset({"member_access_expression"}),
    "swift": frozenset({"navigation_expression"}),
    "kotlin": frozenset({"navigation_expression"}),
    "cpp": frozenset({"field_expression"}),
    "go": frozenset({"selector_expression"}),
}

UNSUPPORTED_LANGUAGE_NOTE = {
    "c": "C has no class/self concept — a struct-pointer parameter is not "
         "syntactically distinguishable from any other parameter, so there is "
         "no reliable receiver signal without full type inference.",
}


def _text(node, source: bytes) -> str:
    return source[node.start_byte:node.end_byte].decode("utf-8", "replace")


def _load_tree_sitter_language(lang: str):
    mod_name, fn_name = _TS_LOADER[lang]
    from tree_sitter import Language
    mod = importlib.import_module(mod_name)
    return Language(getattr(mod, fn_name)())


def parse_source(lang: str, source: bytes):
    """Parse `source` with the tree-sitter grammar for `lang`. Raises
    ImportError if the grammar package isn't installed (it is a mandatory
    graphify dependency for every language in `_TS_LOADER`, so this should
    only fire in a stripped-down install)."""
    from tree_sitter import Parser
    language = _load_tree_sitter_language(lang)
    parser = Parser(language)
    return parser.parse(source)


def _extract_attr_name(lang: str, node, source: bytes, receiver_name: str | None) -> str | None:
    """Return the attribute name if `node` is a self/this-style access,
    else None. One small branch per language — field names and node types
    below were verified against the actual installed grammars, not guessed."""
    if lang == "python":
        obj = node.child_by_field_name("object")
        attr = node.child_by_field_name("attribute")
        if obj is not None and obj.type == "identifier" and _text(obj, source) in ("self", "cls") and attr is not None:
            return _text(attr, source)
        return None
    if lang in ("javascript", "typescript", "tsx"):
        obj = node.child_by_field_name("object")
        prop = node.child_by_field_name("property")
        if obj is not None and obj.type == "this" and prop is not None:
            return _text(prop, source)
        return None
    if lang == "java":
        obj = node.child_by_field_name("object")
        field = node.child_by_field_name("field")
        if obj is not None and obj.type == "this" and field is not None:
            return _text(field, source)
        return None
    if lang == "csharp":
        obj = node.child_by_field_name("expression")
        name = node.child_by_field_name("name")
        if obj is not None and obj.type in ("this", "this_expression") and name is not None:
            return _text(name, source)
        return None
    if lang == "rust":
        value = node.child_by_field_name("value")
        field = node.child_by_field_name("field")
        if value is not None and value.type == "self" and field is not None:
            return _text(field, source)
        return None
    if lang == "ruby":
        # The node IS the instance variable, e.g. "@x" — no receiver to check.
        # This is Ruby's dominant field-access idiom; `self.foo` is a method
        # call (often a generated attr_accessor), not a guaranteed raw field,
        # so it is deliberately not treated as an attribute access here.
        text = _text(node, source)
        return text[1:] if text.startswith("@") and len(text) > 1 else None
    if lang == "php":
        obj = node.child_by_field_name("object")
        name = node.child_by_field_name("name")
        if obj is not None and obj.type == "variable_name" and _text(obj, source) == "$this" and name is not None:
            return _text(name, source)
        return None
    if lang == "swift":
        target = node.child_by_field_name("target")
        suffix = node.child_by_field_name("suffix")
        if target is not None and target.type == "self_expression" and suffix is not None:
            inner = suffix.child_by_field_name("suffix")
            if inner is not None:
                return _text(inner, source)
        return None
    if lang == "kotlin":
        # navigation_expression has no named fields in this grammar — use
        # position: [this_expression, '.', identifier].
        children = node.children
        if len(children) >= 3 and children[0].type == "this_expression":
            tail = children[-1]
            if tail.is_named:
                return _text(tail, source)
        return None
    if lang == "cpp":
        arg = node.child_by_field_name("argument")
        field = node.child_by_field_name("field")
        if arg is not None and arg.type == "this" and field is not None:
            return _text(field, source)
        return None
    if lang == "go":
        if not receiver_name:
            return None
        operand = node.child_by_field_name("operand")
        field = node.child_by_field_name("field")
        if operand is not None and operand.type == "identifier" and _text(operand, source) == receiver_name and field is not None:
            return _text(field, source)
        return None
    return None


def _go_receiver_name(method_node, source: bytes) -> str | None:
    """`func (f *Foo) M()` -> "f". Go has no `self`/`this` keyword; the
    receiver is an arbitrarily-named parameter resolved fresh per method."""
    receiver = method_node.child_by_field_name("receiver")
    if receiver is None:
        return None
    for child in receiver.children:
        if child.type == "parameter_declaration":
            name = child.child_by_field_name("name")
            if name is not None:
                return _text(name, source)
    return None


def _go_receiver_type(method_node, source: bytes) -> str | None:
    """`func (f *Foo) M()` -> "Foo". Go methods aren't nested inside a class
    node at all — they're package-level `method_declaration`s whose receiver
    TYPE is the only thing tying them to "Foo", so this replaces class-name
    matching for Go specifically."""
    receiver = method_node.child_by_field_name("receiver")
    if receiver is None:
        return None
    for child in receiver.children:
        if child.type != "parameter_declaration":
            continue
        type_node = child.child_by_field_name("type")
        if type_node is None:
            return None
        if type_node.type == "pointer_type":
            for c in type_node.children:
                if c.is_named:
                    return _text(c, source)
            return None
        if type_node.type == "type_identifier":
            return _text(type_node, source)
        return None
    return None


def _find_named(node, types: frozenset[str], name_fn) -> "Any | None":
    """First descendant of `node` matching `types` whose name (via
    `name_fn`) matches — does not descend past a match (no nested classes
    with the same name confusion)."""
    for child in node.children:
        if child.type in types:
            return child
        found = _find_named(child, types, name_fn)
        if found is not None:
            return found
    return None


def _class_name(lang: str, class_node, source: bytes) -> str | None:
    if lang == "rust":
        # impl_item's own name is the TYPE it implements, in field "type".
        type_node = class_node.child_by_field_name("type")
        return _text(type_node, source) if type_node is not None else None
    name_node = class_node.child_by_field_name("name")
    return _text(name_node, source) if name_node is not None else None


def _function_name(lang: str, fn_node, source: bytes) -> str | None:
    name_node = fn_node.child_by_field_name("name")
    return _text(name_node, source) if name_node is not None else None


def extract_method_attribute_usage(
    source_file: "str | Path",
    class_label: str,
    method_names: "list[str]",
) -> "dict[str, set[str]] | None":
    """Return `{method_name: {attr_names touched}}` for the methods in
    `method_names` (bare names, no leading "." or trailing "()") that
    belong to the class named `class_label` in `source_file`.

    Returns None (a skip, not an error) when: the extension isn't a
    supported language, the file can't be read, the class isn't found, or
    the grammar package is missing. A method in `method_names` not found in
    the class is simply absent from the result — never raises.
    """
    path = Path(source_file)
    lang = EXT_LANG.get(path.suffix.lower())
    if lang is None:
        return None
    try:
        source = path.read_bytes()
    except OSError:
        return None
    try:
        tree = parse_source(lang, source)
    except ImportError:
        return None
    except Exception:
        return None

    function_types = _FUNCTION_TYPES.get(lang)
    access_types = _ACCESS_TYPES.get(lang)
    if not function_types or not access_types:
        return None

    target_names = {n.lstrip(".").rstrip("()") for n in method_names}
    result: dict[str, set[str]] = {}

    def walk_method(method_node, receiver_name: "str | None") -> set[str]:
        touched: set[str] = set()

        def visit(node) -> None:
            if node.type in access_types:
                attr = _extract_attr_name(lang, node, source, receiver_name)
                if attr:
                    touched.add(attr)
            for child in node.children:
                visit(child)

        visit(method_node)
        return touched

    if lang == "go":
        # No class node at all — package-level method_declarations, tied to
        # "Foo" only via their own receiver TYPE (see _go_receiver_type).
        def scan_go(node) -> None:
            for child in node.children:
                if child.type in function_types:
                    if _go_receiver_type(child, source) == class_label:
                        fname = _function_name("go", child, source)
                        if fname in target_names:
                            result[fname] = walk_method(child, _go_receiver_name(child, source))
                    continue
                scan_go(child)

        scan_go(tree.root_node)
        return result if result else None

    class_types = _CLASS_TYPES.get(lang)
    if not class_types:
        return None

    def visit_class(node) -> None:
        for child in node.children:
            if child.type in class_types:
                if _class_name(lang, child, source) == class_label:
                    collect_methods(child)
                else:
                    visit_class(child)  # keep looking (nested/other classes)
            else:
                visit_class(child)

    def collect_methods(class_node) -> None:
        stack = [class_node]
        while stack:
            node = stack.pop()
            if node is not class_node and node.type in class_types:
                continue  # don't descend into a nested class's own methods
            if node.type in function_types:
                fname = _function_name(lang, node, source)
                if fname in target_names:
                    result[fname] = walk_method(node, None)
                continue  # a method body isn't itself walked for nested classes
            stack.extend(node.children)

    visit_class(tree.root_node)
    return result if result else None


def state_overlap(
    usage: "dict[str, set[str]]",
    members_a: "list[str]",
    members_b: "list[str]",
) -> "dict[str, Any] | None":
    """Jaccard overlap between the UNION of attributes group A's methods
    touch and group B's — high overlap means both proposed classes would
    need the same instance state, i.e. the split is likely cosmetic."""
    def strip(n: str) -> str:
        return n.lstrip(".").rstrip("()")

    attrs_a: set[str] = set()
    for m in members_a:
        attrs_a |= usage.get(strip(m), set())
    attrs_b: set[str] = set()
    for m in members_b:
        attrs_b |= usage.get(strip(m), set())
    if not attrs_a and not attrs_b:
        return None
    shared = attrs_a & attrs_b
    union = attrs_a | attrs_b
    overlap = len(shared) / len(union) if union else 0.0
    return {"overlap": round(overlap, 3), "shared_attrs": sorted(shared)}
