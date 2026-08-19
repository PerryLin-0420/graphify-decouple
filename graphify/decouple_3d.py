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
  - A region with no known floor (no boundary reachable from any of its
    members) is never defaulted to floor 0 — it is rendered on its own
    dedicated "unknown" band below the numbered stack instead of being
    dropped outright. Dropping it silently erased every real link to or
    from it too: a well-connected unit whose only calls happen to land on
    other floor-unknown units looked completely disconnected for a reason
    that had nothing to do with its actual connectivity.
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
    cluster_positions: dict[str, dict[str, float]],
    region_members: dict[str, list[str]],
    floors: dict[str, int],
    community_colors: list[str],
) -> dict[str, Any]:
    """Assemble the JSON payload the 3D page renders.

    Each region (class or module — see `decouple._class_cluster_layout`) is
    placed on the floor its own members predominantly occupy, reusing the
    SAME packed (x, y) disc AND the SAME per-member scatter positions the
    2D view uses (`cluster_positions`) — not a fresh layout recomputed in
    JS. A region sits at the exact same place, with its members in the
    exact same arrangement, in both views; only the floor (Z) lift is new
    here. Recomputing the scatter independently in JS (an earlier version
    of this module did, with a simple sine-hash) drifted from the 2D
    layout and produced a visibly regular-looking pattern of its own —
    a second, gratuitous layout algorithm neither view asked for.

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
        # A region with NO determinable floor is NOT skipped — omitting it
        # here doesn't just leave a class off the stack, it silently drops
        # every link to or from it too (measured on a real corpus: 26 of 69
        # regions had no reachable boundary, and their real neighbors — a
        # test file with 37 genuine cross-file calls, a class with 5 —
        # ended up looking completely disconnected in the 3D view, because
        # the ONLY thing they call is something with no known floor). It is
        # rendered on a dedicated `floor: None` band instead — never
        # defaulted to floor 0, still visibly "not measured", but present
        # so its real wiring stays visible.
        if known:
            counts: dict[int, int] = {}
            for f in known:
                counts[f] = counts.get(f, 0) + 1
            dominant = min(counts, key=lambda f: (-counts[f], f))
            min_floor, max_floor, spans = min(known), max(known), max(known) - min(known)
        else:
            dominant = min_floor = max_floor = spans = None
        if region_id.startswith("_module::"):
            label = region_id[len("_module::"):].rsplit("/", 1)[-1]
        else:
            label = str(G.nodes[region_id].get("label", region_id))
        member_points = []
        for m in members:
            if m not in G.nodes:
                continue
            pos = cluster_positions.get(m)
            if pos is None:
                continue
            member_points.append({
                "label": str(G.nodes[m].get("label", m)),
                "floor": floors.get(m, dominant),
                "x": pos["x"], "y": pos["y"],
            })
        regions.append({
            "id": region_id,
            "label": label,
            "x": cx, "y": cy, "r": radius,
            "floor": dominant,
            "min_floor": min_floor, "max_floor": max_floor,
            "spans": spans,
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
    links = _aggregate_region_links(G, node_region, region_ids)

    # Every RAW floor number that has something to actually draw there — a
    # region's own dominant floor, OR any individual member scattered off
    # onto its own (different) floor — not just the region-dominant set.
    # A floor with nothing in either category (e.g. only rationale/test
    # nodes that never resolve to a region member) gets no Z-slot at all,
    # rather than reserving dead space for a floor nothing ever occupies.
    # `None` (a region/member with no determinable floor) is excluded from
    # the NUMBERED list — it gets its own fixed "unknown" band in the JS
    # renderer (see floorZ), not a slot in the ranked stack.
    used_floors = sorted(
        f for f in ({r["floor"] for r in regions} | {m["floor"] for r in regions for m in r["members"]})
        if f is not None
    )
    return {"regions": regions, "links": links, "floors": used_floors, "_node_region": node_region}


def _aggregate_region_links(
    G: nx.Graph,
    node_region: dict[str, str],
    valid_region_ids: set,
) -> list[dict[str, Any]]:
    """Collapse every underlying edge to ONE weighted line per
    (region, region) pair — shared by the "before" link set
    (`build_floor_scene`) and the "after" one (`write_decouple_3d_html`,
    using a node_region map with extracted members redirected onto their
    proposed group), so the two are built the exact same way and only
    differ in which region each moved member is said to belong to.
    """
    pair_counts: dict[tuple[str, str], int] = {}
    for u, v in G.edges():
        ru, rv = node_region.get(u), node_region.get(v)
        if ru is None or rv is None or ru == rv:
            continue
        if ru not in valid_region_ids or rv not in valid_region_ids:
            continue
        pair_counts[(ru, rv)] = pair_counts.get((ru, rv), 0) + 1
    return [
        {"source": a, "target": b, "weight": w}
        for (a, b), w in sorted(pair_counts.items())
    ]


def _page(scene_json: str, title: str, stats: str, has_proposed: bool) -> str:
    decouple_toggle_html = (
        '<label class="row" style="padding:10px 14px;border-bottom:1px solid #2a2a4e">'
        '<input type="checkbox" id="decouple-view-cb">'
        '<span>Preview decoupled view</span>'
        '<span class="muted" style="margin-left:auto">before/after</span>'
        '</label>'
        if has_proposed else ""
    )
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
<div id="view"><div id="tip"></div><div id="hint">drag to rotate &middot; wheel to zoom &middot; shift+drag to pan &middot; click a region to highlight its connections</div></div>
<div id="sidebar">
  {decouple_toggle_html}
  <h3>Floors</h3>
  <div id="floor-list"></div>
  <h3>Links</h3>
  <div class="row"><span class="swatch" style="background:#f87171"></span>
    <span>crosses floors</span></div>
  <div class="row"><span class="swatch" style="background:#7dd3fc"></span>
    <span>same floor (parallel)</span></div>
  <h3>Cross-floor regions</h3>
  <div id="span-list"></div>
  <div id="notes">
    <b>{stats}</b><br><br>
    Floor 0 is the I/O boundary (where data enters or leaves), detected by a
    <i>name heuristic</i> &mdash; not by I/O analysis. A wrong floor 0 shifts
    everything above it. Units with no reachable boundary sit on the
    <b>Unknown</b> band below floor&nbsp;0, never defaulted to floor&nbsp;0 &mdash;
    still shown, and still wired to whatever they really connect to.
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
// Z position uses the floor's DENSE RANK (its index among occupied floors),
// not its raw number — a raw floor 14 sitting right after an occupied
// floor 10 must not leave 3 floor-spacings of dead air for floors 11-13
// nothing was ever drawn on. `floor` fields elsewhere (labels, tooltips,
// checkboxes) keep the raw number; only the Z height is rank-based.
//
// `null` (no boundary reachable from this unit at all) gets its own fixed
// band a FULL extra spacing below floor 0, rather than a rank in the
// numbered stack — it is not "floor -1", and folding it into the ranked
// sequence would misreport an unmeasured unit as sitting one floor below
// the I/O boundary itself. It still needs a real position, though:
// dropping these units instead of giving them a Z at all is what silently
// erased their links in the first place (see build_floor_scene).
const UNKNOWN_Z = -1.5 * FLOOR_SPACING;
const floorZ = f => f === null ? UNKNOWN_Z : (SCENE.floor_rank[f] || 0) * FLOOR_SPACING;

// ---- build geometry -------------------------------------------------------
const byFloor = new Map();
SCENE.floors.forEach(f => byFloor.set(f, []));
byFloor.set(null, []);

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
// The "unknown" band's own grid, drawn ONLY if some region actually needs
// it — a reddish, sparser grid so it reads as "not a real measured floor"
// rather than blending into the numbered stack.
if (SCENE.regions.some(r => r.floor === null)) {{
  const grid = new THREE.GridHelper(extent * 2.2, 8, 0x5e3a3a, 0x241c24);
  grid.rotation.x = Math.PI / 2;
  grid.position.z = UNKNOWN_Z;
  grid.material.opacity = 0.22;
  grid.material.transparent = true;
  addToFloor(null, grid);
}}

// Region discs + their member points, on the region's own floor.
// `r.state` is "before" (today's real classes/modules) or "after" (a
// RECOMMENDED split's proposed group, from _proposed_group_regions) — every
// mesh belonging to a region carries `regionId` so applyVisibility can gate
// on before/after state, not just on which floor checkboxes are on.
SCENE.regions.forEach(r => {{
  const color = new THREE.Color(r.color);
  const isProposed = r.state === 'after';
  const disc = new THREE.Mesh(
    new THREE.CircleGeometry(r.r, 48),
    new THREE.MeshBasicMaterial({{ color, transparent: true, opacity: isProposed ? 0.28 : 0.20, side: THREE.DoubleSide }})
  );
  disc.position.set(r.x, r.y, floorZ(r.floor));
  disc.userData = {{ label: r.label, kind: 'region', spans: r.spans, floor: r.floor, n: r.member_count, regionId: r.id }};
  addToFloor(r.floor, disc);

  // A dashed ring for a proposed group — same "not real yet" signal the 2D
  // view's diamond ring uses — vs. a solid ring for an existing class/module.
  // Built from a plain circumference point list, NOT THREE.CircleGeometry —
  // that geometry's vertex buffer starts with a CENTER vertex (needed for
  // its own triangle-fan fill), and a LineLoop just walks vertices in
  // buffer order, so reusing it for an outline draws spokes from the
  // center to the rim instead of a clean ring (exactly the "sunburst"
  // pattern that made every disc look like it had radiating lines,
  // independent of and on top of the actual region-to-region links).
  const ringPts = [];
  for (let i = 0; i <= 48; i++) {{
    const a = (i / 48) * 2 * Math.PI;
    ringPts.push(new THREE.Vector3(r.r * Math.cos(a), r.r * Math.sin(a), 0));
  }}
  const ringGeo = new THREE.BufferGeometry().setFromPoints(ringPts);
  const ring = isProposed
    ? new THREE.Line(ringGeo, new THREE.LineDashedMaterial({{ color, transparent: true, opacity: 0.9, dashSize: 14, gapSize: 8 }}))
    : new THREE.Line(ringGeo, new THREE.LineBasicMaterial({{ color, transparent: true, opacity: 0.85 }}));
  if (isProposed) ring.computeLineDistances();
  ring.position.copy(disc.position);
  ring.userData = {{ regionId: r.id }};
  addToFloor(r.floor, ring);

  // Members as points inside the disc, at the EXACT (x, y) the 2D view
  // placed them at (see build_floor_scene) — not a separately recomputed
  // scatter, so a region looks like the literal same place, member for
  // member, in both views. A member off its own region's floor (it landed
  // on a different one than the region's dominant floor) is lifted to
  // ITS floor, not squashed onto the region's — that gap IS the
  // cross-floor signal this view exists to show.
  if (r.members && r.members.length) {{
    const positions = [];
    r.members.forEach(m => {{ positions.push(m.x, m.y, floorZ(m.floor)); }});
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({{ color, size: 14, transparent: true, opacity: 0.95 }}));
    pts.userData = {{ regionId: r.id }};
    addToFloor(r.floor, pts);
  }}
}});

// Region-to-region links. Two SEPARATE link sets — SCENE.links ("before":
// today's real wiring) and SCENE.links_after (every extracted member's
// edges redirected onto its proposed group) — each tagged with linkState
// so only the active half of "Preview decoupled view" ever draws.
//
// ALL links draw by default, same as the 2D view (which never hides an
// edge either) — clicking a region does not hide anything, it HIGHLIGHTS
// that region's own links and dims the rest (see updateLinkEmphasis),
// mirroring vis-network's own node-selection emphasis in the 2D view.
const regionById = new Map(SCENE.regions.map(r => [r.id, r]));
const allLinkLines = [];
function addLinkSet(linkList, linkState) {{
  linkList.forEach(l => {{
    const a = regionById.get(l.source), b = regionById.get(l.target);
    if (!a || !b) return;
    const crosses = a.floor !== b.floor;
    // A same-floor link runs between two discs at the SAME Z, so drawn at
    // floorZ exactly it is coplanar with both discs and the floor grid —
    // buried inside the semi-transparent disc surface and invisible, which
    // made a split whose groups are all parallel (no cross-floor wiring at
    // all) look like it had no wiring whatsoever. Lifting it clear of the
    // plane is what makes "these units talk to each other WITHIN one
    // stage" readable at all; cross-floor links are already slanted, so
    // they need no lift.
    const lift = crosses ? 0 : FLOOR_SPACING * 0.04;
    const geo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(a.x, a.y, floorZ(a.floor) + lift),
      new THREE.Vector3(b.x, b.y, floorZ(b.floor) + lift),
    ]);
    const baseOpacity = crosses ? 0.7 : 0.6;
    const line = new THREE.Line(geo, new THREE.LineBasicMaterial({{
      // Red still means "crosses floors" (the risk this view exists to
      // show); same-floor wiring is deliberately a neutral, non-alarming
      // colour — but a legible one, not near-invisible grey.
      color: crosses ? 0xf87171 : 0x7dd3fc,
      transparent: true,
      opacity: baseOpacity,
    }}));
    // A cross-floor link belongs to BOTH floors for visibility purposes —
    // register it under the lower one, and hide it when either end hides.
    // Math.min would silently coerce a `null` (unknown) end to 0 and file
    // the link under floor 0 — if EITHER end is unknown, the link belongs
    // in the unknown band instead, same as an unknown region's own disc.
    line.userData = {{ crosses, pairFloors: [a.floor, b.floor], linkState, source: l.source, target: l.target, baseOpacity }};
    const bucketFloor = (a.floor === null || b.floor === null) ? null : Math.min(a.floor, b.floor);
    addToFloor(bucketFloor, line);
    allLinkLines.push(line);
  }});
}}
addLinkSet(SCENE.links, 'before');
addLinkSet(SCENE.links_after, 'after');
let selectedRegionId = null;

// Selecting a region HIGHLIGHTS its own links (full base opacity) and DIMS
// every other link (a faint 0.04) rather than hiding anything — same
// "everything stays visible, the click just draws attention" behavior the
// 2D view gets for free from vis-network's node selection.
function updateLinkEmphasis() {{
  allLinkLines.forEach(line => {{
    if (selectedRegionId == null) {{
      line.material.opacity = line.userData.baseOpacity;
      return;
    }}
    const touches = line.userData.source === selectedRegionId || line.userData.target === selectedRegionId;
    line.material.opacity = touches ? line.userData.baseOpacity : 0.04;
  }});
}}

// ---- camera + inline orbit controls --------------------------------------
// Rank space is dense (0..length-1) regardless of the raw floor numbers
// involved, so the midpoint rank is just the middle of that range — no
// need to average raw floor numbers (which could land on an unoccupied,
// unranked value).
const target = new THREE.Vector3(0, 0, ((SCENE.floors.length - 1) / 2) * FLOOR_SPACING);
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
let downX = 0, downY = 0;
renderer.domElement.addEventListener('mousedown', e => {{
  dragging = true; shifted = e.shiftKey; lastX = e.clientX; lastY = e.clientY;
  downX = e.clientX; downY = e.clientY;
}});
window.addEventListener('mouseup', e => {{
  dragging = false;
  // A "click" (barely moved between down and up) selects/deselects a
  // region; anything that moved more was a rotate/pan drag, not a click.
  if (Math.abs(e.clientX - downX) < 4 && Math.abs(e.clientY - downY) < 4) {{
    handleRegionClick(e);
  }}
}});
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

// ---- before/after (decoupled preview) toggle ------------------------------
// Mirrors the 2D view's "Preview decoupled view": OFF (default) shows
// today's real classes/modules ("before"); ON hides every class with a
// RECOMMENDED split and shows its proposed groups instead ("after"), each
// on ITS OWN floor — the only way to actually SEE whether a proposed split
// reduces cross-floor spread, rather than assuming a lower risk_before
// number implies it (a community-based grouping optimizes for coupling,
// not floor-coherence, so it is not guaranteed to).
const replacedIds = new Set(SCENE.regions.filter(r => r.state === 'after').map(r => r.replaces));
let showAfter = false;
function regionStateVisible(regionId) {{
  const r = regionById.get(regionId);
  if (!r) return true;
  if (r.state === 'after') return showAfter;
  if (r.state === 'before' && replacedIds.has(r.id)) return !showAfter;
  return true;
}}
const decoupleCb = document.getElementById('decouple-view-cb');
if (decoupleCb) {{
  decoupleCb.addEventListener('change', e => {{
    showAfter = e.target.checked;
    applyVisibility();
  }});
}}

// ---- floor visibility toggles --------------------------------------------
const visibleFloors = new Set(SCENE.floors);
visibleFloors.add(null);  // the "unknown" band starts visible too
function applyVisibility() {{
  byFloor.forEach((objs, f) => {{
    objs.forEach(o => {{
      const pf = o.userData && o.userData.pairFloors;
      if (pf) {{
        // Every link in the active half (before/after) is drawn whenever
        // BOTH its ends are shown — same as the 2D view, which never hides
        // an edge either. Selecting a region does not hide anything; it
        // HIGHLIGHTS that region's own links and DIMS the rest (see
        // updateLinkEmphasis) — the earlier "hide unless selected" answer
        // over-corrected for a rendering bug (a bad ring geometry that
        // made every disc sprout spokes, see the ring-building comment
        // above) that had nothing to do with how many links were drawn.
        const stateOk = (o.userData.linkState === 'after') === showAfter;
        o.visible = stateOk && visibleFloors.has(pf[0]) && visibleFloors.has(pf[1]);
        return;
      }}
      const rid = o.userData && o.userData.regionId;
      o.visible = visibleFloors.has(f) && regionStateVisible(rid);
    }});
  }});
}}
const floorList = document.getElementById('floor-list');
SCENE.floors.forEach(f => {{
  const n = SCENE.regions.filter(r => r.floor === f && r.state !== 'after').length;
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
if (SCENE.regions.some(r => r.floor === null)) {{
  const n = SCENE.regions.filter(r => r.floor === null && r.state !== 'after').length;
  const row = document.createElement('label');
  row.className = 'row';
  row.innerHTML = '<input type="checkbox" checked data-floor="unknown">'
    + '<span>Unknown <span class="muted">(no boundary reachable)</span></span>'
    + '<span class="muted" style="margin-left:auto">' + n + '</span>';
  row.querySelector('input').addEventListener('change', e => {{
    if (e.target.checked) visibleFloors.add(null); else visibleFloors.delete(null);
    applyVisibility();
  }});
  floorList.appendChild(row);
}}

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
    const floorText = d.floor === null ? 'unknown (no boundary reachable)' : d.floor;
    tip.textContent = d.label + ' — floor ' + floorText + ', ' + d.n + ' members'
      + (d.spans ? ' (spans ' + (d.spans + 1) + ' floors)' : '');
  }} else {{
    tip.style.display = 'none';
  }}
}});

// Click a region disc to reveal ONLY its own links (see the link-drawing
// comment above for why: an always-on link set is unreadable for any
// genuine hub, not just busy). Click the same region again, or empty
// space, to clear the selection back to "no links shown".
function handleRegionClick(e) {{
  const rect = renderer.domElement.getBoundingClientRect();
  const mouse = new THREE.Vector2(
    ((e.clientX - rect.left) / rect.width) * 2 - 1,
    -((e.clientY - rect.top) / rect.height) * 2 + 1
  );
  ray.setFromCamera(mouse, camera);
  const meshes = [];
  byFloor.forEach(objs => objs.forEach(o => {{ if (o.visible && o.userData && o.userData.kind === 'region') meshes.push(o); }}));
  const hit = ray.intersectObjects(meshes)[0];
  const hitId = hit ? hit.object.userData.regionId : null;
  selectedRegionId = (hitId && hitId !== selectedRegionId) ? hitId : null;
  updateLinkEmphasis();
}}

applyVisibility();
updateLinkEmphasis();
(function animate() {{
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}})();
</script>
</body>
</html>"""


def _proposed_group_regions(
    G: nx.Graph,
    plan: dict[str, Any],
    class_discs: dict[str, tuple[float, float, float]],
    cluster_positions: dict[str, dict[str, float]],
    floors: dict[str, int],
) -> list[dict[str, Any]]:
    """The "after" half of the before/after comparison: one region per
    RECOMMENDED split's proposed group (`risk.recommendation == "split"`
    only — same gate `build_augmented_graph` uses, a discouraged candidate
    already has its answer as a number and gets nothing extra drawn), each
    placed on ITS OWN dominant floor rather than the original class's.

    This is the entire point of a floor view for decouple: `risk_before`'s
    cross-floor term (see `data_floor.cross_floor_risk`) says a class
    scores worse for straddling several floors, but a number alone doesn't
    show whether the PROPOSED split actually fixes that — a community-based
    grouping optimizes for coupling, not floor-coherence, so a "recommended"
    split could still straddle just as many floors post-split. Showing each
    new group on its own real floor makes that visible instead of assumed.

    The floor numbers (`floor`/`min_floor`/`max_floor`/`spans`) are READ
    from `g["floor_profile"]` — attached once, by `decouple_plan`, and also
    what `split_risk_score` scores against (see that function's docstring)
    — never recomputed here. `graphify decouple --3d` visualizes the plan
    decouple_plan already built; it does not run its own floor analysis. A
    group with no `floor_profile` (no boundary reachable, or none of its
    members had a determinable floor) is skipped, same as decouple_plan's
    own skip — omitted, not defaulted to floor 0.

    Positioned in a small ring around the ORIGINAL class's own disc anchor
    (not `_class_cluster_layout`'s packing — these are hypothetical nodes
    it never saw), radius scaled to the number of sibling groups so they
    fan out rather than stack on one point. Members inside each proposed
    disc get a FRESH organic scatter (`_stable_unit_pair`, the same
    function `_class_cluster_layout` uses for real classes) computed
    around the NEW group center — not their old (x, y) from the original
    class's disc, which would put them outside the new, smaller disc
    entirely and made the "after" state look regular/clipped rather than
    matching the "before" state's own organic-scatter style.
    """
    import math

    from graphify.decouple import _class_disc_radius, _stable_unit_pair

    regions: list[dict[str, Any]] = []
    member_to_region: dict[str, str] = {}
    for entry in plan.get("god_nodes", []):
        if entry.get("classification") != "god_object":
            continue
        risk = entry.get("risk", {})
        if risk.get("recommendation") != "split":
            continue
        god_id = entry["id"]
        orig_disc = class_discs.get(god_id)
        if orig_disc is None:
            continue
        ax, ay, aradius = orig_disc
        non_residual = [g for g in entry.get("proposed_groups", []) if g.get("community_id") is not None]
        n = len(non_residual)
        if n == 0:
            continue
        for gi, g in enumerate(non_residual):
            # A group with no determinable floor (fp is None) is still
            # rendered — on the same `floor: None` "unknown" band
            # build_floor_scene uses — rather than dropped outright, for
            # the identical reason: dropping it would silently erase every
            # link to or from it too, not just its own disc.
            fp = g.get("floor_profile")
            members = g.get("members", [])

            angle = 2 * math.pi * gi / n
            gx = ax + aradius * 0.7 * math.cos(angle)
            gy = ay + aradius * 0.7 * math.sin(angle)
            gradius = _class_disc_radius(len(members))
            region_id = f"_proposed3d_{god_id}_{gi}"

            member_points = []
            for m in members:
                if m not in G.nodes or m not in floors:
                    continue
                angle_unit, radius_unit = _stable_unit_pair(f"{region_id}::{m}")
                m_angle = angle_unit * 2 * math.pi
                r = math.sqrt(radius_unit) * gradius * 0.82
                member_points.append({
                    "label": str(G.nodes[m].get("label", m)),
                    "floor": floors[m],
                    "x": gx + r * math.cos(m_angle), "y": gy + r * math.sin(m_angle),
                })

            regions.append({
                "id": region_id,
                "label": g.get("name", f"Group {gi}"),
                "x": gx, "y": gy, "r": gradius,
                "floor": fp["floor"] if fp else None,
                "min_floor": fp["min_floor"] if fp else None,
                "max_floor": fp["max_floor"] if fp else None,
                "spans": fp["floor_span"] if fp else None,
                "color": "#22c55e",  # same green family as the 2D "proposed split" diamond
                "member_count": len(members),
                "members": member_points,
                "state": "after",
                "replaces": god_id,
            })
            for m in members:
                member_to_region[m] = region_id
    return regions, member_to_region


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
    from graphify.decouple import _class_cluster_layout
    from graphify.exporters.base import COMMUNITY_COLORS

    floors, _reasons = compute_floors(G)
    if not floors:
        return None

    # region_members is _class_cluster_layout's OWN authoritative membership
    # per region — used as-is, never re-derived by filtering on
    # source_file (a class defined in the same file as a module region's
    # free functions would otherwise get pulled into that region too, even
    # though its members already belong to, and are positioned by, their
    # own class's region — this broke exactly that way before the fix).
    cluster_positions, class_discs, region_members = _class_cluster_layout(G)
    if not class_discs:
        return None

    payload = build_floor_scene(G, class_discs, cluster_positions, region_members, floors, COMMUNITY_COLORS)
    for r in payload["regions"]:
        r["state"] = "before"
    node_region_before = payload.pop("_node_region")

    after_regions, member_to_after_region = _proposed_group_regions(G, plan, class_discs, cluster_positions, floors)
    payload["regions"].extend(after_regions)
    # Recomputed over ALL regions (before + after), same rule as
    # build_floor_scene: a floor gets a Z-slot only if something (a
    # region's own floor, or one of its members') actually lands there.
    # None (unknown floor) is excluded from the numbered list — see
    # build_floor_scene for why it gets a fixed band instead of a rank.
    payload["floors"] = sorted(
        f for f in (
            {r["floor"] for r in payload["regions"]}
            | {m["floor"] for r in payload["regions"] for m in r["members"]}
        )
        if f is not None
    )
    # Dense rank for the Z axis — collapses gaps between occupied floors
    # (e.g. raw floors {0,1,...,6,8,10,14,...} become ranks 0,1,...,6,7,8,9,...)
    # so an unoccupied raw floor number no longer stretches the stack with
    # empty space nothing was ever going to be drawn in.
    payload["floor_rank"] = {f: i for i, f in enumerate(payload["floors"])}

    # "After" links: the SAME edges, the SAME aggregation
    # (_aggregate_region_links), but every extracted member now resolves to
    # its proposed group instead of the class it came from — otherwise
    # toggling "Preview decoupled view" moved the DISCS but left the wires
    # drawn as if nothing had been extracted, which is exactly what made the
    # split's actual coupling shape invisible in the toggle before this.
    if after_regions:
        node_region_after = dict(node_region_before)
        node_region_after.update(member_to_after_region)
        replaced_ids = {r["replaces"] for r in after_regions}
        all_ids = {r["id"] for r in payload["regions"]}
        valid_after_ids = all_ids - replaced_ids
        payload["links_after"] = _aggregate_region_links(G, node_region_after, valid_after_ids)
    else:
        payload["links_after"] = payload["links"]

    n_span = sum(1 for r in payload["regions"] if r["state"] == "before" and (r["spans"] or 0) > 0)
    n_proposed = len(after_regions)
    stats = (
        f"{len(payload['regions']) - n_proposed} units across {len(payload['floors'])} floors; "
        f"{n_span} span more than one"
        + (f"; {n_proposed} proposed split groups available in \"Preview decoupled view\"" if n_proposed else "")
    )
    html = _page(
        json.dumps(payload).replace("</", "<\\/"),
        _html.escape(str(output_path)),
        _html.escape(stats),
        bool(after_regions),
    )
    Path(output_path).write_text(html, encoding="utf-8")
    return Path(output_path)
