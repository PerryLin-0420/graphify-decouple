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
) -> Path:
    """Build the augmented graph for `plan` and render it with
    `exporters.html.to_html` — the identical style used for `graph.html`."""
    from graphify.decouple import build_augmented_graph
    from graphify.exporters.html import to_html

    G2, communities2 = build_augmented_graph(G, plan, communities)
    to_html(G2, communities2, str(output_path), community_labels=community_labels)
    return output_path
