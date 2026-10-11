#!/usr/bin/env python3
# The Offcut Bee Block - plan v1. Piece 02.
# Solitary-bee nesting block from one untreated hardwood offcut. No glue.
# Grounded specs (tavily 2026-10-05): untreated hardwood; closed-end tunnels;
# diameters 2.3-9.5 mm varied (mason bees 7.5-9.5); depth ~150-180 mm; holes
# smooth/splinter-free; angle holes slightly UP so rain runs out; roof overhang;
# mount 1.2-1.8 m, morning-sun face.
# Sources: RSPB bee hotel; borderfreebees Bee-Hotel-Specs; NorCal Nectar mason guide; NC State Extension.
import math

W, H, D = 150, 110, 175          # block width, height, depth (mm)
BACK = 25                        # closed back behind the tunnel ends
TUN_D = 150                      # tunnel depth
TILT = 5                         # tunnel rises 5 deg going in
ROOF_PITCH = 20
OV_FRONT, OV_BACK, OV_SIDE = 55, 25, 15
T = 18                           # roof panel thickness
CLEAT = 20                       # back mounting cleat thickness

RISE = (D + OV_FRONT + OV_BACK) / 2.0 * math.tan(math.radians(ROOF_PITCH))
ROOF_SPAN = D + OV_FRONT + OV_BACK
PANEL_L = math.hypot(ROOF_SPAN / 2.0, RISE)
PANEL_W = W + 2 * OV_SIDE

# hole layout on the 150 x 110 front face: 7 cols x 4 rows, varied dia
COLS = [18, 37, 56, 75, 94, 113, 132]
ROWS = [20, 42, 64, 86]
DIAS = [
    [6.0, 8.0, 5.0, 9.0, 4.0, 7.0, 6.0],
    [9.5, 4.0, 6.0, 3.0, 8.0, 5.0, 9.0],
    [3.0, 6.0, 7.5, 5.0, 9.5, 4.0, 6.0],
    [8.0, 5.0, 3.0, 6.0, 4.0, 7.5, 8.0],
]
N_HOLES = sum(len(r) for r in DIAS)

S = 1.35


def side_geo():
    # side section: x = depth from front (left) to back (right); y = height
    sx = lambda d: 84 + d * S
    sy = lambda z: 240 - z * S
    return sx, sy


# ---------------- SIDE SECTION A-A (through a column of tunnels) ----------------
sx, sy = side_geo()
g = []
g.append(f'<line x1="{sx(-10):.1f}" y1="{sy(0):.1f}" x2="{sx(D+10):.1f}" y2="{sy(0):.1f}" class="ground"/>')
# block body in section
g.append(f'<rect x="{sx(0):.1f}" y="{sy(H):.1f}" width="{D*S:.1f}" height="{H*S:.1f}" class="part"/>')
# back hatched strip (closed ends)
g.append(f'<rect x="{sx(D-BACK):.1f}" y="{sy(H):.1f}" width="{BACK*S:.1f}" height="{H*S:.1f}" class="htch"/>')
for z in range(6, H, 12):
    g.append(f'<line x1="{sx(D-BACK):.1f}" y1="{sy(z):.1f}" x2="{sx(D):.1f}" y2="{sy(z+8):.1f}" class="htchline"/>')
# tunnels (3 shown) rising 5 deg going in
for z0, dia in ((20, 8.0), (55, 6.0), (86, 9.0)):
    x2 = sx(TUN_D * math.cos(math.radians(TILT)))
    z2 = z0 + TUN_D * math.sin(math.radians(TILT))
    y1, y2 = sy(z0), sy(z2)
    ht = dia * S
    g.append(f'<line x1="{sx(10):.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="tun" stroke-width="{ht:.1f}"/>')
# chamfer note
g.append(f'<text x="{sx(D/2):.1f}" y="{sy(H)-10:.1f}" class="lbl">tunnels rise 5&deg; going in</text>')
g.append(f'<text x="{sx(D-BACK/2):.1f}" y="{sy(8):.1f}" class="lbl">closed back {BACK}</text>')
# depth dim
g.append(f'<line x1="{sx(0):.1f}" y1="{sy(0)+34:.1f}" x2="{sx(D):.1f}" y2="{sy(0)+34:.1f}" class="dim"/>'
         f'<line x1="{sx(0):.1f}" y1="{sy(0)+30:.1f}" x2="{sx(0):.1f}" y2="{sy(0)+38:.1f}" class="dim"/>'
         f'<line x1="{sx(D):.1f}" y1="{sy(0)+30:.1f}" x2="{sx(D):.1f}" y2="{sy(0)+38:.1f}" class="dim"/>'
         f'<text x="{(sx(0)+sx(D))/2:.1f}" y="{sy(0)+28:.1f}" class="dimtxt">block depth {D} &middot; tunnel {TUN_D} deep</text>')
# height dim
g.append(f'<line x1="{sx(D)+26:.1f}" y1="{sy(0):.1f}" x2="{sx(D)+26:.1f}" y2="{sy(H):.1f}" class="dim"/>'
         f'<text x="{sx(D)+32:.1f}" y="{sy(H/2):.1f}" class="dimtxt v">{H}</text>')
# roof in section: two slopes, ridge centred
ridge_z = H + RISE
fz = sy(ridge_z)
g.append(f'<polygon points="{sx(-OV_FRONT):.1f},{sy(H):.1f} {sx(D/2):.1f},{fz:.1f} {sx(D/2):.1f},{fz-T*S:.1f} {sx(-OV_FRONT):.1f},{sy(H)-T*S:.1f}" class="rooffill"/>')
g.append(f'<polygon points="{sx(D+OV_BACK):.1f},{sy(H):.1f} {sx(D/2):.1f},{fz:.1f} {sx(D/2):.1f},{fz-T*S:.1f} {sx(D+OV_BACK):.1f},{sy(H)-T*S:.1f}" class="rooffill"/>')
# far gable wall beyond the cut: connects the pitched roof to the block top
g.append(f'<polygon points="{sx(0):.1f},{sy(H):.1f} {sx(D):.1f},{sy(H):.1f} {sx(D/2):.1f},{fz:.1f}" class="gable"/>')
# overhang dimension (front), drawn below the eave
g.append(f'<line x1="{sx(0):.1f}" y1="{sy(H)-2:.1f}" x2="{sx(0):.1f}" y2="{sy(H)+40:.1f}" class="dim"/>')
g.append(f'<line x1="{sx(-OV_FRONT):.1f}" y1="{sy(H)-2:.1f}" x2="{sx(-OV_FRONT):.1f}" y2="{sy(H)+40:.1f}" class="dim"/>')
g.append(f'<line x1="{sx(-OV_FRONT):.1f}" y1="{sy(H)+36:.1f}" x2="{sx(0):.1f}" y2="{sy(H)+36:.1f}" class="dim"/>')
g.append(f'<text x="{sx(-OV_FRONT/2):.1f}" y="{sy(H)+31:.1f}" class="dimtxt">{OV_FRONT}</text>')
# cleat on the back
g.append(f'<rect x="{sx(D):.1f}" y="{sy(H-12):.1f}" width="{CLEAT*S:.1f}" height="{12*S:.1f}" class="part fill"/>')
g.append(f'<text x="{sx(D+CLEAT)+6:.1f}" y="{sy(6):.1f}" class="lbl v">cleat</text>')
side_svg = "\n".join(g)
side_w = sx(D + CLEAT) + 52
side_h = sy(-4) + 44

# ---------------- FRONT ELEVATION ----------------
fx = lambda x: 30 + x * S
fy = lambda z: 40 + (H - z) * S
e = []
e.append(f'<rect x="{fx(0):.1f}" y="{fy(H):.1f}" width="{W*S:.1f}" height="{H*S:.1f}" class="part"/>')
for ri, row in enumerate(ROWS):
    for ci, col in enumerate(COLS):
        dia = DIAS[ri][ci]
        r = dia / 2.0 * S
        e.append(f'<circle cx="{fx(col):.1f}" cy="{fy(row):.1f}" r="{r:.2f}" class="hole"/>')
# width dim
e.append(f'<line x1="{fx(0):.1f}" y1="{fy(0)+26:.1f}" x2="{fx(W):.1f}" y2="{fy(0)+26:.1f}" class="dim"/>'
         f'<line x1="{fx(0):.1f}" y1="{fy(0)+22:.1f}" x2="{fx(0):.1f}" y2="{fy(0)+30:.1f}" class="dim"/>'
         f'<line x1="{fx(W):.1f}" y1="{fy(0)+22:.1f}" x2="{fx(W):.1f}" y2="{fy(0)+30:.1f}" class="dim"/>'
         f'<text x="{(fx(0)+fx(W))/2:.1f}" y="{fy(0)+26:.1f}" class="dimtxt">{W}</text>')
e.append(f'<text x="{fx(W)+14:.1f}" y="{fy(58):.1f}" class="lbl v">{N_HOLES} holes</text>')
e.append(f'<text x="{fx(W)+14:.1f}" y="{fy(48):.1f}" class="lbl v">tunnels</text>')
front_svg = "\n".join(e)
front_w = fx(W) + 70
front_h = fy(0) + 40

# ---------------- TUNNEL DETAIL ----------------
d = []
dx = lambda mm: 20 + mm * 2.4
dy = lambda mm: 140 - mm * 2.4
# tunnel shown in the block: opening at the face
DET_X0, DET_X1 = 22, 62
d.append(f'<rect x="{dx(0):.1f}" y="{dy(14):.1f}" width="{dx(70)-dx(0):.1f}" height="{14*2.4:.1f}" class="part"/>')
_r = 3 * 2.4
_ty = dy(7) - _r
_by = dy(7) + _r
d.append(f'<path d="M {dx(DET_X0):.1f} {_ty:.1f} L {dx(DET_X1):.1f} {_ty:.1f} L {dx(DET_X1):.1f} {_by:.1f} L {dx(DET_X0):.1f} {_by:.1f} A {_r:.1f} {_r:.1f} 0 0 0 {dx(DET_X0):.1f} {_ty:.1f} Z" class="bore"/>')
d.append(f'<text x="{dx(35):.1f}" y="{dy(7)+34:.1f}" class="det">entrance rounded &amp; sanded</text>')
d.append(f'<text x="{dx(35):.1f}" y="{dy(7)+46:.1f}" class="det2">no splinters, no drill-through</text>')
detail_svg = "\n".join(d)
det_w = dx(70) + 40
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
.fill {{ fill:#dcd2c2; }}
.htch {{ fill:#e6ddcc; stroke:#2a2a2a; stroke-width:1; }}
.htchline {{ stroke:#b9ab92; stroke-width:0.7; }}
.tun {{ stroke:#5b4a33; stroke-linecap:butt; }}
.tuncl {{ stroke:#c9a25a; stroke-width:0.9; stroke-dasharray:4 3; }}
.tunface {{ fill:#5b4a33; stroke:#2a2a2a; stroke-width:0.8; }}
.bore {{ fill:#5b4a33; stroke:#7d6a4c; stroke-width:0.8; }}
.hole {{ fill:#fff; stroke:#2a2a2a; stroke-width:0.9; }}
.rooffill {{ fill:#f6f1e7; stroke:#2a2a2a; stroke-width:1; }}
.gable {{ fill:#e6ddcc; stroke:#9a9a9a; stroke-width:0.9; stroke-dasharray:4 3; }}
.ovarr {{ stroke:#8a1f14; stroke-width:0.9; }}
.lbl {{ fill:#555; font-size:8.5px; text-anchor:middle; paint-order:stroke; stroke:#ffffff; stroke-width:3px; }}
.lbl.v {{ text-anchor:start; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.6; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.7; }}
.dimtxt {{ fill:#333; font-size:9px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:3px; }}
.dimtxt.v {{ text-anchor:start; }}
.vt {{ text-anchor:start; font-size:9px; fill:#4a4a4a; letter-spacing:0.5px; }}
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
<h1>The Offcut Bee Block <span class="tag">Mark &middot; piece 02 &middot; v1</span></h1>
<div class="sub">Solitary-bee nesting block from one untreated hardwood offcut. {N_HOLES} closed-end tunnels, varied diameter, no glue. Roof sheds rain, block lifts off its cleat. Dimensions in mm.</div>
<div class="wrap">
  <div class="views">
    <svg width="{side_w:.0f}" height="{side_h:.0f}" viewBox="0 0 {side_w:.0f} {side_h:.0f}">
      {side_svg}
      <text x="30" y="13" class="vt">SIDE SECTION A&ndash;A</text>
    </svg>
    <div class="cap">Cut through a column of tunnels (dashed gable wall each end, beyond the cut). Tunnels stop {BACK} short of the back &mdash; never drilled through &mdash; and rise 5&deg; going in so rain runs out, not in.</div>
    <div style="display:flex; gap:14px; align-items:flex-start;">
      <div>
        <svg width="{front_w:.0f}" height="{front_h:.0f}" viewBox="0 0 {front_w:.0f} {front_h:.0f}">
          {front_svg}
          <text x="30" y="13" class="vt">FRONT ELEVATION</text>
        </svg>
        <div class="cap" style="width:{front_w:.0f}px;">Face the bees see. Diameters span {min(min(r) for r in DIAS):.1f}&ndash;{max(max(r) for r in DIAS):.1f} mm, mixed so different species nest.</div>
      </div>
      <div>
        <svg width="{det_w:.0f}" height="{det_h:.0f}" viewBox="0 0 {det_w:.0f} {det_h:.0f}">
          {detail_svg}
          <text x="20" y="13" class="vt">TUNNEL DETAIL</text>
        </svg>
        <div class="cap" style="width:{det_w:.0f}px;">One tunnel, cut open.</div>
      </div>
    </div>
  </div>
  <div class="side">
    <h2>Cut list</h2>
    <table>
      <tr><th>Part</th><th>Qty</th><th>L</th><th>W</th><th>T</th></tr>
      <tr><td>Nesting block</td><td>1</td><td>{D}</td><td>{W}</td><td>{H}</td></tr>
      <tr><td>Roof panel</td><td>2</td><td>{PANEL_L:.0f}</td><td>{PANEL_W}</td><td>{T}</td></tr>
      <tr><td>Back cleat</td><td>1</td><td>{W}</td><td>{CLEAT}</td><td>{CLEAT}</td></tr>
    </table>
    <div class="sub" style="margin-top:3px;">One block, two roof panels mitred at {ROOF_PITCH}&deg;, one cleat. The block is the offcut; everything else is from the same board.</div>

    <h2>Material</h2>
    <div><b>Untreated hardwood</b>, dry, low-resin (oak, beech, ash). No softwood, no treatment, no resinous pine &mdash; sap and treated timber both harm the bees. Block {H} thick minimum so a {TUN_D} tunnel leaves a closed end.</div>

    <h2>Tunnels</h2>
    <div>{N_HOLES} holes, {min(min(r) for r in DIAS):.1f}&ndash;{max(max(r) for r in DIAS):.1f}&nbsp;mm, drilled from the face to {TUN_D}&nbsp;mm deep at a 5&deg; upward angle. <b>Never drill through.</b> Sand each entrance round and splinter-free. Leave the shavings out; blow the holes clear.</div>

    <h2>Hardware &amp; finish</h2>
    <div>Roof to block: stainless screws 4&times;40, 8. Cleat to block: 4&times;30, 4. No glue &mdash; it has to open for cleaning.<br>
    <b>Nothing</b> on the tunnel faces. Roof and outer block: wood oil only, and keep it off the holes. No paint on the face, no varnish, no treatment.</div>

    <h2>Mounting</h2>
    <div>Cleat to a wall or post, block hangs on it and lifts off. <b>1.2&ndash;1.8&nbsp;m</b> up, on the morning-sun face, sheltered from driving rain. In the southern hemisphere that is roughly north/east. A wall behind it is fine; a branch is not &mdash; it must not swing.</div>

    <h2>Basis</h2>
    <div style="font-size:9px;">Tunnel diameters 2.3&ndash;9.5&nbsp;mm, mason bees 7.5&ndash;9.5&nbsp;mm (borderfreebees Bee-Hotel-Specs). Depth ~150&ndash;180&nbsp;mm (RSPB; borderfreebees). Drill deep, closed ends, never through; angle holes slightly upward so rain stays out (RSPB). Smooth sanded entrances; untreated low-resin hardwood; 50&ndash;75&nbsp;mm roof overhang; mount 1.2&ndash;1.8&nbsp;m facing the sun (NorCal Nectar mason guide). Vary diameters for species diversity (NC State Extension).</div>

    <div class="q"><b>Why the angle matters:</b> a tunnel that rises going in has its opening at the low point, so water arriving on the face drips away instead of running in. Combined with the roof overhang, the tunnels stay dry.</div>
    <div class="q2"><b>Open item for Paul:</b> block {H} thick with {TUN_D} tunnels reads chunky. If he'd rather stack two thinner boards with a grooved face, say so and I'll redraw &mdash; it costs one more part but opens for inspection.</div>
  </div>
</div>
</body></html>'''

open("/workspace/plan/offcut-bee-block.html", "w").write(html)
print("wrote html", len(html))
print(f"RISE={RISE:.1f} PANEL_L={PANEL_L:.1f} PANEL_W={PANEL_W} HOLES={N_HOLES}")
print(f"side {side_w:.0f}x{side_h:.0f} front {front_w:.0f}x{front_h:.0f} det {det_w:.0f}x{det_h:.0f}")
