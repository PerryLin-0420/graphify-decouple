"""Tests for `graphify.decouple_3d` — data-flow floors stacked on Z.

Pins the before/after comparison the view exists to make possible: a
class with a RECOMMENDED split gets its proposed groups rendered as
separate "after" regions, each on its OWN floor — the only way to see
whether a split (which groups by community/coupling) actually reduces
cross-floor spread, or just moves it around.
"""
from __future__ import annotations

import networkx as nx

from graphify.decouple import _class_cluster_layout, decouple_plan
from graphify.decouple_3d import (
    _aggregate_region_links,
    _proposed_group_regions,
    build_floor_scene,
    write_decouple_3d_html,
)
from graphify.exporters.base import COMMUNITY_COLORS


def _code(g, nid, label, source_file, **kw):
    g.add_node(nid, label=label, file_type="code", source_file=source_file, **kw)


def _build_graph():
    """One class ("Loader") at the I/O boundary (floor 0), one god_object
    class ("Dialog") whose 6 members split across TWO communities (so
    decouple_plan actually recommends a split) — group A calls straight
    into the loader (floor 1), group B sits two hops further away
    (floor 3) — so the two proposed groups land on DIFFERENT floors from
    each other and from Dialog's own dominant floor. A free function pair
    forms a module region."""
    g = nx.DiGraph()
    _code(g, "loader", "Loader", "app/io/loader.py", _callable_class=True)
    for i in range(3):
        _code(g, f"lm{i}", f".load_{i}()", "app/io/loader.py")
        g.add_edge("loader", f"lm{i}", relation="method", confidence="EXTRACTED")

    _code(g, "dialog", "Dialog", "app/ui/dialog.py", _callable_class=True)
    for i in range(6):
        _code(g, f"dm{i}", f".dm{i}()", "app/ui/dialog.py")
        g.add_edge("dialog", f"dm{i}", relation="method", confidence="EXTRACTED")
    # Group A (dm0-dm2): one hop from the loader -> floor 1.
    g.add_edge("dm0", "lm0", relation="calls", confidence="EXTRACTED")
    g.add_edge("dm1", "dm0", relation="calls", confidence="EXTRACTED")
    g.add_edge("dm2", "dm0", relation="calls", confidence="EXTRACTED")
    # Group B (dm3-dm5): three hops from the loader -> floor 3.
    g.add_edge("dm3", "dm2", relation="calls", confidence="EXTRACTED")
    g.add_edge("dm4", "dm3", relation="calls", confidence="EXTRACTED")
    g.add_edge("dm5", "dm3", relation="calls", confidence="EXTRACTED")
    # A couple of external callers so member_ratio/afferent stay realistic.
    for i in range(2):
        g.add_node(f"caller{i}", label=f"caller{i}()", file_type="code", source_file="app/ui/caller.py")
        g.add_edge(f"caller{i}", "dialog", relation="calls", confidence="EXTRACTED")

    _code(g, "free_a", "helper_a()", "app/util/tools.py")
    _code(g, "free_b", "helper_b()", "app/util/tools.py")
    return g


def _floors_for(g):
    from graphify.data_floor import compute_floors
    return compute_floors(g)[0]


# ── Z-axis floor compaction ──────────────────────────────────────────────────

def test_floor_rank_compacts_gaps_between_occupied_floors(tmp_path):
    """Floors 2, 3, and 4 exist in the raw graph (a real chain runs through
    them) but resolve to no region and no rendered member: these are
    docstring nodes that document nothing and belong to no file, the one
    category `_class_cluster_layout` still cannot place. Those unoccupied
    floors must not stretch the Z axis: `floors`/`floor_rank` should list
    and rank only 0, 1, 5 — dense, with no reserved slot for the empty
    ones in between."""
    g = nx.DiGraph()
    _code(g, "loader", "Loader", "app/io/loader.py", _callable_class=True)  # floor 0, a boundary
    _code(g, "loader_m", ".load()", "app/io/loader.py")
    g.add_edge("loader", "loader_m", relation="method", confidence="EXTRACTED")

    _code(g, "near", "Near", "app/ui/near.py", _callable_class=True)
    _code(g, "near_m", ".m()", "app/ui/near.py")
    g.add_edge("near", "near_m", relation="method", confidence="EXTRACTED")
    g.add_edge("near_m", "loader_m", relation="calls", confidence="EXTRACTED")  # floor 1

    # A real chain through nodes that never resolve into any region: a
    # docstring with no `rationale_for` subject AND no source_file has
    # neither of the two things that would place it. Floors 2, 3, 4 are
    # genuine but nothing ever gets drawn there.
    g.add_node("r2", label="r2", file_type="rationale")
    g.add_node("r3", label="r3", file_type="rationale")
    g.add_node("r4", label="r4", file_type="rationale")
    g.add_edge("r2", "near_m", relation="calls")
    g.add_edge("r3", "r2", relation="calls")
    g.add_edge("r4", "r3", relation="calls")

    _code(g, "far", "Far", "app/ui/far.py", _callable_class=True)
    _code(g, "far_m", ".m()", "app/ui/far.py")
    g.add_edge("far", "far_m", relation="method", confidence="EXTRACTED")
    g.add_edge("far_m", "r4", relation="calls", confidence="EXTRACTED")  # floor 5

    plan = decouple_plan(g, {}, top_n=20, min_group_size=1)
    out = tmp_path / "DECOUPLE_3D.html"
    write_decouple_3d_html(g, plan, {}, out)
    html = out.read_text(encoding="utf-8")
    import json as _json
    import re as _re
    m = _re.search(r"const SCENE = (\{.*?\});\s*\n\nconst view", html, _re.S)
    assert m, "could not locate the embedded SCENE payload"
    scene = _json.loads(m.group(1))

    assert scene["floors"] == [0, 1, 5]
    assert scene["floor_rank"] == {"0": 0, "1": 1, "5": 2}


# ── build_floor_scene ────────────────────────────────────────────────────────

def test_build_floor_scene_places_region_on_dominant_floor():
    g = _build_graph()
    floors = _floors_for(g)
    _positions, discs, region_members = _class_cluster_layout(g)
    payload = build_floor_scene(g, discs, _positions, region_members, floors, COMMUNITY_COLORS)
    by_label = {r["label"]: r for r in payload["regions"]}
    assert by_label["Loader"]["floor"] == 0
    assert by_label["Loader"]["spans"] == 0


def test_build_floor_scene_reuses_2d_member_positions_exactly():
    """Every member point's (x, y) must be the SAME value
    _class_cluster_layout computed — not a separately recomputed scatter
    (an earlier version used a JS sine-hash that drifted from the 2D
    layout and looked artificially regular)."""
    g = _build_graph()
    floors = _floors_for(g)
    positions, discs, region_members = _class_cluster_layout(g)
    payload = build_floor_scene(g, discs, positions, region_members, floors, COMMUNITY_COLORS)
    dialog = next(r for r in payload["regions"] if r["label"] == "Dialog")
    for m in dialog["members"]:
        # find the matching node by label to cross-check its 2D position
        matches = [nid for nid, p in positions.items() if p["x"] == m["x"] and p["y"] == m["y"]]
        assert matches, f"no 2D position matches member point {m}"


def test_build_floor_scene_renders_unknown_floor_region_on_a_dedicated_band():
    """A region with no determinable floor is NOT dropped — it is rendered
    with floor=None, its own "unknown" band distinct from the numbered
    stack. Dropping it outright (the earlier behavior) silently erased
    every real link to or from it too, not just its own disc — measured on
    a real corpus: a test file with 37 genuine cross-file calls looked
    completely disconnected because its only targets had no known floor."""
    g = nx.DiGraph()
    _code(g, "island", "Island", "app/isolated.py", _callable_class=True)
    for i in range(3):
        _code(g, f"im{i}", f".m{i}()", "app/isolated.py")
        g.add_edge("island", f"im{i}", relation="method", confidence="EXTRACTED")
    _positions, discs, region_members = _class_cluster_layout(g)
    payload = build_floor_scene(g, discs, _positions, region_members, {}, COMMUNITY_COLORS)
    assert len(payload["regions"]) == 1
    region = payload["regions"][0]
    assert region["floor"] is None
    assert region["min_floor"] is None and region["max_floor"] is None and region["spans"] is None
    # None must never leak into the NUMBERED floor list — it has its own band
    assert None not in payload["floors"]


def test_a_unit_wired_only_by_a_non_call_edge_is_placed_parallel_not_unknown():
    """Known (floor 1) reaches Unknown by a `references` edge only — not
    call-shaped, so neither the main pass nor the rescue pass can measure a
    distance to it. It is still WIRED to a measured unit, so it is placed
    ALONGSIDE that unit (same floor, zero-cost parallel placement) rather
    than reported as unmeasurable: "unknown" is reserved for a unit with no
    path of any edge kind to a known floor, which Island below is and this
    is not.

    Also guards the original bug: an unplaced region used to be dropped
    outright, which erased every real link to or from it too, making a
    perfectly normal caller look disconnected for a reason having nothing
    to do with its own connectivity. Links must survive either way.
    """
    g = nx.DiGraph()
    _code(g, "boundary", "load_config()", source_file="app/io/thing.py")
    _code(g, "known", "Known", source_file="app/known.py", _callable_class=True)
    _code(g, "known_m", ".go()", source_file="app/known.py")
    g.add_edge("known", "known_m", relation="method", confidence="EXTRACTED")
    g.add_edge("known_m", "boundary", relation="calls", confidence="EXTRACTED")

    _code(g, "unknown", "Unknown", source_file="app/isolated.py", _callable_class=True)
    for i in range(3):
        _code(g, f"um{i}", f".m{i}()", source_file="app/isolated.py")
        g.add_edge("unknown", f"um{i}", relation="method", confidence="EXTRACTED")
    # A real structural edge, but not call-shaped: no distance to measure,
    # yet real evidence that this unit sits alongside a measured one.
    g.add_edge("known_m", "um0", relation="references", confidence="EXTRACTED")

    # Nothing connects to this one at all — the only genuine unknown here.
    _code(g, "island", "Island", source_file="app/island.py", _callable_class=True)
    _code(g, "island_m", ".alone()", source_file="app/island.py")
    g.add_edge("island", "island_m", relation="method", confidence="EXTRACTED")

    floors = _floors_for(g)
    positions, discs, region_members = _class_cluster_layout(g)
    payload = build_floor_scene(g, discs, positions, region_members, floors, COMMUNITY_COLORS)
    by_label = {r["label"]: r for r in payload["regions"]}
    assert by_label["Known"]["floor"] == 1
    assert by_label["Unknown"]["floor"] == 1  # parallel to its one neighbor
    assert by_label["Island"]["floor"] is None  # no edge to any known floor
    pairs = {(l["source"], l["target"]) for l in payload["links"]}
    assert ("known", "unknown") in pairs


# ── _proposed_group_regions (the before/after "after" half) ────────────────

def test_proposed_group_regions_only_for_recommended_splits():
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)
    after, _member_to_after_region = _proposed_group_regions(g, plan, discs, _positions, floors)
    # Only entries with risk.recommendation == "split" contribute — a class
    # with nothing recommended must contribute nothing, not an empty-looking
    # region.
    for r in after:
        entry = next(e for e in plan["god_nodes"] if e["id"] == r["replaces"])
        assert entry["risk"]["recommendation"] == "split"


def test_proposed_group_regions_get_their_own_floor_not_the_original_class():
    """The entire point: a proposed group's floor is computed from ITS OWN
    members, independently of the original class's dominant floor."""
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)
    after, _member_to_after_region = _proposed_group_regions(g, plan, discs, _positions, floors)
    assert after, "expected at least one proposed group region in this fixture"
    for r in after:
        member_floors = [m["floor"] for m in r["members"]]
        assert r["floor"] in member_floors  # dominant floor came from ITS OWN members
        assert r["state"] == "after"


def test_proposed_group_regions_positioned_near_original_disc():
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)
    after, _member_to_after_region = _proposed_group_regions(g, plan, discs, _positions, floors)
    for r in after:
        ax, ay, aradius = discs[r["replaces"]]
        dist = ((r["x"] - ax) ** 2 + (r["y"] - ay) ** 2) ** 0.5
        assert dist <= aradius + 1e-6  # orbits within the original disc's own radius


def test_proposed_group_regions_read_floor_profile_not_recompute():
    """decouple_plan attaches floor_profile to each proposed group ONCE
    (see split_risk_score's docstring: "graphify decouple --3d visualizes
    the plan decouple_plan already built; it does not run its own floor
    analysis"). Tampering with the attached value must change what
    _proposed_group_regions reports — proving it reads that field rather
    than recomputing floors from the raw `floors` dict itself."""
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)

    dialog_entry = next(e for e in plan["god_nodes"] if e["label"] == "Dialog")
    real_group = next(gr for gr in dialog_entry["proposed_groups"] if gr.get("floor_profile"))
    real_group["floor_profile"] = {"floor": 99, "min_floor": 99, "max_floor": 99, "floor_span": 0}

    after, _m = _proposed_group_regions(g, plan, discs, _positions, floors)
    tampered = next(r for r in after if r["label"] == real_group["name"])
    assert tampered["floor"] == 99


def test_proposed_group_regions_member_scatter_is_organic_and_within_disc():
    """Members inside a proposed group's disc must NOT sit on a regular
    ring (a real bug this replaced: an earlier version reused each
    member's OLD position from the original class's larger disc, which
    routinely landed outside the new, smaller disc entirely)."""
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)
    after, _m = _proposed_group_regions(g, plan, discs, _positions, floors)
    assert after
    for r in after:
        for m in r["members"]:
            dist = ((m["x"] - r["x"]) ** 2 + (m["y"] - r["y"]) ** 2) ** 0.5
            assert dist <= r["r"] + 1e-6, f"{m['label']} sits outside its own group's disc"


def test_proposed_group_regions_deterministic_scatter():
    """Same graph -> same scatter every time (0-LLM, no randomness) —
    calling twice must produce identical member coordinates."""
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    floors = _floors_for(g)
    _positions, discs, _region_members = _class_cluster_layout(g)
    after1, _ = _proposed_group_regions(g, plan, discs, _positions, floors)
    after2, _ = _proposed_group_regions(g, plan, discs, _positions, floors)
    assert [r["members"] for r in after1] == [r["members"] for r in after2]


# ── _aggregate_region_links ─────────────────────────────────────────────────

def test_aggregate_region_links_excludes_same_region_and_counts_weight():
    g = nx.DiGraph()
    for n in ["a1", "a2", "b1"]:
        g.add_node(n)
    g.add_edge("a1", "a2")   # same region -> internal, excluded
    g.add_edge("a1", "b1")   # cross-region
    g.add_edge("a2", "b1")   # cross-region, same pair direction combo differs but source differs
    node_region = {"a1": "A", "a2": "A", "b1": "B"}
    links = _aggregate_region_links(g, node_region, {"A", "B"})
    assert links == [{"source": "A", "target": "B", "weight": 2}]


# ── write_decouple_3d_html: link redirection (the "after" wiring) ──────────

def test_write_decouple_3d_html_redirects_links_for_after_state(tmp_path):
    """The core fix: toggling "Preview decoupled view" must not just move
    the discs — the WIRES between them must reflect the split too. Group A
    (dm0-dm2) and group B (dm3-dm5) have a real edge between them
    (dm3->dm2) that is invisible today (intra-class) and becomes an
    explicit inter-region link only in the "after" state."""
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    out = tmp_path / "DECOUPLE_3D.html"
    write_decouple_3d_html(g, plan, communities, out)
    html = out.read_text(encoding="utf-8")
    assert '"links_after"' in html
    # the before link set must NOT already contain a Dialog-group-to-
    # Dialog-group pair (that call was intra-class before any split) —
    # only the after set redirects it into a visible cross-region link.
    import json as _json
    import re as _re
    m = _re.search(r"const SCENE = (\{.*?\});\s*\n\nconst view", html, _re.S)
    assert m, "could not locate the embedded SCENE payload"
    scene = _json.loads(m.group(1))
    before_pairs = {(l["source"], l["target"]) for l in scene["links"]}
    after_pairs = {(l["source"], l["target"]) for l in scene["links_after"]}
    proposed_ids = {r["id"] for r in scene["regions"] if r["state"] == "after"}
    proposed_cross_pairs = {p for p in after_pairs if p[0] in proposed_ids and p[1] in proposed_ids}
    assert proposed_cross_pairs, "expected at least one link between two proposed sibling groups in the after-state"
    assert not (proposed_cross_pairs & before_pairs)  # these pairs did not exist as regions before


# ── write_decouple_3d_html ───────────────────────────────────────────────────

def test_write_decouple_3d_html_returns_none_without_a_boundary(tmp_path):
    g = nx.DiGraph()
    _code(g, "a", "compute()", "app/core/a.py")
    _code(g, "b", "adjust()", "app/core/b.py")
    g.add_edge("a", "b", relation="calls", confidence="EXTRACTED")
    plan = decouple_plan(g, {}, top_n=20, min_group_size=1)
    result = write_decouple_3d_html(g, plan, {}, tmp_path / "DECOUPLE_3D.html")
    assert result is None
    assert not (tmp_path / "DECOUPLE_3D.html").exists()


def test_write_decouple_3d_html_writes_page_with_before_after_toggle(tmp_path):
    g = _build_graph()
    communities = {0: ["lm0", "lm1", "lm2"], 1: ["dm0", "dm1", "dm2"], 2: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=20, min_group_size=1)
    out = tmp_path / "DECOUPLE_3D.html"
    result = write_decouple_3d_html(g, plan, communities, out)
    assert result == out
    html = out.read_text(encoding="utf-8")
    assert "THREE" in html
    assert "decouple-view-cb" in html  # the before/after toggle checkbox
    assert '"state": "after"' in html or '"state":"after"' in html


def test_write_decouple_3d_html_uses_the_plans_floors_without_recomputing(tmp_path, monkeypatch):
    """This view must not run its own floor computation: it would be the
    second answer to a question the plan already answered, free to
    disagree with the report it illustrates about which unit is on which
    floor — or about which units have no floor at all. Blowing up if it is
    called is the only way to pin that.
    """
    import graphify.data_floor as data_floor

    g = _build_graph()
    communities = {0: ["dm0", "dm1", "dm2"], 1: ["dm3", "dm4", "dm5"]}
    plan = decouple_plan(g, communities, top_n=10, min_group_size=2)

    def _boom(*_a, **_kw):
        raise AssertionError("decouple_3d recomputed floors instead of using the plan's")

    monkeypatch.setattr(data_floor, "compute_floors", _boom)
    monkeypatch.setattr(data_floor, "compute_floors_with_provenance", _boom)
    out = tmp_path / "DECOUPLE_3D.html"
    assert write_decouple_3d_html(g, plan, communities, out) == out


def test_a_regions_floor_is_decided_by_its_measured_members_not_its_parallel_ones():
    """Same rule as data_floor.class_floor_profile, enforced where the
    region discs are actually placed: a region with 2 members measured at
    floor 1 and 4 placed alongside floor 0 stays on floor 1. Measured on
    AutoCheck, three module regions dropped a floor this way — adjacency
    evidence outvoting call-chain evidence purely on count."""
    g = _build_graph()
    positions, discs, region_members = _class_cluster_layout(g)
    dialog_members = region_members["dialog"]
    floors = {"dialog": 1}
    floors.update({m: 1 for m in dialog_members[:2]})
    floors.update({m: 0 for m in dialog_members[2:]})
    measured = set(dialog_members[:2])
    payload = build_floor_scene(
        g, discs, positions, region_members, floors, COMMUNITY_COLORS, measured=measured,
    )
    dialog = next(r for r in payload["regions"] if r["id"] == "dialog")
    assert dialog["floor"] == 1
    # Member points still show where each member actually sits.
    assert {m["floor"] for m in dialog["members"]} == {0, 1}


def test_a_region_with_only_parallel_members_is_placed_not_left_unknown(tmp_path):
    """The other half of the same rule: no measured member at all means the
    parallel placements ARE the evidence, and the region belongs on that
    floor rather than on the unknown band."""
    g = _build_graph()
    positions, discs, region_members = _class_cluster_layout(g)
    dialog_members = region_members["dialog"]
    floors = {m: 3 for m in dialog_members}
    payload = build_floor_scene(
        g, discs, positions, region_members, floors, COMMUNITY_COLORS, measured=set(),
    )
    dialog = next(r for r in payload["regions"] if r["id"] == "dialog")
    assert dialog["floor"] == 3
