"""html — moved verbatim from graphify/export.py."""
from __future__ import annotations

from graphify.exporters.base import COMMUNITY_COLORS  # noqa: E402,F401
from pathlib import Path
import html as _html
from graphify.analyze import _node_community_map
import json
import networkx as nx
from graphify.security import sanitize_label


MAX_NODES_FOR_VIZ = 5_000

def _viz_node_limit() -> int:
    """Return the effective viz node limit, honoring GRAPHIFY_VIZ_NODE_LIMIT env var.

    Falls back to MAX_NODES_FOR_VIZ when the env var is unset, empty, or non-integer.
    Set to 0 to disable HTML viz unconditionally (useful for CI runners).
    """
    import os
    raw = os.environ.get("GRAPHIFY_VIZ_NODE_LIMIT")
    if raw is None or not raw.strip():
        return MAX_NODES_FOR_VIZ
    try:
        return int(raw)
    except ValueError:
        return MAX_NODES_FOR_VIZ

def _html_styles() -> str:
    return """<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #0f0f1a; color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; display: flex; height: 100vh; overflow: hidden; }
  #graph { flex: 1; }
  #sidebar { width: 280px; background: #1a1a2e; border-left: 1px solid #2a2a4e; display: flex; flex-direction: column; overflow: hidden; }
  #search-wrap { padding: 12px; border-bottom: 1px solid #2a2a4e; }
  #search { width: 100%; background: #0f0f1a; border: 1px solid #3a3a5e; color: #e0e0e0; padding: 7px 10px; border-radius: 6px; font-size: 13px; outline: none; }
  #search:focus { border-color: #4E79A7; }
  #search-results { max-height: 140px; overflow-y: auto; padding: 4px 12px; border-bottom: 1px solid #2a2a4e; display: none; }
  .search-item { padding: 4px 6px; cursor: pointer; border-radius: 4px; font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .search-item:hover { background: #2a2a4e; }
  #info-panel { padding: 14px; border-bottom: 1px solid #2a2a4e; min-height: 140px; }
  #info-panel h3 { font-size: 13px; color: #aaa; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; }
  #info-content { font-size: 13px; color: #ccc; line-height: 1.6; }
  #info-content .field { margin-bottom: 5px; }
  #info-content .field b { color: #e0e0e0; }
  #info-content .empty { color: #555; font-style: italic; }
  .neighbor-link { display: block; padding: 2px 6px; margin: 2px 0; border-radius: 3px; cursor: pointer; font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; border-left: 3px solid #333; }
  .neighbor-link:hover { background: #2a2a4e; }
  #neighbors-list { max-height: 160px; overflow-y: auto; margin-top: 4px; }
  #legend-wrap { flex: 1; overflow-y: auto; padding: 12px; }
  #legend-wrap h3 { font-size: 13px; color: #aaa; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.05em; }
  .legend-item { display: flex; align-items: center; gap: 8px; padding: 4px 0; cursor: pointer; border-radius: 4px; font-size: 12px; }
  .legend-item:hover { background: #2a2a4e; padding-left: 4px; }
  .legend-item.dimmed { opacity: 0.35; }
  .legend-dot { width: 12px; height: 12px; border-radius: 50%; flex-shrink: 0; }
  .legend-label { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .legend-count { color: #666; font-size: 11px; }
  #stats { padding: 10px 14px; border-top: 1px solid #2a2a4e; font-size: 11px; color: #555; }
  #legend-controls { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; margin-bottom: 8px; padding: 4px 0; }
  #legend-controls label { display: flex; align-items: center; gap: 6px; cursor: pointer; font-size: 12px; color: #aaa; user-select: none; }
  #legend-controls label:hover { color: #e0e0e0; }
  .legend-cb, #select-all-cb { appearance: none; -webkit-appearance: none; width: 14px; height: 14px; border: 1.5px solid #3a3a5e; border-radius: 3px; background: #0f0f1a; cursor: pointer; position: relative; flex-shrink: 0; }
  .legend-cb:checked, #select-all-cb:checked { background: #4E79A7; border-color: #4E79A7; }
  .legend-cb:checked::after, #select-all-cb:checked::after { content: ''; position: absolute; left: 3.5px; top: 1px; width: 4px; height: 7px; border: solid #fff; border-width: 0 2px 2px 0; transform: rotate(45deg); }
  #select-all-cb:indeterminate { background: #4E79A7; border-color: #4E79A7; }
  #select-all-cb:indeterminate::after { content: ''; position: absolute; left: 2px; top: 5px; width: 8px; height: 2px; background: #fff; border: none; transform: none; }
</style>"""

def _hyperedge_script(hyperedges_json: str) -> str:
    return f"""<script>
// Render hyperedges as shaded confidence-ellipse-style regions — used both
// for graphify's own extracted multi-way relations (README-derived feature
// groups etc., no styling fields set — keeps the original indigo look) and
// for graphify.decouple's class-boundary hulls (fill/stroke/dashed set
// explicitly — see decouple._class_hulls), which need a visually distinct,
// clearly readable style so a class boundary reads as an actual REGION
// (like a cluster plot's confidence ellipse), not a faint hint.
const hyperedges = {hyperedges_json};
// beforeDrawing (not afterDrawing) so the ellipse paints BEHIND nodes/edges
// for that frame — node dots and labels stay crisp on top of the fill,
// matching how a cluster-plot ellipse sits behind its points.
network.on('beforeDrawing', function(ctx) {{
    hyperedges.forEach(h => {{
        // A tagged layer (graphify.decouple's own hulls) is gated by its
        // checkbox.
        if (h.layer && typeof HULL_LAYERS_VISIBLE !== 'undefined' && !HULL_LAYERS_VISIBLE[h.layer]) return;
        // Explicit geometry (graphify.decouple's class discs, which were
        // computed to be provably non-overlapping) wins over fitting a
        // shape to wherever the nodes currently sit — a fit has to be
        // padded outward to cover every member, and that padding is what
        // pushes one class's region into its neighbor's.
        if (h.cx != null && h.cy != null && h.r != null) {{
            drawRegion(ctx, h, h.cx, h.cy, h.r, h.r, 0);
            return;
        }}
        // A pre-existing semantic hyperedge (no `layer` — e.g. a
        // README-derived feature grouping, unrelated to decouple) fits an
        // ellipse to wherever its member nodes CURRENTLY sit. That design
        // assumes physics naturally clustered related nodes close
        // together — true when nothing else is repositioning them. Once
        // "Class boundaries" pins every class to its own explicit,
        // deliberately-spread-apart disc (see decouple._class_cluster_layout),
        // a hyperedge spanning members from several different classes gets
        // its nodes yanked far apart for a reason that has nothing to do
        // with the hyperedge's own meaning — the fit then has to stretch to
        // cover them and produces an ellipse dwarfing every real region
        // (measured on a real corpus: a 4-node hyperedge whose members
        // happened to land in 2 different class discs fit to roughly
        // 5000x6000 units, next to real class regions maxing out around
        // 800). Skipped while that layout is active, not resized — there is
        // no size that makes "these nodes are pinned apart on purpose"
        // read as "these nodes are naturally close together".
        if (!h.layer && typeof HULL_LAYERS_VISIBLE !== 'undefined' && HULL_LAYERS_VISIBLE.class) return;
        const positions = h.nodes
            .map(nid => network.getPositions([nid])[nid])
            .filter(p => p !== undefined);
        if (positions.length < 2) return;
        const n = positions.length;
        const cx = positions.reduce((s, p) => s + p.x, 0) / n;
        const cy = positions.reduce((s, p) => s + p.y, 0) / n;
        // Covariance-matrix ellipse: orient along the point scatter's own
        // principal axes (closed-form 2x2 eigendecomposition) instead of a
        // polygon connecting literal node positions — a smooth region that
        // reads as "this is a group", not a jagged shape that changes
        // silhouette every time physics nudges one outlier node.
        let varX = 0, varY = 0, covXY = 0;
        positions.forEach(p => {{
            const dx = p.x - cx, dy = p.y - cy;
            varX += dx * dx; varY += dy * dy; covXY += dx * dy;
        }});
        varX /= n; varY /= n; covXY /= n;
        const trace = varX + varY, det = varX * varY - covXY * covXY;
        const disc = Math.max(trace * trace / 4 - det, 0);
        const lambda1 = trace / 2 + Math.sqrt(disc);
        const lambda2 = Math.max(trace / 2 - Math.sqrt(disc), 0);
        const angle = Math.abs(covXY) < 1e-9 && Math.abs(varX - varY) < 1e-9
            ? 0 : 0.5 * Math.atan2(2 * covXY, varX - varY);
        let semiMajor = Math.sqrt(lambda1) || 1;
        let semiMinor = Math.max(Math.sqrt(lambda2), semiMajor * 0.3) || 1;
        // Scale up until every member node is strictly inside the ellipse —
        // a covariance ellipse is a statistical fit, not a guaranteed
        // cover; a member drawn OUTSIDE its own class's boundary would be
        // actively misleading here.
        const cosA = Math.cos(-angle), sinA = Math.sin(-angle);
        let k = 1;
        positions.forEach(p => {{
            const dx = p.x - cx, dy = p.y - cy;
            const lx = dx * cosA - dy * sinA, ly = dx * sinA + dy * cosA;
            const ratio = Math.sqrt((lx / semiMajor) ** 2 + (ly / semiMinor) ** 2);
            if (ratio > k) k = ratio;
        }});
        const pad = 1.2;
        const rx = Math.max(semiMajor * k * pad, 45);
        const ry = Math.max(semiMinor * k * pad, 45);
        drawRegion(ctx, h, cx, cy, rx, ry, angle);
    }});
}});

function drawRegion(ctx, h, cx, cy, rx, ry, angle) {{
    ctx.save();
    const fill = h.fill || '#6366f1';
    const stroke = h.stroke || fill;
    ctx.fillStyle = fill;
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 2.5;
    if (h.dashed) ctx.setLineDash([8, 5]);
    ctx.beginPath();
    ctx.ellipse(cx, cy, rx, ry, angle, 0, 2 * Math.PI);
    ctx.closePath();
    ctx.globalAlpha = h.fillAlpha != null ? h.fillAlpha : 0.22;
    ctx.fill();
    ctx.globalAlpha = h.strokeAlpha != null ? h.strokeAlpha : 0.75;
    ctx.stroke();
    ctx.setLineDash([]);
    // Label above the region's top edge (not at dead center, where it would
    // sit under overlapping node dots).
    ctx.globalAlpha = 0.95;
    ctx.fillStyle = h.labelColor || '#4f46e5';
    ctx.font = 'bold 12px sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(h.label, cx, cy - ry - 8);
    ctx.restore();
}}
</script>"""

def _html_script(nodes_json: str, edges_json: str, legend_json: str) -> str:
    return f"""<script>
const RAW_NODES = {nodes_json};
const RAW_EDGES = {edges_json};
const LEGEND = {legend_json};

// HTML-escape helper — prevents XSS when injecting graph data into innerHTML
function esc(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}}

// Build vis datasets
const nodesDS = new vis.DataSet(RAW_NODES.map(n => {{
  const base = {{
    id: n.id, label: n.label, color: n.color, size: n.size,
    font: n.font, title: n.title,
    _community: n.community, _community_name: n.community_name,
    _source_file: n.source_file, _file_type: n.file_type, _degree: n.degree,
    _kind: n.kind || 'real', _risk: n.risk || null,
    _label_plain: n.label, _label_scored: n.label_scored || n.label,
    _extracted_into: n.extracted_into || null,
    _state_overlaps: n.state_overlaps || null,
    _cluster_x: n.cluster_x != null ? n.cluster_x : null,
    _cluster_y: n.cluster_y != null ? n.cluster_y : null,
  }};
  // Conditional keys only — an explicit `undefined` on a vis.DataSet item can
  // still override the network-wide default (e.g. shape: 'dot'), so these are
  // omitted entirely for a node that doesn't set them, rather than forwarded
  // as undefined (this also fixes the pre-existing gap where a learning-
  // overlay ring's borderWidth/shapeProperties never reached vis at all).
  if (n.shape) base.shape = n.shape;
  if (n.borderWidth) base.borderWidth = n.borderWidth;
  if (n.shapeProperties) base.shapeProperties = n.shapeProperties;
  // "Class boundaries" defaults ON — apply the cluster-plot position from
  // the very first frame (not as a post-creation reposition) so the graph
  // never flashes an un-clustered layout before the toggle catches up.
  if (n.cluster_x != null && n.cluster_y != null) {{
    base.x = n.cluster_x; base.y = n.cluster_y;
    base.fixed = {{ x: true, y: true }};
  }}
  if (n.hidden) base.hidden = true;
  return base;
}}));

const edgesDS = new vis.DataSet(RAW_EDGES.map((e, i) => ({{
  id: i, from: e.from, to: e.to,
  label: '',
  title: e.title,
  dashes: e.dashes,
  width: e.width,
  color: e.color,
  arrows: {{ to: {{ enabled: true, scaleFactor: 0.5 }} }},
}})));

const container = document.getElementById('graph');
const network = new vis.Network(container, {{ nodes: nodesDS, edges: edgesDS }}, {{
  physics: {{
    enabled: true,
    solver: 'forceAtlas2Based',
    forceAtlas2Based: {{
      gravitationalConstant: -60,
      centralGravity: 0.005,
      springLength: 120,
      springConstant: 0.08,
      damping: 0.4,
      avoidOverlap: 0.8,
    }},
    stabilization: {{ iterations: 200, fit: true }},
  }},
  interaction: {{
    hover: true,
    tooltipDelay: 100,
    hideEdgesOnDrag: true,
    navigationButtons: false,
    keyboard: false,
  }},
  nodes: {{ shape: 'dot', borderWidth: 1.5 }},
  edges: {{ smooth: {{ type: 'continuous', roundness: 0.2 }}, selectionWidth: 3 }},
}});

network.once('stabilizationIterationsDone', () => {{
  network.setOptions({{ physics: {{ enabled: false }} }});
}});

function showInfo(nodeId) {{
  const n = nodesDS.get(nodeId);
  if (!n) return;
  const neighborIds = network.getConnectedNodes(nodeId);
  const neighborItems = neighborIds.map(nid => {{
    const nb = nodesDS.get(nid);
    const color = nb ? nb.color.background : '#555';
    return `<span class="neighbor-link" style="border-left-color:${{esc(color)}}" data-nid="${{esc(nid)}}">${{esc(nb ? nb.label : nid)}}</span>`;
  }}).join('');
  document.getElementById('info-content').innerHTML = `
    <div class="field"><b>${{esc(n._label_plain)}}</b>${{n._kind === 'proposed' ? ' <span style="color:#a8a29e;font-size:11px">(proposed)</span>' : ''}}</div>
    <div class="field">Type: ${{esc(n._file_type || 'unknown')}}</div>
    <div class="field">Community: ${{esc(n._community_name)}}</div>
    <div class="field">Source: ${{esc(n._source_file || '-')}}</div>
    <div class="field">Degree: ${{n._degree}}</div>
    ${{n._risk ? `<div class="field" style="margin-top:8px;color:#aaa;font-size:11px">Decouple risk</div>
    <div class="field">Recommendation: <b>${{esc(n._risk.recommendation)}}</b></div>
    <div class="field">risk_before &rarr; risk_after: ${{n._risk.risk_before}} &rarr; ${{n._risk.risk_after}} (net ${{n._risk.net_benefit}})</div>` : ''}}
    ${{n._state_overlaps && n._state_overlaps.length ? `<div class="field" style="margin-top:8px;color:#aaa;font-size:11px">Shares state with</div>
    ${{n._state_overlaps.map(o => `
      <div class="field" style="margin-top:4px"><b>${{esc(o.with)}}</b> — overlap ${{o.overlap}} (fields ${{o.field_overlap}}, calls ${{o.call_overlap}})</div>
      ${{o.shared_writes.length ? `<div class="field" style="color:#f87171;font-size:11px">writes: ${{o.shared_writes.map(esc).join(', ')}}</div>` : ''}}
      ${{o.shared_attrs.length ? `<div class="field" style="font-size:11px">fields: ${{o.shared_attrs.map(esc).join(', ')}}</div>` : ''}}
      ${{o.shared_calls.length ? `<div class="field" style="font-size:11px">calls: ${{o.shared_calls.map(esc).join(', ')}}</div>` : ''}}
    `).join('')}}` : ''}}
    ${{n._extracted_into ? `<div class="field" style="margin-top:8px;color:#94a3b8;font-size:11px">Would move into: ${{esc((nodesDS.get(n._extracted_into) || {{}}).label || n._extracted_into)}}</div>` : ''}}
    ${{neighborIds.length ? `<div class="field" style="margin-top:8px;color:#aaa;font-size:11px">Neighbors (${{neighborIds.length}})</div><div id="neighbors-list">${{neighborItems}}</div>` : ''}}
  `;
}}

// Toggle: hide every real node a recommended split would pull out and show
// the diamonds (+ their redirected edges — hidden automatically once their
// diamond endpoint is hidden, so nothing extra to manage there) in their
// place. Off (default) = the graph exactly as extracted, unchanged. On =
// a preview of the wiring AFTER the recommended splits.
function setDecoupleView(showAfter) {{
  const updates = [];
  RAW_NODES.forEach(n => {{
    if (n.kind === 'proposed') updates.push({{ id: n.id, hidden: !showAfter }});
    else if (n.extracted_into) updates.push({{ id: n.id, hidden: showAfter }});
  }});
  if (updates.length) nodesDS.update(updates);
}}

// Toggle: swap every node's displayed label between its plain name and a
// name+score variant. Only nodes carrying a `_label_scored` different from
// their plain label are touched — a no-op when nothing was proposed.
function setScoreMode(showScores) {{
  const updates = RAW_NODES
    .filter(n => n.label_scored && n.label_scored !== n.label)
    .map(n => ({{ id: n.id, label: showScores ? n.label_scored : n.label }}));
  if (updates.length) nodesDS.update(updates);
}}

// Whether decouple's class-boundary regions are drawn. A hull with no
// `layer` at all (a pre-existing semantic hyperedge, not from decouple) is
// ALWAYS drawn, regardless of this map. Background regions mean exactly one
// thing — "this is one class" — so `class` is the only gated layer; a
// proposed split or merge is a CHANGE to the code and is drawn as wiring
// (◆ nodes + proposed edges under "Preview decoupled view") instead.
let HULL_LAYERS_VISIBLE = {{ class: true }};

// Toggling class boundaries also toggles the non-overlapping class layout
// they are drawn over (see graphify.decouple._class_cluster_layout) —
// the regions only make sense at those positions; over raw physics
// positions two classes' methods interleave and the regions collide.
function setClassBoundaryLayout(enabled) {{
  HULL_LAYERS_VISIBLE.class = enabled;
  const updates = RAW_NODES
    .filter(n => n.cluster_x != null && n.cluster_y != null)
    .map(n => enabled
      ? {{ id: n.id, x: n.cluster_x, y: n.cluster_y, fixed: {{ x: true, y: true }} }}
      : {{ id: n.id, fixed: {{ x: false, y: false }} }});
  if (updates.length) nodesDS.update(updates);
  if (enabled) network.stabilize(); else network.startSimulation();
  network.redraw();
}}

function focusNode(nodeId) {{
  network.focus(nodeId, {{ scale: 1.4, animation: true }});
  network.selectNodes([nodeId]);
  showInfo(nodeId);
}}

// Neighbor links use a data attribute + one delegated listener rather than an
// inline onclick. A node id/label sourced from a document or a scraped URL
// (graphify add) can contain a double-quote; dropping the stringified id
// unescaped into a quoted onclick both broke every link and allowed a hostile
// source to inject an event handler into the local report (stored XSS, #1838).
// esc() on data-nid keeps the value inside the attribute; the listener reads it
// back verbatim. Bound to document so it survives the innerHTML rebuild that
// recreates #neighbors-list on each showInfo().
document.addEventListener('click', e => {{
  const el = e.target.closest('.neighbor-link');
  if (el && el.dataset.nid !== undefined) focusNode(el.dataset.nid);
}});

// Track hovered node — hover detection is more reliable than click params
let hoveredNodeId = null;
network.on('hoverNode', params => {{
  hoveredNodeId = params.node;
  container.style.cursor = 'pointer';
}});
network.on('blurNode', () => {{
  hoveredNodeId = null;
  container.style.cursor = 'default';
}});
container.addEventListener('click', () => {{
  if (hoveredNodeId !== null) {{
    showInfo(hoveredNodeId);
    network.selectNodes([hoveredNodeId]);
  }}
}});
network.on('click', params => {{
  if (params.nodes.length > 0) {{
    showInfo(params.nodes[0]);
  }} else if (hoveredNodeId === null) {{
    document.getElementById('info-content').innerHTML = '<span class="empty">Click a node to inspect it</span>';
  }}
}});

const searchInput = document.getElementById('search');
const searchResults = document.getElementById('search-results');
searchInput.addEventListener('input', () => {{
  const q = searchInput.value.toLowerCase().trim();
  searchResults.innerHTML = '';
  if (!q) {{ searchResults.style.display = 'none'; return; }}
  const matches = RAW_NODES.filter(n => n.label.toLowerCase().includes(q)).slice(0, 20);
  if (!matches.length) {{ searchResults.style.display = 'none'; return; }}
  searchResults.style.display = 'block';
  matches.forEach(n => {{
    const el = document.createElement('div');
    el.className = 'search-item';
    el.textContent = n.label;
    el.style.borderLeft = `3px solid ${{n.color.background}}`;
    el.style.paddingLeft = '8px';
    el.onclick = () => {{
      network.focus(n.id, {{ scale: 1.5, animation: true }});
      network.selectNodes([n.id]);
      showInfo(n.id);
      searchResults.style.display = 'none';
      searchInput.value = '';
    }};
    searchResults.appendChild(el);
  }});
}});
document.addEventListener('click', e => {{
  if (!searchResults.contains(e.target) && e.target !== searchInput)
    searchResults.style.display = 'none';
}});

const hiddenCommunities = new Set();

const selectAllCb = document.getElementById('select-all-cb');

function updateSelectAllState() {{
  const total = LEGEND.length;
  const hidden = hiddenCommunities.size;
  selectAllCb.checked = hidden === 0;
  selectAllCb.indeterminate = hidden > 0 && hidden < total;
}}

function toggleAllCommunities(hide) {{
  document.querySelectorAll('.legend-item').forEach(item => {{
    hide ? item.classList.add('dimmed') : item.classList.remove('dimmed');
  }});
  document.querySelectorAll('.legend-cb').forEach(cb => {{
    cb.checked = !hide;
  }});
  LEGEND.forEach(c => {{
    if (hide) hiddenCommunities.add(c.cid); else hiddenCommunities.delete(c.cid);
  }});
  const updates = RAW_NODES.map(n => ({{ id: n.id, hidden: hide }}));
  nodesDS.update(updates);
  updateSelectAllState();
}}

const legendEl = document.getElementById('legend');
LEGEND.forEach(c => {{
  const item = document.createElement('div');
  item.className = 'legend-item';
  const cb = document.createElement('input');
  cb.type = 'checkbox';
  cb.className = 'legend-cb';
  cb.checked = true;
  cb.addEventListener('change', (e) => {{
    e.stopPropagation();
    if (cb.checked) {{
      hiddenCommunities.delete(c.cid);
      item.classList.remove('dimmed');
    }} else {{
      hiddenCommunities.add(c.cid);
      item.classList.add('dimmed');
    }}
    const updates = RAW_NODES
      .filter(n => n.community === c.cid)
      .map(n => ({{ id: n.id, hidden: !cb.checked }}));
    nodesDS.update(updates);
    updateSelectAllState();
  }});
  item.innerHTML = `<div class="legend-dot" style="background:${{c.color}}"></div>
    <span class="legend-label">${{c.label}}</span>
    <span class="legend-count">${{c.count}}</span>`;
  item.prepend(cb);
  item.onclick = (e) => {{
    if (e.target === cb) return;
    cb.checked = !cb.checked;
    cb.dispatchEvent(new Event('change'));
  }};
  legendEl.appendChild(item);
}});
</script>"""


def _html_document_title(output_path: str) -> str:
    """Return a portable label for the graph.html <title>.

    Tracked artifacts must not embed the generator host absolute path
    (regression of #433; reported again as #2598 on Windows). Keep from the
    configured output-dir bare name (``graphify-out`` / ``GRAPHIFY_OUT``
    basename) onward — portable in every case; otherwise fall back to a
    cwd-relative label, and finally the filename only.
    """
    from graphify.paths import GRAPHIFY_OUT_NAME

    raw = str(output_path).replace("\\", "/")
    # Drop Windows drive prefix so Path parts are comparable on any OS.
    if len(raw) >= 3 and raw[1] == ":" and raw[0].isalpha() and raw[2] == "/":
        raw = raw[2:]  # "/Users/..." style after drive strip
    p = Path(raw)

    parts = list(Path(raw).parts)
    # Path("C:/Users/..") on POSIX may keep "C:" as first part — strip it.
    if parts and len(parts[0]) == 2 and parts[0][1] == ":" and parts[0][0].isalpha():
        parts = parts[1:]
    # Prefer keeping from the output-dir marker onward: portable in every
    # case, whereas a cwd-relative path still leaks host/user segments when
    # the graph is built from a directory ABOVE the project (#2598 follow-up).
    marker = GRAPHIFY_OUT_NAME
    for i, part in enumerate(parts):
        if part == marker or part.startswith("graphify-out"):
            return "/".join(parts[i:])

    # No standard out-dir marker (fully custom output path): fall back to a
    # cwd-relative label when the target is under cwd, else the bare filename.
    try:
        resolved = p if p.is_absolute() else (Path.cwd() / p)
        rel = resolved.resolve().relative_to(Path.cwd().resolve())
        label = rel.as_posix()
        if label and label != ".":
            return label
    except (ValueError, OSError, RuntimeError):
        pass

    name = p.name
    return name if name else "graph.html"

def to_html(
    G: nx.Graph,
    communities: dict[int, list[str]],
    output_path: str,
    community_labels: dict[int, str] | None = None,
    member_counts: dict[int, int] | None = None,
    node_limit: int | None = None,
    learning_overlay: dict | None = None,
) -> None:
    """Generate an interactive vis.js HTML visualization of the graph.

    Features: node size by degree, click-to-inspect panel, search box,
    community filter, physics clustering by community, confidence-styled edges.
    Raises ValueError if graph exceeds MAX_NODES_FOR_VIZ.

    If member_counts is provided (aggregated community view), node sizes are
    based on community member counts rather than graph degree.

    If node_limit is set and the graph exceeds it, automatically builds an
    aggregated community-level meta-graph instead of raising ValueError.
    """
    limit = node_limit if node_limit is not None else _viz_node_limit()
    if G.number_of_nodes() > limit:
        if node_limit is not None:
            # Build aggregated community meta-graph
            from collections import Counter as _Counter
            import networkx as _nx
            print(f"Graph has {G.number_of_nodes()} nodes (above {limit} limit). Building aggregated community view...")
            node_to_community = {nid: cid for cid, members in communities.items() for nid in members}
            meta = _nx.Graph()
            for cid, members in communities.items():
                meta.add_node(str(cid), label=(community_labels or {}).get(cid, f"Community {cid}"))
            edge_counts = _Counter()
            for u, v in G.edges():
                cu, cv = node_to_community.get(u), node_to_community.get(v)
                if cu is not None and cv is not None and cu != cv:
                    edge_counts[(min(cu, cv), max(cu, cv))] += 1
            for (cu, cv), w in edge_counts.items():
                meta.add_edge(str(cu), str(cv), weight=w,
                              relation=f"{w} cross-community edges", confidence="AGGREGATED")
            if meta.number_of_nodes() <= 1:
                print("Single community - aggregated view not useful. Skipping graph.html.")
                return
            meta_communities = {cid: [str(cid)] for cid in communities}
            mc = {cid: len(members) for cid, members in communities.items()}
            # Remap hyperedges from semantic node IDs to community IDs
            raw_hyperedges = G.graph.get("hyperedges", [])
            if raw_hyperedges:
                remapped = []
                for he in raw_hyperedges:
                    he_members = he.get("nodes", [])
                    comm_ids, seen = [], set()
                    for nid in he_members:
                        c = node_to_community.get(nid)
                        if c is None:
                            continue
                        s = str(c)
                        if s in seen:
                            continue
                        seen.add(s)
                        comm_ids.append(s)
                    if len(comm_ids) < 2:
                        continue
                    remapped.append({
                        "id": he.get("id", ""),
                        "label": he.get("label") or he.get("relation", "").replace("_", " "),
                        "nodes": comm_ids,
                    })
                meta.graph["hyperedges"] = remapped
            to_html(meta, meta_communities, output_path,
                    community_labels=community_labels, member_counts=mc)
            print(f"graph.html written (aggregated: {meta.number_of_nodes()} community nodes, {meta.number_of_edges()} cross-community edges)")
            print("Tip: run with --obsidian for full node-level detail.")
            return
        raise ValueError(
            f"Graph has {G.number_of_nodes()} nodes - too large for HTML viz "
            f"(limit: {limit}). Use --no-viz, raise GRAPHIFY_VIZ_NODE_LIMIT, "
            f"or reduce input size."
        )

    node_community = _node_community_map(communities)
    degree = dict(G.degree())
    max_deg = max(degree.values(), default=1) or 1
    max_mc = (max(member_counts.values(), default=1) or 1) if member_counts else 1

    # Work-memory overlay (derived sidecar). When not passed explicitly, load it
    # best-effort from the sibling .graphify_learning.json next to the output
    # graph.html (which lives beside graph.json). Empty/missing => no learning
    # fields, so the un-annotated render is byte-identical to pre-feature.
    if learning_overlay is None:
        learning_overlay = {}
        try:
            from graphify.reflect import load_learning_overlay as _llo
            learning_overlay = _llo(Path(output_path))
        except Exception:
            learning_overlay = {}
    # Status -> ring color. preferred=green, contested=amber. Tentative gets no
    # ring (it's not yet trustworthy enough to highlight in the map).
    _RING = {"preferred": "#22c55e", "contested": "#f59e0b"}
    # Ring color for a `kind="proposed"` node (see
    # graphify.decouple.build_augmented_graph, which only ever overlays a
    # `recommendation == "split"` group — a discouraged candidate is already
    # fully expressed as a number in DECOUPLE_PLAN.md/decouple.json and is
    # never drawn here, so there is only one color to pick).
    _DECOUPLE_RING_COLOR = "#22c55e"
    has_proposed = any(data.get("kind") == "proposed" for _, data in G.nodes(data=True))
    hull_layers = {h.get("layer") for h in getattr(G, "graph", {}).get("hyperedges", []) if h.get("layer")}

    # Build nodes list for vis.js
    vis_nodes = []
    for node_id, data in G.nodes(data=True):
        cid = node_community.get(node_id, 0)
        color = COMMUNITY_COLORS[cid % len(COMMUNITY_COLORS)]
        label = sanitize_label(data.get("label", node_id))
        deg = degree.get(node_id, 1)
        if member_counts:
            mc = member_counts.get(cid, 1)
            size = 10 + 30 * (mc / max_mc)
            font_size = 12
        else:
            size = 10 + 30 * (deg / max_deg)
            # Only show label for high-degree nodes by default; others show on hover
            font_size = 12 if deg >= max_deg * 0.15 else 0
        node = {
            "id": node_id,
            "label": label,
            "color": {"background": color, "border": color, "highlight": {"background": "#ffffff", "border": color}},
            "size": round(size, 1),
            "font": {"size": font_size, "color": "#ffffff"},
            "title": _html.escape(label),
            "community": cid,
            "community_name": sanitize_label((community_labels or {}).get(cid, f"Community {cid}")),
            "source_file": sanitize_label(str(data.get("source_file") or "")),
            "file_type": data.get("file_type", ""),
            "degree": deg,
        }
        # A real node that a recommended split would pull out (see
        # graphify.decouple.build_augmented_graph) — the "Preview decoupled
        # view" toggle hides this node (and, being hidden, its edges) and
        # shows the diamond it points to instead.
        extracted_into = data.get("decouple_extracted_into")
        if extracted_into:
            node["extracted_into"] = extracted_into
        # Non-overlapping cluster-plot coordinates (see
        # graphify.decouple._class_cluster_layout) — present only for nodes
        # belonging to an analyzed class. The "Class boundaries" toggle
        # fixes a node here; unchecking it releases the node back to
        # physics. Absent entirely for a plain graph.html (no decouple
        # plan involved), so that render is untouched.
        if "cluster_x" in data and "cluster_y" in data:
            node["cluster_x"] = data["cluster_x"]
            node["cluster_y"] = data["cluster_y"]
        # Conditional learning fields — only present for annotated nodes, so
        # un-annotated output keeps the exact pre-feature node dict shape.
        entry = learning_overlay.get(str(node_id)) if learning_overlay else None
        if entry:
            status = sanitize_label(str(entry.get("status", "")))
            stale = bool(entry.get("stale"))
            node["learning_status"] = status
            node["learning_stale"] = stale
            ring = _RING.get(status)
            if ring:
                # Status-colored ring via the border; stale => desaturated +
                # dashed (vis.js supports per-node `shapeProperties.borderDashes`).
                if stale:
                    ring = "#9ca3af"
                    node["shapeProperties"] = {"borderDashes": [4, 4]}
                node["borderWidth"] = 3
                node["color"] = {
                    "background": color, "border": ring,
                    "highlight": {"background": "#ffffff", "border": ring},
                }
            # Lesson line appended to the hover title.
            if status == "contested":
                lesson = f"Lesson: contested (useful {entry.get('uses', 0)} / dead-end {entry.get('neg', 0)})"
            elif status == "preferred":
                lesson = f"Lesson: preferred source ({entry.get('uses', 0)} useful, score={entry.get('score', 0)})"
            else:
                lesson = f"Lesson: {status} ({entry.get('uses', 0)} useful)"
            if stale:
                lesson += " [code changed — re-verify]"
            node["title"] = _html.escape(label) + "\n" + _html.escape(sanitize_label(lesson))
        # A `kind="proposed"` node (graphify decouple's overlay, #2 in the
        # graphify-decouple fork) is not something the extraction found — it is
        # a hypothetical class a RECOMMENDED split suggests (build_augmented_
        # graph never draws a discouraged candidate). Same renderer, same
        # physics, same community-color background (so it visually stays with
        # the members it would be extracted from) — but a diamond shape and a
        # dashed green ring mark it as a proposal, never confusable with a
        # real EXTRACTED node.
        if data.get("kind") == "proposed":
            node["kind"] = "proposed"
            node["shape"] = "diamond"
            node["borderWidth"] = 3
            node["shapeProperties"] = {"borderDashes": [4, 3]}
            if data.get("hidden"):
                node["hidden"] = True  # "before" is the default view
            node["color"] = {
                "background": color, "border": _DECOUPLE_RING_COLOR,
                "highlight": {"background": "#ffffff", "border": _DECOUPLE_RING_COLOR},
            }
            member_count = data.get("member_count") or 0
            node["size"] = round(10 + 30 * min(member_count / 20, 1.0), 1)
            node["font"] = {"size": 12, "color": "#ffffff"}
            risk = data.get("decouple_risk")
            if risk:
                node["risk"] = risk
                node["label_scored"] = f"{label} ({risk.get('risk_before')}→{risk.get('risk_after')})"
                node["title"] = _html.escape(
                    f"{label} — proposed extraction, "
                    f"risk {risk.get('risk_before')}→{risk.get('risk_after')}"
                )
            state_overlaps = data.get("decouple_state_overlaps")
            if state_overlaps:
                node["state_overlaps"] = [
                    {
                        "with": sanitize_label(str(o["with"])),
                        "overlap": o["overlap"], "field_overlap": o["field_overlap"], "call_overlap": o["call_overlap"],
                        "shared_attrs": [sanitize_label(str(a)) for a in o["shared_attrs"][:10]],
                        "shared_writes": [sanitize_label(str(a)) for a in o["shared_writes"][:10]],
                        "shared_calls": [sanitize_label(str(a)) for a in o["shared_calls"][:10]],
                    }
                    for o in state_overlaps
                ]
        vis_nodes.append(node)

    # Build edges list. Restore original edge direction from _src/_tgt
    # (stashed by build.py for exactly this reason): undirected NetworkX
    # canonicalizes endpoint order, which would otherwise flip the arrow
    # for `calls` and `rationale_for` in the rendered graph (#563).
    vis_edges = []
    for u, v, data in G.edges(data=True):
        if data.get("kind") == "proposed_edge":
            # A proposed CHANGE, in one of two opposite directions — pulling
            # a group OUT of a god node (build_augmented_graph, green, the
            # same color as the ◆ it points at so edge and node read as one
            # unit) or folding scattered duplicates IN to a shared home
            # (overlay_tool_dedup_clusters, blue). Both are `proposed_edge`;
            # keying the label/color off `decouple_recommendation` is what
            # keeps a consolidation from being drawn — and labeled — as if
            # it were an extraction. _src/_tgt (not u/v) for the same reason
            # as the generic path below: an undirected graph canonicalizes
            # edge endpoint order.
            is_merge = data.get("decouple_recommendation") == "merge"
            vis_edges.append({
                "from": data.get("_src", u),
                "to": data.get("_tgt", v),
                "label": "merge_candidate" if is_merge else "extract",
                "title": _html.escape(
                    "decouple: consolidation candidate" if is_merge
                    else "decouple: recommended split"
                ),
                "dashes": True,
                "width": 2,
                "color": {
                    "color": "#3b82f6" if is_merge else _DECOUPLE_RING_COLOR,
                    "opacity": 0.85,
                },
            })
            continue
        if data.get("kind") == "redirected_edge":
            # A real dependency that used to touch an extracted member,
            # repointed onto the diamond it would move into — only visible
            # once "Preview decoupled view" hides that member (hiding a node
            # hides its own edges too, so the ORIGINAL edge just disappears;
            # this is the NEW one taking its place). Solid, not dashed: this
            # coupling is real today, only its endpoint moved.
            weight = data.get("weight", 1)
            vis_edges.append({
                "from": data.get("_src", u),
                "to": data.get("_tgt", v),
                "label": data.get("relation", ""),
                "title": _html.escape(f"redirected: {data.get('relation', '')} (x{weight})"),
                "dashes": False,
                "width": min(1 + weight, 4),
                "color": {"color": "#38bdf8", "opacity": 0.75},
            })
            continue
        if data.get("kind") == "new_coupling_edge":
            # Both ends move into DIFFERENT new classes — coupling that is
            # INVISIBLE today (an intra-class call) and only exists because
            # of the split. This is split_risk_score's cross_group_edges
            # made literal: the same number the risk balance already
            # weighed, now drawn as the edge it actually is.
            weight = data.get("weight", 1)
            vis_edges.append({
                "from": data.get("_src", u),
                "to": data.get("_tgt", v),
                "label": data.get("relation", ""),
                "title": _html.escape(f"new coupling introduced by the split: {data.get('relation', '')} (x{weight})"),
                "dashes": False,
                "width": min(1 + weight, 4),
                "color": {"color": "#f87171", "opacity": 0.85},
            })
            continue
        confidence = data.get("confidence", "EXTRACTED")
        relation = data.get("relation", "")
        true_src = data.get("_src", u)
        true_tgt = data.get("_tgt", v)
        vis_edges.append({
            "from": true_src,
            "to": true_tgt,
            "label": relation,
            "title": _html.escape(f"{relation} [{confidence}]"),
            "dashes": confidence != "EXTRACTED",
            "width": 2 if confidence == "EXTRACTED" else 1,
            "color": {"opacity": 0.7 if confidence == "EXTRACTED" else 0.35},
            "confidence": confidence,
        })

    # Build community legend data
    legend_data = []
    for cid in sorted((community_labels or {}).keys()):
        color = COMMUNITY_COLORS[cid % len(COMMUNITY_COLORS)]
        lbl = _html.escape(sanitize_label((community_labels or {}).get(cid, f"Community {cid}")))
        n = member_counts.get(cid, len(communities.get(cid, []))) if member_counts else len(communities.get(cid, []))
        legend_data.append({"cid": cid, "color": color, "label": lbl, "count": n})

    # Escape </script> sequences so embedded JSON cannot break out of the script tag
    def _js_safe(obj) -> str:
        return json.dumps(obj).replace("</", "<\\/")

    nodes_json = _js_safe(vis_nodes)
    edges_json = _js_safe(vis_edges)
    legend_json = _js_safe(legend_data)
    hyperedges_json = _js_safe(getattr(G, "graph", {}).get("hyperedges", []))
    title = _html.escape(sanitize_label(_html_document_title(output_path)))
    stats = f"{G.number_of_nodes()} nodes &middot; {G.number_of_edges()} edges &middot; {len(communities)} communities"
    # Only rendered when the graph carries at least one proposed (decouple)
    # node — a plain graph.html with nothing proposed stays functionally
    # unchanged (no dead checkboxes for a toggle with nothing to do).
    decouple_controls_html = (
        '<label><input type="checkbox" id="decouple-view-cb" '
        'onchange="setDecoupleView(this.checked)">Preview decoupled view '
        '<span style="color:#666">(hide old, show ◆ proposed)</span></label>'
        '<label><input type="checkbox" id="score-toggle-cb" '
        'onchange="setScoreMode(this.checked)">Show risk scores</label>'
        if has_proposed else ""
    )
    # Class-boundary checkbox: only when class hulls are actually present (a
    # plain graph.html — no decouple plan involved at all — renders none).
    # Defaults CHECKED: unlike a proposal overlay, a class boundary is a
    # fact about the code, and the non-overlapping layout it implies is the
    # readable default (see decouple._class_cluster_layout).
    hull_controls_html = (
        '<label><input type="checkbox" id="hull-class-cb" checked '
        'onchange="setClassBoundaryLayout(this.checked)">Class boundaries '
        '<span style="color:#666">(non-overlapping layout)</span></label>'
        if "class" in hull_layers else ""
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>graphify - {title}</title>
<script src="https://unpkg.com/vis-network@9.1.6/standalone/umd/vis-network.min.js"
        integrity="sha384-Ux6phic9PEHJ38YtrijhkzyJ8yQlH8i/+buBR8s3mAZOJrP1gwyvAcIYl3GWtpX1"
        crossorigin="anonymous"></script>
{_html_styles()}
</head>
<body>
<div id="graph"></div>
<div id="sidebar">
  <div id="search-wrap">
    <input id="search" type="text" placeholder="Search nodes..." autocomplete="off">
    <div id="search-results"></div>
  </div>
  <div id="info-panel">
    <h3>Node Info</h3>
    <div id="info-content"><span class="empty">Click a node to inspect it</span></div>
  </div>
  <div id="legend-wrap">
    <h3>Communities</h3>
    <div id="legend-controls">
      <label><input type="checkbox" id="select-all-cb" checked onchange="toggleAllCommunities(!this.checked)">Select All</label>
      {decouple_controls_html}
      {hull_controls_html}
    </div>
    <div id="legend"></div>
  </div>
  <div id="stats">{stats}</div>
</div>
{_html_script(nodes_json, edges_json, legend_json)}
{_hyperedge_script(hyperedges_json)}
</body>
</html>"""

    Path(output_path).write_text(html, encoding="utf-8")  # nosec
