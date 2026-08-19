"""Tests for `graphify.data_floor` — data-flow layering.

Pins the distinction the feature rests on: floor 0 is the I/O boundary
(where data enters or leaves the process), and a class straddling several
floors is doing boundary work AND downstream work in one unit — a risk the
call-graph metrics in decouple.py cannot see.
"""
from __future__ import annotations

import networkx as nx

from graphify.data_floor import (
    boundary_reason,
    class_floor_profile,
    compute_floors,
    cross_floor_risk,
)


def _code(g, nid, label, source_file="app/core/thing.py", **kw):
    g.add_node(nid, label=label, file_type="code", source_file=source_file, **kw)


# ── boundary detection ───────────────────────────────────────────────────────

def test_boundary_detected_from_path_token():
    g = nx.DiGraph()
    _code(g, "n", "NetworkData", source_file="app/parser/touchstone_parser.py")
    assert "parser" in boundary_reason(g, "n")


def test_boundary_detected_from_symbol_name():
    g = nx.DiGraph()
    _code(g, "n", "load_config()", source_file="app/core/thing.py")
    assert "load" in boundary_reason(g, "n")


def test_plain_domain_node_is_not_a_boundary():
    g = nx.DiGraph()
    _code(g, "n", "compute_average()", source_file="app/core/stats.py")
    assert boundary_reason(g, "n") is None


def test_prose_nodes_are_never_boundaries():
    """A rationale/docstring node whose LABEL IS PROSE will match name
    tokens constantly ("Parse an .s2p file into a TraceSource...") and mean
    nothing about I/O. Measured on a real corpus: 52 of 158 floor-0 hits
    were prose nodes, every one a false positive."""
    g = nx.DiGraph()
    g.add_node("doc", label="Parse an .s2p file into a TraceSource (raises on failure).",
               file_type="rationale", source_file="app/parser/touchstone_parser.py")
    g.add_node("concept", label="Data loading pipeline", file_type="concept", source_file="")
    assert boundary_reason(g, "doc") is None
    assert boundary_reason(g, "concept") is None


def test_path_token_matches_whole_tokens_not_substrings():
    """"io" must not fire on "distribution"."""
    g = nx.DiGraph()
    _code(g, "n", "DistributionDialog", source_file="app/ui/distribution_dialog.py")
    assert boundary_reason(g, "n") is None


# ── compute_floors ───────────────────────────────────────────────────────────

def test_floors_increase_toward_callers_of_the_boundary():
    """mid calls parser, ui calls mid: floor increases one hop per caller
    away from the boundary, not one hop per callee."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "mid", "transform()", source_file="app/core/c.py")
    _code(g, "ui", "render()", source_file="app/ui/u.py")
    g.add_edge("mid", "parser", relation="calls")
    g.add_edge("ui", "mid", relation="calls")
    floors, reasons = compute_floors(g)
    assert floors == {"parser": 0, "mid": 1, "ui": 2}
    assert "parser" in reasons


def test_floor_is_the_longest_chain_not_the_shortest_shortcut():
    """x is reachable from the boundary via a direct 1-hop shortcut AND via
    a 3-hop chain through b/c. x's floor must reflect the longer chain (3),
    not the shortcut (1) — reporting the shortcut would hide how deep x's
    actual dependency really goes."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "x", "compute()", source_file="app/core/x.py")
    _code(g, "b", "step_b()", source_file="app/core/b.py")
    _code(g, "c", "step_c()", source_file="app/core/c.py")
    g.add_edge("x", "boundary", relation="calls")  # shortcut: x is 1 hop from boundary
    g.add_edge("b", "boundary", relation="calls")
    g.add_edge("c", "b", relation="calls")
    g.add_edge("x", "c", relation="calls")  # long chain: x -> c -> b -> boundary (3 hops)
    floors, _ = compute_floors(g)
    assert floors["x"] == 3


def test_mutually_calling_pair_shares_one_floor():
    """a and b call each other (a genuine cycle, not a chain) — they form
    one strongly-connected component and must share a single floor rather
    than each claiming a distance from the other."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "a", "step_a()", source_file="app/core/a.py")
    _code(g, "b", "step_b()", source_file="app/core/b.py")
    g.add_edge("a", "boundary", relation="calls")
    g.add_edge("a", "b", relation="calls")
    g.add_edge("b", "a", relation="calls")  # a <-> b mutual calls
    floors, _ = compute_floors(g)
    assert floors["a"] == floors["b"] == 1


def test_no_boundary_yields_no_floors_not_a_fabricated_layering():
    g = nx.DiGraph()
    _code(g, "a", "compute()", source_file="app/core/a.py")
    _code(g, "b", "adjust()", source_file="app/core/b.py")
    g.add_edge("a", "b", relation="calls")
    floors, reasons = compute_floors(g)
    assert floors == {}
    assert reasons == {}


def test_unreachable_component_has_no_floor_rather_than_zero():
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "island", "compute()", source_file="app/core/a.py")
    floors, _ = compute_floors(g)
    assert floors == {"parser": 0}
    assert "island" not in floors  # absent, NOT floor 0


def test_caller_of_the_boundary_is_one_floor_up():
    """A parser CALLED BY a controller still supplies data to it — floor is
    measured against call direction (caller = boundary's floor + 1), not
    along it, since a boundary node's own callees (if any) are not what
    makes it downstream of anything."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "caller", "controller()", source_file="app/ui/u.py")
    g.add_edge("caller", "parser", relation="calls")  # caller calls parser
    floors, _ = compute_floors(g)
    assert floors["caller"] == 1


# ── class_floor_profile / cross_floor_risk ──────────────────────────────────

def test_profile_reports_span_across_floors():
    g = nx.DiGraph()
    _code(g, "cls", "Dialog", source_file="app/ui/d.py")
    floors = {"cls": 1, "m0": 0, "m1": 2, "m2": 2}
    profile = class_floor_profile(g, "cls", ["m0", "m1", "m2"], floors)
    assert profile["min_floor"] == 0
    assert profile["max_floor"] == 2
    assert profile["floor_span"] == 2
    assert profile["floor"] == 2  # modal floor


def test_profile_dominant_floor_breaks_ties_toward_the_earlier_stage():
    g = nx.DiGraph()
    _code(g, "cls", "Thing", source_file="app/core/t.py")
    floors = {"m0": 1, "m1": 3}  # one each -> tie
    profile = class_floor_profile(g, "cls", ["m0", "m1"], floors)
    assert profile["floor"] == 1


def test_profile_is_none_when_nothing_has_a_known_floor():
    g = nx.DiGraph()
    _code(g, "cls", "Thing", source_file="app/core/t.py")
    assert class_floor_profile(g, "cls", ["m0"], {}) is None


def test_cross_floor_risk_grows_with_span_and_is_zero_for_unknown():
    single = {"floor_span": 0}
    wide = {"floor_span": 4}
    assert cross_floor_risk(single) == 0.0
    assert cross_floor_risk(wide) == 100.0
    assert cross_floor_risk({"floor_span": 2}) == 50.0
    # unknown profile is NOT scored as clean-and-penalized, it is skipped
    assert cross_floor_risk(None) == 0.0
