"""Tests for `graphify decouple` — 0-LLM candidate decoupled architecture.

Pins the core distinction the feature depends on: a god node with many OWN
members spread across communities ("god_object", Extract Class applies) is
not the same thing as a god node with almost no own members but many
INCOMING references ("over_referenced_hub", splitting its body does nothing
for coupling). Real-corpus validation (AutoCheck/Touchstone Explorer) showed
exactly this split: MainWindow/GroupAnalyzeDialog are god_object,
TraceSource is over_referenced_hub despite having the 2nd-highest degree.
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
    g.add_node("god", label="GodClass", file_type="code", source_file="mod.py", source_location="L1")
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
    g.add_node("hub", label="HubClass", file_type="code", source_file="hub.py", source_location="L1")
    for i in range(10):
        g.add_node(f"hubcaller{i}", label=f"hc{i}()", file_type="code", source_file="hcaller.py", source_location="L1")
        g.add_edge(f"hubcaller{i}", "hub", relation="calls", confidence="EXTRACTED")

    # --- cohesive_but_large: "BigClass" — 5 members, all one community ---
    g.add_node("big", label="BigClass", file_type="code", source_file="big.py", source_location="L1")
    for i in range(5):
        _add_member(g, "big", f"b{i}", label=f".b{i}()", source_file="big.py")
    g.add_node("bigcaller", label="bigcaller()", file_type="code", source_file="caller.py", source_location="L1")
    g.add_edge("bigcaller", "big", relation="calls", confidence="EXTRACTED")

    # --- god_object with a BAD split: "TangledClass" — 6 members in 2
    # communities, but the two groups call into each other AND share external
    # callers that depend on both. Structurally still god_object (member_ratio
    # high, 2 communities), but the split itself should be discouraged.
    g.add_node("tangled", label="TangledClass", file_type="code", source_file="tangled.py", source_location="L1")
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
    # "god" -> 2 real groups; "tangled" is still god_object (2 groups) even
    # though discouraged — a discouraged candidate is still drawn (just
    # ringed differently), so both god nodes contribute proposed nodes.
    assert len(proposed) == 4
    for pid in proposed:
        assert g2.nodes[pid]["decouple_recommendation"] in ("split", "marginal", "keep_as_is")
    # every proposed node landed in ITS target community, not the god node's own
    god_data = g2.nodes["god"]
    assert "kind" not in god_data  # the real node is untouched
    for cid, members in communities2.items():
        for m in members:
            if m in proposed:
                assert g2.nodes[m]["kind"] == "proposed"


def test_build_augmented_graph_skips_residual_and_non_god_object():
    g = _build_graph()
    communities = _communities_for(g)
    plan = decouple_plan(g, communities, top_n=20, min_group_size=3)
    g2, _ = build_augmented_graph(g, plan, communities)
    # "hub" (over_referenced_hub) and "big" (cohesive_but_large) never get a
    # proposed node hanging off them.
    assert not any(g2.has_edge("hub", n) and g2.nodes[n].get("kind") == "proposed" for n in g2.nodes)
    assert not any(g2.has_edge("big", n) and g2.nodes[n].get("kind") == "proposed" for n in g2.nodes)


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
