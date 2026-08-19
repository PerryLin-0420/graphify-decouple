"""tool_dedup — corpus-wide near-duplicate function/method detector.

decouple.py's `node_role` (see `_classify_node_role`) can tell you a
function is ALREADY a single shared implementation (the "tool_function"
role — many callers, one definition). It cannot tell you the opposite and
arguably more common case: the same logic reimplemented independently in
several places, none of which is a god node (each copy is called from just
one or two sites, so it never shows up in `analyze.god_nodes`'s degree-based
top-N at all). This module finds THOSE — candidates for consolidating into
one shared utility.

Signature per function: `{param_count, calls}`, where `calls` is the set of
bare callee names used in the body (`os.path.join(...)` contributes "join").
This is a STRUCTURAL proxy, not semantic equivalence:
  - Two functions with the same shape can do unrelated things — `load(path)`
    calling open/read/close looks identical whether it parses a config file
    or a log file.
  - Two functions doing the same thing through a differently-named helper
    (`json.loads` vs `ujson.loads`) will not match.
Every cluster this module returns is a hint to READ, not an automatic merge
— it is never asserted that two clustered functions ARE duplicates, only
that they are structurally similar enough to be worth a human look.

Coverage: the same 13 languages `graphify.state_affinity` covers (its
`EXT_LANG`, reused directly here), via the SAME tree-sitter parse cache
(`state_affinity._cached_parse`) — parsing a file once serves both modules,
not twice. Field names and node types below were verified empirically
against the installed grammars (same discipline `state_affinity` documents
for itself), NOT guessed from documentation or from another language's
shape. The two modules solve different problems, though: `state_affinity`
extracts self/this-ROOTED access only (it needs to know an access belongs
to the receiver); this module extracts every call regardless of receiver,
which is a different (and for most languages simpler) piece of grammar
knowledge — the two field-name tables here are NOT the same tables, even
where the underlying node types coincide. Go's grouped parameter syntax
(`func f(a, b int)`) collapses to one grammar node for both names, which
undercounts `param_count` for that specific spelling — a known, accepted
approximation, not silently treated as exact.

Blocking uses the same MinHash/LSH primitives as `graphify.dedup`'s entity
dedup (see `graphify._minhash`), fingerprinted on the callee-name set
instead of label shingles, and — same discipline as `graphify.dedup` — every
LSH candidate is re-verified with an EXACT Jaccard check over the real sets
before being accepted; LSH only avoids an O(n^2) full comparison; it is
never itself the accept/reject decision.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from graphify._minhash import MinHash, MinHashLSH
from graphify.state_affinity import EXT_LANG, _cached_parse

_DEFAULT_NUM_PERM = 64
_DEFAULT_JACCARD_THRESHOLD = 0.5
_DEFAULT_MIN_CALLS = 2

# ---- per-language grammar knowledge (verified empirically per-language,
# same discipline as graphify.state_affinity — see module docstring) -------

_FUNCTION_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"function_definition"}),
    "javascript": frozenset({"function_declaration", "method_definition"}),
    "typescript": frozenset({"function_declaration", "method_definition"}),
    "tsx": frozenset({"function_declaration", "method_definition"}),
    "java": frozenset({"method_declaration"}),
    "csharp": frozenset({"method_declaration"}),
    "rust": frozenset({"function_item"}),
    "ruby": frozenset({"method"}),
    "php": frozenset({"function_definition", "method_declaration"}),
    "swift": frozenset({"function_declaration"}),
    "kotlin": frozenset({"function_declaration"}),
    "cpp": frozenset({"function_definition"}),
    # go: broader than state_affinity's own mapping (which only needs
    # receiver methods) — this module wants every function, including
    # top-level ones.
    "go": frozenset({"function_declaration", "method_declaration"}),
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
    # go has no class node — container is the receiver TYPE (see
    # _go_receiver_type), resolved without a _CLASS_TYPES entry at all.
}

# Node type(s) meaning "this is a call expression", any receiver. Distinct
# from state_affinity._CALL_WRAP_TYPES/_ACCESS_TYPES, which key off a
# self/this-rooted access specifically.
_CALL_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"call"}),
    "javascript": frozenset({"call_expression"}),
    "typescript": frozenset({"call_expression"}),
    "tsx": frozenset({"call_expression"}),
    "java": frozenset({"method_invocation"}),
    "csharp": frozenset({"invocation_expression"}),
    "rust": frozenset({"call_expression"}),
    "ruby": frozenset({"call"}),
    "php": frozenset({"function_call_expression", "member_call_expression"}),
    "swift": frozenset({"call_expression"}),
    "kotlin": frozenset({"call_expression"}),
    "cpp": frozenset({"call_expression"}),
    "go": frozenset({"call_expression"}),
}

# Named (non-punctuation) child types inside a "parameters" list that count
# as a real parameter, per language. Swift, Kotlin, and C++ have their own
# shapes and are special-cased in `_param_count` instead of using this table.
_PARAM_NODE_TYPES: dict[str, frozenset[str]] = {
    "python": frozenset({"identifier", "typed_parameter", "default_parameter", "typed_default_parameter"}),
    "javascript": frozenset({"identifier", "required_parameter", "optional_parameter", "rest_parameter"}),
    "typescript": frozenset({"identifier", "required_parameter", "optional_parameter", "rest_parameter"}),
    "tsx": frozenset({"identifier", "required_parameter", "optional_parameter", "rest_parameter"}),
    "java": frozenset({"formal_parameter", "spread_parameter"}),
    "csharp": frozenset({"parameter"}),
    "rust": frozenset({"parameter", "self_parameter"}),
    "ruby": frozenset({"identifier", "optional_parameter", "splat_parameter", "keyword_parameter", "hash_splat_parameter"}),
    "php": frozenset({"simple_parameter", "variadic_parameter", "property_promotion_parameter"}),
    "go": frozenset({"parameter_declaration"}),
}


def _text(node, source: bytes) -> str:
    return source[node.start_byte:node.end_byte].decode("utf-8", "replace")


def _callee_name(lang: str, node, source: bytes) -> "str | None":
    """Bare callee name for a call-type node (see `_CALL_TYPES`) — the LAST
    identifier segment regardless of receiver (unlike
    `state_affinity._extract_access`, which only extracts a self/this-rooted
    access). Returns None for a shape with no stable name (a call on a
    subscript, a call result, etc.) — that call simply doesn't contribute a
    name, not an error."""
    if lang == "python":
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "attribute":
            attr = fn.child_by_field_name("attribute")
            return _text(attr, source) if attr is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    if lang in ("javascript", "typescript", "tsx"):
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "member_expression":
            prop = fn.child_by_field_name("property")
            return _text(prop, source) if prop is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    if lang == "java":
        name = node.child_by_field_name("name")
        return _text(name, source) if name is not None else None
    if lang == "csharp":
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "member_access_expression":
            name = fn.child_by_field_name("name")
            return _text(name, source) if name is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    if lang == "rust":
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "field_expression":
            field = fn.child_by_field_name("field")
            return _text(field, source) if field is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    if lang == "ruby":
        method = node.child_by_field_name("method")
        return _text(method, source) if method is not None else None
    if lang == "php":
        # member_call_expression has "name" directly; function_call_expression
        # (bare) has "function" holding a plain `name` node.
        name = node.child_by_field_name("name")
        if name is not None:
            return _text(name, source)
        fn = node.child_by_field_name("function")
        return _text(fn, source) if fn is not None else None
    if lang == "swift":
        # call_expression's callee is an UNNAMED first child in this
        # grammar — simple_identifier (bare) or navigation_expression
        # (member); verified empirically, same as state_affinity's own
        # swift branch of _extract_access.
        if node.child_count == 0:
            return None
        callee = node.children[0]
        if callee.type == "simple_identifier":
            return _text(callee, source)
        if callee.type == "navigation_expression":
            suffix = callee.child_by_field_name("suffix")
            inner = suffix.child_by_field_name("suffix") if suffix is not None else None
            return _text(inner, source) if inner is not None else None
        return None
    if lang == "kotlin":
        # Same unnamed-first-child shape as Swift; navigation_expression has
        # no named fields at all in this grammar (positional, matching
        # state_affinity's own kotlin branch).
        if node.child_count == 0:
            return None
        callee = node.children[0]
        if callee.type == "identifier":
            return _text(callee, source)
        if callee.type == "navigation_expression":
            children = callee.children
            if children and children[-1].is_named:
                return _text(children[-1], source)
            return None
        return None
    if lang == "cpp":
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "field_expression":
            field = fn.child_by_field_name("field")
            return _text(field, source) if field is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    if lang == "go":
        fn = node.child_by_field_name("function")
        if fn is None:
            return None
        if fn.type == "selector_expression":
            field = fn.child_by_field_name("field")
            return _text(field, source) if field is not None else None
        return _text(fn, source) if fn.type == "identifier" else None
    return None


def _param_count(lang: str, func_node, *, is_method: bool) -> int:
    """Parameter count, receiver (self/this/cls-shaped) params excluded when
    `is_method`. A coarse structural count, not full type resolution — see
    module docstring for the known Go grouped-parameter undercount."""
    if lang == "swift":
        return sum(1 for c in func_node.children if c.type == "parameter")
    if lang == "kotlin":
        for c in func_node.children:
            if c.type == "function_value_parameters":
                return sum(1 for gc in c.children if gc.type == "parameter")
        return 0
    if lang == "cpp":
        declarator = func_node.child_by_field_name("declarator")
        while declarator is not None and declarator.type != "function_declarator":
            declarator = declarator.child_by_field_name("declarator")
        if declarator is None:
            return 0
        plist = declarator.child_by_field_name("parameters")
        if plist is None:
            return 0
        return sum(1 for c in plist.children if c.type == "parameter_declaration")

    plist = func_node.child_by_field_name("parameters")
    if plist is None:
        return 0
    param_types = _PARAM_NODE_TYPES.get(lang, frozenset())
    params = [c for c in plist.children if c.type in param_types]
    if lang == "rust":
        # self_parameter IS a receiver, not a real argument.
        params = [p for p in params if p.type != "self_parameter"]
    elif lang == "python" and is_method and params:
        # Python has no dedicated receiver node — self/cls is a plain
        # identifier-shaped param; only ever the FIRST one, so drop it
        # positionally. A @staticmethod (no receiver at all) would lose a
        # real parameter here — an accepted, rare false-negative: this
        # module has no decorator information to distinguish that case.
        params = params[1:]
    return len(params)


def _cpp_function_name(func_node, source: bytes) -> "str | None":
    """C++'s function_definition has no direct "name" field — it is nested
    inside the declarator chain (pointer/reference wrappers around the
    innermost function_declarator's own "declarator" field)."""
    declarator = func_node.child_by_field_name("declarator")
    while declarator is not None and declarator.type != "function_declarator":
        declarator = declarator.child_by_field_name("declarator")
    if declarator is None:
        return None
    name = declarator.child_by_field_name("declarator")
    return _text(name, source) if name is not None else None


def _function_name(lang: str, func_node, source: bytes) -> "str | None":
    if lang == "cpp":
        return _cpp_function_name(func_node, source)
    name = func_node.child_by_field_name("name")
    return _text(name, source) if name is not None else None


def _class_name(lang: str, class_node, source: bytes) -> "str | None":
    if lang == "rust":
        type_node = class_node.child_by_field_name("type")
        return _text(type_node, source) if type_node is not None else None
    name_node = class_node.child_by_field_name("name")
    return _text(name_node, source) if name_node is not None else None


def _go_receiver_type(method_node, source: bytes) -> "str | None":
    """`func (f *Foo) M()` -> "Foo" — mirrors
    `state_affinity._go_receiver_type` (Go methods aren't nested in a class
    node; the receiver TYPE is the only thing tying them to "Foo")."""
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


def _collect_calls(lang: str, func_node, source: bytes) -> set[str]:
    calls: set[str] = set()
    call_types = _CALL_TYPES.get(lang, frozenset())

    def visit(node) -> None:
        if node.type in call_types:
            name = _callee_name(lang, node, source)
            if name:
                calls.add(name)
        for child in node.children:
            visit(child)

    visit(func_node)
    return calls


def _fingerprint(lang: str, func_node, source: bytes, *, container: "str | None") -> "dict[str, Any] | None":
    name = _function_name(lang, func_node, source)
    if name is None:
        return None
    return {
        "name": name,
        "lineno": func_node.start_point[0] + 1,
        "container": container,
        "param_count": _param_count(lang, func_node, is_method=container is not None),
        "calls": _collect_calls(lang, func_node, source),
    }


def extract_functions(source_file: "str | Path") -> "list[dict[str, Any]] | None":
    """Every top-level function and class method in `source_file`, as a
    structural fingerprint (name, line, container class if any, parameter
    count with a receiver excluded, and the set of bare callee names used
    in the body). Nested/inner functions (closures) are NOT walked as
    separate entries — only module-level defs and one level of class
    methods, mirroring what graphify's own extractor treats as a distinct
    callable node.

    Returns None when: the extension isn't a supported language (see
    `graphify.state_affinity.EXT_LANG`), the file can't be read, or the
    grammar package is missing — a skip, not an error, same convention as
    `state_affinity`. Malformed source is NOT one of these cases: unlike the
    stdlib `ast` module, tree-sitter never raises on invalid syntax — it
    parses what it can and marks the rest as error nodes — so a broken file
    may yield a partial, best-effort result instead of None.
    """
    path = Path(source_file)
    lang = EXT_LANG.get(path.suffix.lower())
    if lang is None:
        return None
    parsed = _cached_parse(lang, path)
    if parsed is None:
        return None
    tree, source = parsed

    function_types = _FUNCTION_TYPES.get(lang)
    if not function_types:
        return None

    functions: list[dict[str, Any]] = []

    if lang == "go":
        # No class node at all — a method_declaration's only tie to a
        # "container" is its receiver TYPE (see _go_receiver_type).
        def scan_go(node) -> None:
            for child in node.children:
                if child.type in function_types:
                    container = _go_receiver_type(child, source) if child.type == "method_declaration" else None
                    fp = _fingerprint(lang, child, source, container=container)
                    if fp is not None:
                        functions.append(fp)
                    continue
                scan_go(child)

        scan_go(tree.root_node)
        return functions

    class_types = _CLASS_TYPES.get(lang, frozenset())

    def collect_in_class(class_node, container: str) -> None:
        stack = [class_node]
        while stack:
            node = stack.pop()
            if node is not class_node and node.type in class_types:
                continue  # a nested class's own methods aren't THIS container's
            if node.type in function_types:
                fp = _fingerprint(lang, node, source, container=container)
                if fp is not None:
                    functions.append(fp)
                continue
            stack.extend(node.children)

    def scan(node) -> None:
        for child in node.children:
            if child.type in function_types:
                fp = _fingerprint(lang, child, source, container=None)
                if fp is not None:
                    functions.append(fp)
                continue
            if child.type in class_types:
                name = _class_name(lang, child, source)
                if name is not None:
                    collect_in_class(child, name)
                continue
            scan(child)

    scan(tree.root_node)
    return functions


def _calls_minhash(calls: "set[str]", *, num_perm: int) -> MinHash:
    m = MinHash(num_perm=num_perm)
    for name in calls:
        m.update(name.encode("utf-8"))
    return m


class _UF:
    """Minimal union-find — deliberately local rather than importing
    `graphify.dedup`'s private `_UF`, to keep this module's only dependency
    on that area of the codebase at the primitive (`graphify._minhash`)
    level, not another module's internals."""

    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def find(self, x: str) -> str:
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: str, y: str) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry


def discover_source_files(project_root: "str | Path") -> list[str]:
    """Convenience file discovery for callers that don't already have a
    graphify graph's own `source_file` list to hand — every file in a
    language `graphify.state_affinity` supports, under `project_root`, as
    paths relative to it, skipping the usual non-project directories.
    Prefer passing graphify's own already-computed source_file list instead
    when one is available — it already reflects the project's real ignore
    rules, this does not.
    """
    root = Path(project_root)
    skip_dirs = {
        ".git", "__pycache__", ".venv", "venv", "env", "node_modules",
        ".mypy_cache", ".pytest_cache", ".tox", "build", "dist",
        "graphify-out", ".hypothesis", "target", "vendor",
    }
    results: list[str] = []
    for ext in EXT_LANG:
        for path in root.rglob(f"*{ext}"):
            if any(part in skip_dirs for part in path.relative_to(root).parts):
                continue
            results.append(path.relative_to(root).as_posix())
    return sorted(set(results))


def suggest_merge_target(cluster: dict[str, Any]) -> dict[str, Any]:
    """Where should a cluster's duplicated logic actually live after
    consolidation? Two valid answers, never picked silently when ambiguous:

    - "independent": a new shared class/module. The right call when no
      existing class is an unambiguous home — either every member is a bare
      function (nothing claims this logic yet), or more than one DIFFERENT
      existing class appears among the members (each has an equal claim,
      picking one would be a guess).
    - "merge_into_existing": exactly ONE existing class appears among the
      cluster's members (the rest bare, if any). That class already has SOME
      claim to this logic, so folding the others INTO it is the naturally
      cheaper move — no new class, no new import pattern for callers to
      learn.

    This is a structural heuristic over `container` alone (see
    `extract_functions`) — it knows nothing about which class is
    semantically the better fit beyond "does a class already claim this
    logic". Every existing-class candidate is listed under `candidates`, not
    just the winner, so a "merge_into_existing" pick can be second-guessed
    at a glance, and an "independent" verdict born from ambiguity (as
    opposed to "nothing exists yet") still shows what was ruled out.
    """
    containers = sorted({
        (m["container"], m["source_file"])
        for m in cluster["members"]
        if m["container"] is not None
    })
    candidates = [{"container": c, "source_file": f} for c, f in containers]

    if len(containers) == 1:
        target = candidates[0]
        return {
            "recommendation": "merge_into_existing",
            "target_container": target["container"],
            "target_source_file": target["source_file"],
            "candidates": candidates,
            "rationale": (
                f"One existing class already claims this logic — "
                f"`{target['container']}` in `{target['source_file']}`. The "
                "other member(s) have no existing class of their own, so "
                "folding them into it is cheaper than creating a new home."
            ),
        }
    if not containers:
        return {
            "recommendation": "independent",
            "target_container": None,
            "target_source_file": None,
            "candidates": [],
            "rationale": (
                "None of the cluster's members belong to an existing class — "
                "they are all bare functions. There is no existing home to "
                "fold into; consolidating means creating a new shared "
                "class/module."
            ),
        }
    return {
        "recommendation": "independent",
        "target_container": None,
        "target_source_file": None,
        "candidates": candidates,
        "rationale": (
            f"{len(containers)} different existing classes each already "
            "claim one copy of this logic — there is no unambiguous "
            "existing home to fold into. Defaulting to a new shared class/"
            "module; the existing classes are listed as candidates in case "
            "a human judges one of them the better fit."
        ),
    }


def find_duplicate_function_clusters(
    project_root: "str | Path",
    source_files: "list[str]",
    *,
    min_calls: int = _DEFAULT_MIN_CALLS,
    jaccard_threshold: float = _DEFAULT_JACCARD_THRESHOLD,
    num_perm: int = _DEFAULT_NUM_PERM,
) -> dict[str, Any]:
    """Find near-duplicate function/method IMPLEMENTATIONS scattered across
    DIFFERENT files or classes — see the module docstring for what this is
    and is not, and for language coverage.

    - Functions with fewer than `min_calls` calls are excluded. A one-liner
      accessor (`def x(self): return self._x`) is common, structurally
      trivial, and would otherwise flood clusters with coincidental
      near-empty-fingerprint matches. An already-shared, non-trivial utility
      (the `decouple.py` "tool_function" node_role case) is a DIFFERENT,
      already-answered question — this module only looks for logic that
      is NOT yet consolidated.
    - A candidate pair must differ in `(source_file, container)` — a pair
      sharing both is the intra-class-accessor-duplicate case (e.g. one
      class exposing several near-identical getters), a real but DIFFERENT
      finding from "reimplemented in different places", and is not reported
      here.
    - `param_count` must match exactly — a coarse pre-filter, not a type
      check (this module never resolves what a parameter's actual type is).
    """
    root = Path(project_root)
    entries: list[dict[str, Any]] = []
    for rel in source_files:
        if Path(rel).suffix.lower() not in EXT_LANG:
            continue
        funcs = extract_functions(root / rel)
        if not funcs:
            continue
        for fn in funcs:
            if len(fn["calls"]) < min_calls:
                continue
            entries.append({
                "id": f"{rel}:{fn['lineno']}:{fn['name']}",
                "source_file": rel,
                "container": fn["container"],
                "name": fn["name"],
                "lineno": fn["lineno"],
                "param_count": fn["param_count"],
                "calls": fn["calls"],
            })

    params = {
        "min_calls": min_calls,
        "jaccard_threshold": jaccard_threshold,
        "num_perm": num_perm,
    }
    if len(entries) < 2:
        return {"clusters": [], "n_functions_scanned": len(entries), "params": params, "caveats": _caveats(min_calls)}

    by_id = {e["id"]: e for e in entries}
    minhashes = {eid: _calls_minhash(e["calls"], num_perm=num_perm) for eid, e in by_id.items()}

    lsh = MinHashLSH(threshold=jaccard_threshold, num_perm=num_perm)
    for eid, mh in minhashes.items():
        try:
            lsh.insert(eid, mh)
        except ValueError:
            pass  # duplicate key — can't happen, ids are file:line:name unique, but never fatal

    uf = _UF()
    for eid, mh in minhashes.items():
        entry = by_id[eid]
        for neighbor_id in lsh.query(mh):
            if neighbor_id == eid or uf.find(eid) == uf.find(neighbor_id):
                continue
            neighbor = by_id[neighbor_id]
            if entry["source_file"] == neighbor["source_file"] and entry["container"] == neighbor["container"]:
                continue
            if entry["param_count"] != neighbor["param_count"]:
                continue
            union = entry["calls"] | neighbor["calls"]
            jaccard = len(entry["calls"] & neighbor["calls"]) / len(union) if union else 0.0
            if jaccard < jaccard_threshold:
                continue  # LSH gave an estimate; the exact check is the real gate
            uf.union(eid, neighbor_id)

    groups: dict[str, list[str]] = {}
    for eid in by_id:
        groups.setdefault(uf.find(eid), []).append(eid)

    clusters: list[dict[str, Any]] = []
    for members in groups.values():
        if len(members) < 2:
            continue
        member_entries = sorted((by_id[m] for m in members), key=lambda e: (e["source_file"], e["lineno"]))
        pairwise: list[float] = []
        for i in range(len(member_entries)):
            for j in range(i + 1, len(member_entries)):
                a, b = member_entries[i]["calls"], member_entries[j]["calls"]
                union = a | b
                pairwise.append(len(a & b) / len(union) if union else 0.0)
        clusters.append({
            "members": [
                {
                    "id": e["id"], "source_file": e["source_file"],
                    "container": e["container"], "name": e["name"],
                    "lineno": e["lineno"], "param_count": e["param_count"],
                    "calls": sorted(e["calls"]),
                }
                for e in member_entries
            ],
            "same_name": len({e["name"] for e in member_entries}) == 1,
            "avg_jaccard": round(sum(pairwise) / len(pairwise), 3) if pairwise else 0.0,
        })
        clusters[-1]["merge_target"] = suggest_merge_target(clusters[-1])
    # Confidence first, not cluster size: validated against a real corpus, a
    # tight same-name pair at avg_jaccard 1.0 (near-certain copy-paste) is
    # far stronger evidence than a 5-member cluster of generic same-framework
    # boilerplate (e.g. Qt widget __init__s all calling super()/_build()) —
    # sorting by size first buried the strongest hits below the noisiest ones.
    clusters.sort(key=lambda c: (not c["same_name"], -c["avg_jaccard"], -len(c["members"])))

    return {
        "clusters": clusters,
        "n_functions_scanned": len(entries),
        "params": params,
        "caveats": _caveats(min_calls),
    }


def _caveats(min_calls: int) -> list[str]:
    return [
        "This is a structural proxy (callee-name set + parameter count), not "
        "semantic equivalence — every cluster is a hint to read, not a "
        "verified duplicate or an automatic merge candidate.",
        "Coverage matches graphify.state_affinity.EXT_LANG (13 languages); "
        "files in any other language are silently skipped (contribute no "
        "functions), not treated as an error. Go's grouped parameter syntax "
        "(`func f(a, b int)`) undercounts param_count for that spelling.",
        "A candidate pair sharing (source_file, container) is excluded — "
        "same-class intra-class duplicates are a different finding from "
        "cross-file/cross-class reimplementation, and are not reported here.",
        f"Functions with fewer than {min_calls} calls in their body are "
        "excluded — trivial accessors would otherwise flood clusters with "
        "coincidental near-empty-fingerprint matches.",
    ]


def render_markdown(report: dict[str, Any]) -> str:
    p = report["params"]
    lines = [
        "# Candidate Shared-Utility Consolidation",
        "",
        "_Structural near-duplicate scan (tree-sitter) — no LLM involved._",
        "",
        f"Scanned {report['n_functions_scanned']} functions with >= {p['min_calls']} "
        f"calls; jaccard_threshold={p['jaccard_threshold']}",
        "",
    ]
    if not report["clusters"]:
        lines.append("_No candidate clusters found._")
    for i, cluster in enumerate(report["clusters"], start=1):
        name_note = ", same name" if cluster["same_name"] else ""
        lines.append(f"## Cluster {i} ({len(cluster['members'])} candidates, avg_jaccard={cluster['avg_jaccard']}{name_note})")
        for m in cluster["members"]:
            container = f"{m['container']}." if m["container"] else ""
            lines.append(f"- `{m['source_file']}:{m['lineno']}` — `{container}{m['name']}()` (params={m['param_count']})")
            lines.append(f"  calls: {', '.join(m['calls'][:12])}")
        mt = cluster["merge_target"]
        if mt["recommendation"] == "merge_into_existing":
            lines.append(f"- **suggested merge target:** `{mt['target_container']}` in `{mt['target_source_file']}` (existing class)")
        else:
            lines.append("- **suggested merge target:** independent (new shared class/module)")
            if mt["candidates"]:
                cand_str = ", ".join(f"`{c['container']}` ({c['source_file']})" for c in mt["candidates"])
                lines.append(f"  ambiguous existing candidates ruled out: {cand_str}")
        lines.append(f"  _{mt['rationale']}_")
        cr = cluster.get("consolidation_risk")
        if cr:
            lines.append(
                f"- consolidation_benefit={cr['consolidation_benefit']} "
                f"consolidation_risk={cr['consolidation_risk']} "
                f"net_benefit={cr['net_benefit']} -> **{cr['recommendation']}**"
            )
            floor_note = (
                f"floor_span={cr['floor_span']}" if cr["floor_span_known"]
                else "floor_span=unknown (no I/O boundary reachable)"
            )
            lines.append(
                f"  afferent_total={cr['afferent_total']} {floor_note} "
                f"— independent of any split's risk_before/risk_after (different question, different scale)"
            )
        lines.append("")
    lines.append("## Honesty notes")
    for c in report["caveats"]:
        lines.append(f"- {c}")
    return "\n".join(lines)
