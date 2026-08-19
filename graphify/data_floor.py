"""data_floor — data-flow layering ("which floor is this on?").

`decouple.py` scores a class by how tangled its own members are. That says
nothing about WHERE in the system's data flow the class sits, which is a
different and equally structural question: a class that reads a file, a
class that computes on what was read, and a class that renders the result
are three different jobs, and one class doing all three is a problem the
call-graph metrics can't see (its members can be perfectly cohesive by
call structure while still spanning the whole pipeline).

Floors are BFS distance from the system's I/O boundary:

  - Floor 0 = the boundary itself — where data enters or leaves the process
    (parsers, loaders, readers, writers, exporters, DB/HTTP clients). Both
    ends count: "first data source OR output point".
  - Floor 1 = everything directly touching floor 0.
  - Floor N = N hops from the nearest boundary node.

Distance is measured on the UNDIRECTED graph. A call edge's direction says
who invokes whom, which is not the same as which way data moves (a parser
called BY a controller still supplies data TO it), and resolving true data
direction needs dataflow analysis this module does not attempt. Undirected
distance answers the question it can actually answer honestly: "how many
hops from the boundary is this?"

Honest limits:
  - Boundary detection is a NAME heuristic (path tokens + symbol-name
    patterns), not I/O detection. It cannot see a class that does raw
    socket work under a domain-flavored name, and it will flag a
    `parse_args()` that never touches the outside world. `boundary_reason`
    is recorded per node so every floor-0 call can be audited rather than
    taken on faith.
  - A graph with no detectable boundary yields NO floors at all (an empty
    dict), not a fabricated layering rooted at an arbitrary node.
  - Nodes in a component with no boundary node are absent from the result —
    unreachable, not floor 0.
"""
from __future__ import annotations

import re
from collections import deque
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


def compute_floors(G: nx.Graph) -> "tuple[dict[str, int], dict[str, str]]":
    """BFS distance from the nearest I/O boundary node, for every node
    reachable from one.

    Returns `(floors, boundary_reasons)`. `floors` maps node id -> floor;
    a node in a component containing no boundary node is ABSENT (unknown
    floor), never defaulted to 0. `boundary_reasons` maps each floor-0 node
    to the `boundary_reason` that put it there.

    Deterministic: seeds and neighbors are visited in sorted id order, so
    the same graph always yields the same floors (ties in BFS distance
    cannot produce different results anyway, but sorting keeps the
    traversal itself reproducible for debugging).
    """
    reasons: dict[str, str] = {}
    for nid in sorted(G.nodes):
        reason = boundary_reason(G, nid)
        if reason:
            reasons[nid] = reason
    if not reasons:
        return {}, {}

    floors: dict[str, int] = {nid: 0 for nid in reasons}
    queue: deque[str] = deque(sorted(reasons))
    while queue:
        current = queue.popleft()
        for neighbor in sorted(nx.all_neighbors(G, current)) if G.is_directed() else sorted(G.neighbors(current)):
            if neighbor in floors:
                continue
            floors[neighbor] = floors[current] + 1
            queue.append(neighbor)
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
    """
    known = [floors[n] for n in [class_id, *members] if n in floors]
    if not known:
        return None
    counts: dict[int, int] = {}
    for f in known:
        counts[f] = counts.get(f, 0) + 1
    dominant = min(counts, key=lambda f: (-counts[f], f))
    return {
        "floor": dominant,
        "min_floor": min(known),
        "max_floor": max(known),
        "floor_span": max(known) - min(known),
        "members_with_known_floor": len(known),
        "members_total": len(members) + 1,  # + the class node itself
    }


_FLOOR_SPAN_CAP = 4  # floor_span >= this maxes the cross-floor risk component


def cross_floor_risk(profile: "dict[str, Any] | None") -> float:
    """0-100 risk proxy for how far a class straddles the data flow.

    A class spanning `_FLOOR_SPAN_CAP` or more floors scores 100. Same
    caveat as every other score in this feature: a fixed heuristic weight,
    comparative on THIS graph, not a validated metric. Returns 0.0 for an
    unknown profile — a class whose floors could not be determined is not
    penalized for it (unknown is not the same as clean, and the report says
    which one it is).
    """
    if not profile:
        return 0.0
    return round(100 * min(profile["floor_span"] / _FLOOR_SPAN_CAP, 1.0), 1)
