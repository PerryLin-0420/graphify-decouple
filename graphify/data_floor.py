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

A unit neither pass can place is not necessarily unmeasurable — it may
simply be wired to the rest of the system by an edge that carries no
DISTANCE. Measured on a real corpus: of 1272 units with no floor after
both call passes, exactly zero had a `calls`/`method` edge to a unit that
had one, while 571 of them had a `contains`, `rationale_for`, `imports`,
`uses` or `inherits` edge to one — 299 straight to a floor-0 unit. Those
were reported as "unknown" while the 3D view happily drew their links,
which is two different claims about the same node. A third PARALLEL pass
(`_parallel_floors`) closes that: a unit the call passes could not place,
but which is wired to one they did, is placed ON that unit's floor at ZERO
cost — alongside it, never one floor below. Zero is what makes those edge
kinds usable here at all; charging them a floor is the documented failure
below. After it, "unknown floor" means what it says: no path of ANY edge
kind to a measured unit.

Only edges that represent actual runtime structure carry DISTANCE, and
they are WEIGHTED — see `_HOP_COST`. graphify's graph also carries edges like
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
    known-floor caller NOR any non-runtime edge to a placed unit (the
    parallel pass) is absent from the result — unmeasured, not floor 0.
    That is now a genuinely isolated unit: connected to nothing whose
    floor is known, by any kind of edge.
  - A floor from the parallel pass is WEAKER evidence than a measured one:
    it says "this sits alongside something at floor N", not "this is N
    hops from the boundary". `compute_floors_with_provenance` reports
    which pass placed each unit so the two are never confused; a
    non-`code` node (a docstring, a concept) is never placed by it at all,
    the same restriction `boundary_reason` applies.
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

# Kinds of node the parallel pass (`_parallel_floors`) refuses to place,
# even when wired to a measured unit — the same "prose is not doing
# parser-stage work" exclusion `boundary_reason` applies, generalized to
# every non-code kind graphify's graph carries (see
# `graphify.validate.VALID_FILE_TYPES`). Deliberately a DENY list, not
# `== "code"`: an edge's TARGET is frequently a node the extractor never
# explicitly created — an external package name (`imports_from` naming
# `react`, a Rust crate, an Android API class) round-trips through
# networkx's node_link_graph as a bare id with NO attributes at all,
# `file_type` included. Measured on a real multi-language corpus
# (Bynalix-main: TS/TSX + Rust + Kotlin): 47 such attribute-less nodes,
# every one a genuine external dependency wired by a real `imports_from`
# edge from a floor-2 file — an `== "code"` check excluded every one of
# them from ever receiving a floor, the identical "wired but reported
# unknown" contradiction the parallel pass exists to remove, just via a
# different root cause (a missing attribute instead of a missing region).
_NON_CODE_FILE_TYPES = frozenset({"document", "paper", "image", "rationale", "concept"})


# Where a node's floor came from. Recorded per node because the three
# passes below are three different STRENGTHS of evidence, and a report that
# shows them all as one number cannot be audited: a floor 0 measured by a
# call chain to a parser and a floor 0 inherited from sitting next to one
# are not the same claim.
_PROV_BOUNDARY = "boundary"  # the node is itself an I/O boundary (floor 0)
_PROV_CALL = "call"          # longest call path from a boundary (main pass)
_PROV_RESCUE = "rescue"      # nearest known-floor CALLER (rescue pass)
_PROV_PARALLEL = "parallel"  # non-runtime edge to a known floor (parallel pass)


def _neighbors(G: nx.Graph, n: str) -> set:
    """Every node adjacent to `n`, regardless of edge direction."""
    if G.is_directed():
        return set(G.predecessors(n)) | set(G.successors(n))
    return set(G.neighbors(n))


def _parallel_floors(
    G: nx.Graph,
    floors: dict[str, int],
    region_of: "dict[str, str] | None" = None,
) -> dict[str, int]:
    """Floors for units the CALL passes could not place, taken from a
    non-runtime edge to a unit they could — the third and last pass of
    `compute_floors_with_provenance`.

    The two call passes are already closed over call structure: measured on
    a real corpus, of 1272 units with no floor, exactly ZERO had a `calls`,
    `indirect_call` or `method` edge to a unit that had one. Every remaining
    "unknown" that was visibly wired to the rest of the system was wired by
    a `contains`, `rationale_for`, `imports`, `uses` or `inherits` edge —
    571 of them, 299 attached directly to a floor-0 unit. Those units were
    reported as unknown while the 3D view drew their links (it aggregates
    ALL edges), which is the contradiction this pass removes: a unit with a
    real edge to floor 0 is not unmeasurable, it is ALONGSIDE floor 0.

    So the floor is taken at ZERO cost — a parallel placement, not a hop:
    the unit is put ON the floor of the nearest known unit, never one below
    it. That is the whole reason these edge kinds can be used here at all
    while `_HOP_COST` still excludes them. Charging them a floor was tried
    and is exactly the failure documented in the module docstring (every
    `_rationale_N` node inheriting its subject's floor + 1 pushed the
    tallest floor past 20 out of documentation alone). At zero cost the
    tallest floor cannot move: this pass only ever fills in floors that
    already exist, and it NEVER overwrites one a call pass established.

    Ties go to the SHALLOWEST reachable known floor (the BFS runs one
    source level at a time, floor 0 first), for the rescue pass's reason:
    this asks "is there close evidence", not "what is the worst
    dependency". Propagation relays only through units this pass itself
    placed, so a chain of unknowns hanging off floor 0 all lands on floor 0
    — but a known-floor unit is a SOURCE, never a relay, so evidence cannot
    tunnel through an already-measured unit to a shallower floor behind it.

Excludes known non-code kinds (`_NON_CODE_FILE_TYPES`: document, paper,
    image, rationale, concept) — the same restriction `boundary_reason`
    applies and for the same reason: a docstring or concept node has no
    position in a data flow to report. It can still be adjacent to one, but
    "this prose documents a parser" is not the prose doing parser-stage
    work. Excluding them also keeps this pass from relaying a floor between
    two unrelated code units through the docstring that happens to mention
    both. A DENY list, not an `== "code"` allow list: an edge's target is
    often a node the extractor never explicitly created (an external
    package name — `react`, a Rust crate, an Android API class — that only
    ever appears as an `imports_from` target) and round-trips through
    networkx with NO attributes at all, `file_type` included. Requiring
    `== "code"` excluded every one of those — a genuine external dependency
    with a real wired edge from a measured file — from ever getting a
    floor; measured on a real multi-language corpus, 47 such nodes.

    `region_of`, when given, runs this pass at REGION granularity instead
    of per-node: every member of a region is placed together (a region
    with no measured floor of its own, but wired by ANY edge kind to a
    PLACED region, is placed alongside that region as a WHOLE, not
    node-by-node) — the same reason `compute_floors_with_provenance`
    contracts by region for the call/rescue passes: a class is one unit,
    and this pass must not let two of its own members disagree about which
    neighbor's floor they inherited just because the BFS happened to reach
    them from different directions. A region is eligible for placement
    only if at least one of its members is `file_type == "code"`.

    What is left with no floor after this pass is the honest remainder: a
    unit with no path of ANY edge kind to anything whose floor is known —
    genuinely unmeasured, not merely unmeasured by call structure.
    """
    if not floors:
        return {}
    unit_of = (lambda n: region_of.get(n, n)) if region_of else (lambda n: n)
    # A unit's floor, seeded from whichever of its members already has one
    # — every member of an already-placed region shares that floor by
    # construction (region_of came out of the SAME contraction the
    # call/rescue passes used), so any one of them determines it.
    unit_floor: dict[str, int] = {}
    for n, f in floors.items():
        unit_floor.setdefault(unit_of(n), f)
    members_of: dict[str, list[str]] = {}
    has_code: dict[str, bool] = {}
    for n in G.nodes:
        u = unit_of(n)
        members_of.setdefault(u, []).append(n)
        if G.nodes[n].get("file_type") not in _NON_CODE_FILE_TYPES:
            has_code[u] = True
    assigned: dict[str, int] = {}
    placed = set(unit_floor)
    for level in sorted(set(unit_floor.values())):
        # Sorted at every step: the result must not depend on dict order.
        queue = sorted(u for u in unit_floor if unit_floor[u] == level)
        while queue:
            cur = queue.pop(0)
            neighbor_units = set()
            for n in members_of.get(cur, ()):
                for nb in _neighbors(G, n):
                    neighbor_units.add(unit_of(nb))
            for nu in sorted(neighbor_units):
                if nu in placed or nu in assigned:
                    continue
                if not has_code.get(nu):
                    continue
                assigned[nu] = level
                queue.append(nu)
    result: dict[str, int] = {}
    for u, level in assigned.items():
        for n in members_of.get(u, ()):
            result[n] = level
    return result


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


def _contract_by_region(call_graph: nx.DiGraph, region_of: "dict[str, str]") -> nx.DiGraph:
    """`call_graph`, with every node replaced by `region_of.get(n, n)` —
    a class or module region collapsed to ONE node, the same idea as SCC
    condensation, but for CONTAINMENT rather than cycles.

    Exists because zero-cost `method` propagation alone is not enough to
    make "a function belongs to its class" true for floor purposes. A
    class with many methods at different depths lets its own node inherit
    the DEEPEST one via the zero-cost edge (see the module docstring's
    "route through a class node" case) — correct when there is one
    obvious path, wrong when it means "constructing this class" inherits
    the depth of some rarely-called callback the constructor never
    touches. Measured on a real corpus (AutoCheck): `GroupAnalyzeDialog`
    has 34 methods, 19 of them at floor 1 and one — a correlation-analysis
    button handler — reaching floor 3 through three more classes. Under
    per-node floors, the class's OWN node inherited that outlier (floor 3),
    so a test merely constructing the dialog was measured at floor 4, while
    the SAME class's region in the 3D view displayed floor 1 (the
    DOMINANT vote over its members) — two different numbers for one class,
    and neither matched what was actually drawn: a floor-4 disc linked to
    a floor-1 disc with nothing at floors 2–3 to explain the jump.

    Contracting every member into one node BEFORE the DP runs removes the
    ambiguity: every member of a region shares the exact same floor by
    construction, and that floor is 1 + the deepest thing ANY of the
    region's members reaches OUTSIDE it — the same DP rule as always,
    applied at the granularity where data actually changes hands (a class
    or module), not at the granularity code happens to be split into
    (individual functions).

    An edge whose two ends land in the SAME region (an intra-class or
    intra-module call, or the `method` edge itself) is dropped — it is
    now literally a self-loop, no distance to measure. A node absent from
    `region_of` is its own singleton region, so passing `region_of=None`-
    equivalent (an empty or partial mapping) leaves it exactly as
    `call_graph` already had it.
    """
    H = nx.DiGraph()
    H.add_nodes_from({region_of.get(n, n) for n in call_graph.nodes})
    for u, v, data in call_graph.edges(data=True):
        ru, rv = region_of.get(u, u), region_of.get(v, v)
        if ru == rv:
            continue
        cost = data["cost"]
        if not H.has_edge(ru, rv) or cost > H.edges[ru, rv]["cost"]:
            H.add_edge(ru, rv, cost=cost)
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


def compute_floors_with_provenance(
    G: "nx.DiGraph",
    region_of: "dict[str, str] | None" = None,
) -> "tuple[dict[str, int], dict[str, str], dict[str, str]]":
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

    PLUS a third pass (`_parallel_floors`) for units neither call pass
    could place but which are wired to one that was placed, by an edge
    that carries no distance (`contains`, `imports`, `uses`, `inherits`).
    Those are placed on that unit's floor at zero cost — alongside it.

    All three run inside this one call. There is no later stage that
    "fills in" leftovers: whatever comes back is the finished layering,
    and every consumer in the `decouple` command reads it rather than
    recomputing anything.

    Returns `(floors, boundary_reasons, provenance)`. `floors` maps node
    id -> floor; a unit with no path of ANY edge kind to a placed unit is
    ABSENT (unknown floor), never defaulted to 0. `boundary_reasons` maps
    each floor-0 boundary node to the `boundary_reason` that put it there.
    `provenance` maps every placed node to the pass that placed it
    (`_PROV_BOUNDARY`/`_PROV_CALL`/`_PROV_RESCUE`/`_PROV_PARALLEL`) — the
    first three are distances measured along call structure, the last is
    adjacency, and a report that shows them as one number cannot be
    audited.

    Deterministic: `nx.condensation`'s SCC numbering only depends on `G`'s
    own (insertion-ordered) structure, and every set this function iterates
    over for tie-breaking is sorted before use — the same graph always
    yields the same floors.

    Requires a DIRECTED `G` — `nx.condensation` (and "longest path" itself,
    which needs a direction to be long ALONG) are undefined for an
    undirected graph.

    `region_of`, when given, maps every node to the class/module region it
    belongs to (the same partition `decouple._region_membership` computes)
    and contracts every region to ONE unit before any of the three passes
    run — see `_contract_by_region`. Every member of a region then shares
    the exact same floor, because a function is CONTAINED by its class,
    not a separate stage of the data flow: without this, a class with many
    methods at very different depths let its own node inherit its single
    DEEPEST member via the zero-cost `method` edge (see the module
    docstring's "route through a class" case), so a caller merely
    referencing the class (a constructor call) inherited the depth of a
    method it never actually invokes. Measured on a real corpus
    (AutoCheck): a class with 34 methods, 19 at floor 1 and one — a rare
    callback — reaching floor 3 through three more classes, had its own
    node measured at floor 3 (so a test merely constructing it landed at
    floor 4) while the 3D view displayed the SAME class's region at floor
    1 (the majority vote over its members) — two different numbers for
    one unit, and neither matched the actual drawn links. Contracting
    first removes the ambiguity: a region's floor is 1 + the deepest thing
    ANY of its members reaches OUTSIDE the region, and every member — and
    every OTHER unit that references the region — sees that one number.
    Omit `region_of` (or pass an empty/partial mapping) to get the
    per-node floors exactly as before; a node absent from the mapping is
    its own singleton region either way.
    """
    reasons: dict[str, str] = {}
    for nid in sorted(G.nodes):
        reason = boundary_reason(G, nid)
        if reason:
            reasons[nid] = reason
    if not reasons:
        return {}, {}, {}

    # Propagated over call-shaped edges only (see _call_structure_only) —
    # boundary detection above still looks at every node's own attributes,
    # regardless of what kind of edges connect it, but a hop only counts
    # when it is an actual invocation.
    call_graph = _call_structure_only(G)
    if region_of:
        call_graph = _contract_by_region(call_graph, region_of)

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

    _unit = (lambda n: region_of.get(n, n)) if region_of else (lambda n: n)
    # A CLASS-shaped region's boundary status is judged by the CLASS's OWN
    # identity (its own label + file, via boundary_reason on the class
    # node itself) — never by one of its individual MEMBERS matching a
    # name token, because contraction now means that ONE match seeds the
    # WHOLE class, not just that one method. Measured on a real corpus
    # (AutoCheck): `GroupAnalyzeDialog` has 34 methods; five of them —
    # UI callbacks named `_on_save`, `_select_all_files`,
    # `_open_chart_properties`, `_sync_props_panel`, `_on_file_item_clicked`
    # — coincidentally match `_BOUNDARY_NAME_TOKENS` ("save", "select",
    # "open", "sync", "file") despite being button handlers, not I/O. Under
    # per-node floors this was an isolated false positive on one method;
    # under region-contraction it collapsed the entire 34-method class
    # (including a member genuinely measured at floor 3 via a real 3-hop
    # chain) to floor 0. The class's OWN node ("GroupAnalyzeDialog", file
    # "group_analyze_dialog.py") does not itself match any boundary token,
    # so requiring the region's OWN identity to agree — not merely
    # tolerating a stray member's — correctly leaves this class to be
    # measured by its real calls instead. A module/external region has no
    # single node to ask this of, so it keeps the "any member" rule those
    # were always seeded by.
    seed_units: set[str] = set()
    for n in reasons:
        unit = _unit(n)
        if region_of and unit != n and unit in G.nodes and G.nodes[unit].get("_callable_class"):
            continue  # a member's own reason does not seed its class
        seed_units.add(unit)
    seed_sccs = {node_to_scc[u] for u in seed_units}
    floors_scc: dict[int, int] = {s: 0 for s in seed_sccs}
    # Which pass put each SCC on its floor, so a floor can be audited by the
    # KIND of evidence behind it rather than all three looking alike — see
    # `compute_floors_with_provenance`.
    scc_source: dict[int, str] = {s: _PROV_BOUNDARY for s in seed_sccs}

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
                    scc_source[succ] = _PROV_CALL
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
                scc_source[scc] = _PROV_RESCUE
                changed = True

    # Expanded from the (possibly region-contracted) SCC graph to every
    # ORIGINAL node in G: with `region_of`, `node_to_scc` is keyed by
    # region ids, not by every node, so each node reads its OWN unit's
    # result rather than being looked up directly.
    floors: dict[str, int] = {}
    provenance: dict[str, str] = {}
    for n in G.nodes:
        unit = _unit(n)
        scc = node_to_scc.get(unit)
        if scc is None or scc not in floors_scc:
            continue
        floors[n] = floors_scc[scc]
        provenance[n] = scc_source[scc]

    # (3) PARALLEL pass — see `_parallel_floors`. Runs here, inside the one
    # computation, not as a downstream repair: a caller asking for floors
    # gets the finished layering back, and there is no second, later place
    # where "unknown" means something different than it does here.
    for nid, floor in _parallel_floors(G, floors, region_of=region_of).items():
        floors[nid] = floor
        provenance[nid] = _PROV_PARALLEL
    return floors, reasons, provenance


def compute_floors(
    G: "nx.DiGraph",
    region_of: "dict[str, str] | None" = None,
) -> "tuple[dict[str, int], dict[str, str]]":
    """`compute_floors_with_provenance` without the per-node evidence kind —
    the two-value form every caller that only needs the layering itself uses.
    """
    floors, reasons, _provenance = compute_floors_with_provenance(G, region_of=region_of)
    return floors, reasons


def hypothetical_group_floor(
    G: nx.Graph,
    members: list[str],
    floors: dict[str, int],
    exclude: "set[str]",
) -> "int | None":
    """The floor a PROPOSED group of `members` would occupy if it were
    actually extracted into its own region, separate from the class it
    currently lives in — used by `decouple.split_risk_score` to ask
    whether a split would put its resulting groups on DIFFERENT floors,
    without re-running the corpus's whole floor computation.

    Under region-granularity floors (`compute_floors_with_provenance`'s
    `region_of`), every member of an UNSPLIT class shares the exact same
    floor by construction — that IS what "a function is contained by its
    class" means for this purpose. So a proposed group's members, before
    the split has actually happened, all still carry the ORIGINAL class's
    one number; there is no "do the group's OWN members disagree" signal
    left to read (that information was correctly destroyed by
    contraction). The question worth answering moved: not "does this
    group internally span floors" but "would EXTRACTING it land somewhere
    its siblings are not".

    So this computes the group's floor the same way `compute_floors_with_
    provenance`'s two call-structure passes would if the group were its
    own region, scoped to its own boundary:
      - MAIN: 1 + the deepest floor reached by an edge FROM a group member
        TO something outside `exclude` ("how deep is what I call").
      - RESCUE, only if MAIN found nothing: the shallowest floor among
        callers INTO the group from outside `exclude`, minus one ("how
        shallow is whoever constructs me").
      - Neither: the group has no evidence of its own — absent, not a
        guess (same "unknown means unknown" discipline as everywhere else
        in this module).

    `exclude` is every OTHER member of the SAME original class, including
    sibling proposed groups: a call to one of THOSE is not yet a
    cross-region hop, because the split has not actually happened, and
    `split_risk_score` already scores cross-group coupling as its own,
    separate term (`cross_group_edges`) — this function does not try to
    re-derive that here, only what the group depends on genuinely outside
    its current class.
    """
    best_out: "int | None" = None
    best_in: "int | None" = None
    member_set = set(members)
    directed = G.is_directed()
    for m in sorted(members):
        if m not in G.nodes:
            continue
        for v in sorted(G.successors(m) if directed else G.neighbors(m)):
            if v in exclude or v in member_set or v not in floors:
                continue
            cost = _HOP_COST.get(G.edges[m, v].get("relation"))
            if cost is None:
                continue
            candidate = floors[v] + cost
            if best_out is None or candidate > best_out:
                best_out = candidate
        if not directed:
            continue
        for u in sorted(G.predecessors(m)):
            if u in exclude or u in member_set or u not in floors:
                continue
            if _HOP_COST.get(G.edges[u, m].get("relation")) is None:
                continue
            if best_in is None or floors[u] < best_in:
                best_in = floors[u]
    if best_out is not None:
        return best_out
    if best_in is not None:
        return max(1, best_in - 1)
    return None


def class_floor_profile(
    G: nx.Graph,
    class_id: str,
    members: list[str],
    floors: dict[str, int],
    measured: "set[str] | None" = None,
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

    `measured`, when given, is the set of nodes whose floor was MEASURED
    along call structure (see `compute_floors_with_provenance`: everything
    but the parallel pass). Those decide this unit's floor on their own,
    and a unit's parallel-placed members are ignored while even one
    measured member exists — a floor taken from adjacency must never
    outvote one taken from a call chain. The real case: a module region
    with 3 members measured at floor 1 and 5 placed alongside floor 0
    flipped from floor 1 to floor 0 on the strength of the weaker
    evidence, purely because there was more of it. Only a unit with NO
    measured member at all falls back to its parallel-placed ones (that is
    the coverage the parallel pass exists to add), and says so in
    `floor_basis`. Pass `measured=None` to treat every known floor as
    measured — the historical behavior.

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
    ids = [class_id, *members] if class_id is not None else list(members)
    # Measured evidence first, and alone if there is any of it — see above.
    known = [
        floors[n] for n in ids
        if n in floors and (measured is None or n in measured)
    ]
    basis = "measured"
    if not known:
        known = [floors[n] for n in ids if n in floors]
        basis = "parallel"
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
        # "measured" = decided by members placed along call structure;
        # "parallel" = this unit had none, and sits where its neighbors do.
        "floor_basis": basis,
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
