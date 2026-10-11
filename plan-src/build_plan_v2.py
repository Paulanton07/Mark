#!/usr/bin/env python3
# The Offcut Feeder - plan v2. Fixes from Paul's read:
#  - end view read as a bird house -> now a SECTION B-B through the tray, showing the open sides
#  - side view hid the roof -> roof is now a broad band eave-to-ridge; gable posts stop under it
#  - mesh floor insert added (wet seed drains and airs)
# Units: mm.
import math

W, L, T, WALL = 145, 340, 18, 50
PITCH = 25
SLOPE = math.tan(math.radians(PITCH))
OH_EAVE, OH_GABLE = 15, 20
EAVE = 110                                  # roof underside at the eaves
RIDGE = EAVE + (W / 2.0) * SLOPE            # roof underside at the ridge
ROOF_TOP = RIDGE + T
ROOF_LOW = RIDGE - (W / 2.0 + OH_EAVE) * SLOPE
ROOF_L = L + 2 * OH_GABLE
ROD_Z = 133
MESH_Z = T + 6
PANEL_W = 100                               # roof panel width along slope

S = 1.05
M = 22
TOP = 22


def side_geo():
    sx = lambda l: M + (l + OH_GABLE) * S
    sy = lambda z: TOP + (ROOF_TOP - z) * S
    return sx, sy


def end_geo():
    ex = lambda d: M + (d + OH_EAVE) * S
    ey = lambda z: TOP + (ROOF_TOP - z) * S
    return ex, ey


# ---------------- SIDE ELEVATION (long side) ----------------
sx, sy = side_geo()
g = []
g.append(f'<line x1="{sx(-OH_GABLE)-16:.1f}" y1="{sy(0):.1f}" x2="{sx(L+OH_GABLE)+16:.1f}" y2="{sy(0):.1f}" class="ground"/>')

# far long wall (seen through the open side): thin line at wall top
g.append(f'<line x1="{sx(T):.1f}" y1="{sy(WALL):.1f}" x2="{sx(L-T):.1f}" y2="{sy(WALL):.1f}" class="hidden"/>')
# tray floor
g.append(f'<rect x="{sx(0):.1f}" y="{sy(T):.1f}" width="{L*S:.1f}" height="{T*S:.1f}" class="part"/>')
# end-wall silhouettes, hidden under the roof
g.append(f'<rect x="{sx(0):.1f}" y="{sy(RIDGE):.1f}" width="{T*S:.1f}" height="{RIDGE*S:.1f}" class="hidden"/>')
g.append(f'<rect x="{sx(L-T):.1f}" y="{sy(RIDGE):.1f}" width="{T*S:.1f}" height="{RIDGE*S:.1f}" class="hidden"/>')
# near long wall (in front)
g.append(f'<rect x="{sx(T):.1f}" y="{sy(WALL):.1f}" width="{(L-2*T)*S:.1f}" height="{WALL*S:.1f}" class="part fill"/>')
# roof: near slope face projects as a band from the eave to the ridge
g.append(f'<rect x="{sx(-OH_GABLE):.1f}" y="{sy(ROOF_TOP):.1f}" width="{ROOF_L*S:.1f}" height="{(ROOF_TOP-ROOF_LOW)*S:.1f}" class="rooffill"/>')
g.append(f'<text x="{sx(L*0.72):.1f}" y="{(sy(ROOF_TOP)+sy(ROOF_LOW))/2+3:.1f}" class="pitch">roof slope 25&deg; (see B&ndash;B)</text>')
g.append(f'<line x1="{sx(-OH_GABLE):.1f}" y1="{sy(RIDGE):.1f}" x2="{sx(L+OH_GABLE):.1f}" y2="{sy(RIDGE):.1f}" class="line2"/>')
g.append(f'<line x1="{sx(-OH_GABLE):.1f}" y1="{sy(ROOF_LOW):.1f}" x2="{sx(L+OH_GABLE):.1f}" y2="{sy(ROOF_LOW):.1f}" class="line2"/>')
# rod + mesh, hidden inside
g.append(f'<line x1="{sx(T):.1f}" y1="{sy(ROD_Z):.1f}" x2="{sx(L-T):.1f}" y2="{sy(ROD_Z):.1f}" class="roddash"/>')
g.append(f'<text x="{sx(L/2):.1f}" y="{sy(ROD_Z)+11:.1f}" class="rodlbl">M6 rod &rarr; the one joint</text>')
g.append(f'<line x1="{sx(T):.1f}" y1="{sy(MESH_Z):.1f}" x2="{sx(L-T):.1f}" y2="{sy(MESH_Z):.1f}" class="mesh"/>')
# open feeding gap arrow
g.append(f'<line x1="{sx(60):.1f}" y1="{sy(WALL):.1f}" x2="{sx(60):.1f}" y2="{sy(ROOF_LOW):.1f}" class="openarr"/>')
g.append(f'<text x="{sx(64):.1f}" y="{sy(ROOF_LOW)-7:.1f}" class="opentxt">open {ROOF_LOW-WALL:.0f}</text>')
# dims
g.append(f'<line x1="{sx(0):.1f}" y1="{sy(0)+30:.1f}" x2="{sx(L):.1f}" y2="{sy(0)+30:.1f}" class="dim"/>'
         f'<line x1="{sx(0):.1f}" y1="{sy(0)+26:.1f}" x2="{sx(0):.1f}" y2="{sy(0)+34:.1f}" class="dim"/>'
         f'<line x1="{sx(L):.1f}" y1="{sy(0)+26:.1f}" x2="{sx(L):.1f}" y2="{sy(0)+34:.1f}" class="dim"/>'
         f'<text x="{(sx(0)+sx(L))/2:.1f}" y="{sy(0)+30:.1f}" class="dimtxt">{L}</text>')
g.append(f'<line x1="{sx(-OH_GABLE):.1f}" y1="{sy(0)+50:.1f}" x2="{sx(L+OH_GABLE):.1f}" y2="{sy(0)+50:.1f}" class="dim"/>'
         f'<line x1="{sx(-OH_GABLE):.1f}" y1="{sy(0)+46:.1f}" x2="{sx(-OH_GABLE):.1f}" y2="{sy(0)+54:.1f}" class="dim"/>'
         f'<line x1="{sx(L+OH_GABLE):.1f}" y1="{sy(0)+46:.1f}" x2="{sx(L+OH_GABLE):.1f}" y2="{sy(0)+54:.1f}" class="dim"/>'
         f'<text x="{(sx(-OH_GABLE)+sx(L+OH_GABLE))/2:.1f}" y="{sy(0)+50:.1f}" class="dimtxt">{ROOF_L}</text>')
# vertical dims right
g.append(f'<line x1="{sx(L+OH_GABLE)+22:.1f}" y1="{sy(0):.1f}" x2="{sx(L+OH_GABLE)+22:.1f}" y2="{sy(WALL):.1f}" class="dim"/>'
         f'<text x="{sx(L+OH_GABLE)+28:.1f}" y="{(sy(0)+sy(WALL))/2:.1f}" class="dimtxt v">wall {WALL}</text>')
g.append(f'<line x1="{sx(L+OH_GABLE)+22:.1f}" y1="{sy(0):.1f}" x2="{sx(L+OH_GABLE)+22:.1f}" y2="{sy(ROOF_TOP):.1f}" class="dim"/>'
         f'<text x="{sx(L+OH_GABLE)+28:.1f}" y="{(sy(0)+sy(ROOF_TOP))/2:.1f}" class="dimtxt v">{ROOF_TOP:.0f}</text>')
g.append(f'<line x1="{sx(L/2):.1f}" y1="{sy(ROOF_TOP)-6:.1f}" x2="{sx(L/2):.1f}" y2="{sy(0):.1f}" class="cutline"/>')
g.append(f'<text x="{sx(L/2):.1f}" y="{sy(ROOF_TOP)-12:.1f}" class="cutlbl">B</text>')
g.append(f'<text x="{sx(L/2):.1f}" y="{sy(0)+16:.1f}" class="cutlbl">B</text>')
for yy in (sy(ROOF_TOP)-8, sy(0)+4):
    g.append(f'<polygon points="{sx(L/2)-11:.1f},{yy:.1f} {sx(L/2)-3:.1f},{yy-4:.1f} {sx(L/2)-3:.1f},{yy+4:.1f}" class="cutarr"/>')
side_svg = "\n".join(g)
side_w = sx(L + OH_GABLE) + 62
side_h = sy(0) + 62

# ---------------- END SECTION B-B ----------------
ex, ey = end_geo()
e = []
e.append(f'<line x1="{ex(-OH_EAVE)-14:.1f}" y1="{ey(0):.1f}" x2="{ex(W+OH_EAVE)+14:.1f}" y2="{ey(0):.1f}" class="ground"/>')
# far gable wall, beyond the cut, light outline
e.append(f'<polygon points="{ex(0):.1f},{ey(0):.1f} {ex(W):.1f},{ey(0):.1f} {ex(W):.1f},{ey(EAVE):.1f} {ex(W/2):.1f},{ey(RIDGE):.1f} {ex(0):.1f},{ey(EAVE):.1f}" class="faroutline"/>')
# tray floor in section
e.append(f'<rect x="{ex(0):.1f}" y="{ey(T):.1f}" width="{W*S:.1f}" height="{T*S:.1f}" class="part"/>')
# mesh over the floor
e.append(f'<line x1="{ex(T):.1f}" y1="{ey(MESH_Z):.1f}" x2="{ex(W-T):.1f}" y2="{ey(MESH_Z):.1f}" class="mesh"/>')
# cut long walls
e.append(f'<rect x="{ex(0):.1f}" y="{ey(WALL):.1f}" width="{T*S:.1f}" height="{WALL*S:.1f}" class="part fill"/>')
e.append(f'<rect x="{ex(W-T):.1f}" y="{ey(WALL):.1f}" width="{T*S:.1f}" height="{WALL*S:.1f}" class="part fill"/>')
# roof panels in section (two slopes)
for sgn in (-1, 1):
    x0 = ex(-OH_EAVE) if sgn < 0 else ex(W + OH_EAVE)
    x1 = ex(W / 2.0)
    e.append(f'<polygon points="{x0:.1f},{ey(ROOF_LOW):.1f} {x1:.1f},{ey(RIDGE):.1f} {x1:.1f},{ey(ROOF_TOP):.1f} {x0:.1f},{ey(ROOF_LOW+T):.1f}" class="part fill"/>')
# ridge beam in section
e.append(f'<rect x="{ex(W/2-10):.1f}" y="{ey(RIDGE):.1f}" width="{20*S:.1f}" height="{20*S:.1f}" class="part fill"/>')
# rod dot
e.append(f'<circle cx="{ex(W/2):.1f}" cy="{ey(ROD_Z):.1f}" r="3.4" class="roddot"/>')
# open gaps
for d in (0, W):
    x = ex(d)
    if d == 0:
        e.append(f'<line x1="{x-16:.1f}" y1="{ey(WALL):.1f}" x2="{x-16:.1f}" y2="{ey(ROOF_LOW):.1f}" class="openarr"/>')
    else:
        e.append(f'<line x1="{x+16:.1f}" y1="{ey(WALL):.1f}" x2="{x+16:.1f}" y2="{ey(ROOF_LOW):.1f}" class="openarr"/>')
e.append(f'<text x="{ex(W/2):.1f}" y="{ey(WALL)+24:.1f}" class="opentxt2">open both long sides</text>')
# dims
e.append(f'<line x1="{ex(0):.1f}" y1="{ey(0)+30:.1f}" x2="{ex(W):.1f}" y2="{ey(0)+30:.1f}" class="dim"/>'
         f'<line x1="{ex(0):.1f}" y1="{ey(0)+26:.1f}" x2="{ex(0):.1f}" y2="{ey(0)+34:.1f}" class="dim"/>'
         f'<line x1="{ex(W):.1f}" y1="{ey(0)+26:.1f}" x2="{ex(W):.1f}" y2="{ey(0)+34:.1f}" class="dim"/>'
         f'<text x="{ex(W/2):.1f}" y="{ey(0)+30:.1f}" class="dimtxt">{W}</text>')
e.append(f'<line x1="{ex(-OH_EAVE):.1f}" y1="{ey(0)+50:.1f}" x2="{ex(W+OH_EAVE):.1f}" y2="{ey(0)+50:.1f}" class="dim"/>'
         f'<text x="{ex(W/2):.1f}" y="{ey(0)+50:.1f}" class="dimtxt">{W+2*OH_EAVE}</text>')
end_svg = "\n".join(e)
end_w = ex(W + OH_EAVE) + M
end_h = ey(0) + 62

# ---------------- TRAY DETAIL ----------------
# small zoom: floor, mesh, a long wall, hatch
d = []
dx = lambda mm: 20 + mm * 2.1
dy = lambda mm: 150 - mm * 2.1
d.append(f'<rect x="{dx(0):.1f}" y="{dy(T):.1f}" width="{dx(90)-dx(0):.1f}" height="{T*2.1:.1f}" class="part"/>')
d.append(f'<line x1="{dx(0):.1f}" y1="{dy(MESH_Z):.1f}" x2="{dx(90):.1f}" y2="{dy(MESH_Z):.1f}" class="mesh"/>')
for i in range(0, 90, 6):
    d.append(f'<line x1="{dx(i):.1f}" y1="{dy(MESH_Z-2):.1f}" x2="{dx(i+3):.1f}" y2="{dy(MESH_Z+2):.1f}" class="meshhatch"/>')
d.append(f'<rect x="{dx(0)-9:.1f}" y="{dy(WALL):.1f}" width="{9:.1f}" height="{WALL*2.1:.1f}" class="part fill"/>')
d.append(f'<text x="{dx(45):.1f}" y="{dy(MESH_Z)+26:.1f}" class="det">stainless 6 mm mesh</text>')
d.append(f'<text x="{dx(45):.1f}" y="{dy(MESH_Z)+38:.1f}" class="det2">lifts out to clean</text>')
detail_svg = "\n".join(d)
det_w = dx(90) + 40
det_h = 190

# ---------------- page ----------------
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:9mm; }}
h1 {{ font-size: 19px; margin:0 0 1px 0; }}
h2 {{ font-size: 10px; text-transform:uppercase; letter-spacing:1px; color:#6b6b6b; margin:10px 0 3px 0; border-bottom:1px solid #d8d8d8; padding-bottom:2px;}}
.sub {{ font-size:10px; color:#555; margin-bottom:5px;}}
.wrap {{ display:flex; gap:16px; align-items:flex-start; }}
.views {{ flex: 0 0 500px; }}
.side {{ flex: 1 1 auto; font-size:10px; }}
svg {{ display:block; }}
.part {{ fill:#efe8dc; stroke:#2a2a2a; stroke-width:1; }}
.faroutline {{ fill:none; stroke:#9a9a9a; stroke-width:0.9; stroke-dasharray:3 2; }}
.fill2 {{ fill:#dcd2c2; stroke:#2a2a2a; stroke-width:1; }}
.line2 {{ stroke:#2a2a2a; stroke-width:0.8; fill:none;}}
.hidden {{ fill:none; stroke:#9a9a9a; stroke-width:0.9; stroke-dasharray:3 2; }}
.hole {{ fill:#fff; stroke:#2a2a2a; stroke-width:0.9;}}
.mesh {{ stroke:#1f6f4a; stroke-width:2.2; fill:none; }}
.meshhatch {{ stroke:#1f6f4a; stroke-width:1; }}
.roddash {{ stroke:#b23b2e; stroke-width:2.0; stroke-dasharray:5 3; }}
.rooffill {{ fill:#f6f1e7; stroke:#2a2a2a; stroke-width:1; }}
.pitch {{ fill:#555; font-size:8.5px; text-anchor:middle; }}
.rodlbl {{ fill:#8a1f14; font-size:8px; text-anchor:middle; }}
.cutline {{ stroke:#1f6f4a; stroke-width:0.9; stroke-dasharray:7 3 1 3; }}
.cutlbl {{ fill:#1f6f4a; font-size:9px; text-anchor:middle; font-weight:600; }}
.cutarr {{ fill:#1f6f4a; }}
.roddot {{ fill:#b23b2e; stroke:#7d2118; stroke-width:1; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.6; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.7; }}
.dimtxt {{ fill:#333; font-size:9px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:3px; }}
.dimtxt.v {{ text-anchor:start; }}
.vt {{ text-anchor:start; font-size:9px; fill:#4a4a4a; letter-spacing:0.5px; }}
.openarr {{ stroke:#8a1f14; stroke-width:1; }}
.opentxt {{ fill:#8a1f14; font-size:8px; text-anchor:end; }}
.opentxt2 {{ fill:#8a1f14; font-size:8.5px; text-anchor:middle; }}
.det {{ fill:#333; font-size:8.5px; text-anchor:middle; }}
.det2 {{ fill:#777; font-size:8px; text-anchor:middle; }}
.cap {{ font-size:9px; color:#666; margin:1px 0 6px 0; }}
table {{ width:100%; border-collapse:collapse; font-size:9.5px; }}
th,td {{ text-align:left; padding:2px 3px; border-bottom:1px solid #e4e4e4; }}
th {{ color:#6b6b6b; font-weight:600; text-transform:uppercase; font-size:8px; letter-spacing:0.4px;}}
.q {{ font-size:9.5px; background:#fff6e8; border:1px solid #e8d3a8; padding:5px 7px; margin-top:7px;}}
.q2 {{ font-size:9.5px; background:#eef6f0; border:1px solid #bfe0cb; padding:5px 7px; margin-top:7px;}}
.tag {{ display:inline-block; font-size:8.5px; border:1px solid #999; border-radius:8px; padding:0 5px; margin-left:6px; color:#555;}}
</style></head><body>
<h1>The Offcut Feeder <span class="tag">Mark &middot; piece 01 &middot; v2</span></h1>
<div class="sub">Hanging covered platform feeder, untreated Baltic pine. No glue. One tool-free joint. Roof lifts off, mesh tray lifts out. Dimensions in mm.</div>
<div class="wrap">
  <div class="views">
    <svg width="{side_w:.0f}" height="{side_h:.0f}" viewBox="0 0 {side_w:.0f} {side_h:.0f}">
      {side_svg}
      <text x="{M}" y="13" class="vt">SIDE ELEVATION</text>
    </svg>
    <div class="cap">Roof pitch 25&deg;. Near slope shown; eave {ROOF_LOW:.0f}, ridge {ROOF_TOP:.0f}. Feeding gap {ROOF_LOW-WALL:.0f} above the walls.</div>
    <div style="display:flex; gap:14px; align-items:flex-start;">
      <div>
        <svg width="{end_w:.0f}" height="{end_h:.0f}" viewBox="0 0 {end_w:.0f} {end_h:.0f}">
          {end_svg}
          <text x="{M}" y="13" class="vt">END SECTION B&ndash;B</text>
        </svg>
        <div class="cap" style="width:{end_w:.0f}px;">Cut mid-tray, looking at an end. Gable beyond the cut shown dashed.</div>
      </div>
      <div>
        <svg width="{det_w:.0f}" height="{det_h:.0f}" viewBox="0 0 {det_w:.0f} {det_h:.0f}">
          {detail_svg}
          <text x="20" y="13" class="vt">TRAY DETAIL</text>
        </svg>
        <div class="cap" style="width:{det_w:.0f}px;">Mesh sits on the floor, seed on top.</div>
      </div>
    </div>
  </div>
  <div class="side">
    <h2>Cut list</h2>
    <table>
      <tr><th>Part</th><th>Qty</th><th>L</th><th>W</th><th>T</th></tr>
      <tr><td>End wall / gable</td><td>2</td><td>145</td><td>144</td><td>18</td></tr>
      <tr><td>Tray floor</td><td>1</td><td>340</td><td>145</td><td>18</td></tr>
      <tr><td>Tray long wall</td><td>2</td><td>304</td><td>50</td><td>18</td></tr>
      <tr><td>Roof panel</td><td>2</td><td>380</td><td>100</td><td>18</td></tr>
      <tr><td>Ridge beam (clamp)</td><td>1</td><td>304</td><td>20</td><td>20</td></tr>
    </table>
    <div class="sub" style="margin-top:3px;">End-wall top edge cut to the 25&deg; pitch: {EAVE} at the eaves, {RIDGE:.0f} at the ridge. Roof panels mitred at the ridge.</div>

    <h2>Material</h2>
    <div><b>Untreated</b> Baltic pine, 38 &times; 150 &times; 900, resawn to two 18&nbsp;mm boards. Nothing treated touches this.</div>

    <h2>Hardware &amp; finish</h2>
    <div>M6 stainless threaded rod &times; 350, 2 wing nuts, 2 washers &mdash; the one joint.<br>
    Stainless screws 4&times;40, approx 22.<br>
    Woodoc sealer, all faces, 2 coats. Tray interior and roof underside left bare.</div>

    <h2>Water &amp; service</h2>
    <div>Roof overhang {OH_EAVE} eaves, {OH_GABLE} gables. 4 &times; &Oslash;6 drain holes through the floor. Mesh insert keeps seed off the wet floor so it dries and airs.<br>
    Rod out &rarr; roof off &rarr; mesh and tray lift out. No tools.</div>

    <h2>Hanging</h2>
    <div>Cord over the ridge cap, or two &Oslash;6 eyes in the end walls at the eaves. ~2&nbsp;m up, ~3&nbsp;m clear of trees.</div>

    <h2>Basis</h2>
    <div style="font-size:9px;">Proportions after published platform-feeder plans (Cabin Life covered seed tray; Birdwatching-Bliss long tray). Squirrel clearance 6&ndash;8&nbsp;ft from jump-offs, 5&ndash;6&nbsp;ft up (Cabin Life). Untreated wood for bird contact surfaces; treated avoided (NestWatch nest-box guidance; NPIC on CCA leaching).</div>

    <div class="q"><b>Set:</b> untreated Baltic pine (Paul's call). The treated truss offcut is out &mdash; it leaches on a food surface in the weather. Untreated pine needs re-oiling yearly.</div>
    <div class="q2"><b>v2 change:</b> end view redrawn as a section so the open sides read; roof now drawn full from eave to ridge. Mesh insert added on Paul's note &mdash; wet seed drains and dries instead of sitting in a puddle.</div>
  </div>
</div>
</body></html>'''

open("/workspace/plan/offcut-feeder-plan-v2.html", "w").write(html)
print("wrote html", len(html))
print(f"EAVE={EAVE} RIDGE={RIDGE:.1f} ROOF_TOP={ROOF_TOP:.1f} ROOF_LOW={ROOF_LOW:.1f} gap={ROOF_LOW-WALL:.1f}")
print(f"side {side_w:.0f}x{side_h:.0f} end {end_w:.0f}x{end_h:.0f} det {det_w:.0f}x{det_h:.0f}")
