#!/usr/bin/env python3
# Paul's X-leg herb trough - build guide v1 (phone-readable A4 portrait).
# Drawn from Paul's spec (x-herb box.md) + the agreed 4-stage order:
#   1 X legs   2 stand them + first planks in the V   3 the rest of the 900s   4 sides off an offcut
# Stock: planks 80 wide x 23 thick. Legs 4x 700 (one end cut 32deg). Cross planks 8x 900 (4 front, 4 back).
# Hero drawing is the X JOINT (stage 1). The two angles (32deg foot vs 22.5deg crossing) get
# confirmed against Paul's build photo before v2 ships; the stage order is the value here.
import math

PW   = 80.0
T    = 23.0
LEG  = 700.0
WALL = 900.0
NF   = 4
WALL_H = NF*PW          # 320
TOP_SPREAD = 305.0
FOOT_DEG   = 32.0
CROSS_DEG  = 22.5

half = TOP_SPREAD/2.0
theta = math.degrees(math.asin(half/(LEG/2.0)))   # ~25.8, schematic tilt
vhalf = (LEG/2.0)*math.cos(math.radians(theta))   # ~315

CSS = """
@page { size: A4 portrait; margin: 10mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:0; }
h1 { font-size: 25px; margin:0 0 3px 0; }
h2 { font-size: 15px; text-transform:uppercase; letter-spacing:1px; color:#5a5a5a; margin:11px 0 4px 0; border-bottom:2px solid #cfcfcf; padding-bottom:3px;}
.sub { font-size:15px; color:#444; margin-bottom:6px; line-height:1.34; }
.sub ul { margin:2px 0 4px 0; padding-left:18px; }
.sub li { margin:2px 0; }
.draw { text-align:center; margin:5px 0 1px 0; }
.draw svg { display:block; margin:0 auto; }
.part { fill:#efe8dc; stroke:#2a2a2a; stroke-width:1.1; }
.part2 { fill:#e3d9c6; stroke:#2a2a2a; stroke-width:1.1; }
.leg { fill:#d9c9ad; stroke:#2a2a2a; stroke-width:1.2; }
.soil { fill:#cfe3c2; opacity:0.55; stroke:#7a9a5a; stroke-width:0.8; }
.ground { stroke:#2a2a2a; stroke-width:1.8; }
.dim { stroke:#7a7a7a; stroke-width:0.8; }
.dimtxt { fill:#222; font-size:12px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }
.dimtxt.v { text-anchor:start; }
.vt { text-anchor:start; font-size:14px; font-weight:bold; fill:#3a3a3a; letter-spacing:0.4px; }
.cap { font-size:14px; color:#444; margin:2px auto 8px auto; max-width:690px; line-height:1.28; text-align:center; }
table { width:100%; border-collapse:collapse; font-size:15px; }
th,td { text-align:left; padding:5px 6px; border-bottom:1px solid #ddd; vertical-align:top; }
th { color:#5a5a5a; font-weight:700; text-transform:uppercase; font-size:12px; letter-spacing:0.4px;}
.q { font-size:15px; background:#fff6e8; border:1px solid #e8d3a8; padding:8px 10px; margin-top:9px; border-radius:3px; }
.q ul { margin:4px 0; padding-left:17px; }
.q li { margin:2px 0; }
.tag { display:inline-block; font-size:13px; border:1px solid #999; border-radius:3px; padding:2px 8px; margin-left:8px; color:#555; vertical-align:middle; }
.steps td { padding:7px; line-height:1.30; font-size:15px; }
.steps th { font-size:12px; }
.steps td ul { margin:3px 0; padding-left:16px; }
.steps td li { margin:2px 0; }
.num { font-weight:800; color:#8a1f14; text-align:center; font-size:18px; }
.hl { fill:#f4b183; stroke:#a8410f; stroke-width:1.3; }
.hline { stroke:#a8410f; stroke-width:2.4; fill:none; }
.screw { fill:#8a1f14; }
.steps_grid { display:grid; grid-template-columns:1fr 1fr; gap:6px 9px; }
.tile { border:1px solid #ddd; border-radius:5px; padding:5px 7px 6px 7px; }
.tile svg { display:block; margin:1px auto 3px auto; }
.tnum { display:inline-block; font-weight:800; color:#fff; background:#8a1f14; border-radius:3px; font-size:12px; padding:1px 7px; }
.tcap { font-size:13px; line-height:1.22; color:#222; }
.pg { page-break-before: always; }
"""

def rotrect(cx, cy, length, width, ang, cls):
    return (f'<rect x="{-length/2:.1f}" y="{-width/2:.1f}" width="{length:.1f}" '
            f'height="{width:.1f}" class="{cls}" transform="translate({cx:.1f},{cy:.1f}) rotate({ang:.1f})"/>')

# ---------- HERO: the X joint (stage 1) ----------
def detail_svg():
    s = 0.40
    wx = 470
    pad = 56
    def sx(mx): return wx/2.0 + mx*s
    def sy(my): return pad + (vhalf - my)*s
    crossx, crossy = sx(0.0), sy(0.0)
    Lpx, Wpx = LEG*s, PW*s
    e = []
    e.append(f'<line x1="30" y1="{sy(-vhalf)+4:.1f}" x2="{wx-30}" y2="{sy(-vhalf)+4:.1f}" class="ground"/>')
    # clamped straight plank (the reference you press the 32deg foot against)
    e.append(f'<rect x="{sx(-half-40):.1f}" y="{sy(-vhalf)-Wpx-10:.1f}" width="{(2*half+80)*s:.1f}" height="{Wpx*0.55:.1f}" class="part2"/>')
    e.append(f'<text x="{sx(0):.1f}" y="{sy(-vhalf)+20:.1f}" class="dimtxt" style="font-size:11px;">straight plank clamped to the table</text>')
    # the two legs
    e.append(rotrect(crossx, crossy, Lpx, Wpx, +theta, 'leg'))
    e.append(rotrect(crossx, crossy, Lpx, Wpx, -theta, 'leg'))
    e.append(f'<circle cx="{crossx:.1f}" cy="{crossy:.1f}" r="5" class="screw"/>')
    # top spread dim
    yt = sy(vhalf)-14
    e.append(f'<line x1="{sx(-half):.1f}" y1="{yt:.1f}" x2="{sx(half):.1f}" y2="{yt:.1f}" class="dim"/>')
    for xx in (-half, half):
        e.append(f'<line x1="{sx(xx):.1f}" y1="{yt-5:.1f}" x2="{sx(xx):.1f}" y2="{yt+5:.1f}" class="dim"/>')
    e.append(f'<rect x="{crossx-22:.1f}" y="{yt-9:.1f}" width="44" height="18" fill="#fff"/>')
    e.append(f'<text x="{crossx:.1f}" y="{yt:.1f}" class="dimtxt">305</text>')
    # 700 leg dim along the right leg
    e.append(f'<text x="{sx(half)+30:.1f}" y="{sy(40):.1f}" class="dimtxt v" style="font-size:11px;">700 leg</text>')
    # centre callout
    e.append(f'<line x1="{crossx+8:.1f}" y1="{crossy-4:.1f}" x2="{crossx+70:.1f}" y2="{crossy-34:.1f}" class="dim"/>')
    e.append(f'<text x="{crossx+74:.1f}" y="{crossy-36:.1f}" class="dimtxt v" style="font-size:11px;">centre: 350 along, 40 across</text>')
    # foot angle labels
    e.append(f'<text x="{sx(-half)-10:.1f}" y="{sy(-vhalf)+2:.1f}" class="dimtxt" style="font-size:11px;">32&deg;</text>')
    e.append(f'<text x="{sx(half)+10:.1f}" y="{sy(-vhalf)+2:.1f}" class="dimtxt" style="font-size:11px;">32&deg;</text>')
    e.append(f'<text x="20" y="15" class="vt">X JOINT - stage 1 (schematic)</text>')
    return (f'<svg width="{wx}" height="{int(2*vhalf*s+2*pad):d}" viewBox="0 0 {wx} {int(2*vhalf*s+2*pad):d}">'
            + "".join(e) + '</svg>')

# ---------- stage tiles ----------
def xglyph(cx, cy, sz):
    return (f'<line x1="{cx-sz:.1f}" y1="{cy-sz:.1f}" x2="{cx+sz:.1f}" y2="{cy+sz:.1f}" stroke="#2a2a2a" stroke-width="3.4" stroke-linecap="round"/>'
            f'<line x1="{cx-sz:.1f}" y1="{cy+sz:.1f}" x2="{cx+sz:.1f}" y2="{cy-sz:.1f}" stroke="#2a2a2a" stroke-width="3.4" stroke-linecap="round"/>')

def tile_svg(step):
    step = int(step)
    w, h = 150, 120
    e = []
    LX, RX, cy = 24, 126, 60
    if step == 1:
        e.append(xglyph(75, 54, 38))
        e.append('<circle cx="75" cy="54" r="4.5" fill="#8a1f14"/>')
        e.append('<text x="75" y="106" text-anchor="middle" font-size="11" fill="#8a1f14">32&deg; feet &middot; screw the centre</text>')
    else:
        e.append(xglyph(LX, cy, 24))
        e.append(xglyph(RX, cy, 24))
        bx0, bx1 = LX+26, RX-26
        def bar(yy, cls, x0=bx0, x1=bx1):
            return f'<rect x="{x0:.1f}" y="{yy:.1f}" width="{x1-x0:.1f}" height="6" class="{cls}" rx="1"/>'
        if step == 2:
            e.append(bar(52, 'hl'))
            e.append(bar(61, 'hl'))
            e.append(f'<text x="75" y="106" text-anchor="middle" font-size="11" fill="#8a1f14">first two in the V</text>')
        elif step == 3:
            for k in range(4):
                e.append(bar(30+k*7, 'part'))
            for k in range(4):
                e.append(bar(60+k*7, 'part2'))
            e.append(f'<text x="75" y="106" text-anchor="middle" font-size="11" fill="#8a1f14">4 front + 4 back</text>')
        else:
            for k in range(4):
                e.append(bar(38+k*7, 'part'))
            e.append(f'<rect x="{LX-6:.1f}" y="30" width="7" height="40" class="hl"/>')
            e.append(f'<rect x="{RX-1:.1f}" y="30" width="7" height="40" class="hl"/>')
            e.append(f'<text x="75" y="106" text-anchor="middle" font-size="11" fill="#8a1f14">sides off an offcut</text>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(e)}</svg>'

TILE_CAP = {
 "1":"<b>Stage 1 - the X legs.</b> Cut one end of each 700 leg at 32&deg;. Cross two: centre 350 along, 40 across. Screw or bolt the crossing, 22.5&deg;. Make two, mirrored - one plank inside, one outside, left and right.",
 "2":"<b>Stage 2 - stand them and start the floor.</b> Stand the two X sets parallel. Cut one 900 at 22.5&deg; to sit snug in the V. The back one lands 23&nbsp;mm higher, so trim 23&nbsp;mm off it so both tops come level.",
 "3":"<b>Stage 3 - the rest of the 900s.</b> 4 planks on the front, 4 on the back, flush with the left and right X. The back sits 23&nbsp;mm proud behind the outside leg. Screw down front and back.",
 "4":"<b>Stage 4 - the sides.</b> Hold an offcut in the V, mark the angle, cut the first side piece. Next piece higher: mark off the first, cut, glue and screw on top. Third the same. Mirror the other end.",
}

def tiles_html():
    out = ['<div class="steps_grid">']
    for n in TILE_CAP:
        out.append(f'<div class="tile"><span class="tnum">{n}</span>{tile_svg(n)}<div class="tcap">{TILE_CAP[n]}</div></div>')
    out.append('</div>')
    return "\n".join(out)

STEPS = [
 ("1","<b>The X legs.</b><ul>"
      "<li>Four legs, 700 long. Cut <b>one end of each</b> at 32&deg; - all four off the <b>same saw setting</b>.</li>"
      "<li>Find the centre of each leg: 350 along, 40 across (half of 80).</li>"
      "<li>Clamp a straight plank to the table. Press the 32&deg; end flush against it.</li>"
      "<li>Lay the second leg on top to make the X. Pilot hole at the centre.</li>"
      "<li>Drive a 35&nbsp;mm part-threaded screw so the two pieces sit at 22.5&deg; and the foot sits flush to the clamped plank. About 305&nbsp;mm between the two top corners.</li>"
      "<li>Then 3-4 more screws, or swap to a 6&nbsp;mm or 10&nbsp;mm bolt through the crossing.</li>"
      "<li>Make the second set a <b>mirror</b>: one plank inside, one outside, on both left and right.</li></ul>",
      "<ul><li>One saw setting for all four feet = feet that sit level. Cut them one at a time and they fight.</li>"
      "<li>The clamped plank is the reference - it stops the X leaning while you screw.</li>"
      "<li>A single screw lets the X scissor. Extra screws or a bolt lock the crossing.</li>"
      "<li>Mirrored handed frames make the box symmetrical, so the trough sits level.</li></ul>"),
 ("2","<b>Stand them and lay the first two planks.</b><ul>"
      "<li>Stand the two X sets parallel, on the ground.</li>"
      "<li>Lay the first two 900 planks in the V, one front, one back.</li>"
      "<li>Cut <b>one edge of the front plank at 22.5&deg;</b> so it sits snug in the V.</li>"
      "<li>The back plank lands on top of the front, so it sits 23&nbsp;mm higher. <b>Trim 23&nbsp;mm off</b> it so both tops come level.</li></ul>",
      "<ul><li>Both X sets parallel = the box goes up straight.</li>"
      "<li>The 22.5&deg; cut makes the plank nest into the V, not rock on the corner.</li>"
      "<li>Level first planks = level box. This is the one that sets it.</li></ul>"),
 ("3","<b>Lay the rest of the 900s.</b><ul>"
      "<li>Carry on stacking: 4 planks on the front, 4 on the back, one on top of the other.</li>"
      "<li>All flush with the left and right X planks.</li>"
      "<li>The back stacks 23&nbsp;mm proud, behind the outside leg.</li>"
      "<li>Both sides finish at the same height.</li>"
      "<li>Screw the stack down, front and back, into the X frames.</li></ul>",
      "<ul><li>Flush to the X = straight walls, no stepping.</li>"
      "<li>The back offset clears the leg, so both walls meet the frame the same way.</li>"
      "<li>Equal height both sides = a level rim.</li></ul>"),
 ("4","<b>The sides, scribed off an offcut.</b><ul>"
      "<li>Hold an offcut horizontal in the bottom of the V. Draw a line from inside to mark the angle of the first side piece.</li>"
      "<li>Cut to the line, fit it in the V.</li>"
      "<li>Hold a longer offcut above the first, mark off it, cut the second, glue and screw it on top of the first.</li>"
      "<li>Third the same, on top of the second.</li>"
      "<li>Do the same for the opposite end.</li></ul>",
      "<ul><li>The V is not a set angle you can measure off a drawing - you scribe each piece off the one below.</li>"
      "<li>Glue <b>and</b> screw: end grain is weak, the glue takes the load, the screws hold it while it sets.</li>"
      "<li>Three pieces fill the end from the floor to the rim.</li></ul>"),
]

def steps_table(rows):
    out = ['<table class="steps"><tr><th style="width:22px;">#</th><th style="width:50%;">Stage</th><th>Why</th></tr>']
    for n, s, why in rows:
        out.append(f'<tr><td class="num">{n}</td><td>{s}</td><td>{why}</td></tr>')
    out.append('</table>')
    return "\n".join(out)

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<h1>X-Leg Herb Trough <span class="tag">your build &middot; draft v1</span></h1>
<div class="sub"><ul>
<li>Your numbers. Two X-leg frames carry a 900&nbsp;long trough between them.</li>
<li>Legs <b>4&times;700</b>, one end cut 32&deg;. Cross planks <b>8&times;900</b>, four front and four back. Planks 80 wide &times; 23 thick.</li>
<li>The trough sits in the V of the two X frames. Its floor is the first two 900s; the rest stack up the sides.</li>
<li>The sides are not cut to a number. They are <b>scribed off an offcut</b> held in the V, one on top of the last.</li>
<li>Shown at 900 long, four planks deep. Dimensions in mm.</li></ul></div>

<div class="draw">{detail_svg()}</div>
<div class="cap"><b>Stage 1 - the joint that decides the box.</b> Two 700 legs crossed at their centres. The saw cut at the foot and the angle at the crossing set everything above them: get the crossing flush on the clamped plank and the two frames stand square. Confirm the two angles against your build photo.</div>

<div class="pg">
<h2>Cut list</h2>
<table>
  <tr><th>Part</th><th>Qty</th><th>Length</th><th>Width</th><th>Thick</th><th>Note</th></tr>
  <tr><td>Leg</td><td>4</td><td>700</td><td>80</td><td>23</td><td>one end cut 32&deg;, all four one setting</td></tr>
  <tr><td>Cross plank (wall)</td><td>8</td><td>900</td><td>80</td><td>23</td><td>4 front, 4 back</td></tr>
  <tr><td>Side piece</td><td>6</td><td>scribed</td><td>80</td><td>23</td><td>3 per end, marked off an offcut</td></tr>
  <tr><td>- of those, the bottom pair</td><td>2</td><td>900</td><td>80</td><td>23</td><td>front edge cut 22.5&deg;; back trimmed 23&nbsp;mm</td></tr>
</table>
<h2>Material</h2>
<div class="sub" style="font-size:15px;"><ul>
<li>Untreated pine or hardwood. Untreated: it is a food bed.</li>
<li><b>35&nbsp;mm part-threaded screws</b> for the crossing and the side courses.</li>
<li>A <b>6&nbsp;mm or 10&nbsp;mm bolt</b> through each crossing if you want it to never move.</li>
<li>Stainless or coated only. Wood oil (Woodoc) outside and on the feet.</li>
</ul></div>
<div class="q"><b>Two rules that decide this build</b><ul>
<li><b>One saw setting for all four feet.</b> Cut every 32&deg; end off the same stop. One foot cut on its own and the box stands on three legs.</li>
<li><b>Lock the crossing.</b> A single screw lets the X scissor. Add 3-4 screws, or bolt it.</li></ul></div>
<div class="q"><b>Open - to confirm against your build photo</b><ul>
<li>The spec says the two X pieces sit at <b>22.5&deg;</b> and the feet are cut at <b>32&deg;</b>. On a 700 leg those two do not land on the same 305&nbsp;mm top spread, so the hero drawing is schematic. Send the shot of the crossing and the foot and I fix the exact angles in v2.</li>
</ul></div>
</div>

<div class="pg">
<h1 style="font-size:23px;">The build in four stages <span class="tag">picture sequence</span></h1>
<div class="sub">Four stages, in order. Do not start the sides until the walls are screwed down and level.</div>
{tiles_html()}
</div>

<div class="pg">
<h1 style="font-size:23px;">Stage by stage <span class="tag">1 &ndash; 2</span></h1>
{steps_table(STEPS[0:2])}
</div>

<div class="pg">
<h1 style="font-size:23px;">Stage by stage <span class="tag">3 &ndash; 4</span></h1>
{steps_table(STEPS[2:4])}
</div>

</body></html>'''

open("/workspace/plan/herb-box-v1.html","w").write(html)
print("html", len(html), "theta", round(theta,1), "vhalf", round(vhalf,1))
