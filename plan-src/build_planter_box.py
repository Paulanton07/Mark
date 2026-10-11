#!/usr/bin/env python3
# Standard slatted planter box - build guide, v1 (phone-readable A4 portrait).
# Same illustrated-sequence template as Paul's feeder v5.
# One design, three standard lengths. 5 pages: elevations / cut+material /
# picture sequence / steps 1-5 / steps 6-10.
import math

# ---- master geometry (mm), drawn at the 600 size ----
L = 600.0          # external length
W = 300.0          # external width
H = 360.0          # post height (ground to top)
POST = 45.0        # corner post section
T = 20.0           # board thickness
SLAT_W = 90.0      # wall slat width
GAP = 10.0         # gap between wall courses
CLEAT = 40.0       # floor cleat section
CLEAT_Z = 40.0     # cleat underside above ground (= ground clearance)
FLOOR_T = 20.0
FLOOR_Z = CLEAT_Z + CLEAT   # floor board underside
WALL_Z0 = 70.0     # first wall course underside

# derived lengths
SPAN_L = L - 2*POST     # 510  front/back slat + floor board length
SPAN_W = W - 2*POST     # 210  side slat + cleat length
FLOOR_BOARDS = 3

S = 0.8
M = 96
TOPL = 24

def gx(x): return M + x * S
def gz(z): return TOPL + (H - z) * S

# ---------- FRONT ELEVATION (looking at a 600 face) ----------
def front_svg():
    e = []
    e.append(f'<line x1="{gx(0)-16:.1f}" y1="{gz(0):.1f}" x2="{gx(L)+16:.1f}" y2="{gz(0):.1f}" class="ground"/>')
    # posts
    for x0 in (0.0, L-POST):
        e.append(f'<rect x="{gx(x0):.1f}" y="{gz(H):.1f}" width="{POST*S:.1f}" height="{H*S:.1f}" class="part"/>')
    # floor board band (hidden edge behind slats shown faint)
    e.append(f'<rect x="{gx(POST):.1f}" y="{gz(FLOOR_Z+FLOOR_T):.1f}" width="{SPAN_L*S:.1f}" height="{FLOOR_T*S:.1f}" class="hidden"/>')
    # wall slats, 3 courses
    for i in range(3):
        z0 = WALL_Z0 + i*(SLAT_W+GAP)
        e.append(f'<rect x="{gx(POST):.1f}" y="{gz(z0+SLAT_W):.1f}" width="{SPAN_L*S:.1f}" height="{SLAT_W*S:.1f}" class="part fill"/>')
    # ground clearance dim (left)
    xd = gx(0)-44
    e.append(f'<line x1="{xd:.1f}" y1="{gz(0):.1f}" x2="{xd:.1f}" y2="{gz(FLOOR_Z):.1f}" class="dim"/>')
    e.append(f'<line x1="{xd-4:.1f}" y1="{gz(0):.1f}" x2="{xd+4:.1f}" y2="{gz(0):.1f}" class="dim"/>')
    e.append(f'<line x1="{xd-4:.1f}" y1="{gz(FLOOR_Z):.1f}" x2="{xd+4:.1f}" y2="{gz(FLOOR_Z):.1f}" class="dim"/>')
    e.append(f'<rect x="{xd-38:.1f}" y="{(gz(0)+gz(FLOOR_Z))/2-9:.1f}" width="76" height="18" fill="#fff"/>')
    e.append(f'<text x="{xd:.1f}" y="{(gz(0)+gz(FLOOR_Z))/2:.1f}" class="dimtxt">40 clear</text>')
    # overall length dim
    e.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+30:.1f}" x2="{gx(L):.1f}" y2="{gz(0)+30:.1f}" class="dim"/>')
    e.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(0):.1f}" y2="{gz(0)+35:.1f}" class="dim"/>')
    e.append(f'<line x1="{gx(L):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(L):.1f}" y2="{gz(0)+35:.1f}" class="dim"/>')
    e.append(f'<rect x="{(gx(0)+gx(L))/2-46:.1f}" y="{gz(0)+21:.1f}" width="92" height="18" fill="#fff"/>')
    e.append(f'<text x="{(gx(0)+gx(L))/2:.1f}" y="{gz(0)+30:.1f}" class="dimtxt">600 o/a</text>')
    # post width dim
    e.append(f'<line x1="{gx(0):.1f}" y1="{gz(H)+24:.1f}" x2="{gx(POST):.1f}" y2="{gz(H)+24:.1f}" class="dim"/>')
    e.append(f'<text x="{gx(POST/2):.1f}" y="{gz(H)+38:.1f}" class="dimtxt">45</text>')
    # height dim right
    e.append(f'<line x1="{gx(L)+34:.1f}" y1="{gz(0):.1f}" x2="{gx(L)+34:.1f}" y2="{gz(H):.1f}" class="dim"/>')
    e.append(f'<rect x="{gx(L)+36:.1f}" y="{(gz(0)+gz(H))/2-9:.1f}" width="72" height="18" fill="#fff"/>')
    e.append(f'<text x="{gx(L)+38:.1f}" y="{(gz(0)+gz(H))/2:.1f}" class="dimtxt v">360</text>')
    return "\n".join(e)

def front_w(): return gx(L) + 120
def elev_h(): return gz(0) + 42

# ---------- SIDE ELEVATION (looking at a 300 face) ----------
def side_svg():
    e = []
    e.append(f'<line x1="{gx(0)-16:.1f}" y1="{gz(0):.1f}" x2="{gx(W)+16:.1f}" y2="{gz(0):.1f}" class="ground"/>')
    for x0 in (0.0, W-POST):
        e.append(f'<rect x="{gx(x0):.1f}" y="{gz(H):.1f}" width="{POST*S:.1f}" height="{H*S:.1f}" class="part"/>')
    # floor board END GRAIN: 3 boards across the width (running along L)
    span = SPAN_W
    bw = 60.0; g = (span - FLOOR_BOARDS*bw)/(FLOOR_BOARDS-1)
    x = POST
    for i in range(FLOOR_BOARDS):
        e.append(f'<rect x="{gx(x):.1f}" y="{gz(FLOOR_Z+FLOOR_T):.1f}" width="{bw*S:.1f}" height="{FLOOR_T*S:.1f}" class="hidden"/>')
        x += bw + g
    # wall slats, 3 courses (sides)
    for i in range(3):
        z0 = WALL_Z0 + i*(SLAT_W+GAP)
        e.append(f'<rect x="{gx(POST):.1f}" y="{gz(z0+SLAT_W):.1f}" width="{SPAN_W*S:.1f}" height="{SLAT_W*S:.1f}" class="part fill"/>')
    # clear dim
    e.append(f'<line x1="{gx(0)-44:.1f}" y1="{gz(0):.1f}" x2="{gx(0)-44:.1f}" y2="{gz(FLOOR_Z):.1f}" class="dim"/>')
    e.append(f'<rect x="{gx(0)-82:.1f}" y="{(gz(0)+gz(FLOOR_Z))/2-9:.1f}" width="76" height="18" fill="#fff"/>')
    e.append(f'<text x="{gx(0)-44:.1f}" y="{(gz(0)+gz(FLOOR_Z))/2:.1f}" class="dimtxt">40 clear</text>')
    # width dim
    e.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+30:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+30:.1f}" class="dim"/>')
    e.append(f'<line x1="{gx(0):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(0):.1f}" y2="{gz(0)+35:.1f}" class="dim"/>')
    e.append(f'<line x1="{gx(W):.1f}" y1="{gz(0)+25:.1f}" x2="{gx(W):.1f}" y2="{gz(0)+35:.1f}" class="dim"/>')
    e.append(f'<rect x="{(gx(0)+gx(W))/2-46:.1f}" y="{gz(0)+21:.1f}" width="92" height="18" fill="#fff"/>')
    e.append(f'<text x="{(gx(0)+gx(W))/2:.1f}" y="{gz(0)+30:.1f}" class="dimtxt">300 o/a</text>')
    # height dim
    e.append(f'<line x1="{gx(W)+34:.1f}" y1="{gz(0):.1f}" x2="{gx(W)+34:.1f}" y2="{gz(H):.1f}" class="dim"/>')
    e.append(f'<rect x="{gx(W)+36:.1f}" y="{(gz(0)+gz(H))/2-9:.1f}" width="72" height="18" fill="#fff"/>')
    e.append(f'<text x="{gx(W)+38:.1f}" y="{(gz(0)+gz(H))/2:.1f}" class="dimtxt v">360</text>')
    return "\n".join(e)

def side_w(): return gx(W) + 120

# ---------- progressive build tiles (front view) ----------
TILE_CAP = {
 "1":"Four posts + cleats. Mark 40 up.",
 "2":"Cleats fixed inside the posts.",
 "3":"Floor boards laid, gaps for drainage.",
 "4":"Liner stapled over floor and up the sides.",
 "5":"Side slats, bottom course, all four sides.",
 "6":"Second course, keep the 10 mm gap.",
 "7":"Top course, flush with the post tops.",
 "8":"Sand the top edges and inner slat faces.",
 "9":"Oil the outside faces and top edges.",
 "10":"Position, line it, fill and plant.",
}

def tile_svg(step):
    step = int(step)
    w, h = 150, 132
    xmin, xmax = -12, L + 12
    zmin, zmax = -14, H + 12
    s = min((w-14)/(xmax-xmin), (h-14)/(zmax-zmin))
    ox = (w - (xmax-xmin)*s)/2 - xmin*s
    oy = (h - (zmax-zmin)*s)/2 + zmax*s
    X = lambda x: ox + x*s
    Y = lambda z: oy - z*s
    def rc(x0,x1,z0,z1,cls):
        return f'<rect x="{X(x0):.1f}" y="{Y(z1):.1f}" width="{(x1-x0)*s:.1f}" height="{(z1-z0)*s:.1f}" class="{cls}"/>'
    E = []
    # faint target: full wall outline before slats exist
    if step < 7:
        E.append(rc(POST, L-POST, WALL_Z0, H, 'future'))
    # posts
    pc = 'hl' if step == 1 else 'part'
    E.append(rc(0, POST, 0, H, pc))
    E.append(rc(L-POST, L, 0, H, pc))
    # cleats
    if step >= 2:
        cc = 'hl' if step == 2 else 'part'
        E.append(rc(POST, POST+CLEAT, CLEAT_Z, CLEAT_Z+CLEAT, cc))
        E.append(rc(L-POST-CLEAT, L-POST, CLEAT_Z, CLEAT_Z+CLEAT, cc))
    # floor boards
    if step >= 3:
        fc = 'hl' if step == 3 else 'part'
        E.append(rc(POST, L-POST, FLOOR_Z, FLOOR_Z+FLOOR_T, fc))
    # liner
    if step >= 4:
        E.append(f'<line x1="{X(POST+2):.1f}" y1="{Y(FLOOR_Z+FLOOR_T):.1f}" x2="{X(POST+2):.1f}" y2="{Y(H-2):.1f}" class="{"hline" if step==4 else "liner"}"/>')
        E.append(f'<line x1="{X(L-POST-2):.1f}" y1="{Y(FLOOR_Z+FLOOR_T):.1f}" x2="{X(L-POST-2):.1f}" y2="{Y(H-2):.1f}" class="{"hline" if step==4 else "liner"}"/>')
    # wall slat courses (front)
    for i in range(3):
        z0 = WALL_Z0 + i*(SLAT_W+GAP)
        if step >= 5+i:
            cls = 'hl' if step == 5+i else 'part'
            E.append(rc(POST, L-POST, z0, z0+SLAT_W, cls))
    # sand/oil marks
    if step == 8:
        for x0 in (POST, L-POST-8):
            E.append(f'<line x1="{X(x0):.1f}" y1="{Y(H):.1f}" x2="{X(x0+8):.1f}" y2="{Y(H-8):.1f}" class="hline"/>')
    if step == 9:
        E.append(rc(POST, L-POST, WALL_Z0, H, 'oil'))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(E)}</svg>'

def tiles_html():
    out = ['<div class="steps_grid">']
    for n in TILE_CAP:
        out.append(f'<div class="tile"><span class="tnum">{n}</span>{tile_svg(n)}<div class="tcap">{TILE_CAP[n]}</div></div>')
    out.append('</div>')
    return "\n".join(out)

# ---------- steps ----------
STEPS = [
 ("1","<b>Cut the four posts and the cleats.</b> Posts 45&times;45&times;360, four off. Floor cleats 40&times;40&times;210, two off. Mark a line 40&nbsp;mm up every post.","The 40&nbsp;mm below that line is the foot. It lifts the floor off the ground so the timber dries and the box does not rot from the base."),
 ("2","<b>Fix the cleats.</b> Screw a 40&times;40 cleat between the two short-side posts at each end, top edge exactly on the 40&nbsp;mm line. Pilot the posts first. Two 60&nbsp;mm screws through each post end into the cleat.","The cleats carry the floor and set the drainage height. Fixed to the post ends (not the middle) they cannot split the slats later."),
 ("3","<b>Floor boards.</b> Lay three 510&times;60 boards along the length, resting on the cleats, with even gaps between them (about 15&nbsp;mm). Screw each down to both cleats.","Gaps, not a solid panel: water drains through instead of sitting on the floor. Boards run the long way so each one is only nailed at its two ends."),
 ("4","<b>Line it.</b> Staple a piece of landscape fabric or geotextile over the floor and up the inside of the posts to within 20&nbsp;mm of the top, folding the corners.","The liner holds soil in while letting water through, and it keeps wet soil off bare timber. Fold corners clean so the soil cannot push it down."),
 ("5","<b>Bottom course of slats.</b> Cut two 510 and two 210 boards. Fix the 210s first: screw through each end into the posts. Then the 510s, into the posts and the side-slat ends. Start at the 70&nbsp;mm line so the course sits just above the floor.","Sides first, then front and back: the long course then closes over the short ends, so no end grain shows on the two long faces you look at."),
 ("6","<b>Second course.</b> Same again, one 10&nbsp;mm gap above the first course. Keep the gap even with an offcut as a spacer.","The gap lets air move and lets the boards swell in the wet without jacking each other off the posts. A spacer beats eyeballing every gap."),
 ("7","<b>Top course.</b> Third course, top edge flush with the post tops. Check the whole box is square corner-to-corner before the last screws go in.","Flush with the post tops gives one clean line all round and a 360 outer height. Square now, or the rim will not sit flat."),
 ("8","<b>Sand.</b> Sand the top edges, the inner slat faces and any end grain. Break every corner a hand or a plant root will touch.","Round the top edges so nobody gets a splinter and the finish rail reads as made, not sawn. Inner faces smooth so it does not wear the liner."),
 ("9","<b>Oil.</b> Wood oil (Woodoc) on the outside faces, the top edges and the post feet, two coats, dry between. Leave the inside bare behind the liner.","Oil is the weather coat. Outside and up the feet is where the water sits. The inside stays bare so it can breathe; oil under the liner just traps damp."),
 ("10","<b>Position and plant.</b> Set it level, clear ground under all four feet, fill with a free-draining mix, plant, water in.","Level feet spread the load and stop one corner sitting wet. A free-draining mix matches the open floor: the box is built to let water move."),
]

def steps_table(rows):
    out = ['<table class="steps"><tr><th style="width:26px;">#</th><th style="width:47%;">Step</th><th>Why</th></tr>']
    for n, s, why in rows:
        out.append(f'<tr><td class="num">{n}</td><td>{s}</td><td>{why}</td></tr>')
    out.append('</table>')
    return "\n".join(out)

# ---------- standard-size table ----------
SIZES = [
    ("Small", 450.0, "3 x 110", "165", "~35"),
    ("Medium", 600.0, "3 x 155", "225", "~55"),
    ("Trough", 900.0, "3 x 245", "345", "~95"),
]

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 portrait; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:11mm; }}
h1 {{ font-size: 27px; margin:0 0 3px 0; }}
h2 {{ font-size: 17px; text-transform:uppercase; letter-spacing:1px; color:#5a5a5a; margin:11px 0 4px 0; border-bottom:2px solid #cfcfcf; padding-bottom:3px;}}
.sub {{ font-size:16px; color:#444; margin-bottom:6px; line-height:1.32; }}
.draw {{ text-align:center; margin:6px 0 2px 0; }}
.draw svg {{ display:block; margin:0 auto; }}
.part {{ fill:#efe8dc; stroke:#2a2a2a; stroke-width:1.1; }}
.hidden {{ fill:#ffffff; stroke:#9a9a9a; stroke-width:0.8; stroke-dasharray:3 3; }}
.mesh {{ stroke:#1f6f4a; stroke-width:2.6; fill:none; }}
.liner {{ stroke:#2f6f8a; stroke-width:2.2; fill:none; stroke-dasharray:5 3; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.8; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.8; }}
.dimtxt {{ fill:#222; font-size:13px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }}
.dimtxt.v {{ text-anchor:start; }}
.vt {{ text-anchor:start; font-size:15px; font-weight:bold; fill:#3a3a3a; letter-spacing:0.5px; }}
.cap {{ font-size:15px; color:#444; margin:3px auto 9px auto; max-width:680px; line-height:1.3; text-align:center; }}
table {{ width:100%; border-collapse:collapse; font-size:18px; }}
th,td {{ text-align:left; padding:5px 6px; border-bottom:1px solid #ddd; vertical-align:top; }}
th {{ color:#5a5a5a; font-weight:700; text-transform:uppercase; font-size:14px; letter-spacing:0.4px;}}
.q {{ font-size:17px; background:#fff6e8; border:1px solid #e8d3a8; padding:8px 10px; margin-top:9px; border-radius:3px; }}
.tag {{ display:inline-block; font-size:14px; border:1px solid #999; border-radius:3px; padding:2px 8px; margin-left:8px; color:#555; vertical-align:middle; }}
.steps {{ font-size:18px; }}
.hl {{ fill:#f4b183; stroke:#a8410f; stroke-width:1.3; }}
.hline {{ stroke:#a8410f; stroke-width:2.6; fill:none; }}
.oil {{ fill:#f6d9a8; stroke:#a87b1f; stroke-width:1; opacity:0.55; }}
.future {{ fill:#ffffff; stroke:#c9c9c9; stroke-width:1; stroke-dasharray:3 3; }}
.steps_grid {{ display:grid; grid-template-columns:1fr 1fr; gap:7px 9px; }}
.tile {{ border:1px solid #ddd; border-radius:5px; padding:5px 7px 7px 7px; }}
.tile svg {{ display:block; margin:1px auto 3px auto; }}
.tnum {{ display:inline-block; font-weight:800; color:#fff; background:#8a1f14; border-radius:3px; font-size:13px; padding:1px 7px; }}
.tcap {{ font-size:14px; line-height:1.24; color:#222; }}
.steps td {{ padding:7px 7px; line-height:1.32; }}
.steps th {{ font-size:14px; }}
.num {{ font-weight:800; color:#8a1f14; text-align:center; font-size:19px; }}
.pg {{ page-break-before: always; }}
</style></head><body>

<h1>Slatted Planter Box <span class="tag">standard sizes &middot; build guide v1</span></h1>
<div class="sub">One design, three standard lengths. Slatted walls with drainage gaps, a slatted floor lifted 40&nbsp;mm clear of the ground, corner posts carrying everything. Untreated pine or hardwood. Dimensions in mm. Shown at the 600&times;300&times;360 size.</div>
<div class="draw">
  <svg width="{front_w():.0f}" height="{elev_h():.0f}" viewBox="0 0 {front_w():.0f} {elev_h():.0f}">
    {front_svg()}
    <text x="{M}" y="18" class="vt">FRONT ELEVATION (600 face)</text>
  </svg>
</div>
<div class="cap"><b>Long face.</b> Three slat courses between the posts, 10&nbsp;mm air gap between them. The floor sits 40&nbsp;mm up (dashed, hidden behind the bottom gap). Posts run to the ground as feet.</div>
<div class="draw">
  <svg width="{side_w():.0f}" height="{elev_h():.0f}" viewBox="0 0 {side_w():.0f} {elev_h():.0f}">
    {side_svg()}
    <text x="{M}" y="18" class="vt">SIDE ELEVATION (300 face)</text>
  </svg>
</div>
<div class="cap"><b>Short face.</b> Same three courses. Through the bottom gap you can see the three floor boards end-on (dashed), with drainage gaps between them.</div>

<div class="pg">
<h2>Cut list &mdash; 600 &times; 300 &times; 360</h2>
<table>
  <tr><th>Part</th><th>Qty</th><th>Length</th><th>Width</th><th>Thick</th></tr>
  <tr><td>Corner post (foot below)</td><td>4</td><td>360</td><td>45</td><td>45</td></tr>
  <tr><td>Wall slat, long (front/back)</td><td>6</td><td>510</td><td>90</td><td>{T:.0f}</td></tr>
  <tr><td>Wall slat, short (sides)</td><td>6</td><td>210</td><td>90</td><td>{T:.0f}</td></tr>
  <tr><td>Floor board</td><td>{FLOOR_BOARDS}</td><td>510</td><td>60</td><td>{FLOOR_T:.0f}</td></tr>
  <tr><td>Floor cleat</td><td>2</td><td>210</td><td>40</td><td>40</td></tr>
  <tr><td>Liner (geotextile)</td><td>1</td><td>1800</td><td>420</td><td>&mdash;</td></tr>
</table>
<h2>Standard sizes</h2>
<table>
  <tr><th>Size</th><th>L &times; W &times; H</th><th>Long slat</th><th>Short slat</th><th>Soil (L)</th></tr>
  <tr><td>Small</td><td>450 &times; 300 &times; 360</td><td>3 &times; 360</td><td>3 &times; 210</td><td>~35</td></tr>
  <tr><td>Medium</td><td>600 &times; 300 &times; 360</td><td>3 &times; 510</td><td>3 &times; 210</td><td>~55</td></tr>
  <tr><td>Trough</td><td>900 &times; 300 &times; 360</td><td>3 &times; 810</td><td>3 &times; 210</td><td>~95</td></tr>
</table>
<div class="sub" style="font-size:16px;">Only the long slats and the floor boards change length. Width, height, posts, sides and cleats stay the same for all three. Height 360 gives ~300 of soil.</div>
<h2>Material</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;"><b>Untreated pine or hardwood.</b> Untreated for anything edible. If you use treated timber, keep the liner between the soil and the boards, and never use old pallet or railway timber. Stainless or coated screws only, no bare steel.</div>
<h2>Hardware &amp; finish</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;">60&nbsp;mm coated screws throughout (posts, cleats, slats, floor), all pilot-drilled. Geotextile / landscape fabric liner. Wood oil (Woodoc) outside and on the feet, 2 coats. Inside left bare behind the liner. Re-oil yearly.</div>
<h2>Drainage</h2>
<div class="sub" style="font-size:17px; margin-bottom:4px;">40&nbsp;mm ground clearance at the feet, ~15&nbsp;mm gaps between floor boards, 10&nbsp;mm air gap between wall courses, liner over the floor. Water leaves through the floor, air moves through the walls.</div>
</div>

<div class="pg">
<h1 style="font-size:26px;">The build at a glance <span class="tag">picture sequence</span></h1>
<div class="sub">Ten steps, drawn in order, front view. The highlighted part is what you add on that step; the faint outline is where the build is heading. Full wording follows.</div>
{tiles_html()}
</div>

<div class="pg">
<h1 style="font-size:26px;">How it goes together <span class="tag">steps 1&ndash;5</span></h1>
<div class="sub">In order. Each names the piece, the order, and the reason. Dry-fit the floor and the first course before screws.</div>
{steps_table(STEPS[0:5])}
</div>

<div class="pg">
<h1 style="font-size:26px;">How it goes together <span class="tag">steps 6&ndash;10</span></h1>
{steps_table(STEPS[5:10])}
</div>

</body></html>'''

open("/workspace/plan/planter-box-v1.html","w").write(html)
print("html", len(html))
