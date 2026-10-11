#!/usr/bin/env python3
# Paul's hanging gable feeder - build guide v4 (phone-readable).
# Same content as v3.3, redrawn as A4 PORTRAIT with large type so Paul can read it
# on a phone. 4 pages: elevations / cut+material / steps 1-5 / steps 6-10.
import math

W, L = 200.0, 300.0
T = 18.0
POST = 23.0
WALL_H = 50.0
POST_H = 230.0
PITCH = 45.0
OH_EAVE = 40.0
OH_GABLE = 30.0
SLAT_T = 11.0
RIDGE_Z = POST_H + (W / 2.0) * math.tan(math.radians(PITCH))
ROOF_TOP = RIDGE_Z + SLAT_T
EAVE_X_L = -T - OH_EAVE
EAVE_X_R = W + T + OH_EAVE
EAVE_Z_L = RIDGE_Z - (W / 2.0 + T + OH_EAVE) * math.tan(math.radians(PITCH))
OUT_L, OUT_R = -T, W + T

S = 0.85
M = 56
TOPL = 30

def gx(x): return M + (x - EAVE_X_L) * S
def gz(z): return TOPL + (ROOF_TOP - z) * S

gg = []
gg.append(f'<line x1="{gx(EAVE_X_L)-14:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+14:.1f}" y2="{gz(0):.1f}" class="ground"/>')
for (xa,xb) in ((OUT_L,0.0),(W,OUT_R)):
    gg.append(f'<rect x="{gx(xa):.1f}" y="{gz(POST_H):.1f}" width="{abs(T)*S:.1f}" height="{POST_H*S:.1f}" class="part"/>')
gg.append(f'<rect x="{gx(OUT_L):.1f}" y="{gz(WALL_H):.1f}" width="{((W+2*T))*S:.1f}" height="{WALL_H*S:.1f}" class="part fill"/>')
gg.append(f'<rect x="{gx(0):.1f}" y="{gz(WALL_H):.1f}" width="{W*S:.1f}" height="{WALL_H*S:.1f}" class="voidfill"/>')
gg.append(f'<line x1="{gx(OUT_L):.1f}" y1="{gz(0):.1f}" x2="{gx(OUT_R):.1f}" y2="{gz(0):.1f}" class="mesh"/>')
apex = W/2.0
for (x0,x1) in ((EAVE_X_L, apex),(EAVE_X_R, apex)):
    z0 = EAVE_Z_L
    gg.append(f'<polygon points="{gx(x0):.1f},{gz(z0):.1f} {gx(x1):.1f},{gz(RIDGE_Z):.1f} {gx(x1):.1f},{gz(ROOF_TOP):.1f} {gx(x0):.1f},{gz(z0+SLAT_T):.1f}" class="part fill"/>')
gg.append(f'<rect x="{gx(apex)-11*S:.1f}" y="{gz(ROOF_TOP):.1f}" width="{22*S:.1f}" height="{7*S:.1f}" class="part fill2"/>')
for xc in (-T-8, W+T+8):
    gg.append(f'<line x1="{gx(xc-14):.1f}" y1="{gz(WALL_H/2):.1f}" x2="{gx(xc+14):.1f}" y2="{gz(WALL_H/2):.1f}" class="perch"/>')
gg.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+30:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+30:.1f}" class="dim"/><line x1="{gx(0):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(0):.1f}" y2="{gz(0)+35:.1f}" class="dim"/><line x1="{gx(W):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+35:.1f}" class="dim"/><rect x="{(gx(0)+gx(W))/2-34:.1f}" y="{gz(0)+30-9:.1f}" width="68" height="18" fill="#fff"/><text x="{(gx(0)+gx(W))/2:.1f}" y="{gz(0)+30:.1f}" class="dimtxt">200 in.</text>')
gg.append(f'<line x1="{gx(EAVE_X_L):.1f}" y1="{gz(0)+54:.1f}" x2="{gx(EAVE_X_R):.1f}" y2="{gz(0)+54:.1f}" class="dim"/><line x1="{gx(EAVE_X_L):.1f}" y1="{gz(0)+49:.1f}" x2="{gx(EAVE_X_L):.1f}" y2="{gz(0)+59:.1f}" class="dim"/><line x1="{gx(EAVE_X_R):.1f}" y1="{gz(0)+49:.1f}" x2="{gx(EAVE_X_R):.1f}" y2="{gz(0)+59:.1f}" class="dim"/><rect x="{(gx(EAVE_X_L)+gx(EAVE_X_R))/2-62:.1f}" y="{gz(0)+54-9:.1f}" width="124" height="18" fill="#fff"/><text x="{(gx(EAVE_X_L)+gx(EAVE_X_R))/2:.1f}" y="{gz(0)+54:.1f}" class="dimtxt">316 roof o/a</text>')
gg.append(f'<line x1="{gx(EAVE_X_R)+34:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+34:.1f}" y2="{gz(POST_H):.1f}" class="dim"/><rect x="{gx(EAVE_X_R)+36:.1f}" y="{(gz(0)+gz(POST_H))/2-9:.1f}" width="86" height="18" fill="#fff"/><text x="{gx(EAVE_X_R)+38:.1f}" y="{(gz(0)+gz(POST_H))/2:.1f}" class="dimtxt v">230 posts</text>')
gg.append(f'<line x1="{gx(EAVE_X_R)+34:.1f}" y1="{gz(0):.1f}" x2="{gx(EAVE_X_R)+34:.1f}" y2="{gz(ROOF_TOP):.1f}" class="dim"/><rect x="{gx(EAVE_X_R)+36:.1f}" y="{(gz(ROOF_TOP)+gz(POST_H))/2-9:.1f}" width="40" height="18" fill="#fff"/><text x="{gx(EAVE_X_R)+38:.1f}" y="{(gz(ROOF_TOP)+gz(POST_H))/2:.1f}" class="dimtxt v">{ROOF_TOP:.0f}</text>')
gg.append(f'<text x="{gx(apex)-54:.1f}" y="{(gz(WALL_H)+gz(RIDGE_Z))/2:.1f}" class="pitch">45&deg;</text>')
gable = "\n".join(gg)
gw = gx(EAVE_X_R) + 128
gh = gz(0) + 72

def hx(x): return M + (x + OH_GABLE) * S
def hz(z): return TOPL + (ROOF_TOP - z) * S
hh = []
hh.append(f'<line x1="{hx(-OH_GABLE)-14:.1f}" y1="{hz(0):.1f}" x2="{hx(L+OH_GABLE)+14:.1f}" y2="{hz(0):.1f}" class="ground"/>')
hh.append(f'<rect x="{hx(0):.1f}" y="{hz(WALL_H):.1f}" width="{L*S:.1f}" height="{WALL_H*S:.1f}" class="part fill"/>')
hh.append(f'<line x1="{hx(0):.1f}" y1="{hz(0):.1f}" x2="{hx(L):.1f}" y2="{hz(0):.1f}" class="mesh"/>')
for xa in (0.0, L-T):
    hh.append(f'<rect x="{hx(xa):.1f}" y="{hz(POST_H):.1f}" width="{T*S:.1f}" height="{POST_H*S:.1f}" class="part"/>')
hh.append(f'<rect x="{hx(-OH_GABLE):.1f}" y="{hz(ROOF_TOP):.1f}" width="{(L+2*OH_GABLE)*S:.1f}" height="{(ROOF_TOP-EAVE_Z_L)*S:.1f}" class="rooffill"/>')
for i in range(1,9):
    zc = EAVE_Z_L + i*(ROOF_TOP-EAVE_Z_L)/8.0
    hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(zc):.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(zc):.1f}" class="hatch"/>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(EAVE_Z_L):.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(EAVE_Z_L):.1f}" class="line2"/>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(ROOF_TOP):.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(ROOF_TOP):.1f}" class="line2"/>')
hh.append(f'<line x1="{hx(0):.1f}" y1="{hz(0)+30:.1f}" x2="{hx(L):.1f}" y2="{hz(0)+30:.1f}" class="dim"/><rect x="{(hx(0)+hx(L))/2-34:.1f}" y="{hz(0)+30-9:.1f}" width="68" height="18" fill="#fff"/><text x="{(hx(0)+hx(L))/2:.1f}" y="{hz(0)+30:.1f}" class="dimtxt">300</text>')
hh.append(f'<line x1="{hx(-OH_GABLE):.1f}" y1="{hz(0)+54:.1f}" x2="{hx(L+OH_GABLE):.1f}" y2="{hz(0)+54:.1f}" class="dim"/><rect x="{(hx(-OH_GABLE)+hx(L+OH_GABLE))/2-128:.1f}" y="{hz(0)+54-9:.1f}" width="256" height="18" fill="#fff"/><text x="{(hx(-OH_GABLE)+hx(L+OH_GABLE))/2:.1f}" y="{hz(0)+54:.1f}" class="dimtxt">360 roof (with 30 gable overhang)</text>')
hh.append(f'<line x1="{hx(L+OH_GABLE)+34:.1f}" y1="{hz(0):.1f}" x2="{hx(L+OH_GABLE)+34:.1f}" y2="{hz(ROOF_TOP):.1f}" class="dim"/><rect x="{hx(L+OH_GABLE)+36:.1f}" y="{(hz(0)+hz(ROOF_TOP))/2-9:.1f}" width="40" height="18" fill="#fff"/><text x="{hx(L+OH_GABLE)+38:.1f}" y="{(hz(0)+hz(ROOF_TOP))/2:.1f}" class="dimtxt v">{ROOF_TOP:.0f}</text>')
side = "\n".join(hh)
sw = hx(L+OH_GABLE) + 128
sh = hz(0) + 72

STEPS = [
 ("1","<b>Base frame.</b> Cut two 300 and two 200. Glue and nail the 200s <i>between</i> the 300s, so the long faces show and the ends are hidden.","This is your datum. Get it square and everything above it is square too."),
 ("2","<b>Wire under the base.</b> Cut the mesh so its edge finishes <i>inside</i> the base frame, never past it. Staple one edge to the underside, pull it tight across the opposite edge, then work left, right, front, back.","Keep the wire edge inboard. A cut edge left proud scratches and cuts. Tension stops the floor sagging and the seed falling through."),
 ("3","<b>Close the underside.</b> Four thin cover strips over the stapled edges: two <i>short</i> sides first, then the two <i>long</i> sides in, until all four are closed.","The rebate is a cover plate, not just a seat. Short strips first close the corners; the long strips then bury the short ends and their staples, so every cut edge and staple is covered and a bird's feet touch neither."),
 ("4","<b>Side ladders.</b> Take two 230 uprights, fix a top and a bottom rail across them. Make two. Dry-fit first.","The uprights carry the roof. Pairing them keeps them parallel before they meet the box."),
 ("5","<b>Fix the uprights.</b> Drill a pilot hole first, then run a <b>35&nbsp;mm chipboard screw</b> into the side of each of the four uprights &mdash; work the <i>long side first</i>. Then turn the whole thing over and drive one screw from the <i>bottom up</i> into each upright, so it's held twice and pulled square against the base.","Two 20&nbsp;mm planks is 40&nbsp;mm, so a 35&nbsp;mm screw bites and stops short of breaking through the far face. Side screws first hold the uprights plumb; the bottom screws then lock them down. Two opposing screws, one screw alone lets the upright swing."),
 ("6","<b>Box body.</b> Join the two ladders with the cross members. Check corner-to-corner with a speed square and wipe the glue squeeze-out.","Equal diagonals = a square box. Out of square now and the roof won't seat."),
 ("7","<b>Side mesh.</b> Staple the mesh to each side frame so its edge sits <i>a little inside</i> the frame, then pull it under tension edge to edge. Don't run the wire out flush with the frame.","Do NOT trim the wire flush to the frame. A flush edge leaves wire poking out that can scratch or cut, and it shows. Held inside, the cover strip buries it and nothing sharp meets a bird."),
 ("8","<b>Roof frame.</b> Glue and screw the 2&times;230 + 2&times;250 into one frame. The two gable ends are mitred at the peak; glue the mitre, it takes the opening load.","Build the frame flat on the bench. Two 45&deg; mitres meeting at the peak make a self-supporting gable, no ridge board needed."),
 ("9","<b>Set and screw the roof frame.</b> Drop the frame onto the four 45&deg; post tops, then screw it down <i>from the top</i>, straight down into each upright &mdash; one <b>60&nbsp;mm screw</b> per upright, four in all.","Screwing down into the post tops locks the frame to the body and pulls the four uprights square and plumb as it tightens. Down through the frame, not up from underneath, so the fix is hidden by the slats."),
 ("10","<b>Lay the slats.</b> The 15 slats run <b>lengthwise, along the ridge</b> &mdash; not up the slope. Nail the first slat down along the eave, full length; then work up course by course toward the peak, each course lapping the one below like a shingle. Set the square as a <b>gauge</b>, but the slat to it, nail one end then the other, same distance, then the next. Do one slope eave to ridge, then the other.","Lengthwise, lapped eave to ridge: each course covers the fixings of the one below and sheds water off the roof. Two boards laid the other way would just butt at the ridge and leak. The square as a gauge keeps every course the same distance out; eyeballing drifts. Slat ends trimmed after fixing so the overhang is even."),
]

def steps_table(rows):
    out = ['<table class="steps"><tr><th style="width:26px;">#</th><th style="width:47%;">Step</th><th>Why</th></tr>']
    for n, s, why in rows:
        out.append(f'<tr><td class="num">{n}</td><td>{s}</td><td>{why}</td></tr>')
    out.append('</table>')
    return "\n".join(out)

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 portrait; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:11mm; }}
h1 {{ font-size: 30px; margin:0 0 3px 0; }}
h2 {{ font-size: 17px; text-transform:uppercase; letter-spacing:1px; color:#5a5a5a; margin:11px 0 4px 0; border-bottom:2px solid #cfcfcf; padding-bottom:3px;}}
.sub {{ font-size:17px; color:#444; margin-bottom:8px; line-height:1.35; }}
.draw {{ text-align:center; margin:6px 0 2px 0; }}
.draw svg {{ display:block; margin:0 auto; }}
.part {{ fill:#efe8dc; stroke:#2a2a2a; stroke-width:1.1; }}
.fill2 {{ fill:#dcd2c2; stroke:#2a2a2a; stroke-width:1.1; }}
.voidfill {{ fill:#ffffff; stroke:none; }}
.rooffill {{ fill:#f6f1e7; stroke:#2a2a2a; stroke-width:1.1; }}
.line2 {{ stroke:#2a2a2a; stroke-width:0.9; fill:none; }}
.hatch {{ stroke:#b9a98c; stroke-width:0.9; }}
.mesh {{ stroke:#1f6f4a; stroke-width:2.6; fill:none; }}
.perch {{ stroke:#2a2a2a; stroke-width:3.6; stroke-linecap:round; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.8; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.8; }}
.dimtxt {{ fill:#222; font-size:13px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }}
.dimtxt.v {{ text-anchor:start; }}
.pitch {{ fill:#8a1f14; font-size:14px; font-weight:bold; text-anchor:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }}
.vt {{ text-anchor:start; font-size:15px; font-weight:bold; fill:#3a3a3a; letter-spacing:0.5px; }}
.cap {{ font-size:16px; color:#444; margin:4px auto 14px auto; max-width:640px; line-height:1.35; text-align:center; }}
table {{ width:100%; border-collapse:collapse; font-size:18px; }}
th,td {{ text-align:left; padding:5px 6px; border-bottom:1px solid #ddd; vertical-align:top; }}
th {{ color:#5a5a5a; font-weight:700; text-transform:uppercase; font-size:14px; letter-spacing:0.4px;}}
.q {{ font-size:17px; background:#fff6e8; border:1px solid #e8d3a8; padding:8px 10px; margin-top:9px; border-radius:3px; }}
.tag {{ display:inline-block; font-size:14px; border:1px solid #999; border-radius:3px; padding:2px 8px; margin-left:8px; color:#555; vertical-align:middle; }}
.steps {{ font-size:18px; }}
.steps td {{ padding:7px 7px; line-height:1.32; }}
.steps th {{ font-size:14px; }}
.num {{ font-weight:800; color:#8a1f14; text-align:center; font-size:19px; }}
.pg {{ page-break-before: always; }}
ul.k {{ font-size:17px; line-height:1.4; margin:4px 0 4px 0; padding-left:22px; }}
</style></head><body>

<h1>Hanging Gable Feeder <span class="tag">plan for Paul &middot; v4 &middot; build guide</span></h1>
<div class="sub">A build guide, not just a plan: every step in order, with the reason. Untreated pine, galvanised mesh sides and floor, 45&deg; gable roof. Dimensions in mm. Internal tray 300&times;200.</div>
<div class="draw">
  <svg width="{gw:.0f}" height="{gh:.0f}" viewBox="0 0 {gw:.0f} {gh:.0f}">
    {gable}
    <text x="{M}" y="18" class="vt">GABLE ELEVATION (200 end)</text>
  </svg>
</div>
<div class="cap"><b>Gable end.</b> Ridge runs along the 300 run; this faces the short end. 45&deg; pitch, post tops cut 45&deg;. Slats run <b>lengthwise</b> along the roof, so here they sit end-on.</div>
<div class="draw">
  <svg width="{sw:.0f}" height="{sh:.0f}" viewBox="0 0 {sw:.0f} {sh:.0f}">
    {side}
    <text x="{M}" y="18" class="vt">SIDE ELEVATION (300 side)</text>
  </svg>
</div>
<div class="cap"><b>Long side.</b> Slat courses run <b>lengthwise</b>, laid tier on tier eave to ridge, so they read as horizontal lines here. Roof band: eave {EAVE_Z_L:.0f} to ridge top {ROOF_TOP:.0f}. All four sides are mesh above the tray, so birds feed through the wire.</div>

<div class="pg">
<h2>Cut list</h2>
<table>
  <tr><th>Part</th><th>Qty</th><th>Length</th><th>Width</th><th>Thick</th></tr>
  <tr><td>Upright post, top cut 45&deg;</td><td>4</td><td>230</td><td>23</td><td>23</td></tr>
  <tr><td>Tray long wall</td><td>2</td><td>{L:.0f} o/a</td><td>50</td><td>18</td></tr>
  <tr><td>Tray short wall</td><td>2</td><td>{W+2*T:.0f} o/a</td><td>50</td><td>18</td></tr>
  <tr><td>Rebate base (floor)</td><td>1</td><td>300</td><td>200</td><td>18</td></tr>
  <tr><td>Roof frame member</td><td>2</td><td>230</td><td>40</td><td>22</td></tr>
  <tr><td>Roof frame member</td><td>2</td><td>250</td><td>40</td><td>22</td></tr>
  <tr><td>Roof slat</td><td>15</td><td>300</td><td>40</td><td>11</td></tr>
  <tr><td>Dowel perch</td><td>4</td><td>60</td><td>&Oslash;12</td><td>&mdash;</td></tr>
  <tr><td>Mesh (sides + floor)</td><td>&mdash;</td><td>300</td><td>200</td><td>&Oslash;6</td></tr>
  <tr><td>Trim rebate cap</td><td>4</td><td>&mdash;</td><td>20</td><td>6</td></tr>
</table>
<h2>Material</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;"><b>Untreated</b> pine only. Nothing treated touches this: it is a food surface sitting in the weather.</div>
<h2>Hardware &amp; finish</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;">35&nbsp;mm chipboard screws for the uprights, <b>60&nbsp;mm screws</b> for the roof (they pass through the roof frame down into the uprights), all pilot-drilled. Stainless or hot-dip galvanised screws only, no bare steel.<br>Galvanised or stainless &Oslash;6 mesh. Wood oil (Woodoc) on all outer faces, 2 coats. Tray inside and roof underside left bare. Re-oil yearly.</div>
<h2>Hanging</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;">Two &Oslash;6 eyes under the ridge cap, or a single cord over the ridge. Hang ~2&nbsp;m up, 3&nbsp;m clear of a jump-off.</div>
<div class="q"><b>Cost:</b> ~R92 material high-side (your R30 / 2&nbsp;m boards), ~R60 machine + labour, on R270 sell &rarr; ~R118 clear. Cost stays a footnote; the value here is the how.</div>
</div>

<div class="pg">
<h1 style="font-size:26px;">How it goes together <span class="tag">steps 1&ndash;5</span></h1>
<div class="sub">Steps in order. Each names the piece, the order, and the reason. Dry-fit before glue on the frames.</div>
{steps_table(STEPS[0:5])}
</div>

<div class="pg">
<h1 style="font-size:26px;">How it goes together <span class="tag">steps 6&ndash;10</span></h1>
{steps_table(STEPS[5:10])}
</div>

</body></html>'''

open("/workspace/plan/paul-gable-feeder.html","w").write(html)
print("html", len(html), "gw", round(gw), "gh", round(gh), "sw", round(sw), "sh", round(sh))
