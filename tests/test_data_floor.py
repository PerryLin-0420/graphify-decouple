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
    compute_floors_with_provenance,
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


def test_intra_module_calls_do_not_add_floors():
    """A chain of calls inside ONE source file describes that module's own
    internal composition, not data moving through stages. The real case:
    `FilesPanel.set_sources() -> _FileRow -> _populate_detail_panel()` sat
    on three consecutive floors, all inside files_panel.py. Here a->b->c
    are all in panel.py and must share one floor; only the cross-file hop
    into the boundary's module costs anything."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "a", "outer()", source_file="app/ui/panel.py")
    _code(g, "b", "middle()", source_file="app/ui/panel.py")
    _code(g, "c", "inner()", source_file="app/ui/panel.py")
    g.add_edge("a", "b", relation="calls")  # intra-module: free
    g.add_edge("b", "c", relation="calls")  # intra-module: free
    g.add_edge("c", "boundary", relation="calls")  # crosses modules: costs 1
    floors, _ = compute_floors(g)
    assert floors["a"] == floors["b"] == floors["c"] == 1


def test_cross_module_calls_still_cost_a_floor_each():
    """The intra-module discount must not flatten genuinely separate
    modules — each hop between different files still costs one floor."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "a", "a()", source_file="app/one.py")
    _code(g, "b", "b()", source_file="app/two.py")
    g.add_edge("a", "b", relation="calls")
    g.add_edge("b", "boundary", relation="calls")
    floors, _ = compute_floors(g)
    assert floors["b"] == 1
    assert floors["a"] == 2


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


# ── parallel pass: a non-call edge to a known floor is not "unknown" ───

def test_a_unit_wired_to_floor_zero_by_a_non_call_edge_is_placed_on_floor_zero():
    """The contradiction this pass removes: `helper` has a real, visible
    edge to a floor-0 parser — just not a call-shaped one, so no distance
    to it can be MEASURED. Reporting it as unknown while the 3D view drew
    that very link said two different things about the same node. It sits
    ALONGSIDE the boundary, so it is placed on floor 0 — parallel, at zero
    cost, never one floor below."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "helper", "Helper", source_file="app/core/helper.py")
    g.add_edge("helper", "parser", relation="imports")
    floors, _ = compute_floors(g)
    assert floors["helper"] == 0


def test_parallel_placement_never_deepens_the_stack():
    """Zero cost is the whole reason these edge kinds can be used here at
    all: charging them a floor is the documented failure (`rationale_for`
    nodes inheriting their subject's floor + 1 pushed the tallest floor
    past 20 out of documentation alone). The tallest floor must be the same
    with and without the parallel edge."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "a", "a()", source_file="app/one.py")
    _code(g, "b", "b()", source_file="app/two.py")
    g.add_edge("a", "b", relation="calls")
    g.add_edge("b", "boundary", relation="calls")
    tallest_before = max(compute_floors(g)[0].values())
    _code(g, "doc_ish", "Notes", source_file="app/core/notes.py")
    g.add_edge("doc_ish", "a", relation="references")  # a sits at floor 2
    floors, _ = compute_floors(g)
    assert floors["doc_ish"] == 2  # same floor as `a`, not 3
    assert max(floors.values()) == tallest_before


def test_parallel_pass_never_overwrites_a_call_measured_floor():
    """A measured distance always wins over adjacency. `b` is two hops from
    the boundary by call structure AND directly adjacent to it by an
    `imports` edge — it stays on floor 2."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "a", "a()", source_file="app/one.py")
    _code(g, "b", "b()", source_file="app/two.py")
    g.add_edge("a", "boundary", relation="calls")
    g.add_edge("b", "a", relation="calls")
    g.add_edge("b", "boundary", relation="imports")  # adjacency to floor 0
    floors, _ = compute_floors(g)
    assert floors["b"] == 2


def test_parallel_takes_the_shallowest_reachable_known_floor():
    """Adjacent to both a floor-0 unit and a floor-2 one, the shallow
    evidence wins — the rescue pass's question ("is there close evidence"),
    not the main pass's ("what is the worst dependency")."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "mid", "mid()", source_file="app/one.py")
    _code(g, "deep", "deep()", source_file="app/two.py")
    g.add_edge("mid", "boundary", relation="calls")
    g.add_edge("deep", "mid", relation="calls")  # deep sits at floor 2
    _code(g, "shared", "Shared", source_file="app/util/shared.py")
    g.add_edge("shared", "boundary", relation="uses")
    g.add_edge("shared", "deep", relation="uses")
    floors, _ = compute_floors(g)
    assert floors["deep"] == 2
    assert floors["shared"] == 0


def test_parallel_relays_through_unplaced_units_but_not_through_placed_ones():
    """A chain of unplaced units hanging off a known floor all lands on it
    (`far` is connected to the system, just further along the same chain of
    non-call edges). But an already-measured unit is a SOURCE, never a
    relay: `behind` reaches floor 0 only THROUGH the floor-2 `deep`, so it
    is placed at 2, not tunneled to 0 past it."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "mid", "mid()", source_file="app/one.py")
    _code(g, "deep", "deep()", source_file="app/two.py")
    g.add_edge("mid", "boundary", relation="calls")
    g.add_edge("deep", "mid", relation="calls")  # floor 2

    _code(g, "near", "Near", source_file="app/util/near.py")
    _code(g, "far", "Far", source_file="app/util/far.py")
    g.add_edge("near", "boundary", relation="uses")
    g.add_edge("far", "near", relation="uses")  # relayed via an unplaced unit
    _code(g, "behind", "Behind", source_file="app/util/behind.py")
    g.add_edge("behind", "deep", relation="uses")  # only route out is via floor 2
    floors, _ = compute_floors(g)
    assert floors["near"] == 0
    assert floors["far"] == 0
    assert floors["behind"] == 2


def test_a_non_code_node_is_never_given_a_parallel_floor():
    """Same restriction `boundary_reason` applies, for the same reason: a
    docstring node has no position in a data flow to report. It can be
    adjacent to one — that is what `rationale_for` MEANS — but documenting
    a parser is not doing parser-stage work, and letting prose nodes carry
    floors would also let them relay one between two unrelated units."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    g.add_node("_rationale_1", label="Parses the touchstone file into records.",
               file_type="rationale", source_file="app/parser/p.py")
    g.add_edge("_rationale_1", "parser", relation="rationale_for")
    floors, _ = compute_floors(g)
    assert floors == {"parser": 0}


def test_an_attribute_less_edge_endpoint_is_still_eligible_for_a_parallel_floor():
    """`networkx.node_link_graph` auto-creates a bare, ZERO-attribute node
    for any edge endpoint the JSON never explicitly declared — this is
    exactly what an external package reference looks like in a real
    multi-language corpus (`imports_from` naming `react`, a Rust crate, an
    Android API class round-trips with NO `file_type` at all). The old
    `== "code"` eligibility check excluded these from ever getting a
    floor, contradicting a real, drawn `imports_from` edge from a measured
    file — measured on a real corpus (TS/TSX + Rust + Kotlin): 47 such
    nodes, 116 links reporting "unknown" while visibly wired to a known
    floor. `file_type` unset must be treated as "not verified non-code",
    not lumped in with rationale/concept/document."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    g.add_node("ref_react")  # no attributes at all, same as node_link_graph produces
    g.add_edge("parser", "ref_react", relation="imports_from")
    floors, _ = compute_floors(g)
    assert floors["parser"] == 0
    assert floors["ref_react"] == 0  # placed alongside it, not left unknown


def test_a_unit_with_no_edge_to_any_known_floor_is_the_only_real_unknown():
    """What "unknown" means after this pass: not "no call path", but "no
    path of ANY edge kind". `island` is wired to another unplaced unit and
    to nothing else — the whole component is unmeasured, so both stay
    absent rather than being defaulted to floor 0."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "island", "compute()", source_file="app/core/a.py")
    _code(g, "island2", "adjust()", source_file="app/core/b.py")
    g.add_edge("island", "island2", relation="uses")
    floors, _ = compute_floors(g)
    assert floors == {"parser": 0}


def test_provenance_records_which_pass_placed_each_unit():
    """The three passes are three strengths of evidence, and a report that
    shows them as one number cannot be audited: a floor 0 measured by a
    call chain into a parser and a floor 0 inherited from sitting next to
    one are not the same claim."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "caller", "orchestrate()", source_file="app/core/run.py")
    g.add_edge("caller", "parser", relation="calls")
    _code(g, "built", "Record", source_file="app/model/record.py")
    g.add_edge("parser", "built", relation="calls")  # constructed BY the boundary
    _code(g, "neighbor", "Neighbor", source_file="app/util/n.py")
    g.add_edge("neighbor", "parser", relation="imports")
    floors, reasons, provenance = compute_floors_with_provenance(g)
    assert provenance["parser"] == "boundary"
    assert provenance["caller"] == "call"
    assert provenance["built"] == "rescue"
    assert provenance["neighbor"] == "parallel"
    assert set(provenance) == set(floors)
    assert set(reasons) == {"parser"}


# ── rescue pass: floor via a known-floor CALLER, not just own calls ─────────

def test_a_leaf_constructed_by_the_boundary_is_rescued_to_floor_one():
    """TraceSource(parsed_data), built directly inside a parser, makes no
    calls of its own that reach anywhere — the main pass leaves it with no
    floor. But being constructed BY a floor-0 function is real evidence of
    proximity, rescued to floor max(1, 0-1)=1 — never floor 0 itself, which
    is reserved for the boundary, not merely something built next to it."""
    g = nx.DiGraph()
    _code(g, "parser", "parse_file()", source_file="app/parser/p.py")
    _code(g, "tracesource", "TraceSource", source_file="app/model/trace_source.py")
    g.add_edge("parser", "tracesource", relation="calls")
    floors, _ = compute_floors(g)
    assert floors["tracesource"] == 1


def test_rescue_uses_the_closest_caller_not_the_farthest():
    """A shared utility called by both a floor-0 boundary AND some deep,
    unrelated floor-4 orchestrator must be rescued via the CLOSE evidence
    (floor 0 caller), not dragged down by the deep one — the rescue pass
    asks "is there close evidence", the opposite question from the main
    pass's "what is the worst dependency", so it takes the MIN caller."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    for name in ("n1", "n2", "n3", "n4"):
        _code(g, name, f"{name}()", source_file=f"app/core/{name}.py")
    g.add_edge("n1", "boundary", relation="calls")
    g.add_edge("n2", "n1", relation="calls")
    g.add_edge("n3", "n2", relation="calls")
    g.add_edge("n4", "n3", relation="calls")  # n4 sits at floor 4

    _code(g, "util", "SharedUtil", source_file="app/util/shared.py")
    g.add_edge("boundary", "util", relation="calls")  # close: floor-0 caller
    g.add_edge("n4", "util", relation="calls")  # far: floor-4 caller

    floors, _ = compute_floors(g)
    assert floors["n4"] == 4
    assert floors["util"] == 1  # rescued via boundary (min caller), not n4


def test_rescue_and_main_pass_alternate_to_extend_a_chain():
    """A unit rescued via a known-floor CALLER is not the end of the
    story: once `a` is rescued to floor 1 (boundary constructs it
    directly), `b` — which calls `a` in the NORMAL orchestration sense —
    must extend outward through the MAIN pass's own rule (floor(caller) =
    floor(callee) + 1), landing on floor 2, not get capped at 1 by the
    rescue rule too. `c`, which calls `b`, continues the same way to floor
    3. Rescue seeds a starting point; the main pass still governs normal
    call chains built on top of it."""
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/core/thing.py")
    _code(g, "a", "A", source_file="app/model/a.py")
    _code(g, "b", "B", source_file="app/model/b.py")
    _code(g, "c", "C", source_file="app/model/c.py")
    g.add_edge("boundary", "a", relation="calls")  # a is constructed BY the boundary
    g.add_edge("b", "a", relation="calls")  # b calls a normally
    g.add_edge("c", "b", relation="calls")  # c calls b normally
    floors, _ = compute_floors(g)
    assert floors["a"] == 1  # rescued: boundary (floor 0) constructs it
    assert floors["b"] == 2  # normal caller-direction growth on top of the rescue
    assert floors["c"] == 3


def test_rescue_does_not_apply_to_a_unit_with_no_known_floor_caller_either():
    """A unit whose only caller ALSO has no floor stays unfloored — the
    rescue pass requires real evidence (a caller that is itself
    positioned), not a chain of mutual guesses."""
    g = nx.DiGraph()
    _code(g, "a", "A", source_file="app/model/a.py")
    _code(g, "b", "B", source_file="app/model/b.py")
    g.add_edge("b", "a", relation="calls")  # neither reaches any boundary
    floors, _ = compute_floors(g)
    assert floors == {}


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


def test_profile_reports_how_much_of_the_unit_was_measured():
    """`floor_evidence` is the share of members whose floor is known. A
    proposed group is passed class_id=None and has no class node of its
    own, so counting one would understate its evidence."""
    g = nx.DiGraph()
    _code(g, "cls", "Dialog", source_file="app/ui/d.py")
    floors = {"cls": 1, "m0": 0, "m1": 2}
    # class: 3 of 4 known (cls + 3 members)
    profile = class_floor_profile(g, "cls", ["m0", "m1", "m2"], floors)
    assert profile["members_total"] == 4
    assert profile["floor_evidence"] == 0.75
    # group (class_id=None): 2 of 3 members known, no phantom class node
    group = class_floor_profile(g, None, ["m0", "m1", "m2"], floors)
    assert group["members_total"] == 3
    assert group["floor_evidence"] == round(2 / 3, 2)


def test_cross_floor_risk_scales_down_when_span_rests_on_few_members():
    """The weakest evidence must not produce the strongest penalty. The
    same span of 4 scores full risk when every member was measured, and
    proportionally less when the span rests on a fraction of them — the
    real case this guards: a span of 6 built from 3 of 7 members added 30
    points of split risk and flipped a class's verdict."""
    fully_measured = {"floor_span": 4, "floor_evidence": 1.0}
    barely_measured = {"floor_span": 4, "floor_evidence": 0.25}
    assert cross_floor_risk(fully_measured) == 100.0
    assert cross_floor_risk(barely_measured) == 25.0
    # a profile without the field predates the weighting — not silently zeroed
    assert cross_floor_risk({"floor_span": 4}) == 100.0


def test_parallel_members_never_outvote_measured_ones_for_a_units_floor():
    """A unit's floor is a majority vote over its members, so without this
    rule the weaker evidence wins simply by being more numerous. The real
    case, on AutoCheck: a module region with 3 members measured at floor 1
    and 5 placed alongside floor 0 flipped from floor 1 to floor 0 — the
    parallel pass was supposed to ADD coverage for unplaced units, not
    restate where already-measured ones live."""
    g = nx.DiGraph()
    _code(g, "cls", "Widget", source_file="app/ui/w.py")
    floors = {"m0": 1, "m1": 1, "m2": 1, "p0": 0, "p1": 0, "p2": 0, "p3": 0, "p4": 0}
    measured = {"m0", "m1", "m2"}
    members = ["m0", "m1", "m2", "p0", "p1", "p2", "p3", "p4"]
    profile = class_floor_profile(g, None, members, floors, measured=measured)
    assert profile["floor"] == 1  # the 3 measured members, not the 5 parallel ones
    assert profile["floor_basis"] == "measured"
    assert profile["members_with_known_floor"] == 3
    # Without the measured set, the old majority-vote behavior is unchanged.
    assert class_floor_profile(g, None, members, floors)["floor"] == 0


def test_a_unit_with_only_parallel_members_falls_back_to_them():
    """The coverage the parallel pass exists to add: a unit with NO member
    measured along call structure is placed where its neighbors are rather
    than reported as having no floor — and says which kind of evidence
    that was."""
    g = nx.DiGraph()
    floors = {"p0": 2, "p1": 2}
    profile = class_floor_profile(g, None, ["p0", "p1"], floors, measured=set())
    assert profile["floor"] == 2
    assert profile["floor_basis"] == "parallel"


