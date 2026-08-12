"""Tests for graphify.state_affinity — cross-language self/this-attribute
usage analysis, re-parsing source directly (not graphify's own AST tier,
which does not record field/attribute access for any language).

Node types and field names used by the module were verified empirically
against the actual installed tree-sitter grammars (see the scratch probes
used while building this), not assumed from grammar documentation —
including the read/write/call structure per language (Java/PHP/Ruby use a
DEDICATED node type for a receiver call, distinct from plain field access;
every other language wraps the same access node in a call node).
"""
from __future__ import annotations

from graphify.state_affinity import extract_method_attribute_usage, state_overlap


def test_python_read_write_call_split(tmp_path):
    src = """class Foo:
    def read_it(self):
        return self.x
    def write_it(self):
        self.y = 1
    def call_it(self):
        self.helper()
    def unrelated(self):
        return 42
"""
    p = tmp_path / "foo.py"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".read_it()", ".write_it()", ".call_it()", ".unrelated()"])
    assert usage["read_it"] == {"reads": {"x"}, "writes": set(), "calls": set()}
    assert usage["write_it"] == {"reads": set(), "writes": {"y"}, "calls": set()}
    assert usage["call_it"] == {"reads": set(), "writes": set(), "calls": {"helper"}}
    assert usage["unrelated"] == {"reads": set(), "writes": set(), "calls": set()}


def test_javascript_read_write_call_split(tmp_path):
    src = """class Foo {
  readIt() { return this.x; }
  writeIt() { this.y = 1; }
  callIt() { this.helper(); }
}
"""
    p = tmp_path / "foo.js"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".readIt()", ".writeIt()", ".callIt()"])
    assert usage["readIt"]["reads"] == {"x"}
    assert usage["writeIt"]["writes"] == {"y"}
    assert usage["callIt"]["calls"] == {"helper"}


def test_java_dedicated_method_invocation_node(tmp_path):
    """Java's `this.foo()` is NOT a wrapped field_access — it's its own
    method_invocation node with different field names. Confirms both are
    picked up correctly."""
    src = """class Foo {
  int x;
  int readIt() { return this.x; }
  void callIt() { this.helper(); }
}
"""
    p = tmp_path / "Foo.java"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".readIt()", ".callIt()"])
    assert usage["readIt"]["reads"] == {"x"}
    assert usage["callIt"]["calls"] == {"helper"}


def test_ruby_instance_variable_vs_self_call(tmp_path):
    src = """class Foo
  def read_it
    @x
  end
  def write_it
    @y = 1
  end
  def call_it
    self.helper
  end
end
"""
    p = tmp_path / "foo.rb"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".read_it()", ".write_it()", ".call_it()"])
    assert usage["read_it"]["reads"] == {"x"}
    assert usage["write_it"]["writes"] == {"y"}
    assert usage["call_it"]["calls"] == {"helper"}


def test_go_resolves_per_method_receiver_and_write(tmp_path):
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
    assert usage["ReadIt"]["reads"] == {"x"}
    assert usage["WriteIt"]["writes"] == {"y"}


def test_swift_write_detection(tmp_path):
    src = """class Foo {
  var x: Int = 0
  func writeIt() {
    self.x = 1
  }
  func readIt() -> Int {
    return self.x
  }
}
"""
    p = tmp_path / "foo.swift"
    p.write_text(src, encoding="utf-8")
    usage = extract_method_attribute_usage(p, "Foo", [".writeIt()", ".readIt()"])
    assert usage["writeIt"]["writes"] == {"x"}
    assert usage["readIt"]["reads"] == {"x"}


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


def test_parse_cache_reused_across_calls(tmp_path, monkeypatch):
    """Two calls against the same (unchanged) file must not re-parse."""
    import graphify.state_affinity as sa

    p = tmp_path / "foo.py"
    p.write_text("class Foo:\n    def m(self):\n        return self.x\n", encoding="utf-8")
    sa._PARSE_CACHE.clear()

    calls = {"n": 0}
    real_parse = sa.parse_source

    def counting_parse(lang, source):
        calls["n"] += 1
        return real_parse(lang, source)

    monkeypatch.setattr(sa, "parse_source", counting_parse)
    extract_method_attribute_usage(p, "Foo", [".m()"])
    extract_method_attribute_usage(p, "Foo", [".m()"])
    assert calls["n"] == 1


def test_state_overlap_field_vs_call_and_write_boost():
    usage = {
        "a0": {"reads": {"shared"}, "writes": set(), "calls": set()},
        "a1": {"reads": set(), "writes": {"onlya"}, "calls": {"helper"}},
        "b0": {"reads": {"shared"}, "writes": set(), "calls": {"helper"}},
        "b1": {"reads": set(), "writes": {"onlyb"}, "calls": set()},
    }
    ov = state_overlap(usage, [".a0()", ".a1()"], [".b0()", ".b1()"])
    assert ov is not None
    assert ov["shared_attrs"] == ["shared"]
    assert ov["shared_calls"] == ["helper"]
    assert ov["field_overlap"] > 0
    assert ov["call_overlap"] > 0
    assert ov["overlap"] >= ov["field_overlap"]  # call overlap only adds, never subtracts


def test_state_overlap_write_write_scores_higher_than_read_read():
    # Two attrs each, one shared + one private per side, so field_overlap
    # (1/3) sits well under the 1.0 cap and the write boost is visible.
    read_only = {"a0": {"reads": {"shared", "onlya"}, "writes": set(), "calls": set()},
                 "b0": {"reads": {"shared", "onlyb"}, "writes": set(), "calls": set()}}
    write_write = {"a0": {"reads": {"onlya"}, "writes": {"shared"}, "calls": set()},
                   "b0": {"reads": {"onlyb"}, "writes": {"shared"}, "calls": set()}}
    ov_read = state_overlap(read_only, [".a0()"], [".b0()"])
    ov_write = state_overlap(write_write, [".a0()"], [".b0()"])
    assert ov_write["overlap"] > ov_read["overlap"]


def test_state_overlap_none_when_nothing_touched():
    assert state_overlap({}, [".a0()"], [".b0()"]) is None
