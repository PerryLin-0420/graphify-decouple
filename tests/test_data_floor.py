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


def test_floor_is_one_plus_the_deepest_direct_relationship():
    """Worked example confirmed with the user: a=floor0 (boundary), b calls
    a (floor1), c calls b (floor2). d has TWO direct outgoing calls — to a
    (floor0) and to c (floor2) — of completely different depth. d's floor
    is 1 + the DEEPER of its two direct relationships (c), not the
    shallower one (a): floor(d) == floor(c) + 1, not floor(a) + 1. This is
    the same "1 + max(direct callee floor)" rule applied recursively at
    every hop — not a special case for a single shared target reached via
    a shortcut and a long chain (see test_floor_is_the_longest_chain_...
    above), but the identical rule seen from a node with two DIFFERENT
    direct callees at different depths."""
    g = nx.DiGraph()
    _code(g, "a", "a()", source_file="app/io/a.py")
    _code(g, "b", "b()", source_file="app/core/b.py")
    _code(g, "c", "c()", source_file="app/core/c.py")
    _code(g, "d", "d()", source_file="app/core/d.py")
    g.add_edge("b", "a", relation="calls")
    g.add_edge("c", "b", relation="calls")
    g.add_edge("d", "a", relation="calls")  # shallow direct relationship
    g.add_edge("d", "c", relation="calls")  # deep direct relationship
    floors, _ = compute_floors(g)
    assert floors == {"a": 0, "b": 1, "c": 2, "d": 3}
    assert floors["d"] == floors["c"] + 1


def test_method_edge_is_containment_and_costs_no_floor():
    """A `method` edge is "class C has method m" — two granularities of ONE
    unit, not two stages of a data flow. Charging a floor for it would put
    a class one floor deeper than its own method, which means nothing.
    Here Panel's method calls the boundary directly, so BOTH the method and
    the class it belongs to sit on floor 1 — not the method on 1 and Panel
    on 2."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "panel", "Panel", source_file="app/ui/panel.py", _callable_class=True)
    _code(g, "panel_m", ".refresh()", source_file="app/ui/panel.py")
    g.add_edge("panel", "panel_m", relation="method")
    g.add_edge("panel_m", "boundary", relation="calls")
    floors, _ = compute_floors(g)
    assert floors["panel_m"] == 1
    assert floors["panel"] == 1  # same floor as its method, NOT 2


def test_method_edge_still_carries_the_chain_through_a_class():
    """Zero cost must not mean "ignored": real chains route THROUGH a class
    node (`build() --calls--> Panel --method--> .refresh() --calls-->
    boundary`). Dropping `method` edges outright would disconnect `build`
    from the boundary and leave it with no floor at all (measured on a real
    corpus: coverage fell 41% -> 29%). It stays connected, and only the one
    genuine `calls` hop past the class is charged."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "panel", "Panel", source_file="app/ui/panel.py", _callable_class=True)
    _code(g, "panel_m", ".refresh()", source_file="app/ui/panel.py")
    _code(g, "build", "build()", source_file="app/ui/build.py")
    g.add_edge("panel", "panel_m", relation="method")
    g.add_edge("panel_m", "boundary", relation="calls")
    g.add_edge("build", "panel", relation="calls")  # routes through the class node
    floors, _ = compute_floors(g)
    assert floors["panel"] == 1
    assert floors["build"] == 2  # one real call hop past the class, not two


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


def test_floors_used_are_always_contiguous_no_gap_floors():
    """Reaching floor M requires a chain of M single-hop steps from a
    boundary, and every step of that chain lands on a real node — so
    floor M can never be occupied while some floor below it (down to 0)
    sits empty. Exercised on a shape with a shortcut, a long chain, AND a
    mutual-call cycle folded in, so no single simple path could pass by
    accident."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    for name in ["n1", "n2", "n3", "n4", "n5", "n6"]:
        _code(g, name, f"{name}()", source_file=f"app/core/{name}.py")
    g.add_edge("n1", "boundary", relation="calls")
    g.add_edge("n2", "n1", relation="calls")
    g.add_edge("n3", "n2", relation="calls")
    g.add_edge("n4", "n3", relation="calls")
    g.add_edge("n5", "n4", relation="calls")
    g.add_edge("n5", "n6", relation="calls")  # n5 <-> n6 mutual call (one SCC)
    g.add_edge("n6", "n5", relation="calls")
    floors, _ = compute_floors(g)
    values = sorted(set(floors.values()))
    assert values == list(range(values[0], values[-1] + 1))


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
