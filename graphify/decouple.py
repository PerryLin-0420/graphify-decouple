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
    this is a coupling proxy, not a true LCOM/attribute-usage measurement —
    UNLESS `project_root` is given to `decouple_plan`, in which case
    `state_affinity` re-parses the god node's own source file to measure
    real self/this-attribute overlap between proposed groups (see below).
  - `source_location` has no end line, so group sizes are counted in symbols,
    not lines of code.

A call-graph-only split can look clean while still being cosmetic: two
method groups can have zero cross-group CALLS and still share a pile of the
same `self.` instance state — split them and both new classes need that
state anyway (a back-reference, a shared context object, or duplicated
fields), so coupling didn't go away, it relocated. When `project_root` is
supplied, `graphify.state_affinity` re-parses the god node's source file
(11 languages, tree-sitter — see that module for exact coverage; C is
explicitly unsupported) to measure how much instance state each proposed
group's methods actually touch, and folds the worst pairwise overlap into
`split_risk_score` as a first-class cost — heavier than the call-graph
terms, because it is closer to the actual failure mode. Without
`project_root` this signal is skipped (not assumed clean), and every
skipped entry says so explicitly rather than silently scoring as if it
had been checked.
"""
from __future__ import annotations

import re
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


# Filename fragments that hint a class exists to move data in/out of the
# process (parser, DAO, repository, client, loader...) rather than to hold
# behavior. Used only to shortlist a "data_gateway" node_role — never to
# override the god_object/cohesive_but_large/over_referenced_hub
# classification, which stays purely structural. Matched as whole PATH
# TOKENS (see `_path_tokens`), not substrings — a short, common hint like
# "io" must not false-positive on an unrelated filename that merely
# contains those letters in sequence (e.g. "distribution_dialog.py").
_DATA_GATEWAY_PATH_HINTS = frozenset({
    "parser", "parse", "loader", "loading", "dao", "repository", "gateway",
    "client", "reader", "writer", "ingest", "importer", "exporter", "io",
})

_PATH_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _path_tokens(source_file: str) -> set[str]:
    """Lowercase alnum tokens split on any non-alnum separator (path
    separators, underscores, hyphens, dots) — e.g.
    'app/parser/touchstone_parser.py' -> {'app','parser','touchstone','py'}.
    Token-exact matching only works for the dominant snake_case/kebab-case
    filename convention; an unseparated compound name like 'dataloader.py'
    stays one token and will not match the 'loader' hint — an accepted
    false-negative in exchange for not false-positiving on substrings."""
    return set(_PATH_TOKEN_RE.findall(source_file.lower()))


def _classify_node_role(
    G: nx.DiGraph,
    node_id: str,
    members: list[str],
    *,
    project_root: "str | None" = None,
) -> dict[str, Any]:
    """Role hint for a god-node candidate, computed the SAME way regardless
    of whether it structurally classified as god_object, cohesive_but_large,
    or over_referenced_hub — the role is about WHAT the node is for, which is
    orthogonal to whether its own members happen to span multiple
    communities. A data-access class can just as easily land in god_object
    (many accessor methods, incidentally split across communities — see
    "data_gateway" below) as in over_referenced_hub (few members, mostly
    referenced): checking role only inside one structural bucket would miss
    the other.

    - "tool_function": a plain function (`_callable_class` not set — not a
      class at all) called from several unrelated files. It is already the
      single shared implementation; adding per-consumer facades would mean
      DUPLICATING it, the opposite of consolidation. The applicable check is
      whether near-duplicate reimplementations exist elsewhere in the
      codebase — a separate, corpus-wide similarity scan, not run here.
    - "data_gateway": a class whose own filename reads as a data ingress/
      egress point (parser/loader/DAO/repository/client/...). Splitting or
      narrowing ITS interface does not address the real risk: other code
      bypassing it and touching the same underlying resource directly. That
      bypass is invisible to a same-file/degree check, and the call graph
      itself may not capture it (e.g. a module-level alias like
      `parse_x = parse_y` is not resolved to a call edge in every extractor
      path) — so this role is a shortlist for manual review, not a verified
      finding. A "god_object" data_gateway additionally gets a
      `role_caveat` (see `decouple_plan`) warning that a clean-looking split
      score does not mean the split addresses the actual risk for this role.

    Anything else stays "generic" — `hub_suggestion` keeps its original text,
    and god_object/cohesive_but_large entries get no extra caveat.
    """
    is_class = bool(G.nodes[node_id].get("_callable_class"))
    source_file = str(G.nodes[node_id].get("source_file") or "")

    caller_files = {
        G.nodes[u].get("source_file")
        for u, _v, data in G.in_edges(node_id, data=True)
        if data.get("relation") not in MEMBER_RELATIONS
    }
    caller_files.discard(source_file)
    caller_files.discard(None)
    caller_files.discard("")

    if not is_class:
        if len(caller_files) >= 3:
            return {"role": "tool_function", "distinct_caller_files": len(caller_files)}
        return {"role": "generic"}

    if not _path_tokens(source_file) & _DATA_GATEWAY_PATH_HINTS:
        return {"role": "generic"}

    read_ratio = None
    state_analysis = "skipped (no project_root given, unsupported language, or source unreadable)"
    if project_root and members:
        from pathlib import Path as _Path

        from graphify.state_affinity import extract_method_attribute_usage

        label = str(G.nodes[node_id].get("label", node_id))
        member_labels = [G.nodes[m].get("label", m) for m in members]
        abs_source = str(_Path(project_root) / source_file)
        usage = extract_method_attribute_usage(abs_source, label, member_labels)
        if usage:
            reads = sum(len(u["reads"]) for u in usage.values())
            writes = sum(len(u["writes"]) for u in usage.values())
            if reads + writes:
                read_ratio = round(reads / (reads + writes), 3)
                state_analysis = "ok"

    return {
        "role": "data_gateway",
        "distinct_caller_files": len(caller_files),
        "read_ratio": read_ratio,
        "state_analysis": state_analysis,
    }


def classify_god_node(
    G: nx.DiGraph,
    node_id: str,
    communities: dict[int, list[str]] | None = None,
    *,
    extracted_only: bool = False,
    member_ratio_threshold: float = 0.2,
    min_communities_for_split: int = 2,
    project_root: "str | None" = None,
) -> dict[str, Any]:
    """Classify why `node_id` is a god node.

    - "god_object": many own members (method/contains/defines), spread across
      >= min_communities_for_split communities -> Extract Class applies.
    - "cohesive_but_large": many own members but they cluster in one
      community -> large but not fragmented; no split recommended.
    - "over_referenced_hub": few/no own members relative to total degree ->
      the coupling is inbound (afferent), not internal responsibility bloat;
      splitting the class body would not reduce coupling.

    Every entry, regardless of which of the three above it lands in, also
    gets a `node_role` (see `_classify_node_role`) narrowing "what this node
    is for" into "tool_function", "data_gateway", or "generic" — computed
    independently of the structural classification, since a data-access
    class can land in god_object just as easily as in over_referenced_hub.
    `hub_suggestion` uses it for over_referenced_hub entries; `decouple_plan`
    uses it to attach a `role_caveat` to god_object entries. `project_root`,
    when given, lets a "data_gateway" candidate be corroborated against its
    own members' read/write profile via `graphify.state_affinity`.
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

    result = {
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
        "node_role": _classify_node_role(G, node_id, members, project_root=project_root),
    }
    return result


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
_STATE_OVERLAP_ADD_WEIGHT = 0.6  # extra risk points ADDED (not blended) at 100% state overlap
_ACYCLIC_EDGE_DISCOUNT = 0.5   # halves the cross-group-edge component when proposed groups'
                               # dependencies form a DAG (delegating/pipeline) instead of a
                               # cycle — see split_risk_score's "group_dependency_shape"


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


def _group_state_overlap(
    source_file: "str | None",
    class_label: str,
    non_residual_groups: list[dict[str, Any]],
) -> "dict[str, Any] | None":
    """Worst-case (max) pairwise self/this-attribute overlap between the
    proposed groups, via `graphify.state_affinity`. None on any skip
    (unsupported language, unreadable file, nothing found) — a skip, not a
    zero; callers must not treat None as "verified clean"."""
    if not source_file or len(non_residual_groups) < 2:
        return None
    import itertools

    from graphify.state_affinity import extract_method_attribute_usage
    from graphify.state_affinity import state_overlap as _pair_overlap

    all_labels = [lbl for g in non_residual_groups for lbl in g.get("member_labels", [])]
    usage = extract_method_attribute_usage(source_file, class_label, all_labels)
    if not usage:
        return None
    pairs: list[dict[str, Any]] = []
    for ga, gb in itertools.combinations(non_residual_groups, 2):
        ov = _pair_overlap(usage, ga.get("member_labels", []), gb.get("member_labels", []))
        if ov is None:
            continue
        pairs.append({
            "group_a": ga["name"], "group_b": gb["name"],
            "overlap": ov["overlap"],
            "field_overlap": ov["field_overlap"],
            "call_overlap": ov["call_overlap"],
            "shared_attrs": ov["shared_attrs"],
            "shared_writes": ov["shared_writes"],
            "shared_calls": ov["shared_calls"],
        })
    if not pairs:
        return None
    pairs.sort(key=lambda p: -p["overlap"])
    return {"max_overlap": pairs[0]["overlap"], "pairs": pairs}


def split_risk_score(
    G: nx.DiGraph,
    god_id: str,
    groups: list[dict[str, Any]],
    *,
    state_overlap: "dict[str, Any] | None" = None,
) -> dict[str, Any]:
    """0-100 proxy for the risk the SPLIT ITSELF introduces — complexity that
    does not exist today and only appears because of the split:

    - `cross_group_edges`: calls/references between members that end up in
      DIFFERENT proposed groups. Today these are invisible intra-class edges;
      after extraction they become new, explicit inter-class dependencies.
      Weighted by `group_dependency_shape` (below) before it enters the
      score — a purely one-directional fan of these edges is a materially
      cheaper shape than the same count split across both directions.
    - `group_dependency_shape`: "dag" when the proposed groups' cross-group
      edges, collapsed to one node per group, form NO cycle — i.e. every
      dependency between two proposed groups runs the same way (group A
      calls into group B, never the reverse). This is the delegating/
      pipeline shape (a large orchestrator whose own computation is thin but
      whose members fan out into worker/stage groups it calls one-way) —
      after extraction it needs only a one-directional reference between the
      new classes. "cyclic" means at least one pair of groups calls each
      other (or a longer cycle through 3+ groups) — after extraction that
      pair needs a back-reference or a mediator between them, a strictly
      more expensive shape, so it gets NO discount regardless of how "thin"
      any individual group looks. This is a shape check on THIS split's own
      edges, not a language- or domain-aware "is this a pipeline" judgment —
      a "dag" verdict on a single split with only 2 groups is weak evidence
      either way; it is one signal among several here, not a classification.
    - `straddling_callers`: outside nodes that depend on members from more
      than one proposed group. Today they hold one reference (the original
      class); after extraction they must depend on multiple new classes.
      NOT discounted by `group_dependency_shape` — a straddling caller pays
      the same integration cost regardless of which way the groups call
      each other.
    - `max_state_overlap` (only when `state_overlap` is supplied — see
      `_group_state_overlap` / `graphify.state_affinity`): the worst-case
      share of `self`/`this` state two proposed groups have in common. This
      gets MORE weight than the call-graph terms above: two groups can have
      zero cross-group calls and still both need the same instance state,
      which the call graph cannot see at all — that is the "moved the
      methods, didn't reduce the coupling" failure mode. Also NOT discounted
      by `group_dependency_shape`: shared instance state is a cost whether
      the calls between the groups are one-way or mutual.

    A single non-residual group (nothing left to compare against) has no
    split risk by construction — there is no second class to be coupled to.
    """
    non_residual = [g for g in groups if g["community_id"] is not None]
    if len(non_residual) < 2:
        return {
            "n_new_classes": len(non_residual),
            "cross_group_edges": 0,
            "group_dependency_shape": "n/a (nothing to compare)",
            "straddling_callers": 0,
            "straddling_caller_labels": [],
            "state_analysis": "n/a (nothing to compare)",
            "max_state_overlap": None,
            "state_overlap_pairs": [],
            "score": 0.0,
        }

    member_group: dict[str, int] = {m: gi for gi, g in enumerate(non_residual) for m in g["members"]}
    all_members = set(member_group)

    cross_group_edges = 0
    group_pairs: set[tuple[int, int]] = set()
    for u, v in G.edges():
        gu, gv = member_group.get(u), member_group.get(v)
        if gu is not None and gv is not None and gu != gv:
            cross_group_edges += 1
            group_pairs.add((gu, gv))

    # Collapse the proposed groups to one node each and check whether their
    # mutual dependencies form a cycle — see the "group_dependency_shape"
    # entry in this function's docstring for what "dag" vs "cyclic" means
    # and why only "dag" gets a discount.
    group_condensation: nx.DiGraph = nx.DiGraph()
    group_condensation.add_nodes_from(range(len(non_residual)))
    group_condensation.add_edges_from(group_pairs)
    is_dag = nx.is_directed_acyclic_graph(group_condensation)
    group_dependency_shape = "dag" if is_dag else "cyclic"

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
    if is_dag:
        edge_component *= _ACYCLIC_EDGE_DISCOUNT
    straddle_component = min(len(straddlers) / total_callers, 1.0)
    group_overhead = min((len(non_residual) - 1) / _SPLIT_GROUP_CAP, 1.0)

    # Same call-graph weights regardless of whether the state check ran —
    # keeps the two signals independent instead of one diluting the other.
    call_graph_score = 100 * (0.45 * edge_component + 0.40 * straddle_component + 0.15 * group_overhead)

    if state_overlap is not None:
        state_component = state_overlap.get("max_overlap") or 0.0
        # ADDITIVE, not blended into the weighted average above: state
        # coupling and call-graph coupling are two INDEPENDENT reasons a
        # split can fail, and either one is bad news on its own. Averaging
        # them let a call-graph score that was already high (near its cap)
        # get pulled DOWN by a merely-moderate state overlap — the opposite
        # of what a second bad signal should do. Adding it on top (capped at
        # 100) means the state check can only reveal MORE risk, never less.
        score = round(min(100.0, call_graph_score + _STATE_OVERLAP_ADD_WEIGHT * 100 * state_component), 1)
        state_analysis = "ok"
    else:
        score = round(call_graph_score, 1)
        state_analysis = "skipped (no project_root given, unsupported language, or source unreadable)"

    return {
        "n_new_classes": len(non_residual),
        "cross_group_edges": cross_group_edges,
        "group_dependency_shape": group_dependency_shape,
        "straddling_callers": len(straddlers),
        "straddling_caller_labels": [G.nodes[c].get("label", c) for c in straddlers[:8]],
        "state_analysis": state_analysis,
        "max_state_overlap": state_overlap.get("max_overlap") if state_overlap else None,
        "state_overlap_pairs": state_overlap.get("pairs", []) if state_overlap else [],
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


def _data_gateway_rationale(node_role: dict[str, Any]) -> str:
    """Shared wording for a "data_gateway" node_role — used by both
    `hub_suggestion` (over_referenced_hub) and `decouple_plan`'s
    `role_caveat` (god_object), so the same warning doesn't drift into two
    different texts depending on which structural bucket the node landed in."""
    if node_role.get("state_analysis") == "ok":
        state_note = f"own members are read-heavy (read_ratio={node_role.get('read_ratio')}), consistent with a data-access class"
    else:
        state_note = f"member read/write profile not checked ({node_role.get('state_analysis')})"
    return (
        "This class's filename and role look like a data ingress/egress point "
        f"(parser/loader/DAO/repository/client) — {state_note}. A clean-looking "
        "coupling score does not mean the real risk is addressed: other code "
        "bypassing this class and touching the same underlying resource (file, "
        "table, endpoint) directly, which fragments where that data can be "
        "validated or changed. Check other call sites into this file's "
        "lower-level read/parse/write functions for direct access that skips "
        "this class — that check is call-graph-based and can miss aliased "
        "re-exports (e.g. `f = other_module.g`)."
    )


def hub_suggestion(
    G: nx.DiGraph,
    node_id: str,
    *,
    node_role: "dict[str, Any] | None" = None,
    sample_size: int = 8,
) -> dict[str, Any]:
    """Suggestion for an over-referenced hub: not a split candidate. Splitting
    its body would not reduce coupling because the coupling is inbound.

    `node_role` (from `classify_god_node`, see `_classify_node_role`) swaps in
    role-specific advice for two shapes where the generic "narrow the
    interface / add per-consumer facades" text is backwards: an
    already-shared plain function ("tool_function") and a data ingress/
    egress class ("data_gateway"). Omitted or "generic" keeps the original
    text — callers using this function directly, outside `decouple_plan`,
    see unchanged behavior.
    """
    callers = sorted(G.predecessors(node_id), key=lambda n: (-G.degree(n), str(n)))[:sample_size]
    role = (node_role or {}).get("role", "generic")

    if role == "tool_function":
        recommendation = "keep_centralized"
        rationale = (
            "This is a plain function (not a class), already called from "
            f"{node_role.get('distinct_caller_files')} different files — it is "
            "already the single shared implementation, not a fragmented one. "
            "Narrowing its interface or adding per-consumer facades would mean "
            "DUPLICATING it, the opposite of consolidation. The applicable check "
            "is whether near-duplicate reimplementations of the same logic exist "
            "elsewhere in the codebase (a separate, corpus-wide similarity scan — "
            "not run as part of this report)."
        )
    elif role == "data_gateway":
        recommendation = "verify_single_entry_point"
        rationale = (
            "Extract-Class on ITS body would not address the real risk here: "
            + _data_gateway_rationale(node_role)
        )
    else:
        recommendation = "interface_segregation"
        rationale = (
            "Most of this node's edges are incoming references from other parts of "
            "the codebase, not its own methods/members. Extract-Class would not "
            "reduce coupling here; consider narrowing its public interface or "
            "introducing per-consumer facades instead."
        )

    return {
        "recommendation": recommendation,
        "role": role,
        "rationale": rationale,
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
    project_root: "str | None" = None,
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

    `project_root`, when given, lets `split_risk_score` fold in
    `graphify.state_affinity`'s self/this-attribute overlap between proposed
    groups (re-parses the god node's own `source_file`, resolved as
    `project_root / source_file`). Omit it and the call-graph-only score is
    used, honestly marked `state_analysis: "skipped"` rather than looking
    equally confident as a verified one.
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
            project_root=project_root,
        )
        if info["classification"] == "god_object":
            groups = candidate_groups(
                G, info["members"], communities, community_labels,
                min_group_size=min_group_size,
            )
            info["proposed_groups"] = groups
            risk_before = original_risk_score(info)
            non_residual = [gr for gr in groups if gr["community_id"] is not None]
            abs_source = None
            if project_root and info.get("source_file"):
                from pathlib import Path as _Path
                abs_source = str(_Path(project_root) / info["source_file"])
            overlap = _group_state_overlap(abs_source, info["label"], non_residual)
            split = split_risk_score(G, node_id, groups, state_overlap=overlap)
            info["risk"] = balance_risk(risk_before, split, net_benefit_threshold=net_benefit_threshold)
            if info.get("node_role", {}).get("role") == "data_gateway":
                # The split verdict above scores cross-group coupling only —
                # it says nothing about whether extracting accessor methods
                # off a data-access class is even the right move for this
                # role (see _classify_node_role). Attached regardless of
                # "split"/"marginal"/"keep_as_is": every one of those
                # verdicts is answering a different question than "is this
                # class's data being accessed from a single place".
                info["role_caveat"] = _data_gateway_rationale(info["node_role"])
        elif info["classification"] == "over_referenced_hub":
            info["hub_suggestion"] = hub_suggestion(G, node_id, node_role=info.get("node_role"))
        entries.append(info)

    return {
        "params": {
            "top_n": top_n,
            "min_group_size": min_group_size,
            "extracted_only": extracted_only,
            "member_ratio_threshold": member_ratio_threshold,
            "min_communities_for_split": min_communities_for_split,
            "net_benefit_threshold": net_benefit_threshold,
            "project_root": project_root,
        },
        "god_nodes": entries,
        "caveats": [
            "Member detection uses AST relation edges only (method/contains/defines); "
            "instance fields are not graph nodes for most languages, so this is a "
            "coupling proxy, not a true LCOM/attribute-usage measurement, EXCEPT where "
            "state_analysis == 'ok' (project_root was given and the language is "
            "supported) — there, max_state_overlap comes from re-parsing the actual "
            "source for self/this-attribute usage. See graphify.state_affinity for "
            "exact language coverage (C is explicitly unsupported).",
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
            "state_analysis == 'skipped' means max_state_overlap was NOT checked for "
            "that entry (no project_root given, unsupported language, or the source "
            "file could not be read/parsed) — it is an unknown, not a verified zero. "
            "Its recommendation rests on the call-graph terms alone.",
            "node_role ('tool_function'/'data_gateway'/'generic', see "
            "_classify_node_role) is a filename- and shape-based HINT, computed "
            "the same way regardless of classification, not a verified finding — "
            "in particular, 'data_gateway' bypass risk is call-graph-based and "
            "can miss a bypass hidden behind a module-level alias (e.g. "
            "`f = other_module.g`), which some extractor paths do not resolve to "
            "a call edge at all. A god_object entry with node_role=='data_gateway' "
            "gets a role_caveat alongside its split verdict — the two answer "
            "different questions (split coupling cost vs. single-entry-point "
            "risk) and neither one overrides the other.",
            "group_dependency_shape == 'dag' halves the cross-group-edge "
            "component of split_risk_score (a fixed 0.5 factor, not a "
            "validated constant) on the theory that a purely one-directional "
            "dependency between two proposed groups is cheaper than a mutual "
            "one — see split_risk_score's docstring. This is a shape check on "
            "the proposed split's own edges, not a semantic 'is this a "
            "pipeline' judgment, and a 2-group split is weak evidence either "
            "way; straddling_callers and max_state_overlap are NOT discounted "
            "by it.",
        ],
    }


def build_augmented_graph(
    G: nx.DiGraph,
    plan: dict[str, Any],
    communities: dict[int, list[str]],
) -> tuple[nx.Graph, dict[int, list[str]]]:
    """Overlay a decouple_plan()'s RECOMMENDED splits onto a COPY of G as
    extra nodes/edges, tagged `kind="proposed"` / `kind="proposed_edge"`.

    Only `risk.recommendation == "split"` groups are drawn. A `marginal` or
    `keep_as_is` candidate was already weighed by `balance_risk` and found
    not worth it — the balanced verdict IS the number (risk_before vs
    risk_after in DECOUPLE_PLAN.md / decouple.json), so there is nothing
    useful added by also drawing it on the graph.

    Adding the diamond alone does not show how the WIRING changes — the real
    members and their edges are still sitting there unchanged. So every real
    member of a recommended group is marked `decouple_extracted_into=<diamond
    id>`, and every edge that touches one is redirected onto the diamond it
    would move into (`kind="redirected_edge"` for an edge to something
    outside the split, `kind="new_coupling_edge"` when BOTH ends move into
    DIFFERENT new classes — the coupling the split itself introduces,
    already scored by `split_risk_score`). `exporters.html.to_html` renders
    a "Preview decoupled view" toggle that hides the extracted real nodes and
    shows the diamonds + redirected edges in their place — same graph,
    before/after, not two disconnected pictures. An edge whose both ends move
    into the SAME new class becomes purely internal and is dropped, not
    redirected. `method`/`contains`/`defines` ownership edges (the god node's
    own edge to each member) are skipped here — they are already the single
    "extract" edge below.

    The point of tagging rather than building a separate diagram: this graph
    is handed straight to `graphify.exporters.html.to_html()`, the SAME
    renderer that draws graph.html — identical physics, community colors,
    search, legend, info panel.

    Each proposed node is placed in its TARGET community (the group's own
    `community_id`), not the god node's community — so hiding that
    community's legend entry hides the proposed extraction along with the
    real members it would be made of. Residual groups (`community_id is
    None`) are never drawn — they stay on the original class, not a split.
    """
    G2 = G.copy()
    communities2 = {cid: list(members) for cid, members in communities.items()}
    member_to_diamond: dict[str, str] = {}
    diamond_ids: set[str] = set()
    # G2 is a plain (non-multi) DiGraph — add_edge on an existing pair
    # OVERWRITES it rather than adding a parallel edge. A member that itself
    # calls another member of ITS OWN god node via a non-ownership relation
    # (e.g. an explicit "calls" alongside the "method" edge) would otherwise
    # redirect onto the exact same (god_id, diamond_id) pair as the "extract"
    # edge below and silently clobber its styling. Track those pairs and
    # skip any redirect that would land on one — the extract edge is
    # canonical, never overwritten.
    extract_pairs: set[tuple[str, str]] = set()
    counter = 0

    for entry in plan.get("god_nodes", []):
        if entry.get("classification") != "god_object":
            continue
        risk = entry.get("risk", {})
        if risk.get("recommendation") != "split":
            continue
        god_id = entry["id"]
        state_pairs = risk.get("split_detail", {}).get("state_overlap_pairs", [])
        for g in entry.get("proposed_groups", []):
            cid = g.get("community_id")
            if cid is None:
                continue
            node_id = f"_proposed_{god_id}_{counter}"
            counter += 1
            # Pairs involving THIS group, from the other side's perspective —
            # so the info panel can say "shares X with Y" when you click
            # either diamond, not just when you click the one named group_a.
            my_overlaps = []
            for pair in state_pairs:
                if pair["group_a"] == g["name"]:
                    other = pair["group_b"]
                elif pair["group_b"] == g["name"]:
                    other = pair["group_a"]
                else:
                    continue
                if pair["overlap"] <= 0:
                    continue
                my_overlaps.append({
                    "with": other, "overlap": pair["overlap"],
                    "field_overlap": pair["field_overlap"], "call_overlap": pair["call_overlap"],
                    "shared_attrs": pair["shared_attrs"], "shared_writes": pair["shared_writes"],
                    "shared_calls": pair["shared_calls"],
                })
            my_overlaps.sort(key=lambda o: -o["overlap"])
            G2.add_node(
                node_id,
                label=g["name"],
                file_type="concept",
                source_file="",
                kind="proposed",
                hidden=True,  # default view is "before" — the toggle reveals it
                decouple_recommendation="split",
                decouple_risk={
                    "risk_before": risk.get("risk_before"),
                    "risk_after": risk.get("risk_after"),
                    "net_benefit": risk.get("net_benefit"),
                    "recommendation": "split",
                },
                decouple_state_overlaps=my_overlaps,
                member_count=len(g["members"]),
                cohesion_confidence=g.get("cohesion_confidence"),
            )
            G2.add_edge(
                god_id, node_id,
                relation="extract",
                confidence="EXTRACTED",
                kind="proposed_edge",
                decouple_recommendation="split",
                _src=god_id, _tgt=node_id,
            )
            communities2.setdefault(cid, []).append(node_id)
            diamond_ids.add(node_id)
            extract_pairs.add((god_id, node_id))
            for m in g["members"]:
                member_to_diamond[m] = node_id
                if m in G2.nodes:
                    G2.nodes[m]["decouple_extracted_into"] = node_id

    if not member_to_diamond:
        return G2, communities2

    # Redirect every non-ownership edge that touches an extracted member.
    # Aggregated by (new_src, new_tgt) so many original calls collapse into
    # ONE drawn edge with a weight, instead of cluttering the page.
    redirects: dict[tuple[str, str], dict[str, Any]] = {}
    for a, b, data in G.edges(data=True):
        if data.get("relation") in MEMBER_RELATIONS:
            continue  # already the single "extract" edge above
        a_moved = a in member_to_diamond
        b_moved = b in member_to_diamond
        if not a_moved and not b_moved:
            continue
        new_a = member_to_diamond.get(a, a)
        new_b = member_to_diamond.get(b, b)
        if new_a == new_b:
            continue  # both ends move into the SAME new class -> now internal
        if (new_a, new_b) in extract_pairs:
            continue  # would collide with the canonical "extract" edge
        info = redirects.setdefault((new_a, new_b), {"count": 0, "relations": set()})
        info["count"] += 1
        info["relations"].add(str(data.get("relation", "")) or "calls")

    for (new_a, new_b), info in redirects.items():
        kind = "new_coupling_edge" if new_a in diamond_ids and new_b in diamond_ids else "redirected_edge"
        G2.add_edge(
            new_a, new_b,
            relation=", ".join(sorted(info["relations"])),
            confidence="EXTRACTED",
            kind=kind,
            weight=info["count"],
            _src=new_a, _tgt=new_b,
        )

    return G2, communities2


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
        node_role = entry.get("node_role", {}).get("role", "generic")
        role_suffix = f" ({node_role})" if node_role != "generic" else ""
        lines.append(f"## `{entry['label']}` — {entry['classification']}{role_suffix}")
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
            if entry.get("role_caveat"):
                lines.append(f"  - **role caveat ({node_role}):** {entry['role_caveat']}")
            if sd.get("n_new_classes"):
                lines.append(
                    f"  - would create {sd['n_new_classes']} new classes; "
                    f"{sd['cross_group_edges']} cross-group edges introduced "
                    f"({sd.get('group_dependency_shape')}); "
                    f"{sd['straddling_callers']} caller(s) would depend on more than one new class"
                )
                if sd.get("state_analysis") == "ok":
                    lines.append(f"  - max shared instance-state overlap between two proposed groups: {sd['max_state_overlap']}")
                    for pair in sd.get("state_overlap_pairs", [])[:5]:
                        if pair["overlap"] <= 0:
                            continue
                        lines.append(
                            f"    - `{pair['group_a']}` <-> `{pair['group_b']}`: "
                            f"overlap={pair['overlap']} (fields={pair['field_overlap']}, calls={pair['call_overlap']})"
                        )
                        if pair["shared_attrs"]:
                            lines.append(f"      shared fields: {', '.join(pair['shared_attrs'][:8])}")
                        if pair["shared_writes"]:
                            lines.append(f"      shared WRITES (both mutate): {', '.join(pair['shared_writes'][:8])}")
                        if pair["shared_calls"]:
                            lines.append(f"      shared helper calls: {', '.join(pair['shared_calls'][:8])}")
                else:
                    lines.append(f"  - state-sharing check: {sd.get('state_analysis', 'skipped')}")
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
