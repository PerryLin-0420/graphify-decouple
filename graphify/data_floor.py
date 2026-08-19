"""data_floor — data-flow layering ("which floor is this on?").

`decouple.py` scores a class by how tangled its own members are. That says
nothing about WHERE in the system's data flow the class sits, which is a
different and equally structural question: a class that reads a file, a
class that computes on what was read, and a class that renders the result
are three different jobs, and one class doing all three is a problem the
call-graph metrics can't see (its members can be perfectly cohesive by
call structure while still spanning the whole pipeline).

Floors are the LONGEST directed path (in hops) from the system's I/O
boundary:

  - Floor 0 = the boundary itself — where data enters or leaves the process
    (parsers, loaders, readers, writers, exporters, DB/HTTP clients). Both
    ends count: "first data source OR output point".
  - Floor N = the length of the LONGEST call chain from any boundary node
    to this one — not the shortest. A node reachable from the boundary via
    both a direct shortcut edge (1 hop) AND a long serial chain (say 4
    hops through 3 intermediate stages) is genuinely downstream of that
    4-stage pipeline; reporting the shortcut's floor would hide the actual
    depth of what it depends on. This is "worst-case propagation depth",
    not "closest possible route".

Computed on the graph's strongly-connected-component CONDENSATION
(`nx.condensation`), not the raw graph: longest path is only well-defined
on a DAG, and a genuine dependency cycle (A calls B calls A) has no longest
path at all (the cycle could be walked any number of times). Every node in
the SAME strongly connected component shares ONE floor — they are mutually
reachable, so there is no "who is upstream of whom" between them to
measure; a whole SCC is treated as a single indivisible unit for this
purpose.

Distance is measured on the DIRECTED graph — call direction is who-invokes-
whom, which is not strictly the same thing as which way data moves (a
parser called BY a controller still supplies data TO it), and resolving
true data direction would need dataflow analysis this module does not
attempt. Call direction is the only direction available, and "longest
path" is meaningless without one to be long ALONG.

That "who calls whom" pass only credits a unit for what it ITSELF calls,
which misses a whole category of unit: a shared data/utility type — a
domain model, a value object — that a boundary function constructs
directly (`TraceSource(parsed_data)` built inside a parser) but which
makes no calls of its own that reach anywhere. Structurally it never
"calls down to" the boundary, so the main pass leaves it with no floor at
all, even though being constructed BY a floor-0 function is exactly the
kind of evidence this module exists to use. A second RESCUE pass covers
this: a unit with no floor from its own calls, but with at least one
CALLER that has a floor, is placed at floor `max(1, min(caller floors) - 1)`
— never floor 0 (reserved for the boundary itself, not merely something
next to it), and using the closest caller's evidence rather than the
farthest, because this pass asks "is there close evidence", the opposite
of the main pass's "what is the worst dependency". Iterated to a fixed
point, since a rescued unit can rescue its own still-unreached callees in
turn. Measured on a real corpus: 41% of callable code had a floor from the
main pass alone; the rescue pass raised that to 71% without deepening the
tallest floor at all.

Only edges that represent actual runtime structure count, and they are
WEIGHTED — see `_HOP_COST`. graphify's graph also carries edges like
`rationale_for` (a docstring node documenting a symbol), `contains` (file
lists symbol), `imports`, `references`, `inherits`,
`conceptually_related_to`: none of these is a runtime relationship, and
counting them manufactures fake depth. Measured on a real corpus: every
`_rationale_N` docstring node attached to a deep symbol via `rationale_for`
inherited that symbol's floor plus one, purely from being documented — not
from doing anything at that depth itself — which pushed the tallest floor
past 20 for no structural reason.

Costs exist rather than a flat one-floor-per-edge rule because two kinds of
hop move WITHIN one unit instead of between two stages, and both cost zero:

  - A `method` edge is containment ("class C has method m") — C and m are
    two granularities of one unit. Charged a floor, a class reads as
    sitting one floor below its own `__init__`, and a class disc lands on
    a different floor from its own members, leaving floors populated by
    stray member points and no class at all. It cannot merely be dropped
    either, because real chains route THROUGH a class node (`_build_ui()
    --calls--> FilesPanel --method--> .set_sources()`); removing it
    disconnects the chain and costs real coverage (41% -> 29%). Zero cost
    keeps the chain intact while charging nothing for the detour.
  - An INTRA-MODULE call (both ends in the same source file) is the same
    claim at module granularity. `FilesPanel.set_sources() -> _FileRow ->
    _populate_detail_panel()` was three consecutive floors entirely inside
    `files_panel.py` — one UI widget's internal composition, not data
    passing through three stages.

Measured on a real corpus, the two together cut the tallest floor from 10
to 4 with no loss of coverage: 3 of the floors removed were `method` hops
in the deepest chain, and 3 more were intra-module calls.

Honest limits:
  - Boundary detection is a NAME heuristic (path tokens + symbol-name
    patterns), not I/O detection. It cannot see a class that does raw
    socket work under a domain-flavored name, and it will flag a
    `parse_args()` that never touches the outside world. `boundary_reason`
    is recorded per node so every floor-0 call can be audited rather than
    taken on faith.
  - A graph with no detectable boundary yields NO floors at all (an empty
    dict), not a fabricated layering rooted at an arbitrary node.
  - A unit reachable from NEITHER a boundary via its own calls NOR a
    known-floor caller (via the rescue pass) is absent from the result —
    unreachable, not floor 0. This includes a unit whose ONLY edges are
    non-call ones (a rationale node with nothing but a `rationale_for`
    edge, a file-level `contains` leaf) — it is not "at the boundary" just
    because it has no distance to measure.
  - A boundary node's own floor is fixed at 0 even if some OTHER, longer
    chain also happens to reach it — being an I/O boundary is what floor 0
    MEANS, not a distance to be second-guessed by a path through something
    else.
"""
from __future__ import annotations

import re
from typing import Any

import networkx as nx

# Path tokens that mark a file as a place data enters or leaves the process.
# Matched as whole tokens (see `_tokens`), never substrings — a short token
# like "io" would otherwise fire on "distribution".
#
# Deliberately language-NEUTRAL: this is a name heuristic over paths and
# symbols, so it works on any language graphify can extract, without a
# per-language grammar table (unlike state_affinity/tool_dedup, which do
# need one). The vocabulary spans the naming conventions of the ecosystems
# graphify covers rather than one language's — Java/Kotlin/C# lean on
# Repository/Dao/Stream/Context, Go on Reader/Writer/Encoder/Conn, Rust on
# serde/io, JS/TS on fetch/request/api, PHP on PDO/curl, Ruby on
# ActiveRecord finders. A token is included only when it means "data
# crosses a process boundary here" in whichever ecosystem uses it; broadly
# ambiguous words (service, manager, model, entity, context, handler) are
# left out on purpose — they would make most of a codebase floor 0 and
# flatten the layering into noise.
_BOUNDARY_PATH_TOKENS = frozenset({
    # generic / cross-language
    "parser", "parse", "loader", "load", "reader", "writer", "io",
    "serializer", "serialiser", "codec", "storage", "store", "stream",
    "streams", "file", "fs", "net", "socket", "conn", "connection",
    # persistence layers
    "dao", "repository", "repo", "repos", "persistence", "orm", "db",
    "database", "sql", "jdbc", "jpa", "hibernate", "mapper", "migration",
    # remote / transport
    "gateway", "client", "api", "http", "rest", "rpc", "grpc", "graphql",
    "transport", "request", "response", "endpoint", "webhook",
    # architectural boundary layers (ports-and-adapters naming)
    "adapter", "adapters", "driver", "drivers", "infra", "infrastructure",
    # ingest / egress
    "ingest", "importer", "exporter", "export", "publisher", "subscriber",
})

# Symbol-name stems that mark a FUNCTION as boundary-ish even when its file
# name is domain-flavored. Same whole-token discipline as paths, and the
# same cross-ecosystem intent: Go's Marshal/Unmarshal/Scan, .NET's
# Flush/Dispose-adjacent stream verbs, JVM's persist/flush, JS's fetch,
# Ruby/ActiveRecord's save, SQL's insert/select all name the same act —
# data crossing in or out.
_BOUNDARY_NAME_TOKENS = frozenset({
    "load", "save", "read", "write", "parse", "dump", "fetch", "query",
    "open", "close", "send", "recv", "receive", "download", "upload",
    "serialize", "serialise", "deserialize", "deserialise", "encode",
    "decode", "export", "import", "connect", "commit", "flush",
    "marshal", "unmarshal", "scan", "persist", "retrieve", "insert",
    "select", "publish", "subscribe", "consume", "poll", "sync",
    "reader", "writer", "stream", "file", "socket",
})

# How many floors each kind of edge is worth. Only edges listed here take
# part in the layering at all; graphify's graph also carries `contains`
# (file lists symbol), `rationale_for` (docstring documents symbol),
# `imports`/`imports_from`, `references`, `inherits`, `shares_data_with`,
# `uses`, `conceptually_related_to`, `semantically_similar_to` — none of
# those is a runtime relationship between two units of behavior, and
# counting one manufactures depth out of documentation or file layout.
#
# `method` is included but costs ZERO floors, which is the whole point of
# having costs at all. A `method` edge is CONTAINMENT ("class C has method
# m"), not invocation, so C and m are two granularities of one unit, not
# two stages of a data flow — charging a floor for that hop says "MainWindow
# sits one floor deeper than its own __init__", which is meaningless. But
# it cannot simply be dropped either: real chains route THROUGH a class
# node (`_build_ui() --calls--> FilesPanel --method--> .set_sources()`), so
# removing it disconnects the chain and the downstream half loses its floor
# entirely (measured on a real corpus: floor coverage fell 41% -> 29%).
# Zero cost keeps the chain connected while charging nothing for the
# detour — on that same corpus it cut the tallest floor from 10 to 7, and
# the 3 floors it removed were exactly the 3 `method` hops in the deepest
# chain.
_HOP_COST: dict[str, int] = {"calls": 1, "indirect_call": 1, "method": 0}


def _same_module(G: nx.Graph, u: str, v: str) -> bool:
    """Whether two nodes are implemented in the same source file."""
    su = G.nodes[u].get("source_file")
    sv = G.nodes[v].get("source_file")
    return bool(su) and su == sv


def _call_structure_only(G: nx.DiGraph) -> nx.DiGraph:
    """`G` restricted to the edges in `_HOP_COST`, all nodes kept, each
    edge carrying its floor cost as a `cost` attribute.

    An INTRA-MODULE call (both ends in the same source file) is charged
    zero, for the same reason a `method` edge is: it moves between two
    parts of one unit rather than between two stages of a data flow. The
    granularity differs — `method` is containment within a class, this is
    containment within a module — but the claim is identical, and without
    it a single component's internal structure reads as pipeline depth.
    Measured on a real corpus: `FilesPanel.set_sources() -> _FileRow ->
    _populate_detail_panel()` is three consecutive floors, all inside
    `files_panel.py`, describing one UI widget's own composition rather
    than data moving through three stages. Charging zero for those cut the
    tallest floor from 7 to 4 without costing any coverage.

    The honest limit: a genuinely large module that really does run several
    pipeline stages internally collapses to one floor here. That is the
    accepted cost of treating the module as the unit of "stage" — and
    `decouple.py`'s own question is whether a unit spans stages, which is
    only meaningful if a stage is bigger than one function call.

    A node whose only edges are excluded ones (a rationale node with
    nothing but a `rationale_for` edge, a symbol reachable only via
    `contains`) ends up with no edges here — same outcome as never being
    connected to the call graph at all, which is what it actually is for
    this purpose.
    """
    H = nx.DiGraph()
    H.add_nodes_from(G.nodes(data=True))
    for u, v, data in G.edges(data=True):
        cost = _HOP_COST.get(data.get("relation"))
        if cost is None:
            continue
        if cost and _same_module(G, u, v):
            cost = 0
        H.add_edge(u, v, cost=cost)
    return H


_TOKEN_RE = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall((text or "").lower()))


def boundary_reason(G: nx.Graph, node_id: str) -> "str | None":
    """Why `node_id` counts as floor 0, or None if it doesn't. Returned as
    text (not a bool) so a floor-0 classification can be audited in the
    report instead of being trusted blind — this is a name heuristic, and
    every one of its calls is second-guessable by design.

    Only `file_type == "code"` nodes can be a boundary. graphify's graph
    also carries `rationale` nodes (docstrings, design notes) and `concept`
    nodes, whose LABEL IS PROSE — matching name tokens against an English
    sentence fires constantly and means nothing about I/O (measured on a
    real corpus: 52 of 158 floor-0 hits were prose nodes containing the
    word "parse" or "read", every one a false positive). A doc node
    describing a parser is not itself a data boundary.
    """
    data = G.nodes[node_id]
    if data.get("file_type") != "code":
        return None
    path_hits = _tokens(str(data.get("source_file") or "")) & _BOUNDARY_PATH_TOKENS
    if path_hits:
        return f"source file path contains {sorted(path_hits)[0]!r}"
    label = str(data.get("label") or node_id)
    name_hits = _tokens(label) & _BOUNDARY_NAME_TOKENS
    if name_hits:
        return f"symbol name contains {sorted(name_hits)[0]!r}"
    return None


def compute_floors(G: "nx.DiGraph") -> "tuple[dict[str, int], dict[str, str]]":
    """Longest directed-path distance (hops) from the nearest I/O boundary
    node, computed on `G`'s strongly-connected-component condensation —
    see the module docstring for why longest (not shortest) and why the
    condensation (cycles have no longest path otherwise) — PLUS a second
    rescue pass for units with no floor from their own calls but at least
    one caller that has one (see the module docstring for why that is a
    genuinely different, complementary signal, not the same computation
    run twice).

    Hops are WEIGHTED by `_HOP_COST`, not counted flat: an invocation costs
    one floor, a `method` containment edge costs zero (see the module
    docstring).

    Returns `(floors, boundary_reasons)`. `floors` maps node id -> floor;
    a unit reachable from NEITHER a boundary (via its own calls) NOR a
    known-floor caller (via the rescue pass) is ABSENT (unknown floor),
    never defaulted to 0 — this includes a unit whose only edges are
    excluded ones (documentation, imports, file containment), which has no
    more of a real position in the call structure than one with no edges
    at all. `boundary_reasons` maps each floor-0 node to the
    `boundary_reason` that put it there.

    Deterministic: `nx.condensation`'s SCC numbering only depends on `G`'s
    own (insertion-ordered) structure, and every set this function iterates
    over for tie-breaking is sorted before use — the same graph always
    yields the same floors.

    Requires a DIRECTED `G` — `nx.condensation` (and "longest path" itself,
    which needs a direction to be long ALONG) are undefined for an
    undirected graph.
    """
    reasons: dict[str, str] = {}
    for nid in sorted(G.nodes):
        reason = boundary_reason(G, nid)
        if reason:
            reasons[nid] = reason
    if not reasons:
        return {}, {}

    # Propagated over call-shaped edges only (see _call_structure_only) —
    # boundary detection above still looks at every node's own attributes,
    # regardless of what kind of edges connect it, but a hop only counts
    # when it is an actual invocation.
    call_graph = _call_structure_only(G)

    # Condensed on the REVERSED graph, not call_graph itself: a call edge
    # (u, v) means "u calls v", i.e. v is closer to the boundary than u is
    # (u is the one downstream, consuming whatever v produces). Floor must
    # increase walking from a boundary node OUT TO ITS CALLERS, which is
    # the successor direction on the reversed graph, not the original —
    # reversing first lets the same forward topological-sort/relax loop
    # below do the right thing. SCC membership is identical either way (a
    # cycle is a cycle regardless of which way it's read), so this doesn't
    # change which nodes get condensed together, only which way floors flow.
    condensation = nx.condensation(call_graph.reverse(copy=False))
    node_to_scc: dict[str, int] = condensation.graph["mapping"]

    seed_sccs = {node_to_scc[n] for n in reasons}
    floors_scc: dict[int, int] = {s: 0 for s in seed_sccs}

    # Cost of each condensed edge = the MAX cost of any underlying edge
    # between those two SCCs. When one SCC is reached from another both by
    # a real call (cost 1) and by containment (cost 0), the call is the hop
    # that actually moved a floor, so the pair is worth a floor. Built by
    # walking the underlying edges once and mapping each to its SCC pair —
    # note the reversal: a `call_graph` edge u -> v ("u calls v") is a
    # v -> u edge in the condensed, reversed graph the DP walks.
    scc_edge_cost: dict[tuple[int, int], int] = {}
    for u, v, data in call_graph.edges(data=True):
        pair = (node_to_scc[v], node_to_scc[u])
        if pair[0] == pair[1]:
            continue  # inside one SCC — no floor difference to charge
        if data["cost"] > scc_edge_cost.get(pair, -1):
            scc_edge_cost[pair] = data["cost"]

    # nx.condensation is a DAG by construction (SCCs cannot cycle among
    # themselves — if they did, they would BE one SCC), so topological
    # order always exists. Two alternating relaxations, run to a fixed
    # point, share this order and this SCC graph:
    #
    #   (1) MAIN: processing SCCs in topological order and relaxing only
    #       FORWARD (to already-later nodes) is the standard
    #       longest-path-in-DAG algorithm — by the time an SCC is visited,
    #       every predecessor that could still improve its floor has
    #       already been fully processed. This is "how deep is what I
    #       call" — a unit's floor grows with the worst thing it depends on.
    #   (2) RESCUE: an SCC untouched by (1) may still be a shared
    #       data/utility type — makes no calls of its own that reach
    #       anywhere, but is constructed directly BY something with a known
    #       floor (`TraceSource(parsed_data)` built inside a parser). That
    #       caller relationship is evidence in the OPPOSITE direction: "how
    #       shallow is whoever constructs me". Rescued to
    #       floor max(1, min(caller floors) - 1) — never floor 0 itself
    #       (reserved for the boundary, not merely adjacent to it), and the
    #       MINIMUM over callers, not the maximum, because this asks "does
    #       close evidence exist", the opposite question from (1)'s "what
    #       is the worst dependency" — a single deep, unrelated caller must
    #       not drag a shared utility away from strong close-caller
    #       evidence.
    #
    # Neither pass alone is enough: a unit rescued by (2) can be the
    # boundary-side end of a normal orchestration chain that (1) must then
    # extend outward through ITS OWN callers (a controller that merely
    # calls a rescued utility is genuinely one hop further out, not
    # rescued itself) — and a unit rescued by (2) can also unblock another
    # (2) rescue further downstream. Alternating both to a fixed point
    # (never revisiting an SCC once it has a floor, so this always
    # terminates) handles both. Measured on a real corpus: the main pass
    # alone covers 41% of callable code; alternating rescue in raises that
    # to 71%, without deepening the tallest floor at all.
    changed = True
    while changed:
        changed = False
        for scc in nx.topological_sort(condensation):
            if scc not in floors_scc:
                continue  # not (yet, or ever) reached from any known floor
            base = floors_scc[scc]
            for succ in sorted(condensation.successors(scc)):
                if succ in seed_sccs:
                    continue  # a boundary SCC's floor is fixed at 0, never overwritten
                candidate = base + scc_edge_cost.get((scc, succ), 1)
                if succ not in floors_scc or candidate > floors_scc[succ]:
                    floors_scc[succ] = candidate
                    changed = True
        for scc in condensation.nodes:
            if scc in floors_scc:
                continue
            caller_floors = [
                floors_scc[caller] for caller in condensation.successors(scc)
                if caller in floors_scc
            ]
            if caller_floors:
                floors_scc[scc] = max(1, min(caller_floors) - 1)
                changed = True

    floors: dict[str, int] = {
        n: floors_scc[scc] for n, scc in node_to_scc.items() if scc in floors_scc
    }
    return floors, reasons


def class_floor_profile(
    G: nx.Graph,
    class_id: str,
    members: list[str],
    floors: dict[str, int],
) -> "dict[str, Any] | None":
    """Which floor(s) a class occupies, and by how much it straddles them.

    A class whose members all sit on one floor does one job at one stage of
    the data flow. A class whose members are spread over several floors is
    doing boundary work AND downstream work in the same unit — the
    structural smell `floor_span` is meant to surface. That span is a
    RISK-relevant signal `decouple.py`'s call-graph metrics cannot see:
    members can be tightly cohesive by call structure and still span the
    whole pipeline.

    `floor` is the class's dominant floor (the modal member floor, lowest
    on a tie — the earliest stage it participates in). Returns None when
    no member (nor the class node itself) has a known floor, rather than
    guessing a layer for it.

    `floor_evidence` is the share of this unit's members whose floor is
    actually known (0.0-1.0) — how much of the unit `floor_span` was
    measured over, NOT how confident the boundary heuristic is. It exists
    because span and evidence turn out to be INVERSELY related on real
    data: sparse coverage lets a handful of scattered points stretch a
    large span, while a unit whose floors are fully known usually turns out
    to sit on one floor. Measured on a real corpus, every group reporting
    span > 0 had weak evidence (the worst: span 6 from 3 of 7 members, one
    member per floor), while the two groups with 100% known floors both had
    span 0. `cross_floor_risk` scales by this so a span built on two
    isolated points cannot outweigh one measured across a whole class.
    """
    known = [floors[n] for n in [class_id, *members] if n in floors]
    if not known:
        return None
    counts: dict[int, int] = {}
    for f in known:
        counts[f] = counts.get(f, 0) + 1
    dominant = min(counts, key=lambda f: (-counts[f], f))
    # A proposed group is passed class_id=None (it has no class node of its
    # own yet) — counting a nonexistent node would understate its evidence.
    total = len(members) + (1 if class_id is not None else 0)
    return {
        "floor": dominant,
        "min_floor": min(known),
        "max_floor": max(known),
        "floor_span": max(known) - min(known),
        "members_with_known_floor": len(known),
        "members_total": total,
        "floor_evidence": round(len(known) / total, 2) if total else 0.0,
    }


_FLOOR_SPAN_CAP = 4  # floor_span >= this maxes the cross-floor risk component


def cross_floor_risk(profile: "dict[str, Any] | None") -> float:
    """0-100 risk proxy for how far a class straddles the data flow,
    SCALED by how much of the class that span was actually measured over.

    A class spanning `_FLOOR_SPAN_CAP` or more floors scores 100 only when
    every one of its members has a known floor; at half coverage the same
    span scores half as much. This is not a confidence interval — it is a
    deliberate refusal to let a span computed from two isolated points
    carry the same weight as one measured across a whole class. Without
    it, the weakest evidence produced the strongest intervention: on a real
    corpus a span of 6, resting on 3 of 7 members with a single member per
    floor, added 30 points of split risk and flipped that class's verdict
    from "split" to "marginal" — while the classes whose floors were fully
    known contributed nothing, because they genuinely sat on one floor.

    Same caveat as every other score in this feature: a fixed heuristic
    weight, comparative on THIS graph, not a validated metric. Returns 0.0
    for an unknown profile — a class whose floors could not be determined
    is not penalized for it (unknown is not the same as clean, and the
    report says which one it is).
    """
    if not profile:
        return 0.0
    span_component = min(profile["floor_span"] / _FLOOR_SPAN_CAP, 1.0)
    # Older/hand-built profiles without the field are treated as fully
    # measured rather than silently discounted to zero.
    evidence = profile.get("floor_evidence", 1.0)
    return round(100 * span_component * evidence, 1)
