"""decouple_html — render a Candidate Decoupled Architecture plan using the
SAME visual engine as `graph.html` (see graphify.exporters.html.to_html),
instead of a separate diagram language.

`graphify.decouple.build_augmented_graph` overlays the plan's proposed groups
onto a copy of the real graph as extra nodes/edges tagged `kind="proposed"` /
`kind="proposed_edge"`; `exporters.html.to_html` reads those tags to draw a
proposed group as a dashed diamond (green/amber/red ring by its
recommendation) sharing the same community color, physics, search box,
legend, and info panel as every real node — a proposal never looks like a
second, unrelated diagram. A "Show risk scores" toggle (only rendered when
the plan contains at least one proposed node) swaps each proposed node's
on-graph label between its plain name and a risk_before→risk_after badge;
the full breakdown is always available in the click-to-inspect info panel.

`tool_dedup_report`, when given, additionally overlays
`graphify.decouple.overlay_tool_dedup_clusters` on top — the same class-
boundary hull mechanism, in a distinct blue family, showing where scattered
near-duplicate functions would consolidate (see that function's docstring).
This is a SEPARATE analysis from the plan (tool_dedup scans source files
directly, not the god-node ranking `decouple_plan` uses), so it is optional
and additive: omit it and this renders exactly as before.

CLI: wired into ``graphify decouple`` (writes DECOUPLE.html next to
DECOUPLE_PLAN.md / decouple.json).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any


def write_decouple_html(
    G,
    plan: dict[str, Any],
    communities: dict[int, list[str]],
    community_labels: dict[int, str] | None,
    output_path: Path,
    *,
    tool_dedup_report: "dict[str, Any] | None" = None,
) -> Path:
    """Build the augmented graph for `plan` and render it with
    `exporters.html.to_html` — the identical style used for `graph.html`."""
    from graphify.decouple import build_augmented_graph, overlay_tool_dedup_clusters
    from graphify.exporters.html import to_html

    G2, communities2 = build_augmented_graph(G, plan, communities)
    if tool_dedup_report is not None:
        G2, communities2 = overlay_tool_dedup_clusters(G2, communities2, tool_dedup_report)
    to_html(G2, communities2, str(output_path), community_labels=community_labels)
    return output_path
