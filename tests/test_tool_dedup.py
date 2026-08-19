"""Tests for `graphify.tool_dedup` — corpus-wide near-duplicate function scan.

Pins the distinction the feature depends on: two functions with the same
callee-set/param-count shape in DIFFERENT files/classes are a consolidation
candidate; the same shape repeated inside ONE class (intra-class accessor
duplication) is a different finding and must NOT be reported here.
"""
from __future__ import annotations

from graphify.tool_dedup import (
    discover_source_files,
    extract_functions,
    find_duplicate_function_clusters,
    render_markdown,
    suggest_merge_target,
)


def _write(path, content):
    path.write_text(content, encoding="utf-8")


# ── extract_functions ────────────────────────────────────────────────────────

def test_extract_functions_finds_top_level_and_methods(tmp_path):
    f = tmp_path / "mod.py"
    _write(f, """
def top_level(a, b):
    return open(a).read()

class Foo:
    def method(self, x):
        return self.helper(x)
""")
    functions = extract_functions(f)
    by_name = {fn["name"]: fn for fn in functions}
    assert by_name["top_level"]["container"] is None
    assert by_name["top_level"]["param_count"] == 2
    assert "open" in by_name["top_level"]["calls"]
    assert by_name["method"]["container"] == "Foo"
    assert by_name["method"]["param_count"] == 1  # self excluded


def test_extract_functions_returns_none_for_missing_file(tmp_path):
    missing = tmp_path / "does_not_exist.py"
    assert extract_functions(missing) is None


def test_extract_functions_returns_none_for_unsupported_extension(tmp_path):
    f = tmp_path / "notes.txt"
    _write(f, "def f(a, b): pass\n")
    assert extract_functions(f) is None


def test_extract_functions_tolerates_malformed_syntax(tmp_path):
    """Unlike the stdlib `ast` module, tree-sitter never raises on malformed
    source — it parses what it can and marks the rest as error nodes. This
    module inherits that tolerance rather than working around it: a
    genuinely broken file may still yield a partial, best-effort result
    instead of None. The contract is "never raises", not "never partial"."""
    bad = tmp_path / "bad.py"
    _write(bad, "def broken(:\n")
    extract_functions(bad)  # must not raise


# ── find_duplicate_function_clusters ────────────────────────────────────────

def test_same_name_high_confidence_cluster_sorts_before_larger_noisy_one(tmp_path):
    """Validated against a real corpus: a tight same-name pair at
    avg_jaccard 1.0 is much stronger evidence (near-certain copy-paste) than
    a bigger cluster of generic same-framework boilerplate (e.g. several
    unrelated __init__ methods that merely all call super()). Confidence
    (same_name, then avg_jaccard) must sort before raw cluster size."""
    # A 3-member, DIFFERENTLY-NAMED, lower-jaccard "noisy" cluster: three
    # differently-named functions sharing only some generic builder calls.
    _write(tmp_path / "noisy_a.py", """
def setup_widget_a(parent):
    obj = Builder()
    obj.attach(parent)
    obj.render()
""")
    _write(tmp_path / "noisy_b.py", """
def setup_widget_b(parent):
    obj = Builder()
    obj.attach(parent)
    obj.paint()
""")
    _write(tmp_path / "noisy_c.py", """
def configure_panel(parent):
    obj = Builder()
    obj.attach(parent)
""")
    # A 2-member, same-name, jaccard=1.0 pair in different files — the
    # strongest possible signal.
    _write(tmp_path / "tight_a.py", """
def fmt_x_readout(value):
    return fmt_freq(value) if value else fmt_time(value)
""")
    _write(tmp_path / "tight_b.py", """
def fmt_x_readout(value):
    return fmt_freq(value) if value else fmt_time(value)
""")

    files = ["noisy_a.py", "noisy_b.py", "noisy_c.py", "tight_a.py", "tight_b.py"]
    report = find_duplicate_function_clusters(tmp_path, files)
    assert len(report["clusters"]) == 2
    first = report["clusters"][0]
    assert first["same_name"] is True
    assert first["avg_jaccard"] == 1.0
    assert len(first["members"]) == 2
    assert len(report["clusters"][1]["members"]) == 3


def test_finds_cross_file_near_duplicate(tmp_path):
    _write(tmp_path / "a.py", """
def load_config(path):
    with open(path) as f:
        data = json.load(f)
    return validate(data)
""")
    _write(tmp_path / "b.py", """
def load_settings(path):
    with open(path) as f:
        data = json.load(f)
    return validate(data)
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"])
    assert len(report["clusters"]) == 1
    names = {m["name"] for m in report["clusters"][0]["members"]}
    assert names == {"load_config", "load_settings"}


def test_excludes_same_class_intra_duplicate(tmp_path):
    """Same shape, but both methods live on the SAME class — that is the
    intra-class-accessor-duplicate case, a different finding, not reported
    by this module."""
    _write(tmp_path / "a.py", """
class NetworkData:
    def s11_db(self):
        return to_db(self.matrix, 0, 0)

    def s12_db(self):
        return to_db(self.matrix, 0, 1)
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py"])
    assert report["clusters"] == []


def test_cross_class_same_file_is_still_a_candidate(tmp_path):
    """Same file, but DIFFERENT classes — still a valid candidate; only
    same-file-AND-same-container pairs are excluded."""
    _write(tmp_path / "a.py", """
class Reader:
    def load(self, path):
        with open(path) as f:
            return parse(f.read())

class Writer:
    def load(self, path):
        with open(path) as f:
            return parse(f.read())
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py"])
    assert len(report["clusters"]) == 1
    mt = report["clusters"][0]["merge_target"]
    assert mt["recommendation"] == "independent"  # Reader AND Writer both claim it — ambiguous
    assert {c["container"] for c in mt["candidates"]} == {"Reader", "Writer"}


# ── suggest_merge_target ─────────────────────────────────────────────────────

def _member(container, source_file="a.py", name="load"):
    return {"container": container, "source_file": source_file, "name": name}


def test_merge_target_independent_when_all_bare(tmp_path):
    cluster = {"members": [_member(None, "a.py"), _member(None, "b.py")]}
    mt = suggest_merge_target(cluster)
    assert mt["recommendation"] == "independent"
    assert mt["candidates"] == []


def test_merge_target_merges_into_the_one_existing_class(tmp_path):
    cluster = {"members": [_member("Loader", "a.py"), _member(None, "b.py")]}
    mt = suggest_merge_target(cluster)
    assert mt["recommendation"] == "merge_into_existing"
    assert mt["target_container"] == "Loader"
    assert mt["target_source_file"] == "a.py"


def test_merge_target_independent_when_multiple_existing_classes_conflict(tmp_path):
    cluster = {"members": [_member("Reader", "a.py"), _member("Writer", "b.py")]}
    mt = suggest_merge_target(cluster)
    assert mt["recommendation"] == "independent"
    assert {c["container"] for c in mt["candidates"]} == {"Reader", "Writer"}


def test_find_duplicate_function_clusters_attaches_merge_target(tmp_path):
    _write(tmp_path / "a.py", """
class Loader:
    def load(self, path):
        with open(path) as f:
            return parse(f.read())
""")
    _write(tmp_path / "b.py", """
def load(path):
    with open(path) as f:
        return parse(f.read())
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"])
    assert len(report["clusters"]) == 1
    mt = report["clusters"][0]["merge_target"]
    assert mt["recommendation"] == "merge_into_existing"
    assert mt["target_container"] == "Loader"


def test_mismatched_param_count_not_clustered(tmp_path):
    _write(tmp_path / "a.py", """
def load(path):
    with open(path) as f:
        return parse(f.read())
""")
    _write(tmp_path / "b.py", """
def load(path, encoding):
    with open(path) as f:
        return parse(f.read())
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"])
    assert report["clusters"] == []


def test_trivial_low_call_functions_excluded(tmp_path):
    _write(tmp_path / "a.py", """
def x():
    return self._x
""")
    _write(tmp_path / "b.py", """
def y():
    return self._y
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"], min_calls=2)
    assert report["n_functions_scanned"] == 0
    assert report["clusters"] == []


def test_unrelated_functions_not_clustered(tmp_path):
    _write(tmp_path / "a.py", """
def load_config(path):
    with open(path) as f:
        return json.load(f)
""")
    _write(tmp_path / "b.py", """
def render_report(title, rows):
    doc = Document(title)
    doc.add_table(rows)
    return doc.save()
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"])
    assert report["clusters"] == []


def test_unsupported_language_files_are_skipped(tmp_path):
    _write(tmp_path / "a.py", """
def load(path):
    with open(path) as f:
        return parse(f.read())
""")
    _write(tmp_path / "notes.txt", "load(path) { return fs.readFileSync(path); }")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "notes.txt"])
    assert report["clusters"] == []
    assert report["n_functions_scanned"] == 1  # only a.py's load() is scanned; .txt has no language


# ── discover_source_files ────────────────────────────────────────────────────

def test_discover_source_files_skips_common_noise_dirs(tmp_path):
    (tmp_path / "pkg").mkdir()
    _write(tmp_path / "pkg" / "mod.py", "def f(): pass\n")
    (tmp_path / ".venv" / "lib").mkdir(parents=True)
    _write(tmp_path / ".venv" / "lib" / "vendored.py", "def f(): pass\n")

    files = discover_source_files(tmp_path)
    assert files == ["pkg/mod.py"]


# ── render_markdown ──────────────────────────────────────────────────────────

def test_render_markdown_lists_clusters_and_caveats(tmp_path):
    _write(tmp_path / "a.py", """
def load_config(path):
    with open(path) as f:
        return json.load(f)
""")
    _write(tmp_path / "b.py", """
def load_settings(path):
    with open(path) as f:
        return json.load(f)
""")
    report = find_duplicate_function_clusters(tmp_path, ["a.py", "b.py"])
    md = render_markdown(report)
    assert "load_config" in md
    assert "load_settings" in md
    assert "Honesty notes" in md


# ── cross-language coverage ─────────────────────────────────────────────────
# One near-duplicate pair per language `state_affinity.EXT_LANG` covers,
# exercising: bare calls, receiver/member calls (self./this./obj.), and
# container extraction (class name, or Go's receiver type). Field names and
# node types were verified empirically per language (see probe scripts),
# same discipline `state_affinity`'s own tests apply.

def _assert_one_cross_file_cluster(tmp_path, files):
    report = find_duplicate_function_clusters(tmp_path, files)
    assert len(report["clusters"]) == 1, report
    assert len(report["clusters"][0]["members"]) == 2
    return report["clusters"][0]


def test_javascript_bare_and_member_calls(tmp_path):
    _write(tmp_path / "a.js", """
function loadConfig(path) {
  var data = fs.readFileSync(path);
  return JSON.parse(data);
}
""")
    _write(tmp_path / "b.js", """
function loadSettings(path) {
  var data = fs.readFileSync(path);
  return JSON.parse(data);
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["a.js", "b.js"])
    assert cluster["avg_jaccard"] == 1.0


def test_java_method_invocation_and_container(tmp_path):
    _write(tmp_path / "Loader.java", """
class Loader {
    String loadConfig(String path) {
        String data = this.readFile(path);
        return parse(data);
    }
}
""")
    _write(tmp_path / "Settings.java", """
class Settings {
    String loadSettings(String path) {
        String data = this.readFile(path);
        return parse(data);
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["Loader.java", "Settings.java"])
    containers = {m["container"] for m in cluster["members"]}
    assert containers == {"Loader", "Settings"}


def test_go_receiver_type_as_container(tmp_path):
    _write(tmp_path / "loader.go", """
package main

func (l *Loader) LoadConfig(path string) string {
    data := readFile(path)
    return parse(data)
}
""")
    _write(tmp_path / "settings.go", """
package main

func (s *Settings) LoadSettings(path string) string {
    data := readFile(path)
    return parse(data)
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["loader.go", "settings.go"])
    containers = {m["container"] for m in cluster["members"]}
    assert containers == {"Loader", "Settings"}


def test_go_top_level_function_has_no_container(tmp_path):
    _write(tmp_path / "a.go", "package main\n\nfunc F(path string) string {\n    return readFile(path)\n}\n")
    functions = extract_functions(tmp_path / "a.go")
    assert functions[0]["container"] is None


def test_swift_self_navigation_and_bare_call(tmp_path):
    _write(tmp_path / "Loader.swift", """
class Loader {
    func loadConfig(path: String) -> String {
        let data = self.readFile(path)
        return parse(data)
    }
}
""")
    _write(tmp_path / "Settings.swift", """
class Settings {
    func loadSettings(path: String) -> String {
        let data = self.readFile(path)
        return parse(data)
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["Loader.swift", "Settings.swift"])
    assert cluster["avg_jaccard"] == 1.0


def test_kotlin_this_navigation_and_bare_call(tmp_path):
    _write(tmp_path / "Loader.kt", """
class Loader {
    fun loadConfig(path: String): String {
        val data = this.readFile(path)
        return parse(data)
    }
}
""")
    _write(tmp_path / "Settings.kt", """
class Settings {
    fun loadSettings(path: String): String {
        val data = this.readFile(path)
        return parse(data)
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["Loader.kt", "Settings.kt"])
    assert cluster["avg_jaccard"] == 1.0


def test_cpp_inline_method_and_nested_declarator_name(tmp_path):
    _write(tmp_path / "loader.cpp", """
class Loader {
public:
    std::string loadConfig(std::string path) {
        std::string data = readFile(path);
        return parse(data);
    }
};
""")
    _write(tmp_path / "settings.cpp", """
class Settings {
public:
    std::string loadSettings(std::string path) {
        std::string data = readFile(path);
        return parse(data);
    }
};
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["loader.cpp", "settings.cpp"])
    names = {m["name"] for m in cluster["members"]}
    assert names == {"loadConfig", "loadSettings"}


def test_rust_self_parameter_excluded_and_field_expression_call(tmp_path):
    _write(tmp_path / "loader.rs", """
struct Loader;
impl Loader {
    fn load_config(&self, path: &str) -> String {
        let data = self.read_file(path);
        parse(&data)
    }
}
""")
    _write(tmp_path / "settings.rs", """
struct Settings;
impl Settings {
    fn load_settings(&self, path: &str) -> String {
        let data = self.read_file(path);
        parse(&data)
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["loader.rs", "settings.rs"])
    for m in cluster["members"]:
        assert m["param_count"] == 1  # &self excluded


def test_csharp_member_access_expression_call(tmp_path):
    _write(tmp_path / "Loader.cs", """
class Loader {
    string LoadConfig(string path) {
        string data = this.ReadFile(path);
        return Parse(data);
    }
}
""")
    _write(tmp_path / "Settings.cs", """
class Settings {
    string LoadSettings(string path) {
        string data = this.ReadFile(path);
        return Parse(data);
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["Loader.cs", "Settings.cs"])
    assert cluster["avg_jaccard"] == 1.0


def test_php_member_call_and_bare_call(tmp_path):
    _write(tmp_path / "loader.php", """<?php
class Loader {
    function loadConfig($path) {
        $data = $this->readFile($path);
        return parse($data);
    }
}
""")
    _write(tmp_path / "settings.php", """<?php
class Settings {
    function loadSettings($path) {
        $data = $this->readFile($path);
        return parse($data);
    }
}
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["loader.php", "settings.php"])
    assert cluster["avg_jaccard"] == 1.0


def test_ruby_implicit_self_call(tmp_path):
    _write(tmp_path / "loader.rb", """
class Loader
  def load_config(path)
    data = read_file(path)
    parse(data)
  end
end
""")
    _write(tmp_path / "settings.rb", """
class Settings
  def load_settings(path)
    data = read_file(path)
    parse(data)
  end
end
""")
    cluster = _assert_one_cross_file_cluster(tmp_path, ["loader.rb", "settings.rb"])
    assert cluster["avg_jaccard"] == 1.0
