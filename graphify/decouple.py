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
_CROSS_FLOOR_ADD_WEIGHT = 0.35   # fraction of data_floor.cross_floor_risk ADDED to the
                                 # CURRENT-risk score — see original_risk_score
_GROUP_FLOOR_ADD_WEIGHT = 0.3    # fraction of the worst PROPOSED GROUP's own
                                 # cross_floor_risk ADDED to split_risk_score — see
                                 # that function's docstring
_ACYCLIC_EDGE_DISCOUNT = 0.5   # halves the cross-group-edge component when proposed groups'
                               # dependencies form a DAG (delegating/pipeline) instead of a
                               # cycle — see split_risk_score's "group_dependency_shape"


def original_risk_score(entry: dict[str, Any]) -> float:
    """0-100 proxy for the god node's CURRENT risk: how much is bundled
    together (size), how coupled it already is (afferent+efferent), how
    many distinct responsibilities are mixed in (fragmentation), and how
    far it straddles the system's data flow (`floor_span`, when a floor
    profile is available — see `graphify.data_floor`).

    The cross-floor term is ADDITIVE, capped at 100, rather than being
    blended into the weighted average: straddling the data flow is an
    INDEPENDENT reason a class is risky, orthogonal to how big or coupled
    it is (a small, loosely-coupled class that both reads files and renders
    UI is genuinely mixed-responsibility, and averaging that signal against
    a low size score would hide it). Same direction as
    `split_risk_score`'s state-overlap term, for the same reason: a second
    bad signal must only ever reveal MORE risk, never less.

    A node with no floor profile (`floor_risk` absent, e.g. no I/O boundary
    detected anywhere in the graph) simply omits the term — unknown is not
    scored as clean, it is scored as "this component wasn't measured", and
    the report says which.

    Weights/caps are a fixed heuristic, not a validated complexity metric —
    useful to compare candidates on THIS graph, not as an absolute score."""
    size = min(entry["member_count"] / _RISK_SIZE_CAP, 1.0)
    coupling = min((entry["afferent"] + entry["efferent"]) / _RISK_COUPLING_CAP, 1.0)
    fragmentation = min(entry["distinct_member_communities"] / _RISK_FRAGMENTATION_CAP, 1.0)
    base = 100 * (0.40 * size + 0.35 * coupling + 0.25 * fragmentation)
    floor_risk = entry.get("floor_risk") or 0.0
    return round(min(100.0, base + _CROSS_FLOOR_ADD_WEIGHT * floor_risk), 1)


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
    - `max_group_floor_risk` (only when a group in `groups` carries a
      `floor_profile` — attached by `decouple_plan`, see
      `graphify.data_floor`, BEFORE this function is called; this function
      never computes floors itself): the worst
      `data_floor.cross_floor_risk` among the proposed groups' OWN member
      floors. A split grouped by community/coupling optimizes for a
      DIFFERENT axis than floor-coherence — a "recommended" split can
      still leave one or more resulting groups straddling the same several
      data-flow stages the original class did. This is ADDITIVE, same
      reasoning as the state-overlap term: crossing floors is bad news
      independent of how clean the call-graph shape looks, so a second bad
      signal must only ever reveal MORE risk. It does not veto a split —
      the weight (`_GROUP_FLOOR_ADD_WEIGHT`) is deliberately a fraction,
      not the whole 100, so a split can still net-benefit despite some
      residual floor-crossing if the coupling reduction is large enough.
      Absent (skipped) when no proposed group has a determinable floor —
      an unknown, never scored as if verified floor-coherent.

    A single non-residual group (nothing left to compare against) has no
    split risk by construction — there is no second class to be coupled to.
    """
    non_residual = [g for g in groups if g["community_id"] is not None]
    if len(non_residual) < 2:
        return {
            "n_new_classes": len(non_residual),
            "cross_group_edges": 0,
            "group_dependency_shape": "n/a",  # embedded inline in render_markdown's
                                               # parenthetical — the longer "nothing to
                                               # compare" phrasing already appears on
                                               # its own line via state_analysis below.
            "straddling_callers": 0,
            "straddling_caller_labels": [],
            "state_analysis": "n/a (nothing to compare)",
            "max_state_overlap": None,
            "state_overlap_pairs": [],
            "group_floor_analysis": "n/a (nothing to compare)",
            "max_group_floor_risk": None,
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

    score = call_graph_score

    if state_overlap is not None:
        state_component = state_overlap.get("max_overlap") or 0.0
        # ADDITIVE, not blended into the weighted average above: state
        # coupling and call-graph coupling are two INDEPENDENT reasons a
        # split can fail, and either one is bad news on its own. Averaging
        # them let a call-graph score that was already high (near its cap)
        # get pulled DOWN by a merely-moderate state overlap — the opposite
        # of what a second bad signal should do. Adding it on top (capped at
        # 100) means the state check can only reveal MORE risk, never less.
        score = min(100.0, score + _STATE_OVERLAP_ADD_WEIGHT * 100 * state_component)
        state_analysis = "ok"
    else:
        state_analysis = "skipped (no project_root given, unsupported language, or source unreadable)"

    # group_floor_profile is attached by decouple_plan (graphify.data_floor),
    # BEFORE this function runs — never recomputed here. A group missing it
    # (no boundary reachable, or no member had a determinable floor) is
    # simply absent from `group_profiles`, not treated as floor-coherent.
    from graphify.data_floor import cross_floor_risk as _cross_floor_risk

    group_profiles = [g["floor_profile"] for g in non_residual if g.get("floor_profile")]
    if group_profiles:
        max_group_floor_risk = max(_cross_floor_risk(p) for p in group_profiles)
        score = min(100.0, score + _GROUP_FLOOR_ADD_WEIGHT * max_group_floor_risk)
        group_floor_analysis = "ok"
    else:
        max_group_floor_risk = None
        group_floor_analysis = "skipped (no I/O boundary reachable, or no proposed group had a determinable floor)"

    return {
        "n_new_classes": len(non_residual),
        "cross_group_edges": cross_group_edges,
        "group_dependency_shape": group_dependency_shape,
        "straddling_callers": len(straddlers),
        "straddling_caller_labels": [G.nodes[c].get("label", c) for c in straddlers[:8]],
        "state_analysis": state_analysis,
        "max_state_overlap": state_overlap.get("max_overlap") if state_overlap else None,
        "state_overlap_pairs": state_overlap.get("pairs", []) if state_overlap else [],
        "group_floor_analysis": group_floor_analysis,
        "max_group_floor_risk": max_group_floor_risk,
        "score": round(score, 1),
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

    from graphify.data_floor import class_floor_profile, compute_floors, cross_floor_risk

    # Data-flow floors for the whole graph, computed once (BFS from the I/O
    # boundary — see graphify.data_floor). Empty when no boundary is
    # detectable at all, in which case every entry's floor fields stay
    # absent rather than defaulting to a fabricated layer.
    floors, floor_reasons = compute_floors(G)

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
        floor_profile = class_floor_profile(G, node_id, info["members"], floors) if floors else None
        if floor_profile:
            info["floor_profile"] = floor_profile
            # Consumed by original_risk_score as an additive term — a class
            # straddling several data-flow stages is risky in a way the
            # call-graph metrics cannot see.
            info["floor_risk"] = cross_floor_risk(floor_profile)
        if info["classification"] == "god_object":
            groups = candidate_groups(
                G, info["members"], communities, community_labels,
                min_group_size=min_group_size,
            )
            # Each non-residual group's OWN floor profile, attached HERE —
            # the single place it is computed. split_risk_score reads it
            # (never recomputes it) to score whether the split actually
            # resolves cross-floor spread; render_markdown/decouple.json
            # carry it for reporting; decouple_3d.py reads the SAME
            # attached value again for its before/after view — nothing
            # downstream of decouple_plan recomputes floors from scratch.
            if floors:
                for g in groups:
                    if g["community_id"] is not None:
                        g["floor_profile"] = class_floor_profile(G, None, g["members"], floors)
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
            "floor_profile / floor_risk come from graphify.data_floor: BFS "
            "distance from the system's I/O boundary, where the boundary is "
            "detected by a NAME heuristic (path tokens + symbol-name stems), "
            "not by actual I/O analysis — it can miss a boundary hidden "
            "behind a domain-flavored name and can flag a parse_args() that "
            "never touches the outside world. Distance is measured on the "
            "UNDIRECTED graph: a call edge's direction is who-invokes-whom, "
            "which is not the same as which way data moves. A class with no "
            "floor_profile was NOT measured (no boundary reachable), which "
            "is not the same as sitting on a single floor — its "
            "risk_before carries no cross-floor term either way.",
            "Each proposed group ALSO gets its own floor_profile (attached "
            "once, here, and read — never recomputed — by split_risk_score "
            "and by decouple_3d.py's before/after view). max_group_floor_risk "
            "in a split's detail is the worst one, added into that split's "
            "score at a fraction (_GROUP_FLOOR_ADD_WEIGHT) of full weight — "
            "grouping by community/coupling optimizes for a DIFFERENT axis "
            "than floor-coherence, so a 'recommended' split is not "
            "guaranteed to leave every resulting group on a single floor; "
            "this makes that visible in the number instead of assumed. It "
            "is a weighted cost, not a veto — a split can still net-benefit "
            "despite some residual floor-crossing.",
        ],
    }


def _stable_unit_pair(seed: str) -> tuple[float, float]:
    """Two stable floats in [0, 1) derived from `seed` — a deterministic
    stand-in for `random.random()`. Used to scatter a class's members inside
    its own disc without them landing on a visibly regular ring; the point
    is an organic-looking spread, not statistical quality, but it MUST be
    reproducible (the same graph.json has to render identically every time,
    matching the rest of decouple's 0-LLM/deterministic contract)."""
    import hashlib

    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    a = int.from_bytes(digest[0:4], "big") / 2**32
    b = int.from_bytes(digest[4:8], "big") / 2**32
    return a, b


def _class_disc_radius(member_count: int) -> float:
    """Radius of the disc a class's own node + members are scattered into.
    Grows with sqrt(members) so AREA grows linearly with member count —
    node density inside a large class's disc stays comparable to a small
    one's instead of the big classes becoming solid blobs."""
    import math

    return 70.0 + 42.0 * math.sqrt(max(member_count, 1))


def _pack_discs(sizes: list[tuple[str, float]]) -> dict[str, tuple[float, float]]:
    """Place each (key, radius) disc so NO two overlap, largest first, by
    walking an Archimedean spiral outward from the origin and taking the
    first position that clears every disc already placed.

    Greedy and O(n^2) in the number of discs — fine for the scale this runs
    at (tens of classes per corpus, not thousands) and, unlike a physics
    relaxation, it terminates with a hard non-overlap guarantee rather than
    an approximate one. Largest-first matters: placing a big disc after the
    small ones would push it far out past a ring of small discs it could
    have sat inside.
    """
    import math

    placed: list[tuple[float, float, float]] = []
    out: dict[str, tuple[float, float]] = {}
    gap = 60.0  # visual breathing room between two hull edges
    for key, radius in sorted(sizes, key=lambda kv: -kv[1]):
        if not placed:
            out[key] = (0.0, 0.0)
            placed.append((0.0, 0.0, radius))
            continue
        # Spiral step is tied to the disc being placed so a large disc takes
        # coarse steps (it needs a large clearing anyway) and a small one
        # searches finely — a fixed step either crawls for big discs or
        # skips over gaps a small disc would have fit into.
        step = max(radius * 0.35, 25.0)
        theta = 0.0
        while True:
            r = step * theta / (2 * math.pi)
            x, y = r * math.cos(theta), r * math.sin(theta)
            if all(
                math.hypot(x - px, y - py) >= radius + pr + gap
                for px, py, pr in placed
            ):
                out[key] = (x, y)
                placed.append((x, y, radius))
                break
            theta += 0.35
    return out


def _class_cluster_layout(
    G: nx.DiGraph,
) -> "tuple[dict[str, dict[str, float]], dict[str, tuple[float, float, float]], dict[str, list[str]]]":
    """Fixed (x, y) positions for EVERY class in the graph and its own
    members, laid out so class regions never overlap each other.

    The default force-directed physics positions a method by the CALL
    graph, which routinely interleaves two different classes' methods in
    the same screen region (a class's methods call all over the codebase,
    not just each other), so a boundary drawn around a class over physics
    positions collides with its neighbors by construction — no amount of
    hull styling fixes that. This assigns each class its own disc instead
    (see `_pack_discs`, which guarantees non-overlap), and scatters that
    class's own node plus its members inside that disc
    (`_stable_unit_pair`) — deliberately NOT on a regular ring: the members'
    arrangement WITHIN a class carries no meaning worth encoding, and a
    visible ring implies an ordering that doesn't exist.

    Covers every node with `_callable_class` set (graphify's own extractor
    attribute — see extractors/engine.py), not just the god nodes a
    decouple plan analyzed: a class boundary is a fact about the code, true
    whether or not that particular class scored high enough to be a split
    candidate. A class with no members is skipped — there is no region to
    draw, and pinning a lone node would only fight the physics layout for
    nothing.

    Free functions — real callables that belong to no class — are grouped
    by their own SOURCE FILE into module regions, so every implementation
    node ends up inside some boundary rather than floating unattached
    (measured on a real corpus: 368 callable nodes, most of a procedural
    module's content, sat outside every class region). A module region is
    the same kind of statement a class region is: "this is one unit".
    Nodes that are pure DECLARATION rather than implementation are
    deliberately left out — the synthetic file-level hub node graphify's
    extractor creates per file, method stubs, and external symbols with no
    source file of their own (`numpy.ndarray` and friends): they declare
    that something exists elsewhere, they are not code living in this unit.

    Returns `(positions, discs, region_members)`. `discs` maps each region's
    key (a class node id, or a `_module::<path>` synthetic key) to its
    `(center_x, center_y, radius)`. The renderer draws THAT circle rather
    than fitting an ellipse to the member positions: the disc is the exact
    region `_pack_discs` proved non-overlapping, whereas a fitted ellipse
    has to be padded outward to cover every member and can then cross into
    a neighbor (measured on a real corpus: 7 overlapping pairs from fitting
    alone, on a layout whose discs were provably disjoint). `region_members`
    is the AUTHORITATIVE membership for each key — callers must use it
    rather than re-deriving "who's in this module region" from source_file
    (an earlier version of this code's caller did exactly that, filtering
    `positions` by `source_file`, and silently pulled in a DIFFERENT class's
    members whenever a class shared a file with free functions — every node
    is claimed by exactly ONE region here, so this dict is the single
    source of truth for it).
    """
    from graphify.analyze import _is_file_node

    sizes: list[tuple[str, float]] = []
    members_by_class: dict[str, list[str]] = {}
    in_a_class: set[str] = set()
    for nid, data in G.nodes(data=True):
        if not data.get("_callable_class"):
            continue
        members = member_ids(G, nid)
        if not members:
            continue
        members_by_class[nid] = members
        in_a_class.add(nid)
        in_a_class.update(members)
        sizes.append((nid, _class_disc_radius(len(members))))

    # Module regions for the free functions left over.
    free_by_file: dict[str, list[str]] = {}
    for nid, data in G.nodes(data=True):
        if nid in in_a_class:
            continue
        if data.get("file_type") != "code" or not data.get("_callable"):
            continue
        if data.get("_callable_class"):
            continue  # a memberless class: no region, see above
        source_file = str(data.get("source_file") or "")
        if not source_file:
            continue  # external symbol — declared elsewhere, not code here
        if _is_file_node(G, nid):
            continue  # synthetic file hub / stub — declaration, not implementation
        free_by_file.setdefault(source_file, []).append(nid)
    for source_file, free_nodes in free_by_file.items():
        if len(free_nodes) < 2:
            continue  # a lone function is not a "unit" worth outlining
        key = f"_module::{source_file}"
        members_by_class[key] = sorted(free_nodes)
        sizes.append((key, _class_disc_radius(len(free_nodes))))

    if not sizes:
        return {}, {}, {}

    import math

    anchors = _pack_discs(sizes)
    positions: dict[str, dict[str, float]] = {}
    discs: dict[str, tuple[float, float, float]] = {}
    for class_id, members in members_by_class.items():
        ax, ay = anchors[class_id]
        radius = _class_disc_radius(len(members))
        # A module region has no node of its own to pin (its key is
        # synthetic) — only its members get positions.
        if not class_id.startswith("_module::"):
            positions[class_id] = {"x": ax, "y": ay}
        discs[class_id] = (ax, ay, radius)
        for m in members:
            angle_unit, radius_unit = _stable_unit_pair(f"{class_id}::{m}")
            angle = angle_unit * 2 * math.pi
            # sqrt() on the radial term spreads points evenly over AREA;
            # using the raw uniform value would visibly bunch them toward
            # the disc's center.
            r = math.sqrt(radius_unit) * radius * 0.82
            positions[m] = {"x": ax + r * math.cos(angle), "y": ay + r * math.sin(angle)}

    # Scale the whole packed layout up to the same order of magnitude the
    # browser's forceAtlas2Based physics spreads the REST of the graph over
    # (everything not in a class — free functions, docs, config — still
    # settles at runtime, and this Python-side layout cannot see where).
    # Empirically that spread grows with sqrt(node count): a ~1200-node
    # corpus settles to roughly ±3700 units, while the packed discs alone
    # came to ±1477 — leaving every class boundary crammed into the middle
    # 40% of the canvas and buried under the free nodes drawn over them.
    # Scaling uniformly preserves the non-overlap guarantee (every pairwise
    # distance grows by the same factor) and enlarges the regions
    # themselves, rather than only spreading their centers further apart.
    extent = max(
        (max(abs(p["x"]), abs(p["y"])) for p in positions.values()),
        default=0.0,
    )
    target_extent = 140.0 * math.sqrt(G.number_of_nodes())
    if extent > 0 and target_extent > extent:
        scale = target_extent / extent
        for p in positions.values():
            p["x"] *= scale
            p["y"] *= scale
        # Radii scale with the centers — scaling only the centers would
        # spread the discs apart while leaving each region the same small
        # size, which is what made them invisible at corpus scale.
        discs = {k: (cx * scale, cy * scale, r * scale) for k, (cx, cy, r) in discs.items()}
    return positions, discs, members_by_class


def _resolve_function_node(G: nx.DiGraph, source_file: str, name: str) -> "str | None":
    """Best-effort match of a `tool_dedup` function fingerprint (bare name +
    source_file, tree-sitter/`ast`-derived) to a real graph node id
    (graphify's own extractor, a SEPARATE pass over the same file). Matches
    on source_file + a label equal to `name` once graphify's own decoration
    (a leading "." for a method, a trailing "()") is stripped. Returns None
    — a skip, not a guess — when zero or more than one node matches; an
    ambiguous match drawn on the graph would be actively misleading."""
    candidates = [
        nid for nid, data in G.nodes(data=True)
        if data.get("source_file") == source_file
        and str(data.get("label", "")).strip().lstrip(".").rstrip("()") == name
    ]
    return candidates[0] if len(candidates) == 1 else None


def _resolve_class_node(G: nx.DiGraph, container: "str | None", source_file: "str | None") -> "str | None":
    """Same idea as `_resolve_function_node`, for a class name instead of a
    function name — used to find the real node for a merge_target's
    `target_container`."""
    if container is None:
        return None
    return _resolve_function_node(G, source_file or "", container)


_CONSOLIDATION_AFFERENT_CAP = 40.0    # summed afferent degree across all copies >= this maxes concentration
_CONSOLIDATION_FLOOR_SPAN_CAP = 3.0   # floor span across resolved copies >= this maxes the cross-floor component
_CONSOLIDATION_BENEFIT_CAP = 4.0      # (copies - 1) >= this maxes the raw duplication-removed benefit
_CONSOLIDATION_NET_THRESHOLD = 5.0    # net_benefit must exceed this to recommend consolidating


def consolidation_risk_score(
    G: nx.DiGraph,
    cluster: dict[str, Any],
    resolved_ids: list[str],
    floors: "dict[str, int] | None",
) -> dict[str, Any]:
    """Risk/benefit verdict for ONE `tool_dedup` cluster's consolidation —
    same STYLE as `split_risk_score`/`balance_risk` (named, capped weighted
    components; an explicit net_benefit verdict), but never compared
    against a split's numbers or folded into `risk_before`/`risk_after`.
    A split's net_benefit answers a LOCAL question (is this one class's
    internal responsibility split worth it); a merge's answers a GLOBAL one
    (how many far-apart places currently duplicate this logic, and what
    would depending on one shared place cost). Putting both on one scale
    would produce a number that looks precise while comparing two
    different things — see the design discussion this function resolves.

    Benefit: `(copies - 1)` — how many redundant implementations would go
    away — capped, and scaled by `avg_jaccard` (cluster["avg_jaccard"]):
    a low-confidence match earns little benefit credit for "removing
    duplication" it isn't confident is even real duplication.

    Risk, three independent components:
    - `afferent_total`: summed in-degree across every resolved copy — how
      many distinct call sites currently depend on ONE OF the copies.
      After consolidation they all depend on the SAME node — a
      concentration risk (single point of failure / wider blast radius)
      that scales with how heavily-used the duplicated logic already is.
    - `floor_span`: the spread, in `graphify.data_floor` terms, across the
      resolved copies' floors. Consolidating logic that currently lives at
      different distances from the I/O boundary pulls the new shared unit
      across that same span — the same structural risk
      `data_floor.cross_floor_risk` scores for an existing class, applied
      here to a proposed one.
    - `uncertainty`: `1 - avg_jaccard` — structural similarity is a proxy,
      not semantic equivalence (see `tool_dedup`'s own module docstring);
      a weaker match is a real correctness risk if merged anyway, not just
      a weaker signal.

    `floors` may be `None` or incomplete (no I/O boundary detected, or a
    resolved node outside every reachable component) — the floor
    component is then 0, not penalized and not silently treated as
    "verified single-floor"; `state_analysis`-style callers should read
    `floor_span_known` to tell the two apart.
    """
    afferent_total = sum(G.in_degree(nid) for nid in resolved_ids if nid in G.nodes)
    afferent_component = min(afferent_total / _CONSOLIDATION_AFFERENT_CAP, 1.0)

    known_floors = [floors[nid] for nid in resolved_ids if floors and nid in floors]
    floor_span = (max(known_floors) - min(known_floors)) if known_floors else 0
    floor_component = min(floor_span / _CONSOLIDATION_FLOOR_SPAN_CAP, 1.0)

    avg_jaccard = float(cluster.get("avg_jaccard") or 0.0)
    uncertainty_component = max(0.0, 1.0 - avg_jaccard)

    risk = round(100 * (
        0.45 * afferent_component
        + 0.30 * floor_component
        + 0.25 * uncertainty_component
    ), 1)

    n_copies = len(cluster.get("members", []))
    raw_benefit = min(max(n_copies - 1, 0) / _CONSOLIDATION_BENEFIT_CAP, 1.0)
    benefit = round(100 * raw_benefit * avg_jaccard, 1)

    net_benefit = round(benefit - risk, 1)
    if net_benefit > _CONSOLIDATION_NET_THRESHOLD:
        recommendation = "consolidate"
    elif net_benefit < -_CONSOLIDATION_NET_THRESHOLD:
        recommendation = "keep_separate"
    else:
        recommendation = "marginal"

    return {
        "consolidation_benefit": benefit,
        "consolidation_risk": risk,
        "net_benefit": net_benefit,
        "recommendation": recommendation,
        "afferent_total": afferent_total,
        "floor_span": floor_span,
        "floor_span_known": bool(known_floors),
        "avg_jaccard": avg_jaccard,
    }


def annotate_consolidation_risk(
    G: nx.DiGraph,
    report: dict[str, Any],
    floors: "dict[str, int] | None" = None,
) -> dict[str, Any]:
    """Attach a `consolidation_risk` verdict (see `consolidation_risk_score`)
    to every cluster in a `tool_dedup.find_duplicate_function_clusters`
    report, IN PLACE, and return it. A cluster where fewer than 2 members
    resolve to real graph nodes is left un-annotated (`consolidation_risk`
    absent) — the same under-report-don't-guess rule
    `overlay_tool_dedup_clusters` applies, so a report rendered before vs.
    after this call never disagrees about which clusters are actionable.

    Deliberately separate from `overlay_tool_dedup_clusters`: that function
    builds a VISUALIZATION (needs the plan's proposed nodes to already
    exist); this one only needs the report and the graph, so it can run
    before `render_markdown`/`decouple.json` are written — the CLI calls it
    first, so the risk verdict is already there when the report renders,
    not only on the graph the HTML view builds afterward.
    """
    for cluster in report.get("clusters", []):
        resolved_ids = [
            nid for nid in (
                _resolve_function_node(G, m["source_file"], m["name"])
                for m in cluster["members"]
            )
            if nid is not None
        ]
        if len(resolved_ids) < 2:
            continue
        cluster["consolidation_risk"] = consolidation_risk_score(G, cluster, resolved_ids, floors)
    return report


def overlay_tool_dedup_clusters(
    G: nx.DiGraph,
    communities: dict[int, list[str]],
    report: dict[str, Any],
) -> tuple[nx.Graph, dict[int, list[str]]]:
    """Overlay a `tool_dedup.find_duplicate_function_clusters` report's
    consolidation candidates onto a COPY of `G` as WIRING — never as a
    background region. Background tints are reserved exclusively for class
    boundaries (see `_class_cluster_layout`); a consolidation is a proposed
    CHANGE to the code, in the same category as a split, so it belongs in
    the same "Preview decoupled view" vocabulary the splits use (proposed
    nodes + proposed edges), not in the vocabulary that means "this is one
    class".

    `tool_dedup` finds functions from source files directly (tree-sitter),
    independently of graphify's own extraction — the two do not share an id
    scheme. Each cluster member is resolved back to a real graph node via
    `_resolve_function_node` FIRST; a cluster where fewer than 2 members
    resolve is skipped entirely (skipped, never drawn with a guessed
    position) — this is expected to under-report, not over-report.

    - `merge_into_existing`: a dashed `merge_candidate` edge from each
      resolved duplicate to the existing target class's node — "this would
      move into that class".
    - `independent`: a new `kind="proposed"` node (same visual vocabulary as
      a split's diamond — hidden by default, shown by the same "Preview
      decoupled view" toggle) representing the not-yet-created shared
      class/module, with a `merge_candidate` edge from each duplicate.

    Can be combined with `build_augmented_graph`'s output by calling this
    SECOND on its result — proposed nodes/edges accumulate, and the class
    hulls that function created are read and preserved untouched.
    """
    G2 = G.copy()
    communities2 = {cid: list(members) for cid, members in communities.items()}
    hulls: list[dict[str, Any]] = list(G.graph.get("hyperedges", []))
    counter = 0

    for cluster in report.get("clusters", []):
        resolved = [
            (m, _resolve_function_node(G2, m["source_file"], m["name"]))
            for m in cluster["members"]
        ]
        resolved_ids = [nid for _m, nid in resolved if nid is not None]
        if len(resolved_ids) < 2:
            continue

        mt = cluster["merge_target"]
        if mt["recommendation"] == "merge_into_existing":
            target_id = _resolve_class_node(G2, mt["target_container"], mt["target_source_file"])
        else:
            target_id = f"_merge_proposed_{counter}"
            counter += 1
            sample_name = cluster["members"][0]["name"]
            G2.add_node(
                target_id,
                label=f"(shared) {sample_name}",
                file_type="concept",
                source_file="",
                kind="proposed",
                hidden=True,
                decouple_recommendation="merge",
                member_count=len(resolved_ids),
            )
            # Best-effort placement at the centroid of whichever resolved
            # duplicates already have a class-cluster position (see
            # build_augmented_graph/_class_cluster_layout) — NOT a hard
            # guarantee like the class layer's: a duplicate outside any
            # analyzed class (most of them, in practice — see this
            # function's own docstring) has no cluster position to average,
            # so this can fall back to nothing, leaving the node
            # physics-placed. Only the "class" layer promises no overlap.
            positioned = [
                (G2.nodes[nid]["cluster_x"], G2.nodes[nid]["cluster_y"])
                for nid in resolved_ids
                if "cluster_x" in G2.nodes.get(nid, {})
            ]
            if positioned:
                G2.nodes[target_id]["cluster_x"] = sum(p[0] for p in positioned) / len(positioned)
                G2.nodes[target_id]["cluster_y"] = sum(p[1] for p in positioned) / len(positioned)

        # NO hull for a merge candidate, for the same reason a split gets
        # none (see build_augmented_graph): a background tint already means
        # "this is one class", and a second wash of regions over the class
        # boundaries hid the thing they were drawn on top of. The
        # consolidation is expressed as WIRING instead — a
        # `merge_candidate` edge from each scattered duplicate to the place
        # it would move into, revealed by the same "Preview decoupled view"
        # toggle as the split diamonds.
        if target_id is not None:
            for nid in resolved_ids:
                if nid == target_id:
                    continue
                G2.add_edge(
                    nid, target_id,
                    relation="merge_candidate",
                    confidence="INFERRED",
                    kind="proposed_edge",
                    decouple_recommendation="merge",
                    _src=nid, _tgt=target_id,
                )

    G2.graph["hyperedges"] = hulls
    return G2, communities2


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

    Every analyzed class also gets a HULL — a shaded boundary drawn around
    itself and its own existing members (via `exporters.html`'s hyperedge
    renderer; see `_hyperedge_script`) — regardless of whether a split is
    recommended. This exists because a flat node-and-edge graph cannot show
    "these methods already live in the same class" as anything other than
    edges identical in kind to every other edge: nothing distinguishes
    "these nodes happen to be connected" from "these nodes are the SAME
    class". A baseline hull, colored per-class from the same categorical
    palette used for community coloring elsewhere in the app, answers that
    directly, and a recommended split then gets its OWN green hull around
    the diamond + the real members it would take — so a class splitting is
    visible as one hull becoming several (in a NEW color, not just "the same
    class's hull, but smaller"), not just as new edges appearing. Baseline
    hulls use the existing class's own node id + `entry["members"]`; split
    hulls use a group's diamond id + `g["members"]` — appended to (never
    replacing) whatever hyperedges the graph already carries (e.g.
    README-derived semantic groupings), tagged with `fill`/`stroke`/`dashed`
    so they render in a visually distinct style from those.
    """
    from graphify.exporters.base import COMMUNITY_COLORS

    G2 = G.copy()
    communities2 = {cid: list(members) for cid, members in communities.items()}
    member_to_diamond: dict[str, str] = {}
    diamond_ids: set[str] = set()
    hulls: list[dict[str, Any]] = list(G.graph.get("hyperedges", []))

    # Non-overlapping positions for EVERY class in the graph + its members
    # (see _class_cluster_layout) — stamped as `cluster_x`/`cluster_y` node
    # attributes, NOT applied as the node's actual `x`/`y` here.
    # exporters.html's "Class boundaries" toggle (checked by default) is
    # what actually fixes nodes to these coordinates in the browser;
    # unchecking it lets physics take back over. Stamping happens
    # regardless of that toggle's default so the data is there either way.
    cluster_positions, class_discs, region_members = _class_cluster_layout(G)
    for nid, pos in cluster_positions.items():
        if nid in G2.nodes:
            G2.nodes[nid]["cluster_x"] = pos["x"]
            G2.nodes[nid]["cluster_y"] = pos["y"]

    # A boundary for EVERY class, not only the god nodes this plan analyzed:
    # "these methods live in this class" is a fact about the code, equally
    # true for a class that never scored high enough to be a split
    # candidate. Each gets its own color from the same categorical palette
    # used for community coloring elsewhere in the app — one flat color for
    # every class made adjacent boundaries indistinguishable from each
    # other. Ordered by node id so the color assignment is stable across
    # runs (dict iteration order follows insertion, which follows the
    # graph's own node order — stable for a given graph.json, but sorting
    # makes that independent of it).
    for i, region_id in enumerate(sorted(class_discs)):
        cx, cy, radius = class_discs[region_id]
        color = COMMUNITY_COLORS[i % len(COMMUNITY_COLORS)]
        if region_id.startswith("_module::"):
            # A module region groups the free functions of one file — same
            # kind of "this is one unit" statement as a class region, drawn
            # identically, labeled by the file it came from. Membership
            # comes from region_members (the layout's own authoritative
            # list), NOT re-derived by filtering on source_file — a class
            # defined in the SAME file as free functions would otherwise
            # get pulled into this region too, even though its members
            # already belong to (and are correctly positioned by) their
            # own class's region.
            source_file = region_id[len("_module::"):]
            region_nodes = list(region_members.get(region_id, []))
            label = source_file.rsplit("/", 1)[-1]
        else:
            region_nodes = [region_id] + list(member_ids(G, region_id))
            label = G.nodes[region_id].get("label", region_id)
        hulls.append({
            "nodes": region_nodes,
            "label": label,
            "fill": color, "stroke": color, "labelColor": color,
            "layer": "class",
            # Explicit geometry — the exact disc `_pack_discs` proved
            # disjoint. The renderer uses this instead of fitting an
            # ellipse to member positions, which has to pad outward to
            # cover every member and can then cross into a neighbor.
            "cx": cx, "cy": cy, "r": radius,
        })
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
            # Place the diamond at its own god class's cluster anchor — it is
            # a NEW node _class_cluster_layout never saw, but it belongs
            # conceptually at the class it was extracted from, not wherever
            # physics happens to drop it.
            if god_id in G2.nodes and "cluster_x" in G2.nodes[god_id]:
                G2.nodes[node_id]["cluster_x"] = G2.nodes[god_id]["cluster_x"]
                G2.nodes[node_id]["cluster_y"] = G2.nodes[god_id]["cluster_y"]
            # NO hull for a proposed split group. A background tint says
            # "these belong together", which is exactly the CLASS
            # relationship — reusing it for "these would be pulled OUT into
            # a new class" overloads the same visual with a second,
            # unrelated meaning, and drawing both at once buried the class
            # boundaries under a wash of near-identical regions. The split
            # is already fully expressed inside the decouple preview
            # itself: the ◆ diamond, its `extract` edge, and the redirected
            # wiring below (all revealed together by "Preview decoupled
            # view").

    G2.graph["hyperedges"] = hulls

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
        fp = entry.get("floor_profile")
        if fp:
            span_note = (
                f" — straddles {fp['floor_span'] + 1} data-flow floors "
                f"(cross_floor_risk={entry.get('floor_risk')})"
                if fp["floor_span"] else " — single floor"
            )
            lines.append(
                f"- data-flow floor={fp['floor']} (range {fp['min_floor']}-{fp['max_floor']})"
                f"{span_note}"
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
                if sd.get("group_floor_analysis") == "ok":
                    lines.append(f"  - worst proposed group's own cross-floor risk: {sd['max_group_floor_risk']}")
                else:
                    lines.append(f"  - cross-floor check on proposed groups: {sd.get('group_floor_analysis', 'skipped')}")
            for g in entry.get("proposed_groups", []):
                conf = g.get("cohesion_confidence", "n/a")
                lines.append("")
                lines.append(f"### Proposed: {g['name']} ({len(g['members'])} members, confidence={conf})")
                fp = g.get("floor_profile")
                if fp:
                    lines.append(
                        f"- floor={fp['floor']} (range {fp['min_floor']}-{fp['max_floor']})"
                        + (f" — still spans {fp['floor_span'] + 1} floors" if fp["floor_span"] else " — single floor")
                    )
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
