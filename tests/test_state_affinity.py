"""Tests for graphify.state_affinity — cross-language self/this-attribute
usage analysis, re-parsing source directly (not graphify's own AST tier,
which does not record field/attribute access for any language).

Node types and field names used by the module were verified empirically
against the actual installed tree-sitter grammars (see the scratch probes
used while building this), not assumed from grammar documentation.
"""
from __future__ import annotations

from graphify.state_affinity import extract_method_attribute_usage, state_overlap


def test_python_extracts_self_attributes(tmp_path):
    src = """class Foo:
    def read_it(self):
        return self.x
    def write_it(self):
        self.y = 1
    def unrelated(self):
        return 42
"""
    p = tmp_path / "foo.py"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".read_it()", ".write_it()", ".unrelated()"])
    assert usage["read_it"] == {"x"}
    assert usage["write_it"] == {"y"}
    assert usage["unrelated"] == set()


def test_javascript_this_attributes(tmp_path):
    src = """class Foo {
  readIt() { return this.x; }
  writeIt() { this.y = 1; }
}
"""
    p = tmp_path / "foo.js"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".readIt()", ".writeIt()"])
    assert usage["readIt"] == {"x"}
    assert usage["writeIt"] == {"y"}


def test_ruby_instance_variables(tmp_path):
    src = """class Foo
  def read_it
    @x
  end
  def write_it
    @y = 1
  end
end
"""
    p = tmp_path / "foo.rb"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".read_it()", ".write_it()"])
    assert usage["read_it"] == {"x"}
    assert usage["write_it"] == {"y"}


def test_go_resolves_per_method_receiver(tmp_path):
    src = """package foo

type Foo struct {
	x int
	y int
}

func (f *Foo) ReadIt() int {
	return f.x
}

func (g *Foo) WriteIt() {
	g.y = 1
}
"""
    p = tmp_path / "foo.go"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".ReadIt()", ".WriteIt()"])
    # Different receiver names per method ("f" vs "g") — each resolved independently.
    assert usage["ReadIt"] == {"x"}
    assert usage["WriteIt"] == {"y"}


def test_unsupported_extension_returns_none(tmp_path):
    p = tmp_path / "foo.c"
    p.write_text("struct Foo { int x; };\n", encoding="utf-8")
    assert extract_method_attribute_usage(p, "Foo", [".m()"]) is None


def test_missing_file_returns_none(tmp_path):
    assert extract_method_attribute_usage(tmp_path / "nope.py", "Foo", [".m()"]) is None


def test_class_not_found_returns_none(tmp_path):
    p = tmp_path / "foo.py"
    p.write_text("class Bar:\n    def m(self):\n        return self.x\n", encoding="utf-8")
    assert extract_method_attribute_usage(p, "Foo", [".m()"]) is None


def test_state_overlap_full_and_none():
    usage = {"a0": {"shared", "onlya"}, "a1": {"shared"}, "b0": {"shared"}, "b1": {"shared", "onlyb"}}
    ov = state_overlap(usage, [".a0()", ".a1()"], [".b0()", ".b1()"])
    assert ov is not None
    assert "shared" in ov["shared_attrs"]
    assert 0 < ov["overlap"] < 1

    disjoint_usage = {"a0": {"onlya"}, "b0": {"onlyb"}}
    ov2 = state_overlap(disjoint_usage, [".a0()"], [".b0()"])
    assert ov2["overlap"] == 0.0

    assert state_overlap({}, [".a0()"], [".b0()"]) is None
