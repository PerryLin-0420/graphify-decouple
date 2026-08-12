"""decouple_html — emit a self-contained Mermaid HTML view of a Candidate
Decoupled Architecture plan (see graphify.decouple).

Deterministic; renders a `decouple_plan()` result: each god_object's existing
class as a solid node, each proposed split group as a dashed node (mirrors the
`concept`/non-real-node dashed convention already used in callflow_html), with
an `extract` edge between them. Over-referenced hubs (no split recommended)
are listed in the sidebar, not drawn as split candidates — drawing a split
that isn't recommended would misrepresent the plan.

CLI: wired into ``graphify decouple`` (writes DECOUPLE.html next to
DECOUPLE_PLAN.md / decouple.json).
"""
from __future__ import annotations

import html as _html
import re
from pathlib import Path
from typing import Any, Dict, List

_SAFE = re.compile(r"[^a-zA-Z0-9_]")


def _mid(prefix: str, s: str) -> str:
    """A Mermaid-safe node id: alnum/underscore only, length-capped."""
    return f"{prefix}_{_SAFE.sub('_', s)[:60]}"


def _esc(s: str) -> str:
    # Mermaid node labels are quoted strings; escape the quote and any
    # newline-like content that would break out of the "..." label.
    return str(s).replace('"', "&quot;").replace("\n", " ")


def build_mermaid(plan: Dict[str, Any]) -> str:
    """Build a `flowchart LR` Mermaid definition for every god_object entry's
    proposed split. Only a `recommendation == "split"` group gets the
    dashed `extract` edge in the "proposed" style — `marginal`/`keep_as_is`
    groups are still drawn (so the candidate that WAS considered is visible)
    but in a `discouraged` style with an edge label explaining why, so the
    diagram reflects the risk balance rather than every structural candidate.
    Returns an empty flowchart (with just the classDefs) when there is
    nothing to split — the caller still gets valid Mermaid source."""
    lines: List[str] = ["flowchart LR"]
    any_edge = False
    for gi, entry in enumerate(plan.get("god_nodes", [])):
        if entry.get("classification") != "god_object":
            continue
        risk = entry.get("risk", {})
        recommendation = risk.get("recommendation", "split")
        god_mid = _mid(f"g{gi}", entry["id"])
        risk_note = f" risk {risk['risk_before']}→{risk['risk_after']}" if risk else ""
        lines.append(f'  {god_mid}["{_esc(entry["label"])} (existing{risk_note})"]:::existing')
        for pj, g in enumerate(entry.get("proposed_groups", [])):
            if g.get("community_id") is None:
                continue  # residual — stays on the original class, not a split
            pid = _mid(f"g{gi}_p{pj}", g["name"])
            conf = g.get("cohesion_confidence", "n/a")
            count = len(g.get("members", []))
            if recommendation == "split":
                lines.append(f'  {pid}["{_esc(g["name"])} ({count} members, {conf})"]:::proposed')
                lines.append(f"  {god_mid} -.->|extract| {pid}")
            else:
                lines.append(f'  {pid}["{_esc(g["name"])} ({count} members, {conf})"]:::discouraged')
                lines.append(f"  {god_mid} -.->|{recommendation}: not worth it| {pid}")
            any_edge = True
    lines.append("  classDef existing fill:#1e293b,stroke:#38bdf8,color:#e2e8f0,stroke-width:1.5px;")
    lines.append("  classDef proposed fill:#292524,stroke:#a8a29e,color:#fafaf9,stroke-dasharray:5 3;")
    lines.append("  classDef discouraged fill:#292524,stroke:#f87171,color:#fecaca,stroke-dasharray:2 4;")
    if not any_edge:
        lines.insert(1, '  _empty["No god_object split candidates in this plan"]:::existing')
    return "\n".join(lines)


def _render_detail_block(entry: Dict[str, Any]) -> str:
    parts = [
        f"<h2>{_html.escape(entry['label'])} "
        f"<span class=\"tag {_html.escape(entry['classification'])}\">{_html.escape(entry['classification'])}</span></h2>",
        f"<p class=\"meta\">source: <code>{_html.escape(entry.get('source_file', ''))}</code> · "
        f"afferent={entry['afferent']} · efferent={entry['efferent']} · "
        f"member_count={entry['member_count']} · member_ratio={entry['member_ratio']}</p>",
    ]
    if entry["classification"] == "god_object":
        risk = entry.get("risk", {})
        sd = risk.get("split_detail", {})
        if risk:
            parts.append(
                f"<p class=\"meta\">risk_before={risk.get('risk_before')} · "
                f"risk_after={risk.get('risk_after')} · net_benefit={risk.get('net_benefit')} → "
                f"<strong>{_html.escape(str(risk.get('recommendation')))}</strong>"
                + (
                    f" · {sd['cross_group_edges']} new cross-group edges · "
                    f"{sd['straddling_callers']} straddling caller(s)"
                    if sd.get("n_new_classes") else ""
                )
                + "</p>"
            )
        for g in entry.get("proposed_groups", []):
            conf = g.get("cohesion_confidence", "n/a")
            title = "Residual (kept on original class)" if g.get("community_id") is None else g["name"]
            parts.append(f"<h3>{_html.escape(title)} — {len(g['members'])} members, confidence: {_html.escape(str(conf))}</h3>")
            parts.append("<ul>")
            for lbl in g["member_labels"]:
                parts.append(f"<li>{_html.escape(str(lbl))}</li>")
            parts.append("</ul>")
    elif "hub_suggestion" in entry:
        hs = entry["hub_suggestion"]
        parts.append(f"<p>{_html.escape(hs['rationale'])}</p>")
        parts.append("<p><strong>Top dependents:</strong></p><ul>")
        for d in hs["sample_dependents"]:
            parts.append(f"<li>{_html.escape(str(d['label']))}</li>")
        parts.append("</ul>")
    else:
        parts.append("<p><em>No split recommended — large but cohesive (members cluster in one community).</em></p>")
    return "\n".join(parts)


def _render_details(plan: Dict[str, Any]) -> str:
    return "\n".join(f'<section class="entry">{_render_detail_block(e)}</section>' for e in plan.get("god_nodes", []))


_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{ font-family: 'Segoe UI', sans-serif; margin: 0; padding: 24px; background: #0f172a; color: #e2e8f0; }}
  h1 {{ font-size: 1.8rem; margin: 0 0 8px; }}
  .caveats {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 16px; font-size: 0.85rem; color: #94a3b8; margin-bottom: 20px; }}
  #diagram {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-bottom: 24px; overflow-x: auto; }}
  section.entry {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 20px; margin-bottom: 16px; }}
  section.entry h2 {{ margin-top: 4px; }}
  .tag {{ font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; margin-left: 8px; vertical-align: middle; }}
  .tag.god_object {{ background: #7c2d12; color: #fed7aa; }}
  .tag.over_referenced_hub {{ background: #1e3a8a; color: #bfdbfe; }}
  .tag.cohesive_but_large {{ background: #14532d; color: #bbf7d0; }}
  .meta {{ color: #94a3b8; font-size: 0.85rem; }}
  code {{ background: #0f172a; padding: 1px 4px; border-radius: 4px; }}
  ul {{ margin: 4px 0; }}
</style>
</head>
<body>
  <h1>{header}</h1>
  <p class="caveats">{caveats_html}</p>
  <div id="diagram">
    <pre class="mermaid">
{mermaid}
    </pre>
  </div>
  {details_html}
  <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
  <script>mermaid.initialize({{ startOnLoad: true, theme: 'dark' }});</script>
</body>
</html>
"""


def emit_html(plan: Dict[str, Any], *, title: str, header: str) -> str:
    mermaid = build_mermaid(plan)
    caveats_html = "<br>".join(_html.escape(c) for c in plan.get("caveats", []))
    details_html = _render_details(plan)
    return _HTML_TEMPLATE.format(
        title=_html.escape(title),
        header=_html.escape(header),
        mermaid=mermaid.replace("</", "<\\/"),
        caveats_html=caveats_html,
        details_html=details_html,
    )


def write_decouple_html(plan: Dict[str, Any], output_path: Path, *, project_label: "str | None" = None) -> Path:
    title = f"{project_label or 'graphify'} — Candidate Decoupled Architecture"
    html = emit_html(plan, title=title, header=title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    return output_path
