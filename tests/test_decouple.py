"""Tests for `graphify decouple` — 0-LLM candidate decoupled architecture.

Pins the core distinction the feature depends on: a god node with many OWN
members spread across communities ("god_object", Extract Class applies) is
not the same thing as a god node with almost no own members but many
INCOMING references ("over_referenced_hub", splitting its body does nothing
for coupling). Validation against a real desktop-app corpus showed exactly
this split: MainWindow/GroupAnalyzeDialog are god_object, TraceSource is
over_referenced_hub despite having the 2nd-highest degree.
"""
from __future__ import annotations

import json

import networkx as nx
import pytest
from networkx.readwrite import json_graph

import graphify.__main__ as mainmod
from graphify.decouple import (
    balance_risk,
    build_augmented_graph,
    candidate_groups,
    classify_god_node,
    decouple_plan,
    hub_suggestion,
    member_ids,
    original_risk_score,
    overlay_tool_dedup_clusters,
    render_markdown,
    split_risk_score,
)
from graphify.decouple_html import write_decouple_html


def _add_member(g, god_id, member_id, *, label, source_file, relation="method", confidence="EXTRACTED"):
    g.add_node(member_id, label=label, file_type="code", source_file=source_file, source_location="L1")
    g.add_edge(god_id, member_id, relation=relation, confidence=confidence)


def _build_graph():
    """One god_object (2 member communities), one over_referenced_hub (no own
    members, many callers), one cohesive_but_large (5 members, 1 community)."""
    g = nx.DiGraph()

    # --- god_object: "GodClass" — 6 members split across 2 communities ---
    g.add_node("god", label="GodClass", file_type="code", _callable_class=True, source_file="mod.py", source_location="L1")
    for i in range(3):
        _add_member(g, "god", f"m{i}", label=f".m{i}()", source_file="mod.py")
    for i in range(3, 6):
        _add_member(g, "god", f"m{i}", label=f".m{i}()", source_file="mod.py")
    # a cross-file "method" edge (symbol-resolution ghost) — must be excluded
    g.add_node("ghost", label=".ghost()", file_type="code", source_file="other.py", source_location="L1")
    g.add_edge("god", "ghost", relation="method", confidence="EXTRACTED")
    # an INFERRED member edge — excluded only under extracted_only=True
    _add_member(g, "god", "m_inferred", label=".m_inferred()", source_file="mod.py", confidence="INFERRED")
    # afferent edges (fewer than efferent, so member_ratio stays high)
    for i in range(2):
        g.add_node(f"caller{i}", label=f"caller{i}()", file_type="code", source_file="caller.py", source_location="L1")
        g.add_edge(f"caller{i}", "god", relation="calls", confidence="EXTRACTED")

    # --- over_referenced_hub: "HubClass" — 0 own members, 10 callers ---
    g.add_node("hub", label="HubClass", file_type="code", _callable_class=True, source_file="hub.py", source_location="L1")
    for i in range(10):
        g.add_node(f"hubcaller{i}", label=f"hc{i}()", file_type="code", source_file="hcaller.py", source_location="L1")
        g.add_edge(f"hubcaller{i}", "hub", relation="calls", confidence="EXTRACTED")

    # --- cohesive_but_large: "BigClass" — 5 members, all one community ---
    g.add_node("big", label="BigClass", file_type="code", _callable_class=True, source_file="big.py", source_location="L1")
    for i in range(5):
        _add_member(g, "big", f"b{i}", label=f".b{i}()", source_file="big.py")
    g.add_node("bigcaller", label="bigcaller()", file_type="code", source_file="caller.py", source_location="L1")
    g.add_edge("bigcaller", "big", relation="calls", confidence="EXTRACTED")

    # --- god_object with a BAD split: "TangledClass" — 6 members in 2
    # communities, but the two groups call into each other AND share external
    # callers that depend on both. Structurally still god_object (member_ratio
    # high, 2 communities), but the split itself should be discouraged.
    g.add_node("tangled", label="TangledClass", file_type="code", _callable_class=True, source_file="tangled.py", source_location="L1")
    for i in range(3):
        _add_member(g, "tangled", f"t{i}", label=f".t{i}()", source_file="tangled.py")
    for i in range(3, 6):
        _add_member(g, "tangled", f"t{i}", label=f".t{i}()", source_file="tangled.py")
    # cross-group edges: members of group A call members of group B
    g.add_edge("t0", "t3", relation="calls", confidence="EXTRACTED")
    g.add_edge("t1", "t4", relation="calls", confidence="EXTRACTED")
    g.add_edge("t2", "t5", relation="calls", confidence="EXTRACTED")
    g.add_edge("t3", "t0", relation="calls", confidence="EXTRACTED")
    # straddling callers: each depends on a member from BOTH groups
    for i in range(3):
        g.add_node(f"ext{i}", label=f"ext{i}()", file_type="code", source_file="ext.py", source_location="L1")
        g.add_edge(f"ext{i}", "t0", relation="calls", confidence="EXTRACTED")
        g.add_edge(f"ext{i}", "t4", relation="calls", confidence="EXTRACTED")
    g.add_node("tangledcaller", label="tangledcaller()", file_type="code", source_file="ext.py", source_location="L1")
    g.add_edge("tangledcaller", "tangled", relation="calls", confidence="EXTRACTED")

    # --- god_object with a DELEGATING split: "PipelineClass" — identical to
    # TangledClass (same member/group/straddler shape) EXCEPT there is no
    # reverse edge: group A calls into group B, never the other way. This
    # isolates the group_dependency_shape effect — same cross_group_edges
    # count and same straddling_callers as "tangled", only the direction
    # differs, so any score difference between the two is attributable to
    # the dag/cyclic discount alone.
    g.add_node("pipeline", label="PipelineClass", file_type="code", _callable_class=True, source_file="pipeline.py", source_location="L1")
    for i in range(3):
        _add_member(g, "pipeline", f"p{i}", label=f".p{i}()", source_file="pipeline.py")
    for i in range(3, 6):
        _add_member(g, "pipeline", f"p{i}", label=f".p{i}()", source_file="pipeline.py")
    g.add_edge("p0", "p3", relation="calls", confidence="EXTRACTED")
    g.add_edge("p1", "p4", relation="calls", confidence="EXTRACTED")
    g.add_edge("p2", "p5", relation="calls", confidence="EXTRACTED")
    # a 4th forward edge (still group A -> group B, same direction) so the
    # total cross_group_edges count matches "tangled"'s 4 exactly, isolating
    # direction as the only variable between the two fixtures.
    g.add_edge("p0", "p4", relation="calls", confidence="EXTRACTED")
    for i in range(3):
        g.add_node(f"pext{i}", label=f"pext{i}()", file_type="code", source_file="ext.py", source_location="L1")
        g.add_edge(f"pext{i}", "p0", relation="calls", confidence="EXTRACTED")
        g.add_edge(f"pext{i}", "p4", relation="calls", confidence="EXTRACTED")
    g.add_node("pipelinecaller", label="pipelinecaller()", file_type="code", source_file="ext.py", source_location="L1")
    g.add_edge("pipelinecaller", "pipeline", relation="calls", confidence="EXTRACTED")

    return g


def _communities_for(g):
    """Manually-assigned communities matching the graph's intended structure —
    unit tests exercise decouple.py's own logic, not Louvain's behavior on a
    tiny synthetic graph."""
    return {
        0: ["m0", "m1", "m2"],
        1: ["m3", "m4", "m5"],
        2: ["b0", "b1", "b2", "b3", "b4"],
        3: ["t0", "t1", "t2"],
        4: ["t3", "t4", "t5"],
        5: ["p0", "p1", "p2"],
        6: ["p3", "p4", "p5"],
    }


# ── member_ids ──────────────────────────────────────────────────────────────

def test_member_ids_excludes_cross_file_ghost():
    g = _build_graph()
    members = member_ids(g, "god")
    assert "ghost" not in members
    assert "m0" in members and "m5" in members


def test_member_ids_extracted_only_excludes_inferred():
    g = _build_graph()
    assert "m_inferred" in member_ids(g, "god", extracted_only=False)
    assert "m_inferred" not in member_ids(g, "god", extracted_only=True)


# ── classify_god_node ────────────────────────────────────────────────────────

def test_classify_god_object():
    g = _build_graph()
    info = classify_god_node(g, "god", _communities_for(g))
    assert info["classification"] == "god_object"
    assert info["distinct_member_communities"] == 2
    assert info["member_count"] == 7  # ghost excluded; m0-m5 + m_inferred included by default


def test_classify_over_referenced_hub_despite_no_members():
    g = _build_graph()
    info = classify_god_node(g, "hub", _communities_for(g))
    assert info["classification"] == "over_referenced_hub"
    assert info["member_count"] == 0
    assert info["afferent"] == 10


def test_classify_cohesive_but_large():
    g = _build_graph()
    info = classify_god_node(g, "big", _communities_for(g))
    assert info["classification"] == "cohesive_but_large"
    assert info["distinct_member_communities"] == 1


# ── candidate_groups ─────────────────────────────────────────────────────────

def test_candidate_groups_splits_by_community():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "god")
    groups = candidate_groups(g, members, communities, min_group_size=3)
    non_residual = [gr for gr in groups if gr["community_id"] is not None]
    assert len(non_residual) == 2
    all_grouped = {m for gr in groups for m in gr["members"]}
    assert all_grouped == set(members)


def test_candidate_groups_residual_below_min_size():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "god")
    groups = candidate_groups(g, members, communities, min_group_size=10)
    # both communities (size 3 each) fall under min_group_size=10 -> everything residual
    assert len(groups) == 1
    assert groups[0]["community_id"] is None


def test_candidate_groups_uses_supplied_label():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "god")
    labels = {0: "First Half", 1: "Second Half"}
    groups = candidate_groups(g, members, communities, labels, min_group_size=3)
    names = {gr["name"] for gr in groups if gr["community_id"] is not None}
    assert names == {"First Half", "Second Half"}


# ── risk scoring: original vs. split, and the balance between them ──────────

def test_split_risk_score_zero_for_single_group():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "big")
    groups = candidate_groups(g, members, communities, min_group_size=10)  # collapses to 1 residual group
    split = split_risk_score(g, "big", groups)
    assert split["score"] == 0.0
    assert split["n_new_classes"] <= 1


def test_split_risk_score_penalizes_cross_group_coupling_and_straddlers():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "tangled")
    groups = candidate_groups(g, members, communities, min_group_size=3)
    split = split_risk_score(g, "tangled", groups)
    assert split["cross_group_edges"] > 0
    assert split["straddling_callers"] > 0
    assert split["score"] > 0.0


def test_split_risk_score_zero_for_clean_separation():
    g = _build_graph()
    communities = _communities_for(g)
    members = member_ids(g, "god")
    groups = candidate_groups(g, members, communities, min_group_size=3)
    split = split_risk_score(g, "god", groups)
    # m0-m2 and m3-m5 have no edges between them and no shared external callers —
    # the only remaining cost is the fixed per-new-class overhead component.
    assert split["cross_group_edges"] == 0
    assert split["straddling_callers"] == 0
    assert split["score"] < 5.0


def test_split_risk_score_discounts_dag_shaped_cross_group_edges():
    """"pipeline" and "tangled" are structurally identical (same edge count,
    same straddling callers) except "pipeline" has no reverse edge between
    its two groups — group A calls into group B, never back. That is the
    delegating/pipeline shape (a large orchestrator whose members fan out
    into worker groups it calls one-way), and it must score strictly lower
    than the mutually-coupled "tangled" split even though both report the
    same cross_group_edges and straddling_callers counts."""
    g = _build_graph()
    communities = _communities_for(g)

    tangled_groups = candidate_groups(g, member_ids(g, "tangled"), communities, min_group_size=3)
    tangled = split_risk_score(g, "tangled", tangled_groups)

    pipeline_groups = candidate_groups(g, member_ids(g, "pipeline"), communities, min_group_size=3)
    pipeline = split_risk_score(g, "pipeline", pipeline_groups)

    assert pipeline["cross_group_edges"] == tangled["cross_group_edges"]
    assert pipeline["straddling_callers"] == tangled["straddling_callers"]
    assert pipeline["group_dependency_shape"] == "dag"
    assert tangled["group_dependency_shape"] == "cyclic"
    assert pipeline["score"] < tangled["score"]


def test_balance_risk_recommends_split_when_split_risk_is_low():
    result = balance_risk(50.0, {"score": 10.0, "n_new_classes": 2, "cross_group_edges": 0,
                                  "straddling_callers": 0, "straddling_caller_labels": []})
    assert result["recommendation"] == "split"
    assert result["net_benefit"] == 40.0


def test_balance_risk_keeps_as_is_when_split_risk_is_high():
    result = balance_risk(20.0, {"score": 60.0, "n_new_classes": 2, "cross_group_edges": 4,
                                  "straddling_callers": 3, "straddling_caller_labels": []})
    assert result["recommendation"] == "keep_as_is"
    assert result["net_benefit"] < 0


def test_balance_risk_marginal_within_threshold():
    result = balance_risk(30.0, {"score": 32.0, "n_new_classes": 2, "cross_group_edges": 1,
                                  "straddling_callers": 0, "straddling_caller_labels": []},
                           net_benefit_threshold=5.0)
    assert result["recommendation"] == "marginal"


def test_decouple_plan_recommends_split_for_clean_god_object():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, {0: "First Half", 1: "Second Half"}, top_n=20, min_group_size=3)
    by_id = {e["id"]: e for e in plan["god_nodes"]}
    assert by_id["god"]["risk"]["recommendation"] == "split"
    assert by_id["god"]["risk"]["net_benefit"] > 0


def test_decouple_plan_discourages_tangled_split():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    by_id = {e["id"]: e for e in plan["god_nodes"]}
    tangled = by_id["tangled"]
    assert tangled["classification"] == "god_object"  # structurally still looks fragmented
    assert tangled["risk"]["recommendation"] in ("keep_as_is", "marginal")
    assert tangled["risk"]["net_benefit"] < by_id["god"]["risk"]["net_benefit"]


def test_original_risk_score_increases_with_size_and_coupling():
    small = {"member_count": 3, "afferent": 2, "efferent": 3, "distinct_member_communities": 1}
    large = {"member_count": 25, "afferent": 40, "efferent": 40, "distinct_member_communities": 4}
    assert original_risk_score(large) > original_risk_score(small)


# ── state_affinity integration: a call-graph-clean split that shares state ──

def test_decouple_plan_state_overlap_discourages_a_call_graph_clean_split(tmp_path):
    """Two proposed groups with ZERO cross-group edges and ZERO straddling
    callers (the call graph looks perfectly clean) but whose real methods
    all read the SAME instance attribute — the exact "moved the methods,
    didn't reduce the coupling" failure mode a call-graph-only score cannot
    see. project_root=None must not detect this; project_root=tmp_path must.
    """
    g = nx.DiGraph()
    g.add_node("stategod", label="StateGod", file_type="code", source_file="stategod.py", source_location="L1")
    for i in range(3):
        _add_member(g, "stategod", f"sa{i}", label=f".sa{i}()", source_file="stategod.py")
    for i in range(3):
        _add_member(g, "stategod", f"sb{i}", label=f".sb{i}()", source_file="stategod.py")
    for i in range(2):
        g.add_node(f"scaller{i}", label=f"scaller{i}()", file_type="code", source_file="caller.py", source_location="L1")
        g.add_edge(f"scaller{i}", "stategod", relation="calls", confidence="EXTRACTED")

    communities = {20: ["sa0", "sa1", "sa2"], 21: ["sb0", "sb1", "sb2"]}
    labels = {20: "Group SA", 21: "Group SB"}

    src = (
        "class StateGod:\n"
        "    def sa0(self):\n        return self._shared\n"
        "    def sa1(self):\n        return self._shared\n"
        "    def sa2(self):\n        return self._shared\n"
        "    def sb0(self):\n        return self._shared\n"
        "    def sb1(self):\n        return self._shared\n"
        "    def sb2(self):\n        return self._shared\n"
    )
    (tmp_path / "stategod.py").write_text(src, encoding="utf-8")

    plan_without = decouple_plan(g, communities, labels, top_n=20, min_group_size=3)
    plan_with = decouple_plan(g, communities, labels, top_n=20, min_group_size=3, project_root=str(tmp_path))

    without = next(e for e in plan_without["god_nodes"] if e["id"] == "stategod")["risk"]
    with_ = next(e for e in plan_with["god_nodes"] if e["id"] == "stategod")["risk"]

    assert without["split_detail"]["cross_group_edges"] == 0
    assert without["split_detail"]["straddling_callers"] == 0
    assert without["split_detail"]["state_analysis"].startswith("skipped")
    assert without["recommendation"] == "split"  # call-graph-only sees nothing wrong

    assert with_["split_detail"]["state_analysis"] == "ok"
    assert with_["split_detail"]["max_state_overlap"] == 1.0  # both groups touch ONLY _shared
    assert with_["risk_after"] > without["risk_after"]
    assert with_["net_benefit"] < without["net_benefit"]


# ── hub_suggestion ───────────────────────────────────────────────────────────

def test_hub_suggestion_lists_dependents():
    g = _build_graph()
    hs = hub_suggestion(g, "hub", sample_size=3)
    assert hs["recommendation"] == "interface_segregation"
    assert len(hs["sample_dependents"]) == 3


# ── decouple_plan / render_markdown ──────────────────────────────────────────

def test_decouple_plan_end_to_end():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, {0: "First Half", 1: "Second Half"}, top_n=10, min_group_size=3)
    by_id = {e["id"]: e for e in plan["god_nodes"]}
    assert by_id["god"]["classification"] == "god_object"
    assert by_id["hub"]["classification"] == "over_referenced_hub"
    assert by_id["big"]["classification"] == "cohesive_but_large"
    assert "hub_suggestion" in by_id["hub"]
    assert "proposed_groups" in by_id["god"]
    md = render_markdown(plan)
    assert "GodClass" in md and "HubClass" in md and "Honesty notes" in md


# ── build_augmented_graph / write_decouple_html (same style as graph.html) ──

def test_build_augmented_graph_adds_proposed_nodes_for_recommended_splits():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, {0: "First Half", 1: "Second Half"}, top_n=20, min_group_size=3)
    g2, communities2 = build_augmented_graph(g, plan, communities)

    proposed = [n for n, d in g2.nodes(data=True) if d.get("kind") == "proposed"]
    # "god" -> 2 real, RECOMMENDED groups. "tangled" is still classified
    # god_object but its split is discouraged (see the dedicated test below)
    # and must contribute nothing here — a discouraged candidate is a number
    # in the report, not a shape on the graph.
    assert len(proposed) == 2
    for pid in proposed:
        assert g2.nodes[pid]["decouple_recommendation"] == "split"
    # every proposed node landed in ITS target community, not the god node's own
    god_data = g2.nodes["god"]
    assert "kind" not in god_data  # the real node is untouched
    for cid, members in communities2.items():
        for m in members:
            if m in proposed:
                assert g2.nodes[m]["kind"] == "proposed"


def test_build_augmented_graph_redirects_wiring_around_a_split():
    """The core of 'how do the links change': an external caller into an
    extracted member redirects onto that member's diamond; a call BETWEEN
    two members that end up in DIFFERENT new classes becomes a new,
    literal inter-class edge (new_coupling_edge — split_risk_score's
    cross_group_edges made visible); a call between two members that end up
    in the SAME new class disappears (it's internal now, not a cross-
    boundary edge); the ownership edges are untouched (still just the one
    "extract" edge, never doubled up by a redirect landing on the same pair).
    """
    g = nx.DiGraph()
    g.add_node("god2", label="SplitGod", file_type="code", source_file="s.py", source_location="L1")
    for nid in ("sa0", "sa1", "sb0"):
        g.add_node(nid, label=f".{nid}()", file_type="code", source_file="s.py", source_location="L1")
        g.add_edge("god2", nid, relation="method", confidence="EXTRACTED")
    g.add_node("extcaller", label="extcaller()", file_type="code", source_file="ext.py", source_location="L1")
    g.add_edge("extcaller", "sa0", relation="calls", confidence="EXTRACTED")  # external -> redirect
    g.add_edge("sa1", "sb0", relation="calls", confidence="EXTRACTED")  # cross-group -> new coupling
    g.add_edge("sa0", "sa1", relation="calls", confidence="EXTRACTED")  # same-group -> dropped

    plan = {
        "god_nodes": [{
            "id": "god2",
            "classification": "god_object",
            "risk": {"recommendation": "split", "risk_before": 50.0, "risk_after": 10.0, "net_benefit": 40.0},
            "proposed_groups": [
                {"community_id": 10, "name": "Group A", "members": ["sa0", "sa1"],
                 "member_labels": [], "cohesion_confidence": "high"},
                {"community_id": 11, "name": "Group B", "members": ["sb0"],
                 "member_labels": [], "cohesion_confidence": "high"},
            ],
        }],
    }
    communities = {10: ["sa0", "sa1"], 11: ["sb0"]}
    g2, _ = build_augmented_graph(g, plan, communities)

    diamond_a = next(n for n, d in g2.nodes(data=True) if d.get("kind") == "proposed" and d["label"] == "Group A")
    diamond_b = next(n for n, d in g2.nodes(data=True) if d.get("kind") == "proposed" and d["label"] == "Group B")

    assert g2.nodes["sa0"]["decouple_extracted_into"] == diamond_a
    assert g2.nodes["sb0"]["decouple_extracted_into"] == diamond_b

    assert g2.get_edge_data("extcaller", diamond_a)["kind"] == "redirected_edge"
    assert g2.get_edge_data(diamond_a, diamond_b)["kind"] == "new_coupling_edge"
    assert not g2.has_edge(diamond_a, diamond_a)  # same-group edge did not survive as a self-loop

    # ownership edges are untouched — exactly one edge god2->diamond_a, still "proposed_edge"
    assert g2.get_edge_data("god2", diamond_a)["kind"] == "proposed_edge"

    # the ORIGINAL edges are left alone too (the toggle hides nodes, not edges)
    assert g2.has_edge("extcaller", "sa0")
    assert g2.has_edge("sa1", "sb0")


def test_build_augmented_graph_skips_residual_and_non_god_object():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    g2, _ = build_augmented_graph(g, plan, communities)
    # "hub" (over_referenced_hub) and "big" (cohesive_but_large) never get a
    # proposed node hanging off them.
    assert not any(g2.has_edge("hub", n) and g2.nodes[n].get("kind") == "proposed" for n in g2.nodes)
    assert not any(g2.has_edge("big", n) and g2.nodes[n].get("kind") == "proposed" for n in g2.nodes)


def test_build_augmented_graph_skips_discouraged_god_object():
    """`tangled` is structurally god_object but its split is discouraged
    (heavy cross-group coupling, see test_decouple_plan_discourages_tangled_
    split) — build_augmented_graph must draw nothing for it at all, not even
    ringed differently."""
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    by_id = {e["id"]: e for e in plan["god_nodes"]}
    assert by_id["tangled"]["risk"]["recommendation"] != "split"
    g2, _ = build_augmented_graph(g, plan, communities)
    assert not any(g2.has_edge("tangled", n) for n in g2.nodes if g2.nodes[n].get("kind") == "proposed")
    assert not any(n.startswith("_proposed_tangled_") for n in g2.nodes)


# ── overlay_tool_dedup_clusters ──────────────────────────────────────────────

def _dup_member(source_file, name, container=None):
    return {"source_file": source_file, "name": name, "container": container, "lineno": 1, "param_count": 1, "calls": []}


def test_overlay_merges_into_existing_class_node():
    g = nx.DiGraph()
    g.add_node("loader_load", label="load()", file_type="code", source_file="a.py")
    g.add_node("settings_load", label="load()", file_type="code", source_file="b.py")
    g.add_node("loader_class", label="Loader", file_type="code", source_file="a.py")
    report = {"clusters": [{
        "members": [_dup_member("a.py", "load", "Loader"), _dup_member("b.py", "load")],
        "merge_target": {
            "recommendation": "merge_into_existing",
            "target_container": "Loader", "target_source_file": "a.py",
            "candidates": [], "rationale": "x",
        },
    }]}
    g2, _ = overlay_tool_dedup_clusters(g, {}, report)
    assert g2.has_edge("settings_load", "loader_class")
    assert g2["settings_load"]["loader_class"]["relation"] == "merge_candidate"
    # Consolidation is drawn as WIRING, never as a background region —
    # background regions mean "this is one class" and nothing else.
    assert g2.graph["hyperedges"] == []


def test_overlay_independent_creates_proposed_shared_node():
    g = nx.DiGraph()
    g.add_node("a_load", label="load()", file_type="code", source_file="a.py")
    g.add_node("b_load", label="load()", file_type="code", source_file="b.py")
    report = {"clusters": [{
        "members": [_dup_member("a.py", "load"), _dup_member("b.py", "load")],
        "merge_target": {
            "recommendation": "independent",
            "target_container": None, "target_source_file": None,
            "candidates": [], "rationale": "x",
        },
    }]}
    g2, _ = overlay_tool_dedup_clusters(g, {}, report)
    proposed = [n for n, d in g2.nodes(data=True) if d.get("kind") == "proposed"]
    assert len(proposed) == 1
    assert g2.nodes[proposed[0]]["hidden"] is True
    assert g2.has_edge("a_load", proposed[0])
    assert g2.has_edge("b_load", proposed[0])


def test_overlay_skips_cluster_with_unresolvable_members():
    g = nx.DiGraph()
    g.add_node("only_one", label="load()", file_type="code", source_file="a.py")
    report = {"clusters": [{
        "members": [_dup_member("a.py", "load"), _dup_member("nonexistent.py", "load")],
        "merge_target": {"recommendation": "independent", "target_container": None,
                          "target_source_file": None, "candidates": [], "rationale": "x"},
    }]}
    g2, _ = overlay_tool_dedup_clusters(g, {}, report)
    assert g2.graph["hyperedges"] == []
    assert not any(d.get("kind") == "proposed" for _n, d in g2.nodes(data=True))


def test_overlay_preserves_class_hulls_from_build_augmented_graph():
    """Composability contract: calling overlay_tool_dedup_clusters SECOND, on
    build_augmented_graph's own output, must leave the class hulls that
    function created untouched — it adds wiring, never regions."""
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    g2, communities2 = build_augmented_graph(g, plan, communities)
    hulls_before = g2.graph.get("hyperedges", [])
    assert len(hulls_before) > 0
    assert all(h["layer"] == "class" for h in hulls_before)

    g2.add_node("dup_a", label="helper()", file_type="code", source_file="extra_a.py")
    g2.add_node("dup_b", label="helper()", file_type="code", source_file="extra_b.py")
    report = {"clusters": [{
        "members": [_dup_member("extra_a.py", "helper"), _dup_member("extra_b.py", "helper")],
        "merge_target": {"recommendation": "independent", "target_container": None,
                          "target_source_file": None, "candidates": [], "rationale": "x"},
    }]}
    g3, _ = overlay_tool_dedup_clusters(g2, communities2, report)
    assert g3.graph["hyperedges"] == hulls_before  # unchanged, not appended to


def test_build_augmented_graph_hulls_cover_every_class_not_just_god_nodes():
    """A class boundary is a fact about the code, not a property of scoring
    high enough to be a split candidate — every class with members gets one,
    including "BigClass" (cohesive_but_large, never split) and the classes a
    top_n cutoff would exclude."""
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=2, min_group_size=3)  # only 2 god nodes analyzed
    g2, _ = build_augmented_graph(g, plan, communities)
    labels = {h["label"] for h in g2.graph["hyperedges"]}
    # every class WITH members, regardless of what the plan looked at
    assert labels == {"GodClass", "BigClass", "TangledClass", "PipelineClass"}
    assert "HubClass" not in labels  # no members -> no region to draw


def test_write_decouple_html_reuses_visjs_style(tmp_path):
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, {0: "First Half", 1: "Second Half"}, top_n=20, min_group_size=3)
    out = tmp_path / "DECOUPLE.html"
    write_decouple_html(g, plan, communities, {0: "First Half", 1: "Second Half"}, out)
    html = out.read_text(encoding="utf-8")
    assert "vis-network" in html  # same renderer as graph.html, not a separate diagram
    assert "mermaid" not in html.lower()
    assert "Show risk scores" in html  # toggle present because a proposed node exists
    assert '"shape":"diamond"' in html or '"shape": "diamond"' in html


def test_write_decouple_html_overlays_tool_dedup_report(tmp_path):
    g = _build_graph()
    g.add_node("dup_a", label="helper()", file_type="code", source_file="extra_a.py")
    g.add_node("dup_b", label="helper()", file_type="code", source_file="extra_b.py")
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    report = {"clusters": [{
        "members": [_dup_member("extra_a.py", "helper"), _dup_member("extra_b.py", "helper")],
        "merge_target": {"recommendation": "independent", "target_container": None,
                          "target_source_file": None, "candidates": [], "rationale": "x"},
    }]}
    out = tmp_path / "DECOUPLE.html"
    write_decouple_html(g, plan, communities, {}, out, tool_dedup_report=report)
    html = out.read_text(encoding="utf-8")
    # the proposed shared home is a NODE (revealed by "Preview decoupled
    # view"), not a background region
    assert "(shared) helper" in html
    assert "merge_candidate" in html


# ── CLI end-to-end (smoke) ────────────────────────────────────────────────────

def _write_graph_json(g, path):
    path.write_text(json.dumps(json_graph.node_link_data(g, edges="links")), encoding="utf-8")


def _run(monkeypatch, argv):
    monkeypatch.setattr(mainmod, "_check_skill_version", lambda _: None)
    monkeypatch.setattr(mainmod.sys, "argv", argv)
    mainmod.main()


def test_decouple_cli_writes_outputs(monkeypatch, tmp_path, capsys):
    g = _build_graph()
    gp = tmp_path / "graph.json"
    _write_graph_json(g, gp)
    out_dir = tmp_path / "out"
    _run(monkeypatch, [
        "graphify", "decouple", "--graph", str(gp), "--output-dir", str(out_dir),
        "--min-group-size", "2",
    ])
    out = capsys.readouterr().out
    assert (out_dir / "DECOUPLE_PLAN.md").is_file()
    assert (out_dir / "decouple.json").is_file()
    assert (out_dir / "DECOUPLE.html").is_file()
    assert "analyzed" in out and "god node" in out

    plan = json.loads((out_dir / "decouple.json").read_text(encoding="utf-8"))
    assert "god_nodes" in plan and "caveats" in plan
    assert isinstance(plan["god_nodes"], list) and plan["god_nodes"]


def test_decouple_cli_json_stdout(monkeypatch, tmp_path, capsys):
    g = _build_graph()
    gp = tmp_path / "graph.json"
    _write_graph_json(g, gp)
    _run(monkeypatch, ["graphify", "decouple", "--graph", str(gp), "--json"])
    data = json.loads(capsys.readouterr().out)
    assert "god_nodes" in data


def test_decouple_cli_missing_graph_errors(monkeypatch, tmp_path, capsys):
    with pytest.raises(SystemExit) as exc:
        _run(monkeypatch, ["graphify", "decouple", "--graph", str(tmp_path / "nope.json")])
    assert exc.value.code == 1
    assert "graph.json not found" in capsys.readouterr().err
