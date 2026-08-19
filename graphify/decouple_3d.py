"""decouple_3d — data-flow floors as a stacked 3D view.

The 2D `DECOUPLE.html` (see `decouple_html`) answers "what belongs to what":
class and module regions, non-overlapping, drawn over graphify's own
vis-network renderer. It cannot show the OTHER structural axis
`graphify.data_floor` computes — how far each unit sits from the system's
I/O boundary — because vis-network is strictly 2D and that axis needs a
third dimension to read as layering rather than as another color scale.

This module renders that axis directly: one horizontal plane per floor,
stacked on Z, with each class/module region drawn as a disc ON its own
floor's plane and its member nodes scattered inside it. An edge between
two floors becomes a visibly slanted line — the "this unit reaches across
N layers" risk (`data_floor.cross_floor_risk`) made literal, instead of
being only a number in the report.

Deliberately a SEPARATE file from DECOUPLE.html rather than a replacement:
the 2D view's search, legend, info panel, and region rendering are all
built on vis-network and work; rebuilding them on a 3D engine would risk
regressing verified behavior to gain nothing the 2D view was doing well.

Renderer: three.js (UMD build, pinned + SRI, same discipline as the
vis-network dependency in `exporters.html`). Orbit/zoom is implemented
inline rather than pulling `OrbitControls` as a second CDN dependency —
drag-to-rotate and wheel-to-zoom over a fixed target is a few lines, and
one pinned script is one less supply-chain surface.

Honest limits, surfaced in the page itself:
  - Floors come from `data_floor`, a NAME heuristic for the I/O boundary,
    not I/O analysis. A wrong floor 0 shifts everything above it.
  - A node with no known floor (no boundary reachable in its component) is
    NOT drawn on a plane — it is omitted from the stack rather than
    defaulted to floor 0.
"""
from __future__ import annotations

import html as _html
import json
from pathlib import Path
from typing import Any

import networkx as nx

_THREE_SRC = "https://unpkg.com/three@0.128.0/build/three.min.js"
# Verified by downloading the pinned artifact and hashing it, not copied
# from documentation.
_THREE_SRI = "sha384-CI3ELBVUz9XQO+97x6nwMDPosPR5XvsxW2ua7N1Xeygeh1IxtgqtCkGfQY9WWdHu"

_FLOOR_SPACING = 900.0  # world units between adjacent floor planes


def build_floor_scene(
    G: nx.Graph,
    class_discs: dict[str, tuple[float, float, float]],
    region_members: dict[str, list[str]],
    floors: dict[str, int],
    community_colors: list[str],
) -> dict[str, Any]:
    """Assemble the JSON payload the 3D page renders.

    Each region (class or module — see `decouple._class_cluster_layout`) is
    placed on the floor its own members predominantly occupy, reusing the
    SAME packed (x, y) disc the 2D view uses so the two views are directly
    comparable: a region sits at the same place on the map in both, only
    lifted onto its floor here.

    A region whose members span several floors is placed on its dominant
    floor and flagged `spans` with the range — that is the case the whole
    view exists to make visible, so it is marked rather than silently
    flattened.
    """
    regions: list[dict[str, Any]] = []
    for i, region_id in enumerate(sorted(class_discs)):
        cx, cy, radius = class_discs[region_id]
        members = region_members.get(region_id, [])
        known = [floors[m] for m in [region_id, *members] if m in floors]
        if not known:
            continue  # no floor could be determined — omitted, not defaulted
        counts: dict[int, int] = {}
        for f in known:
            counts[f] = counts.get(f, 0) + 1
        dominant = min(counts, key=lambda f: (-counts[f], f))
        if region_id.startswith("_module::"):
            label = region_id[len("_module::"):].rsplit("/", 1)[-1]
        else:
            label = str(G.nodes[region_id].get("label", region_id))
        member_points = []
        for m in members:
            if m not in G.nodes:
                continue
            member_points.append({
                "label": str(G.nodes[m].get("label", m)),
                "floor": floors.get(m, dominant),
            })
        regions.append({
            "id": region_id,
            "label": label,
            "x": cx, "y": cy, "r": radius,
            "floor": dominant,
            "min_floor": min(known), "max_floor": max(known),
            "spans": max(known) - min(known),
            "color": community_colors[i % len(community_colors)],
            "member_count": len(members),
            "members": member_points,
        })

    # Region-to-region links, aggregated: one drawn line per ordered pair,
    # with the count. Drawing every underlying edge would bury the
    # cross-floor structure this view exists to show under a hairball.
    node_region: dict[str, str] = {}
    for region_id, members in region_members.items():
        for m in [region_id, *members]:
            node_region[m] = region_id
    region_ids = {r["id"] for r in regions}
    pair_counts: dict[tuple[str, str], int] = {}
    for u, v in G.edges():
        ru, rv = node_region.get(u), node_region.get(v)
        if ru is None or rv is None or ru == rv:
            continue
        if ru not in region_ids or rv not in region_ids:
            continue
        pair_counts[(ru, rv)] = pair_counts.get((ru, rv), 0) + 1
    links = [
        {"source": a, "target": b, "weight": w}
        for (a, b), w in sorted(pair_counts.items())
    ]

    used_floors = sorted({r["floor"] for r in regions})
    return {"regions": regions, "links": links, "floors": used_floors}


def _page(scene_json: str, title: str, stats: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>graphify 3D floors - {title}</title>
<script src="{_THREE_SRC}" integrity="{_THREE_SRI}" crossorigin="anonymous"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: #0f0f1a; color: #e0e0e0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; display: flex; height: 100vh; overflow: hidden; }}
  #view {{ flex: 1; position: relative; }}
  #sidebar {{ width: 290px; background: #1a1a2e; border-left: 1px solid #2a2a4e; display: flex; flex-direction: column; overflow-y: auto; }}
  #sidebar h3 {{ font-size: 13px; color: #aaa; padding: 12px 14px 8px; text-transform: uppercase; letter-spacing: .05em; }}
  .row {{ display: flex; align-items: center; gap: 8px; padding: 5px 14px; font-size: 12px; cursor: pointer; }}
  .row:hover {{ background: #2a2a4e; }}
  .swatch {{ width: 11px; height: 11px; border-radius: 2px; flex-shrink: 0; }}
  .muted {{ color: #666; font-size: 11px; }}
  #notes {{ padding: 12px 14px; font-size: 11px; color: #777; line-height: 1.55; border-top: 1px solid #2a2a4e; margin-top: auto; }}
  #hint {{ position: absolute; left: 12px; bottom: 10px; font-size: 11px; color: #556; }}
  #tip {{ position: absolute; padding: 4px 8px; background: #000c; border: 1px solid #3a3a5e; border-radius: 4px; font-size: 12px; pointer-events: none; display: none; }}
</style>
</head>
<body>
<div id="view"><div id="tip"></div><div id="hint">drag to rotate &middot; wheel to zoom &middot; shift+drag to pan</div></div>
<div id="sidebar">
  <h3>Floors</h3>
  <div id="floor-list"></div>
  <h3>Cross-floor regions</h3>
  <div id="span-list"></div>
  <div id="notes">
    <b>{stats}</b><br><br>
    Floor 0 is the I/O boundary (where data enters or leaves), detected by a
    <i>name heuristic</i> &mdash; not by I/O analysis. A wrong floor 0 shifts
    everything above it. Units whose floor could not be determined are omitted
    from the stack rather than defaulted to floor&nbsp;0.
  </div>
</div>
<script>
const SCENE = {scene_json};

const view = document.getElementById('view');
const renderer = new THREE.WebGLRenderer({{ antialias: true }});
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setClearColor(0x0f0f1a);
view.appendChild(renderer.domElement);
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, 1, 1, 200000);

// The floor planes reuse the 2D view's (x, y) packing, whose extent scales
// with corpus size — so the gap BETWEEN floors has to scale with it too. A
// fixed spacing looks correct on a small graph and collapses into a nearly
// flat stack on a large one (measured: a 69-region corpus spreads to
// ~4900 units wide, against which a fixed 900-unit gap reads as no
// separation at all).
let extent = 1000;
SCENE.regions.forEach(r => {{
  extent = Math.max(extent, Math.abs(r.x) + r.r, Math.abs(r.y) + r.r);
}});
const FLOOR_SPACING = Math.max(extent * 0.55, {_FLOOR_SPACING});
const floorZ = f => f * FLOOR_SPACING;

// ---- build geometry -------------------------------------------------------
const byFloor = new Map();
SCENE.floors.forEach(f => byFloor.set(f, []));

function addToFloor(f, obj) {{
  if (!byFloor.has(f)) byFloor.set(f, []);
  byFloor.get(f).push(obj);
  scene.add(obj);
}}

// Floor planes: a faint grid per occupied floor, so the stack reads as
// discrete layers even where a floor holds only one region.
SCENE.floors.forEach(f => {{
  const grid = new THREE.GridHelper(extent * 2.2, 16, 0x3a3a5e, 0x24243c);
  grid.rotation.x = Math.PI / 2;          // GridHelper is XZ by default; we work in XY
  grid.position.z = floorZ(f);
  grid.material.opacity = 0.28;
  grid.material.transparent = true;
  addToFloor(f, grid);
}});

// Region discs + their member points, on the region's own floor.
SCENE.regions.forEach(r => {{
  const color = new THREE.Color(r.color);
  const disc = new THREE.Mesh(
    new THREE.CircleGeometry(r.r, 48),
    new THREE.MeshBasicMaterial({{ color, transparent: true, opacity: 0.20, side: THREE.DoubleSide }})
  );
  disc.position.set(r.x, r.y, floorZ(r.floor));
  disc.userData = {{ label: r.label, kind: 'region', spans: r.spans, floor: r.floor, n: r.member_count }};
  addToFloor(r.floor, disc);

  const ring = new THREE.LineLoop(
    new THREE.CircleGeometry(r.r, 48),
    new THREE.LineBasicMaterial({{ color, transparent: true, opacity: 0.85 }})
  );
  ring.position.copy(disc.position);
  addToFloor(r.floor, ring);

  // Members as points inside the disc — deterministic scatter mirroring the
  // 2D view's, so a region looks like "the same place" in both views.
  if (r.member_count) {{
    const positions = [];
    for (let i = 0; i < r.member_count; i++) {{
      const a = (Math.sin(i * 12.9898 + r.x) * 43758.5453) % 1;
      const b = (Math.sin(i * 78.233 + r.y) * 43758.5453) % 1;
      const ang = Math.abs(a) * Math.PI * 2;
      const rad = Math.sqrt(Math.abs(b)) * r.r * 0.8;
      positions.push(r.x + rad * Math.cos(ang), r.y + rad * Math.sin(ang), floorZ(r.floor));
    }}
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({{ color, size: 14, transparent: true, opacity: 0.95 }}));
    addToFloor(r.floor, pts);
  }}
}});

// Region-to-region links. A link between different floors is drawn brighter
// and thicker-looking (opacity) than a within-floor one: crossing floors is
// the thing this view exists to surface.
const regionById = new Map(SCENE.regions.map(r => [r.id, r]));
SCENE.links.forEach(l => {{
  const a = regionById.get(l.source), b = regionById.get(l.target);
  if (!a || !b) return;
  const crosses = a.floor !== b.floor;
  const geo = new THREE.BufferGeometry().setFromPoints([
    new THREE.Vector3(a.x, a.y, floorZ(a.floor)),
    new THREE.Vector3(b.x, b.y, floorZ(b.floor)),
  ]);
  const line = new THREE.Line(geo, new THREE.LineBasicMaterial({{
    color: crosses ? 0xf87171 : 0x64748b,
    transparent: true,
    opacity: crosses ? 0.55 : 0.18,
  }}));
  line.userData = {{ crosses, floors: [a.floor, b.floor] }};
  // A cross-floor link belongs to BOTH floors for visibility purposes —
  // register it under the lower one, and hide it when either end hides.
  addToFloor(Math.min(a.floor, b.floor), line);
  line.userData.pairFloors = [a.floor, b.floor];
}});

// ---- camera + inline orbit controls --------------------------------------
const target = new THREE.Vector3(0, 0, floorZ((SCENE.floors[0] + SCENE.floors[SCENE.floors.length - 1]) / 2));
// Start near side-on (pitch toward PI/2) rather than looking down: the
// whole point of this view is the vertical stacking, which a top-down
// default hides completely.
let dist = extent * 3.2, yaw = -0.6, pitch = 1.32, panX = 0, panY = 0;
function updateCamera() {{
  const cy = Math.cos(pitch) * dist;
  camera.position.set(
    target.x + panX + Math.sin(yaw) * Math.sin(pitch) * dist,
    target.y + panY + Math.cos(yaw) * Math.sin(pitch) * dist,
    target.z + cy
  );
  camera.up.set(0, 0, 1);
  camera.lookAt(target.x + panX, target.y + panY, target.z);
}}
let dragging = false, shifted = false, lastX = 0, lastY = 0;
renderer.domElement.addEventListener('mousedown', e => {{
  dragging = true; shifted = e.shiftKey; lastX = e.clientX; lastY = e.clientY;
}});
window.addEventListener('mouseup', () => {{ dragging = false; }});
window.addEventListener('mousemove', e => {{
  if (!dragging) return;
  const dx = e.clientX - lastX, dy = e.clientY - lastY;
  lastX = e.clientX; lastY = e.clientY;
  if (shifted) {{ panX -= dx * dist * 0.0015; panY += dy * dist * 0.0015; }}
  else {{
    yaw -= dx * 0.006;
    pitch = Math.max(0.08, Math.min(Math.PI - 0.08, pitch - dy * 0.006));
  }}
  updateCamera();
}});
renderer.domElement.addEventListener('wheel', e => {{
  e.preventDefault();
  dist = Math.max(extent * 0.25, Math.min(extent * 12, dist * (e.deltaY > 0 ? 1.12 : 0.89)));
  updateCamera();
}}, {{ passive: false }});

function resize() {{
  const w = view.clientWidth, h = view.clientHeight;
  renderer.setSize(w, h);
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
}}
window.addEventListener('resize', resize);
resize();
updateCamera();

// ---- floor visibility toggles --------------------------------------------
const visibleFloors = new Set(SCENE.floors);
function applyVisibility() {{
  byFloor.forEach((objs, f) => {{
    objs.forEach(o => {{
      const pf = o.userData && o.userData.pairFloors;
      // A cross-floor link is only meaningful when BOTH its ends are shown.
      o.visible = pf ? (visibleFloors.has(pf[0]) && visibleFloors.has(pf[1]))
                     : visibleFloors.has(f);
    }});
  }});
}}
const floorList = document.getElementById('floor-list');
SCENE.floors.forEach(f => {{
  const n = SCENE.regions.filter(r => r.floor === f).length;
  const row = document.createElement('label');
  row.className = 'row';
  row.innerHTML = '<input type="checkbox" checked data-floor="' + f + '">'
    + '<span>Floor ' + f + (f === 0 ? ' <span class="muted">(I/O boundary)</span>' : '') + '</span>'
    + '<span class="muted" style="margin-left:auto">' + n + '</span>';
  row.querySelector('input').addEventListener('change', e => {{
    if (e.target.checked) visibleFloors.add(f); else visibleFloors.delete(f);
    applyVisibility();
  }});
  floorList.appendChild(row);
}});

const spanList = document.getElementById('span-list');
const spanning = SCENE.regions.filter(r => r.spans > 0).sort((a, b) => b.spans - a.spans);
if (!spanning.length) {{
  spanList.innerHTML = '<div class="row muted">None &mdash; every unit sits on one floor.</div>';
}}
spanning.slice(0, 20).forEach(r => {{
  const row = document.createElement('div');
  row.className = 'row';
  row.innerHTML = '<span class="swatch" style="background:' + r.color + '"></span>'
    + '<span>' + r.label + '</span>'
    + '<span class="muted" style="margin-left:auto">' + r.min_floor + '&ndash;' + r.max_floor + '</span>';
  spanList.appendChild(row);
}});

// ---- hover readout --------------------------------------------------------
const tip = document.getElementById('tip');
const ray = new THREE.Raycaster();
ray.params.Points = {{ threshold: 18 }};
renderer.domElement.addEventListener('mousemove', e => {{
  const rect = renderer.domElement.getBoundingClientRect();
  const mouse = new THREE.Vector2(
    ((e.clientX - rect.left) / rect.width) * 2 - 1,
    -((e.clientY - rect.top) / rect.height) * 2 + 1
  );
  ray.setFromCamera(mouse, camera);
  const meshes = [];
  byFloor.forEach(objs => objs.forEach(o => {{ if (o.visible && o.userData && o.userData.kind === 'region') meshes.push(o); }}));
  const hit = ray.intersectObjects(meshes)[0];
  if (hit) {{
    const d = hit.object.userData;
    tip.style.display = 'block';
    tip.style.left = (e.clientX - rect.left + 12) + 'px';
    tip.style.top = (e.clientY - rect.top + 10) + 'px';
    tip.textContent = d.label + ' — floor ' + d.floor + ', ' + d.n + ' members'
      + (d.spans ? ' (spans ' + (d.spans + 1) + ' floors)' : '');
  }} else {{
    tip.style.display = 'none';
  }}
}});

applyVisibility();
(function animate() {{
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}})();
</script>
</body>
</html>"""


def write_decouple_3d_html(
    G: nx.Graph,
    plan: dict[str, Any],
    communities: dict[int, list[str]],
    output_path: Path,
) -> "Path | None":
    """Render the data-flow floor stack for `G` to `output_path`.

    Returns the path, or None when no floors could be determined at all
    (no I/O boundary detected anywhere) — in that case NO page is written,
    rather than an empty stack that would imply the analysis ran and found
    a flat system.
    """
    from graphify.data_floor import compute_floors
    from graphify.decouple import _class_cluster_layout, member_ids
    from graphify.exporters.base import COMMUNITY_COLORS

    floors, _reasons = compute_floors(G)
    if not floors:
        return None

    cluster_positions, class_discs = _class_cluster_layout(G)
    if not class_discs:
        return None

    region_members: dict[str, list[str]] = {}
    for region_id in class_discs:
        if region_id.startswith("_module::"):
            source_file = region_id[len("_module::"):]
            region_members[region_id] = [
                nid for nid in cluster_positions
                if G.nodes.get(nid, {}).get("source_file") == source_file
            ]
        else:
            region_members[region_id] = member_ids(G, region_id)

    payload = build_floor_scene(G, class_discs, region_members, floors, COMMUNITY_COLORS)
    n_span = sum(1 for r in payload["regions"] if r["spans"] > 0)
    stats = (
        f"{len(payload['regions'])} units across {len(payload['floors'])} floors; "
        f"{n_span} span more than one"
    )
    html = _page(
        json.dumps(payload).replace("</", "<\\/"),
        _html.escape(str(output_path)),
        _html.escape(stats),
    )
    Path(output_path).write_text(html, encoding="utf-8")
    return Path(output_path)
