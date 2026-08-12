"""decouple — deterministic (0-LLM) Extract-Class / decoupling suggestions for god nodes.

Reuses the graph structure graphify already computes for every corpus:
god-node ranking (analyze.god_nodes), community detection (cluster.cluster),
and community naming (cluster.label_communities_by_hub or a prior LLM labeling
pass persisted in .graphify_labels.json). No new LLM call is introduced.

Key finding this module encodes: raw edge count alone does not tell you
WHY a node is a god node. A class with many *own* methods spread across
several communities is a true God Object (Extract Class applies). A class
with almost no own methods but many *incoming* references is an
over-referenced hub/data-model (splitting its body does nothing for
coupling — interface segregation is the applicable move instead). See
`classify_god_node`.

Honest limits (surfaced in every report, not just here):
  - Member detection uses AST relation edges only (method/contains/defines).
    Instance fields are not represented as graph nodes for most languages, so
    this is a coupling proxy, not a true LCOM/attribute-usage measurement.
  - `source_location` has no end line, so group sizes are counted in symbols,
    not lines of code.
"""
from __future__ import annotations

from typing import Any

import networkx as nx

# Edges that mean "this god node structurally owns that member" — the AST
# tier's class/method backbone (engine.py). Deliberately excludes "calls"/
# "references": those are coupling *to* other things, not membership.
MEMBER_RELATIONS = frozenset({"method", "contains", "defines"})


def _invert_communities(communities: dict[int, list[str]] | None) -> dict[str, int]:
    if not communities:
        return {}
    return {n: cid for cid, nodes in communities.items() for n in nodes}


def _is_owned_member(G: nx.DiGraph, god_id: str, target_id: str) -> bool:
    """True if `target_id` is a real member of `god_id`, not a symbol-resolution
    ghost repointed to a same-named function in a different file (observed on
    real corpora — a 'method' edge can cross files after cross-file call
    resolution)."""
    god_file = G.nodes[god_id].get("source_file") or ""
    tgt_file = G.nodes[target_id].get("source_file") or ""
    return bool(god_file) and god_file == tgt_file


def member_ids(G: nx.DiGraph, god_id: str, *, extracted_only: bool = False) -> list[str]:
    """Return the node ids `god_id` structurally owns (method/contains/defines
    edges, same source_file only). `G` must be directed — load it with
    `graphify.affected.load_graph`, which forces `directed=True`."""
    ids: set[str] = set()
    for _src, tgt, data in G.out_edges(god_id, data=True):
        if data.get("relation") not in MEMBER_RELATIONS:
            continue
        if extracted_only and data.get("confidence", "EXTRACTED") != "EXTRACTED":
            continue
        if not _is_owned_member(G, god_id, tgt):
            continue
        ids.add(tgt)
    return sorted(ids)


def classify_god_node(
    G: nx.DiGraph,
    node_id: str,
    communities: dict[int, list[str]] | None = None,
    *,
    extracted_only: bool = False,
    member_ratio_threshold: float = 0.2,
    min_communities_for_split: int = 2,
) -> dict[str, Any]:
    """Classify why `node_id` is a god node.

    - "god_object": many own members (method/contains/defines), spread across
      >= min_communities_for_split communities -> Extract Class applies.
    - "cohesive_but_large": many own members but they cluster in one
      community -> large but not fragmented; no split recommended.
    - "over_referenced_hub": few/no own members relative to total degree ->
      the coupling is inbound (afferent), not internal responsibility bloat;
      splitting the class body would not reduce coupling.
    """
    members = member_ids(G, node_id, extracted_only=extracted_only)
    afferent = G.in_degree(node_id)
    efferent = G.out_degree(node_id)
    total = afferent + efferent
    member_ratio = (len(members) / total) if total else 0.0

    node_comm = _invert_communities(communities)
    distinct = len({node_comm[m] for m in members if m in node_comm})

    if not members:
        classification = "over_referenced_hub"
    elif member_ratio >= member_ratio_threshold and distinct >= min_communities_for_split:
        classification = "god_object"
    elif member_ratio >= member_ratio_threshold:
        classification = "cohesive_but_large"
    else:
        classification = "over_referenced_hub"

    return {
        "id": node_id,
        "label": G.nodes[node_id].get("label", node_id),
        "source_file": G.nodes[node_id].get("source_file", ""),
        "afferent": afferent,
        "efferent": efferent,
        "member_count": len(members),
        "member_ratio": round(member_ratio, 3),
        "distinct_member_communities": distinct,
        "classification": classification,
        "members": members,
    }


def _name_group(
    G: nx.DiGraph,
    member_list: list[str],
    community_labels: dict[int, str] | None,
    cid: int | None,
) -> str:
    """Name a proposed split group. Prefers an existing community label
    (LLM-labeled via skill Step 5, or the deterministic
    `cluster.label_communities_by_hub` fallback) — zero marginal cost, no new
    LLM call. Falls back to the highest-degree member's own name."""
    if community_labels and cid is not None and cid in community_labels:
        return community_labels[cid]
    if not member_list:
        return f"Group {cid}"
    hub = min(member_list, key=lambda n: (-G.degree(n), str(n)))
    name = str(G.nodes[hub].get("label") or hub).strip()
    if name.startswith("."):
        name = name[1:]
    if name.endswith("()"):
        name = name[:-2]
    return name or f"Group {cid}"


def _external_neighbors(G: nx.DiGraph, node_id: str, exclude: set[str]) -> set[str]:
    neigh = set(G.predecessors(node_id)) | set(G.successors(node_id))
    return neigh - exclude


def _add_cohesion_confidence(G: nx.DiGraph, groups: list[dict], all_members: list[str]) -> None:
    """Corroborate each proposed group with a second, independent signal: do
    its members share more external neighbors with EACH OTHER than chance
    would suggest? High pairwise Jaccard overlap on external (non-member)
    neighbors means the members are pulled together by the same outside
    callers/callees, not just co-assigned by the whole-graph community pass —
    two votes agreeing is stronger evidence than one.

    This is a proxy signal, not a rerun of Louvain — deliberately cheap and
    fully explainable in the report."""
    exclude = set(all_members)
    for g in groups:
        members = g["members"]
        if len(members) < 2:
            g["shared_neighbor_score"] = None
            g["cohesion_confidence"] = "low"
            continue
        neighbor_sets = [_external_neighbors(G, m, exclude) for m in members]
        pair_scores = []
        for i in range(len(neighbor_sets)):
            for j in range(i + 1, len(neighbor_sets)):
                a, b = neighbor_sets[i], neighbor_sets[j]
                union = a | b
                pair_scores.append(len(a & b) / len(union) if union else 0.0)
        avg = sum(pair_scores) / len(pair_scores) if pair_scores else 0.0
        g["shared_neighbor_score"] = round(avg, 3)
        g["cohesion_confidence"] = "high" if avg >= 0.15 else "medium" if avg >= 0.05 else "low"


def candidate_groups(
    G: nx.DiGraph,
    members: list[str],
    communities: dict[int, list[str]] | None,
    community_labels: dict[int, str] | None = None,
    *,
    min_group_size: int = 3,
) -> list[dict[str, Any]]:
    """Group a god node's own members by the community they already fell into
    in the whole-graph clustering pass. Groups smaller than `min_group_size`
    are folded into a `_residual` group (kept on the original class — not
    worth extracting)."""
    node_comm = _invert_communities(communities)
    by_cid: dict[int | None, list[str]] = {}
    for m in members:
        cid = node_comm.get(m)
        by_cid.setdefault(cid, []).append(m)

    groups: list[dict[str, Any]] = []
    residual: list[str] = []
    for cid, member_list in by_cid.items():
        if cid is None or len(member_list) < min_group_size:
            residual.extend(member_list)
            continue
        ordered = sorted(member_list, key=str)
        groups.append({
            "community_id": cid,
            "name": _name_group(G, member_list, community_labels, cid),
            "members": ordered,
            "member_labels": [G.nodes[n].get("label", n) for n in ordered],
        })
    groups.sort(key=lambda g: (-len(g["members"]), g["name"]))

    _add_cohesion_confidence(G, groups, members)

    if residual:
        ordered = sorted(residual, key=str)
        groups.append({
            "community_id": None,
            "name": "_residual (kept on original class)",
            "members": ordered,
            "member_labels": [G.nodes[n].get("label", n) for n in ordered],
            "shared_neighbor_score": None,
            "cohesion_confidence": "n/a",
        })
    return groups


_RISK_SIZE_CAP = 30           # member_count >= this maxes the "size" component
_RISK_COUPLING_CAP = 100       # afferent+efferent >= this maxes the "coupling" component
_RISK_FRAGMENTATION_CAP = 5    # distinct_member_communities >= this maxes "fragmentation"
_SPLIT_EDGE_CAP = 10           # new cross-group edges >= this maxes the "new coupling" component
_SPLIT_GROUP_CAP = 5           # new classes - 1 >= this maxes the "group overhead" component


def original_risk_score(entry: dict[str, Any]) -> float:
    """0-100 proxy for the god node's CURRENT risk: how much is bundled
    together (size), how coupled it already is (afferent+efferent), and how
    many distinct responsibilities are mixed in (fragmentation).

    Weights/caps are a fixed heuristic, not a validated complexity metric —
    useful to compare candidates on THIS graph, not as an absolute score."""
    size = min(entry["member_count"] / _RISK_SIZE_CAP, 1.0)
    coupling = min((entry["afferent"] + entry["efferent"]) / _RISK_COUPLING_CAP, 1.0)
    fragmentation = min(entry["distinct_member_communities"] / _RISK_FRAGMENTATION_CAP, 1.0)
    return round(100 * (0.40 * size + 0.35 * coupling + 0.25 * fragmentation), 1)


def split_risk_score(G: nx.DiGraph, god_id: str, groups: list[dict[str, Any]]) -> dict[str, Any]:
    """0-100 proxy for the risk the SPLIT ITSELF introduces — complexity that
    does not exist today and only appears because of the split:

    - `cross_group_edges`: calls/references between members that end up in
      DIFFERENT proposed groups. Today these are invisible intra-class edges;
      after extraction they become new, explicit inter-class dependencies.
    - `straddling_callers`: outside nodes that depend on members from more
      than one proposed group. Today they hold one reference (the original
      class); after extraction they must depend on multiple new classes.

    A single non-residual group (nothing left to compare against) has no
    split risk by construction — there is no second class to be coupled to.
    """
    non_residual = [g for g in groups if g["community_id"] is not None]
    if len(non_residual) < 2:
        return {
            "n_new_classes": len(non_residual),
            "cross_group_edges": 0,
            "straddling_callers": 0,
            "straddling_caller_labels": [],
            "score": 0.0,
        }

    member_group: dict[str, int] = {m: gi for gi, g in enumerate(non_residual) for m in g["members"]}
    all_members = set(member_group)

    cross_group_edges = 0
    for u, v in G.edges():
        gu, gv = member_group.get(u), member_group.get(v)
        if gu is not None and gv is not None and gu != gv:
            cross_group_edges += 1

    caller_groups: dict[str, set[int]] = {}
    for u, v in G.edges():
        if v in member_group and u not in all_members and u != god_id:
            caller_groups.setdefault(u, set()).add(member_group[v])
        if u in member_group and v not in all_members and v != god_id:
            caller_groups.setdefault(v, set()).add(member_group[u])
    straddlers = sorted(
        (c for c, gs in caller_groups.items() if len(gs) >= 2),
        key=lambda c: (-len(caller_groups[c]), str(c)),
    )

    total_callers = len(caller_groups) or 1
    edge_component = min(cross_group_edges / _SPLIT_EDGE_CAP, 1.0)
    straddle_component = min(len(straddlers) / total_callers, 1.0)
    group_overhead = min((len(non_residual) - 1) / _SPLIT_GROUP_CAP, 1.0)
    score = round(100 * (0.45 * edge_component + 0.40 * straddle_component + 0.15 * group_overhead), 1)

    return {
        "n_new_classes": len(non_residual),
        "cross_group_edges": cross_group_edges,
        "straddling_callers": len(straddlers),
        "straddling_caller_labels": [G.nodes[c].get("label", c) for c in straddlers[:8]],
        "score": score,
    }


def balance_risk(
    risk_before: float, split: dict[str, Any], *, net_benefit_threshold: float = 5.0
) -> dict[str, Any]:
    """Compare risk_before (the god node as-is) against split["score"] (the
    NEW risk the split introduces) and decide whether the split is actually
    worth it. A split that scores structurally as `god_object` can still end
    up `keep_as_is` here if its groups turn out to be too entangled."""
    net_benefit = round(risk_before - split["score"], 1)
    if net_benefit > net_benefit_threshold:
        recommendation = "split"
    elif net_benefit < -net_benefit_threshold:
        recommendation = "keep_as_is"
    else:
        recommendation = "marginal"
    return {
        "risk_before": risk_before,
        "risk_after": split["score"],
        "net_benefit": net_benefit,
        "recommendation": recommendation,
        "split_detail": split,
    }


def hub_suggestion(G: nx.DiGraph, node_id: str, *, sample_size: int = 8) -> dict[str, Any]:
    """Suggestion for an over-referenced hub: not a split candidate. Splitting
    its body would not reduce coupling because the coupling is inbound."""
    callers = sorted(G.predecessors(node_id), key=lambda n: (-G.degree(n), str(n)))[:sample_size]
    return {
        "recommendation": "interface_segregation",
        "rationale": (
            "Most of this node's edges are incoming references from other parts of "
            "the codebase, not its own methods/members. Extract-Class would not "
            "reduce coupling here; consider narrowing its public interface or "
            "introducing per-consumer facades instead."
        ),
        "sample_dependents": [
            {"id": c, "label": G.nodes[c].get("label", c)} for c in callers
        ],
    }


def decouple_plan(
    G: nx.DiGraph,
    communities: dict[int, list[str]] | None,
    community_labels: dict[int, str] | None = None,
    *,
    top_n: int = 10,
    min_group_size: int = 3,
    extracted_only: bool = False,
    member_ratio_threshold: float = 0.2,
    min_communities_for_split: int = 2,
    net_benefit_threshold: float = 5.0,
) -> dict[str, Any]:
    """Build a Candidate Decoupled Architecture plan for the top-N god nodes.

    Fully deterministic given the same graph.json + communities + labels: no
    LLM call, no randomness (Louvain/Leiden are already seeded upstream by
    `graphify.cluster.cluster`). Every god_object entry is scored twice — its
    current risk (`original_risk_score`) and the NEW risk the proposed split
    would introduce (`split_risk_score`) — and `balance_risk` decides whether
    the split is actually worth recommending. The final diagram
    (decouple_html) only draws a group as a recommended extraction when that
    balance says so.
    """
    from graphify.analyze import god_nodes as _god_nodes

    gods = _god_nodes(G, top_n=top_n)
    entries: list[dict[str, Any]] = []
    for g in gods:
        node_id = g["id"]
        info = classify_god_node(
            G, node_id, communities,
            extracted_only=extracted_only,
            member_ratio_threshold=member_ratio_threshold,
            min_communities_for_split=min_communities_for_split,
        )
        if info["classification"] == "god_object":
            groups = candidate_groups(
                G, info["members"], communities, community_labels,
                min_group_size=min_group_size,
            )
            info["proposed_groups"] = groups
            risk_before = original_risk_score(info)
            split = split_risk_score(G, node_id, groups)
            info["risk"] = balance_risk(risk_before, split, net_benefit_threshold=net_benefit_threshold)
        elif info["classification"] == "over_referenced_hub":
            info["hub_suggestion"] = hub_suggestion(G, node_id)
        entries.append(info)

    return {
        "params": {
            "top_n": top_n,
            "min_group_size": min_group_size,
            "extracted_only": extracted_only,
            "member_ratio_threshold": member_ratio_threshold,
            "min_communities_for_split": min_communities_for_split,
            "net_benefit_threshold": net_benefit_threshold,
        },
        "god_nodes": entries,
        "caveats": [
            "Member detection uses AST relation edges only (method/contains/defines); "
            "instance fields are not graph nodes for most languages, so this is a "
            "coupling proxy, not a true LCOM/attribute-usage measurement.",
            "source_location has no end line, so group sizes are counted in symbols, "
            "not lines of code.",
            "A same-source_file ownership guard excludes 'method' edges that symbol "
            "resolution repointed across files.",
            "cohesion_confidence is a second, independent signal (shared external "
            "neighbors between members of the same proposed group) — not a rerun of "
            "community detection. Treat 'low' groups as weaker evidence, not as wrong.",
            "risk_before/risk_after are heuristic 0-100 proxies (fixed weights/caps on "
            "size, coupling, and fragmentation; and, for the split, new cross-group "
            "edges and straddling callers) — comparative on THIS graph, not a "
            "formally validated complexity metric.",
            "recommendation is decided at whole-god-node granularity (extract ALL "
            "proposed groups, or none) — it does not search partial/alternative "
            "groupings for a better balance.",
        ],
    }


def render_markdown(plan: dict[str, Any]) -> str:
    p = plan["params"]
    lines = [
        "# Candidate Decoupled Architecture",
        "",
        "_Generated deterministically from graph.json — no LLM involved._",
        "",
        f"Params: top_n={p['top_n']} min_group_size={p['min_group_size']} "
        f"extracted_only={p['extracted_only']} "
        f"member_ratio_threshold={p['member_ratio_threshold']}",
        "",
    ]
    for entry in plan["god_nodes"]:
        lines.append(f"## `{entry['label']}` — {entry['classification']}")
        lines.append(f"- source: `{entry['source_file']}`")
        lines.append(
            f"- afferent={entry['afferent']} efferent={entry['efferent']} "
            f"member_count={entry['member_count']} member_ratio={entry['member_ratio']}"
        )
        if entry["classification"] == "god_object":
            risk = entry.get("risk", {})
            sd = risk.get("split_detail", {})
            lines.append(
                f"- risk_before={risk.get('risk_before')} risk_after={risk.get('risk_after')} "
                f"net_benefit={risk.get('net_benefit')} -> **{risk.get('recommendation')}**"
            )
            if sd.get("n_new_classes"):
                lines.append(
                    f"  - would create {sd['n_new_classes']} new classes; "
                    f"{sd['cross_group_edges']} cross-group edges introduced; "
                    f"{sd['straddling_callers']} caller(s) would depend on more than one new class"
                )
            for g in entry.get("proposed_groups", []):
                conf = g.get("cohesion_confidence", "n/a")
                lines.append("")
                lines.append(f"### Proposed: {g['name']} ({len(g['members'])} members, confidence={conf})")
                for lbl in g["member_labels"]:
                    lines.append(f"- {lbl}")
        elif "hub_suggestion" in entry:
            hs = entry["hub_suggestion"]
            lines.append("")
            lines.append(hs["rationale"])
            lines.append("")
            lines.append("Top dependents:")
            for d in hs["sample_dependents"]:
                lines.append(f"- {d['label']}")
        else:
            lines.append("")
            lines.append("_No split recommended — large but cohesive (members cluster in one community)._")
        lines.append("")
    lines.append("## Honesty notes")
    for c in plan["caveats"]:
        lines.append(f"- {c}")
    return "\n".join(lines)
