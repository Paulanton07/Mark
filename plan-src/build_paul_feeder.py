#!/usr/bin/env python3
# Paul's hanging gable feeder - measured plan from his own hand sketch.
# His numbers (red ink): frame 300x200 (short side inside); rebate base 300x200;
# 4 uprights 230 cut 45deg; roof 2x230 + 2x250; roof slats 15 x 300 long, 40 wide 11 thick;
# 4 dowel perches 60mm on the short side; mesh 300x200 stapled under, trim rebate over staples.
# Units mm. Pitch 45deg (Paul's cut).
import math

W, L = 200.0, 300.0          # short span (gable), long run (ridge direction)
T = 18.0                     # frame stock thickness
POST = 22.0                  # corner post section
WALL_H = 50.0                # tray wall height
POST_H = 230.0               # upright length (Paul)
PITCH = 45.0
OH_EAVE = 40.0
OH_GABLE = 30.0
SLAT_T = 11.0
RIDGE_Z = POST_H + (W / 2.0) * math.tan(math.radians(PITCH))   # underside at ridge
ROOF_TOP = RIDGE_Z + SLAT_T
EAVE_X_L = -T - OH_EAVE
EAVE_X_R = W + T + OH_EAVE
EAVE_Z_L = RIDGE_Z - (W / 2.0 + T + OH_EAVE) * math.tan(math.radians(PITCH))
OUT_L, OUT_R = -T, W + T

def s(v): return v
S = 0.8

M = 52
TOPL = 26

# ---- gable elevation (looking at the 200 end) ----
def gx(x): return M + (x - EAVE_X_L) * S
def gz(z): return TOPL + (ROOF_TOP - z) * S

gg = []
gg.append(f'<line x1="{gx(EAVE_X_L)-14:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+14:.1f}" y2="{gz(0):.1f}" class="ground"/>')
# posts
for (xa,xb) in ((OUT_L,0.0),(W,OUT_R)):
    gg.append(f'<rect x="{gx(xa):.1f}" y="{gz(POST_H):.1f}" width="{abs(T)*S:.1f}" height="{POST_H*S:.1f}" class="part"/>')
# tray wall (front, cut) + floor
gg.append(f'<rect x="{gx(OUT_L):.1f}" y="{gz(WALL_H):.1f}" width="{((W+2*T))*S:.1f}" height="{WALL_H*S:.1f}" class="part fill"/>')
gg.append(f'<rect x="{gx(0):.1f}" y="{gz(WALL_H):.1f}" width="{W*S:.1f}" height="{WALL_H*S:.1f}" class="voidfill"/>')
# mesh line under floor
gg.append(f'<line x1="{gx(OUT_L):.1f}" y1="{gz(0):.1f}" x2="{gx(OUT_R):.1f}" y2="{gz(0):.1f}" class="mesh"/>')
# roof: two slopes, with thickness
apex = W/2.0
for (x0,x1) in ((EAVE_X_L, apex),(EAVE_X_R, apex)):
    z0 = EAVE_Z_L
    gg.append(f'<polygon points="{gx(x0):.1f},{gz(z0):.1f} {gx(x1):.1f},{gz(RIDGE_Z):.1f} {gx(x1):.1f},{gz(ROOF_TOP):.1f} {gx(x0):.1f},{gz(z0+SLAT_T):.1f}" class="part fill"/>')
# slat hatching across the roof
for i in range(9):
    t = i/8.0
    xa = EAVE_X_L + t*(apex-EAVE_X_L); za = EAVE_Z_L + t*(RIDGE_Z-EAVE_Z_L)
    xb = EAVE_X_R - t*(EAVE_X_R-apex); zb = EAVE_Z_L + t*(RIDGE_Z-EAVE_Z_L)
    gg.append(f'<line x1="{gx(xa):.1f}" y1="{gz(za+SLAT_T/2):.1f}" x2="{gx(xb):.1f}" y2="{gz(zb-SLAT_T/2):.1f}" class="hatch"/>')
# ridge cap
gg.append(f'<rect x="{gx(apex)-11*S:.1f}" y="{gz(ROOF_TOP):.1f}" width="{22*S:.1f}" height="{7*S:.1f}" class="part fill2"/>')
# perches on the short sides
for xc in (-T-8, W+T+8):
    gg.append(f'<line x1="{gx(xc-14):.1f}" y1="{gz(WALL_H/2):.1f}" x2="{gx(xc+14):.1f}" y2="{gz(WALL_H/2):.1f}" class="perch"/>')
# dims
gg.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+26:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+26:.1f}" class="dim"/><line x1="{gx(0):.1f}" y1="{gz(0)+22:.1f}" x2="{gx(0):.1f}" y2="{gz(0)+30:.1f}" class="dim"/><line x1="{gx(W):.1f}" y1="{gz(0)+22:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+30:.1f}" class="dim"/><text x="{(gx(0)+gx(W))/2:.1f}" y="{gz(0)+26:.1f}" class="dimtxt">200 in.</text>')
gg.append(f'<line x1="{gx(EAVE_X_L):.1f}" y1="{gz(0)+46:.1f}" x2="{gx(EAVE_X_R):.1f}" y2="{gz(0)+46:.1f}" class="dim"/><line x1="{gx(EAVE_X_L):.1f}" y1="{gz(0)+42:.1f}" x2="{gx(EAVE_X_L):.1f}" y2="{gz(0)+50:.1f}" class="dim"/><line x1="{gx(EAVE_X_R):.1f}" y1="{gz(0)+42:.1f}" x2="{gx(EAVE_X_R):.1f}" y2="{gz(0)+50:.1f}" class="dim"/><text x="{(gx(EAVE_X_L)+gx(EAVE_X_R))/2:.1f}" y="{gz(0)+46:.1f}" class="dimtxt">316 roof o/a</text>')
gg.append(f'<line x1="{gx(EAVE_X_R)+30:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+30:.1f}" y2="{gz(POST_H):.1f}" class="dim"/><text x="{gx(EAVE_X_R)+34:.1f}" y="{(gz(0)+gz(POST_H))/2:.1f}" class="dimtxt v">230 posts</text>')
gg.append(f'<line x1="{gx(EAVE_X_R)+30:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+30:.1f}" y2="{gz(ROOF_TOP):.1f}" class="dim"/><text x="{gx(EAVE_X_R)+34:.1f}" y="{(gz(ROOF_TOP)+gz(POST_H))/2:.1f}" class="dimtxt v">{ROOF_TOP:.0f}</text>')
gg.append(f'<text x="{gx(apex)+18:.1f}" y="{gz(RIDGE_Z)+16:.1f}" class="pitch">45&deg;</text>')
gable = "\n".join(gg)
gw = gx(EAVE_X_R) + 78
gh = gz(0) + 62

# ---- side elevation (looking at a 300 long face) ----
def hx(x): return M + (x + OH_GABLE) * S
def hz(z): return TOPL + (ROOF_TOP - z) * S
hh = []
hh.append(f'<line x1="{hx(-OH_GABLE)-14:.1f}" y1="{hz(0):.1f}" x2="{hx(L+OH_GABLE)+14:.1f}" y2="{hz(0):.1f}" class="ground"/>')
hh.append(f'<rect x="{hx(0):.1f}" y="{hz(WALL_H):.1f}" width="{L*S:.1f}" height="{WALL_H*S:.1f}" class="part fill"/>')
hh.append(f'<line x1="{hx(0):.1f}" y1="{hz(0):.1f}" x2="{hx(L):.1f}" y2="{hz(0):.1f}" class="mesh"/>')
for xa in (0.0, L-T):
    hh.append(f'<rect x="{hx(xa):.1f}" y="{hz(POST_H):.1f}" width="{T*S:.1f}" height="{POST_H*S:.1f}" class="part"/>')
hh.append(f'<rect x="{hx(-OH_GABLE):.1f}" y="{hz(ROOF_TOP):.1f}" width="{(L+2*OH_GABLE)*S:.1f}" height="{(ROOF_TOP-EAVE_Z_L)*S:.1f}" class="rooffill"/>')
for i in range(9):
    xa = -OH_GABLE + i*(L+2*OH_GABLE)/8.0
    hh.append(f'<line x1="{hx(xa):.1f}" y1="{hz(EAVE_Z_L+SLAT_T/2):.1f}" x2="{hx(xa):.1f}" y2="{hz(ROOF_TOP-SLAT_T/2):.1f}" class="hatch"/>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(EAVE_Z_L):.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(EAVE_Z_L):.1f}" class="line2"/>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(ROOF_TOP):.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(ROOF_TOP):.1f}" class="line2"/>')
hh.append(f'<line x1="{hx(0):.1f}" y1="{hz(0)+26:.1f}" x2="{hx(L):.1f}" y2="{hz(0)+26:.1f}" class="dim"/><text x="{(hx(0)+hx(L))/2:.1f}" y="{hz(0)+26:.1f}" class="dimtxt">300</text>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(0)+46:.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(0)+46:.1f}" class="dim"/><text x="{(hx(-OH_GABLE)+hx(L+OH_GABLE))/2:.1f}" y="{hz(0)+46:.1f}" class="dimtxt">360 roof (with 30 gable overhang)</text>')
hh.append(f'<line x1="{hx(L+OH_GABLE)+30:.1f}" y1="{hz(0):.1f}" x2="{hx(L+OH_GABLE)+30:.1f}" y2="{hz(ROOF_TOP):.1f}" class="dim"/><text x="{hx(L+OH_GABLE)+34:.1f}" y="{(hz(0)+hz(ROOF_TOP))/2:.1f}" class="dimtxt v">{ROOF_TOP:.0f}</text>')
side = "\n".join(hh)
sw = hx(L+OH_GABLE) + 78
sh = hz(0) + 62

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:9mm; }}
h1 {{ font-size: 19px; margin:0 0 1px 0; }}
h2 {{ font-size: 10px; text-transform:uppercase; letter-spacing:1px; color:#6b6b6b; margin:10px 0 3px 0; border-bottom:1px solid #d8d8d8; padding-bottom:2px;}}
.sub {{ font-size:10px; color:#555; margin-bottom:5px;}}
.wrap {{ display:flex; gap:16px; align-items:flex-start; }}
.views {{ flex: 0 0 520px; }}
.side {{ flex: 1 1 auto; font-size:10px; }}
svg {{ display:block; }}
.part {{ fill:#efe8dc; stroke:#2a2a2a; stroke-width:1; }}
.fill2 {{ fill:#dcd2c2; stroke:#2a2a2a; stroke-width:1; }}
.voidfill {{ fill:#ffffff; stroke:none; }}
.rooffill {{ fill:#f6f1e7; stroke:#2a2a2a; stroke-width:1; }}
.line2 {{ stroke:#2a2a2a; stroke-width:0.8; fill:none; }}
.hatch {{ stroke:#b9a98c; stroke-width:0.8; }}
.mesh {{ stroke:#1f6f4a; stroke-width:2.2; fill:none; }}
.perch {{ stroke:#2a2a2a; stroke-width:3.2; stroke-linecap:round; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.6; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.7; }}
.dimtxt {{ fill:#333; font-size:9px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:3px; }}
.dimtxt.v {{ text-anchor:start; }}
.pitch {{ fill:#8a1f14; font-size:9px; text-anchor:middle; paint-order:stroke; stroke:#ffffff; stroke-width:3px; }}
.vt {{ text-anchor:start; font-size:9px; fill:#4a4a4a; letter-spacing:0.5px; }}
.cap {{ font-size:9px; color:#666; margin:1px 0 8px 0; }}
table {{ width:100%; border-collapse:collapse; font-size:9.5px; }}
th,td {{ text-align:left; padding:2px 3px; border-bottom:1px solid #e4e4e4; }}
th {{ color:#6b6b6b; font-weight:600; text-transform:uppercase; font-size:8px; letter-spacing:0.4px;}}
.q {{ font-size:9.5px; background:#fff6e8; border:1px solid #e8d3a8; padding:5px 7px; margin-top:7px;}}
.q2 {{ font-size:9.5px; background:#eef6f0; border:1px solid #bfe0cb; padding:5px 7px; margin-top:7px;}}
.tag {{ display:inline-block; font-size:8.5px; border:1px solid #999; border-radius:8px; padding:0 5px; margin-left:6px; color:#555;}}
</style></head><body>
<h1>Hanging Gable Feeder <span class="tag">Mark &middot; plan for Paul &middot; v1.1</span></h1>
<div class="sub">Drawn from your built feeder and your hand sheet. Untreated pine, stapled galvanised mesh floor, 45&deg; roof. Dimensions in mm. Internal tray 300&times;200.</div>
<div class="wrap">
  <div class="views">
    <svg width="{gw:.0f}" height="{gh:.0f}" viewBox="0 0 {gw:.0f} {gh:.0f}">
      {gable}
      <text x="{M}" y="15" class="vt">GABLE ELEVATION (200 end)</text>
    </svg>
    <div class="cap">Ridge runs along the 300 run, gable faces the short end. 45&deg; pitch, 100 rise. Post tops cut 45&deg;.</div>
    <svg width="{sw:.0f}" height="{sh:.0f}" viewBox="0 0 {sw:.0f} {sh:.0f}">
      {side}
      <text x="{M}" y="15" class="vt">SIDE ELEVATION (300 side)</text>
    </svg>
    <div class="cap">Roof reads as a band, eave {EAVE_Z_L:.0f} to ridge top {ROOF_TOP:.0f}. Open on all four sides above the tray.</div>
  </div>
  <div class="side">
    <h2>Cut list</h2>
    <table>
      <tr><th>Part</th><th>Qty</th><th>L</th><th>W</th><th>T</th></tr>
      <tr><td>Upright post, top cut 45&deg;</td><td>4</td><td>230</td><td>22</td><td>22</td></tr>
      <tr><td>Tray long wall</td><td>2</td><td>{L:.0f} o/a</td><td>50</td><td>18</td></tr>
      <tr><td>Tray short wall</td><td>2</td><td>{W+2*T:.0f} o/a</td><td>50</td><td>18</td></tr>
      <tr><td>Rebate base (floor)</td><td>1</td><td>300</td><td>200</td><td>18</td></tr>
      <tr><td>Roof frame member</td><td>2</td><td>230</td><td>40</td><td>22</td></tr>
      <tr><td>Roof frame member</td><td>2</td><td>250</td><td>40</td><td>22</td></tr>
      <tr><td>Roof slat</td><td>15</td><td>300</td><td>40</td><td>11</td></tr>
      <tr><td>Dowel perch</td><td>4</td><td>60</td><td>&Oslash;12</td><td>&mdash;</td></tr>
      <tr><td>Mesh floor</td><td>1</td><td>300</td><td>200</td><td>6 mesh</td></tr>
      <tr><td>Trim rebate cap</td><td>4</td><td>&mdash;</td><td>20</td><td>6</td></tr>
    </table>
    <div class="sub" style="margin-top:3px;"><b>Roof frame</b> = the 2&times;230 + 2&times;250 members, glued and screwed as one sub-assembly, then set on the post tops. Slats are nailed across the frame after it is square. Post tops cut 45&deg; to seat it.</div>

    <h2>Cost</h2>
    <table>
      <tr><th>Item</th><th>Value</th><th>Basis</th></tr>
      <tr><td>Your board</td><td>R30</td><td>2000 &times; 90 pine, per board (yours)</td></tr>
      <tr><td>Boards per feeder</td><td>~2</td><td>slats + frame, incl. waste (est.)</td></tr>
      <tr><td>Timber</td><td>~R60</td><td>estimate</td></tr>
      <tr><td>Mesh + dowels + screws</td><td>~R27</td><td>estimate</td></tr>
      <tr><td>Wood oil</td><td>~R5</td><td>estimate</td></tr>
      <tr><td>Material subtotal</td><td>~R92</td><td>estimate</td></tr>
      <tr><td>Machine + finish + margin</td><td>~R178</td><td>the rest of R270</td></tr>
      <tr><td>Sell price (yours)</td><td>R270</td><td>each</td></tr>
    </table>
    <div class="sub" style="margin-top:3px;">Built from your R30 / 2m board. Thickness wasn't on the board you quoted, so I took 22&nbsp;mm to match the post section; if your boards are thinner the timber line drops. Offcuts are cheaper than boards, so this is the high side. Tell me your machine rate and I split that R178 into machine / finish / profit.</div>

    <h2>Material</h2>
    <div><b>Untreated</b> pine only. Nothing treated touches this: it is a food surface in the weather.</div>

    <h2>Hardware &amp; finish</h2>
    <div>Stainless or hot-dip galvanised screws only, no bare steel.<br>Galvanised or stainless &Oslash;6 mesh, stapled under the frame, trim rebate cap screwed over the staples.<br>Wood oil (Woodoc), all outer faces, 2 coats. Tray inside and roof underside left bare. Re-oil yearly.</div>

    <h2>Water &amp; service</h2>
    <div>Roof overhang {OH_EAVE:.0f} at the eaves, {OH_GABLE:.0f} at the gables. Mesh floor drains and airs the seed. Lift the whole feeder off its hook to tip out and scrub.</div>

    <h2>Hanging</h2>
    <div>Two &Oslash;6 eyes under the ridge cap or a single cord over the ridge. ~2&nbsp;m up, 3&nbsp;m clear of a jump-off.</div>

    <div class="q2"><b>You confirmed:</b> the 2&times;230 + 2&times;250 are the roof frame; slats nail across it; the frame sets on the uprights. Drawn that way now.</div>
    <div class="q"><b>Still my call (tell me if wrong):</b> post section drawn 22 square and tray wall height 50, since your sheet didn't give those. Board thickness taken as 22 too, since your rate was per board not per m&sup3;. Cost figures are estimates until your machine rate lands.</div>
    <div class="q2"><b>Kept from your build:</b> stapled mesh under the frame with a rebate cap over the staples is the right move: seed stays up, staples don't lift into a bird's feet.</div>
  </div>
</div>
</body></html>'''

open("/workspace/plan/paul-gable-feeder.html","w").write(html)
print("html", len(html), "gw", round(gw), "gh", round(gh), "sw", round(sw), "sh", round(sh))
print("RIDGE_Z", round(RIDGE_Z,1), "ROOF_TOP", round(ROOF_TOP,1), "EAVE_Z_L", round(EAVE_Z_L,1))
