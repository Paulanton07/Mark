#!/usr/bin/env python3
# Paul's X-leg herb trough - build guide v3 (phone-readable A4 portrait).
# v3 (16 Oct): Paul's numbers settled - 33deg foot/leg lean, 22.5deg on the base plank's
# inner long edge where it lands on the far leg. Adds the cut diagram and the V-nest panel.
# Drawn from Paul's spec (x-herb box.md) + the agreed 4-stage order:
#   1 X legs   2 stand them + first planks in the V   3 the rest of the 900s   4 sides off an offcut
# Stock: planks 80 wide x 23 thick. Legs 4x 700 (one end cut 33deg). Cross planks 8x 900 (4 front, 4 back).
# Hero drawing is the X JOINT (stage 1). Each leg stands 33deg off vertical (his foot bevel is the same 33).
# The legs cross one on top of the other - no notch. Top gauge = 300 inside corner to inside corner.
import math

PW   = 80.0
T    = 23.0
LEG  = 700.0
WALL = 900.0
NF   = 4
WALL_H = NF*PW          # 320
TILT_DEG   = 33.0   # each leg off vertical - Paul's call, 15 Oct (same as the foot bevel)
FOOT_DEG   = 33.0   # foot bevel (Paul's call, 14 Oct)
V_BEVEL    = 22.5   # Paul, 16 Oct: the cut on the base plank's inner long edge, in the V
LAP        = True   # the two legs cross one ON TOP of the other (Paul's own words)

half  = (LEG/2.0)*math.sin(math.radians(TILT_DEG))   # leg centrelines, top and bottom
vhalf = (LEG/2.0)*math.cos(math.radians(TILT_DEG))
# inner faces of the two legs at the top - this is the 300 he tapes
half_inner = half - (PW/2.0)/math.cos(math.radians(TILT_DEG))
theta = TILT_DEG
TOP_GUAGE = 300.0

CSS = """
@page { size: A4 portrait; margin: 10mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:0; }
h1 { font-size: 30px; margin:0 0 3px 0; }
h2 { font-size: 18px; text-transform:uppercase; letter-spacing:1px; color:#5a5a5a; margin:11px 0 4px 0; border-bottom:2px solid #cfcfcf; padding-bottom:3px;}
.sub { font-size:17px; color:#444; margin-bottom:6px; line-height:1.34; }
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
.dimtxt { fill:#222; font-size:14px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }
.dimtxt.v { text-anchor:start; }
.wall { fill:#e3d9c6; stroke:#2a2a2a; stroke-width:1.3; }
.leg2 { fill:#cbb894; stroke:#2a2a2a; stroke-width:1.3; }
.div { stroke:#6f6f6f; stroke-width:1.0; stroke-dasharray:5 4; }
.gauge { stroke:#8a1f14; stroke-width:1.8; }
.glab { font-size:18px; fill:#8a1f14; text-anchor:middle; font-weight:bold; }
.vlab { font-size:18px; fill:#2a2a2a; text-anchor:middle; font-weight:bold; }
.plab { font-size:16px; fill:#3a3a3a; text-anchor:start; }

.vt { text-anchor:start; font-size:17px; font-weight:bold; fill:#3a3a3a; letter-spacing:0.4px; }
.cap { font-size:16px; color:#444; margin:2px auto 8px auto; max-width:690px; line-height:1.28; text-align:center; }
table { width:100%; border-collapse:collapse; font-size:17px; }
th,td { text-align:left; padding:5px 6px; border-bottom:1px solid #ddd; vertical-align:top; }
th { color:#5a5a5a; font-weight:700; text-transform:uppercase; font-size:14px; letter-spacing:0.4px;}
.q { font-size:17px; background:#fff6e8; border:1px solid #e8d3a8; padding:8px 10px; margin-top:9px; border-radius:3px; }
.q ul { margin:4px 0; padding-left:17px; }
.q li { margin:2px 0; }
.tag { display:inline-block; font-size:15px; border:1px solid #999; border-radius:3px; padding:2px 8px; margin-left:8px; color:#555; vertical-align:middle; }
.steps td { padding:8px; line-height:1.32; font-size:17px; }
.steps th { font-size:14px; }
.steps td ul { margin:3px 0; padding-left:16px; }
.steps td li { margin:2px 0; }
.num { font-weight:800; color:#8a1f14; text-align:center; font-size:22px; }
.hl { fill:#f4b183; stroke:#a8410f; stroke-width:1.3; }
.hline { stroke:#a8410f; stroke-width:2.4; fill:none; }
.screw { fill:#8a1f14; }
.steps_grid { display:grid; grid-template-columns:1fr 1fr; gap:6px 9px; }
.tile { border:1px solid #ddd; border-radius:5px; padding:5px 7px 6px 7px; }
.tile svg { display:block; margin:1px auto 3px auto; }
.tnum { display:inline-block; font-weight:800; color:#fff; background:#8a1f14; border-radius:3px; font-size:14px; padding:1px 7px; }
.tcap { font-size:15px; line-height:1.22; color:#222; }
.pg { page-break-before: always; }
.refgrid { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:6px; }
.refgrid figure { margin:0; border:1px solid #ddd; border-radius:5px; padding:5px; }
.refgrid img { width:100%; height:84mm; object-fit:cover; display:block; border-radius:3px; }
.refgrid figcaption { font-size:15px; color:#333; padding:4px 2px 0 2px; line-height:1.22; }
"""

def rotrect(cx, cy, length, width, ang, cls):
    return (f'<rect x="{-length/2:.1f}" y="{-width/2:.1f}" width="{length:.1f}" '
            f'height="{width:.1f}" class="{cls}" transform="translate({cx:.1f},{cy:.1f}) rotate({ang:.1f})"/>')

def legpoly(cx, cy, length, width, ang, cls):
    # A leg whose BOTTOM end is cut at 33deg (foot face horizontal, sits flat on the
    # ground), not square. Top end stays square to the axis. The foot is the horizontal
    # line through the bottom centre point, so the face runs 33deg off the square end.
    a  = math.radians(ang)
    ca, sa = math.cos(a), math.sin(a)
    L, W = length, width
    cot = ca/sa
    def pt(lx, ly):
        return (cx + lx*ca - ly*sa, cy + lx*sa + ly*ca)
    tl = pt(L/2.0,  W/2.0)
    tr = pt(L/2.0, -W/2.0)
    br = pt(-L/2.0 + (W/2.0)*cot, -W/2.0)   # where the flat foot meets the right edge
    bl = pt(-L/2.0 - (W/2.0)*cot,  W/2.0)   # where the flat foot meets the left edge
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (tl, tr, br, bl))
    return f'<polygon points="{pts}" class="{cls}"/>'

# ---------- HERO: the X joint (stage 1) ----------
def detail_svg():
    s = 0.40
    wx = 470
    pad = 56
    def sx(mx): return wx/2.0 + mx*s
    def sy(my): return pad + (vhalf - my)*s
    crossx, crossy = sx(0.0), sy(0.0)
    Lpx, Wpx = LEG*s, PW*s
    tpx = T*s
    e = []
    e.append(f'<line x1="30" y1="{sy(-vhalf)+4:.1f}" x2="{wx-30}" y2="{sy(-vhalf)+4:.1f}" class="ground"/>')
    # lower leg first (outside leg), then upper leg shifted up one thickness (inside leg)
    # both feet cut at 33deg: the foot face is flat on the ground
    e.append(legpoly(crossx, crossy, Lpx, Wpx, -(90.0-theta), 'leg'))
    e.append(legpoly(crossx, crossy - tpx, Lpx, Wpx, -(90.0+theta), 'leg'))
    # the crossing: upper leg lies on top of lower; one centre screw through both
    e.append(f'<circle cx="{crossx:.1f}" cy="{crossy-tpx/2:.1f}" r="5" class="screw"/>')
    # top spread dim, between the leg tips
    yt = sy(vhalf)-14
    e.append(f'<line x1="{sx(-half_inner):.1f}" y1="{yt:.1f}" x2="{sx(half_inner):.1f}" y2="{yt:.1f}" class="dim"/>')
    for xx in (-half_inner, half_inner):
        e.append(f'<line x1="{sx(xx):.1f}" y1="{yt-5:.1f}" x2="{sx(xx):.1f}" y2="{yt+5:.1f}" class="dim"/>')
    e.append(f'<rect x="{crossx-46:.1f}" y="{yt-9:.1f}" width="92" height="18" fill="#fff"/>')
    e.append(f'<text x="{crossx:.1f}" y="{yt:.1f}" class="dimtxt">{TOP_GUAGE:.0f} top, inside to inside</text>')
    # 700 leg dim along the right leg
    e.append(f'<text x="{sx(half)+30:.1f}" y="{sy(40):.1f}" class="dimtxt v" style="font-size:11px;">700 leg</text>')
    # crossing callout
    e.append(f'<line x1="{crossx+8:.1f}" y1="{crossy-6:.1f}" x2="{crossx+60:.1f}" y2="{crossy-40:.1f}" class="dim"/>')
    e.append(f'<text x="{crossx+64:.1f}" y="{crossy-42:.1f}" class="dimtxt v" style="font-size:11px;">upper leg on top</text>')
    # foot angle labels
    e.append(f'<text x="{sx(-half)-14:.1f}" y="{sy(-vhalf)+22:.1f}" class="dimtxt" style="font-size:11px;text-anchor:middle;">33&deg; foot</text>')
    e.append(f'<text x="{sx(half)+14:.1f}" y="{sy(-vhalf)+22:.1f}" class="dimtxt" style="font-size:11px;text-anchor:middle;">33&deg; foot</text>')
    # leg-tilt callouts at the crossing
    e.append(f'<line x1="{crossx:.1f}" y1="{crossy:.1f}" x2="{crossx:.1f}" y2="{crossy-vhalf*s*0.72:.1f}" class="dim" stroke-dasharray="4 3"/>')
    e.append(f'<text x="{crossx-6:.1f}" y="{crossy-vhalf*s*0.62:.1f}" class="dimtxt" style="font-size:12px;text-anchor:end;">{TILT_DEG:.1f}&deg; a side</text>')
    e.append(f'<text x="20" y="15" class="vt">X JOINT - stage 1</text>')
    return (f'<svg width="{wx}" height="{int(2*vhalf*s+2*pad):d}" viewBox="0 0 {wx} {int(2*vhalf*s+2*pad):d}">'
            + "".join(e) + '</svg>')

# ---------- stage tiles ----------
def xglyph(cx, cy, sz):
    hw = sz*math.tan(math.radians(33.0))   # true crossing: legs 33deg off vertical
    return (f'<line x1="{cx-hw:.1f}" y1="{cy-sz:.1f}" x2="{cx+hw:.1f}" y2="{cy+sz:.1f}" stroke="#2a2a2a" stroke-width="3.4" stroke-linecap="round"/>'
            f'<line x1="{cx+hw:.1f}" y1="{cy-sz:.1f}" x2="{cx-hw:.1f}" y2="{cy+sz:.1f}" stroke="#2a2a2a" stroke-width="3.4" stroke-linecap="round"/>')

def tile_svg(step):
    step = int(step)
    w, h = 150, 120
    e = []
    LX, RX, cy = 24, 126, 60
    if step == 1:
        e.append(xglyph(75, 54, 38))
        e.append('<circle cx="75" cy="54" r="4.5" fill="#8a1f14"/>')
        e.append('<text x="75" y="106" text-anchor="middle" font-size="11" fill="#8a1f14">33&deg; feet &middot; screw the centre</text>')
    else:
        e.append(xglyph(LX, cy, 24))
        e.append(xglyph(RX, cy, 24))
        bx0, bx1 = LX+20, RX-20
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
 "1":"<b>Stage 1 - the X legs.</b> Cut one end of each 700 leg at 33&deg;. Cross two: the upper leg lies straight <b>on top of</b> the lower one. Centre 350 along, 40 across, one screw through the middle. Make two, mirrored - one set inside, one outside, both at the same 300 top.",
 "2":"<b>Stage 2 - stand them and start the floor.</b> Stand the two X sets parallel, 300 top. Cut one <b>long edge</b> of the first 900 at <b>22.5&deg;</b> - the inner edge that lands on the far leg - so it beds into the V. The second lands one thickness (23&nbsp;mm) higher, so trim 23&nbsp;mm off its edge so both tops come level.",
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
      "<li>Four legs, 700 long. Cut <b>one end of each</b> at 33&deg; - all four off the <b>same saw setting</b>.</li>"
      "<li>Find the centre of each leg: 350 along, 40 across (half of 80).</li>"
      "<li>Clamp a straight plank to the table. Press the 33&deg; end flush against it.</li>"
      "<li>Lay the second leg <b>straight on top of the first</b> to make the X. Pilot hole at the centre.</li>"
      "<li>Drive a 35&nbsp;mm part-threaded screw down through both at the centre so the upper leg sits on the lower one.</li>"
      "<li>Then 3-4 more screws, or swap to a 6&nbsp;mm or 10&nbsp;mm bolt through the crossing.</li>"
      "<li>Set the <b>top to 300, inside corner to inside corner</b> - that is your gauge. Make the second set the same.</li></ul>",
      "<ul><li>One saw setting for all four feet = feet that sit level. Cut them one at a time and they fight.</li>"
      "<li>The clamped plank is the reference - it stops the X leaning while you screw.</li>"
      "<li>The legs do not notch into each other: one lies full-thickness on top of the other. That gives an inside leg and an outside leg.</li>"
      "<li>A single screw lets the X scissor. Extra screws or a bolt lock the crossing.</li>"
      "<li>300 top on both sets = the box sits level and the walls line up.</li></ul>"),
 ("2","<b>Stand them and lay the first two planks.</b><ul>"
      "<li>Stand the two X sets parallel, on the ground.</li>"
      "<li>Lay the first two 900 planks in the V, one front, one back.</li>"
      "<li>Cut <b>one long edge of the first plank at 22.5&deg;</b> - the inner edge where it meets the far leg - so it beds into the V.</li>"
      "<li>The second plank lands one thickness (23&nbsp;mm) higher, so <b>trim 23&nbsp;mm off</b> its edge so both tops come level.</li></ul>",
      "<ul><li>Both X sets parallel = the box goes up straight.</li>"
      "<li>The 22.5&deg; on the inner edge is what lets the plank bed into the V instead of rocking on the leg corner.</li>"
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


# ---------- cut diagram ----------
def cutdiag_svg():
    W = 470; sc = 0.26; x0 = 20; h = 13
    e = []
    def rect(x, y, L, cls='part'):
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{L:.1f}" height="{h}" class="{cls}" rx="1"/>'
    def lab(x, y, t):
        return f'<text x="{x:.1f}" y="{y:.1f}" class="dimtxt v" style="font-size:10px;">{t}</text>'
    y = 18
    L = 700*sc; dx = h*math.tan(math.radians(33))
    e.append(f'<polygon points="{x0+dx:.1f},{y} {x0+L:.1f},{y} {x0+L:.1f},{y+h} {x0:.1f},{y+h}" class="leg"/>')
    e.append(lab(x0+L+10, y+11, '4&times; leg 700 &middot; one end 33&deg;'))
    y += 40
    L = 900*sc
    e.append(rect(x0, y, L))
    e.append(lab(x0+L+10, y+11, '8&times; wall plank 900'))
    y += 40
    dx = h*math.tan(math.radians(22.5))
    e.append(f'<polygon points="{x0+dx:.1f},{y} {x0+L:.1f},{y} {x0+L:.1f},{y+h} {x0:.1f},{y+h}" class="part2"/>')
    e.append(lab(x0+L+10, y+11, '1st plank &middot; bottom edge 22.5&deg;'))
    y += 40
    e.append(rect(x0, y, L-23*sc))
    e.append(lab(x0+L+10, y+11, '2nd plank &middot; trim 23&nbsp;mm off'))
    y += 40
    e.append(f'<polygon points="{x0},{y+h} {x0+52},{y} {x0+96},{y} {x0+44},{y+h}" class="part"/>')
    e.append(lab(x0+106, y+11, '6&times; side piece &middot; scribed'))
    H = y + h + 14
    return f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(e)}</svg>'

# ---------- the 22.5 V panel ----------
def _poly(pts, cls):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" class="{cls}"/>'

def nest_svg():
    # END VIEW - looking along the trough at one X frame.
    # The pieces of the box LIE INSIDE the V of the legs; the leg tops stand proud above
    # the rim. Everything below is derived from Paul's own numbers:
    #   legs 700 x 80, 33deg off vertical, crossed at their centres, top gauge 300
    #   inside-to-inside; the trough sides lean in at 22.5 to a narrow bottom.
    GY   = LEG*math.cos(math.radians(TILT_DEG))                       # foot plane below the tops
    topx = TOP_GUAGE/2.0 + (PW/2.0)/math.cos(math.radians(TILT_DEG))  # leg centre at the top
    dx, dy = (topx - GY*math.tan(math.radians(TILT_DEG))) - topx, GY
    L = math.hypot(dx, dy); ux, uy = dx/L, dy/L
    nx, ny = uy, -ux
    def leg_pts(sign):
        cxt = sign*topx
        A = (cxt + nx*PW/2.0,  ny*PW/2.0)
        B = (cxt - nx*PW/2.0, -ny*PW/2.0)
        def edge(pp):
            t = (GY - pp[1])/uy
            return (pp[0] + ux*t, GY)
        C, D = edge(A), edge(B)
        pts = [A, B, D, C]
        if sign < 0: pts = [(-x, y) for (x, y) in pts]
        return pts
    rim    = 30.0
    rim_hw = 95.0
    def ox(y): return rim_hw - (y-rim)*math.tan(math.radians(V_BEVEL))
    def ix(y): return ox(y) - T/math.cos(math.radians(V_BEVEL))
    bot = 200.0
    def wall_pts(sign):
        return [(sign*ox(rim),rim),(sign*ox(bot),bot),(sign*ix(bot),bot),(sign*ix(rim),rim)]

    model = []
    # trough first - it sits INSIDE the V, so the legs are drawn over it
    for sgn in (-1, 1):
        model.append(('poly', wall_pts(sgn), 'wall'))
    for yy in (rim + (bot-rim)/3.0, rim + 2*(bot-rim)/3.0):
        for sgn in (-1, 1):
            model.append(('line', [(sgn*ix(yy), yy), (sgn*ox(yy), yy)], 'div'))
    model.append(('poly', leg_pts(-1), 'leg2'))
    model.append(('poly', leg_pts(1), 'leg'))
    model.append(('line', [(-246, GY), (246, GY)], 'ground'))

    xs = [p[0] for _, pts, _ in model for p in pts] + [-150.0, 150.0]
    ys = [p[1] for _, pts, _ in model for p in pts] + [-30.0, 0.0, GY+52.0]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    S = 0.50
    MX, MY = 42.0, 30.0
    Wpx = (maxx-minx)*S + 2*MX
    Hpx = (maxy-miny)*S + 2*MY
    def X(x): return MX + (x-minx)*S
    def Y(y): return MY + (y-miny)*S
    e = []
    for kind, pts, cls in model:
        if kind == 'poly':
            e.append('<polygon points="%s" class="%s"/>' % (" ".join("%.1f,%.1f" % (X(x), Y(y)) for x, y in pts), cls))
        else:
            e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="%s"/>' %
                     (X(pts[0][0]), Y(pts[0][1]), X(pts[1][0]), Y(pts[1][1]), cls))
    # the 300 gauge across the leg tops
    e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="gauge"/>' % (X(-150), Y(-16), X(150), Y(-16)))
    e.append('<text x="%.1f" y="%.1f" class="glab">300 gauge, inside to inside</text>' % (X(0), Y(-26)))
    e.append('<text x="%.1f" y="%.1f" class="vlab">the pieces lie inside the V of the legs</text>' % (X(0), Y(GY+34)))
    e.append('<text x="%.1f" y="%.1f" class="plab">legs stand proud</text>' % (X(232), Y(-34)))
    e.append('<text x="%.1f" y="%.1f" class="plab">22.5&deg; V</text>' % (X(rim_hw+36), Y(rim-6)))
    return ('<svg width="%.0f" height="%.0f" viewBox="0 0 %.0f %.0f">%s</svg>'
            % (Wpx, Hpx, Wpx, Hpx, "".join(e)))


def _datauri(path):
    import base64 as _b
    ext="jpeg"
    return "data:image/%s;base64,%s" % (ext, _b.b64encode(open(path,"rb").read()).decode())
REF={"ref_joint.jpg":"ref_joint.jpg","ref_foot.jpg":"ref_foot.jpg","ref_floor.jpg":"ref_floor.jpg","ref_top.jpg":"ref_top.jpg"}

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<h1>X-Leg Herb Trough <span class="tag">your build &middot; v4</span></h1>
<div class="sub"><ul>
<li>Your numbers. Two X-leg frames carry a 900&nbsp;long trough between them.</li>
<li>Legs <b>4&times;700</b>, one end cut 33&deg;. Cross planks <b>8&times;900</b>, four front and four back. Planks 80 wide &times; 23 thick.</li>
<li><b>The X is set by the top.</b> Both leg tops sit <b>300 apart, inside corner to inside corner</b> - that is your gauge, and you cut to it so every X matches.</li>
<li>The two legs do not notch: the upper leg lies straight <b>on top of</b> the lower one, so there is an inside leg and an outside leg.</li>
<li>The pieces that close the ends are not cut to a number. They <b>lie inside the V of the legs</b> and are <b>scribed off an offcut</b>, one on top of the last.</li>
<li>Shown at 900 long, four planks deep. Dimensions in mm.</li></ul></div>

<div class="draw">{detail_svg()}</div>
<div class="cap"><b>Stage 1 - the joint that decides the box.</b> Two 700 legs crossed at their centres, upper leg lying on the lower, top set to 300. Get the foot flush on the clamped plank and the top to 300 and the frame stands true - and both frames match.</div>

<div class="pg">
<h2>Cut list</h2>
<table>
  <tr><th>Part</th><th>Qty</th><th>Length</th><th>Width</th><th>Thick</th><th>Note</th></tr>
  <tr><td>Leg</td><td>4</td><td>700</td><td>80</td><td>23</td><td>one end cut 33&deg;, all four one setting</td></tr>
  <tr><td>Cross plank (wall)</td><td>8</td><td>900</td><td>80</td><td>23</td><td>4 front, 4 back</td></tr>
  <tr><td>Side piece</td><td>6</td><td>scribed</td><td>80</td><td>23</td><td>3 per end, marked off an offcut</td></tr>
  <tr><td>- of those, the bottom pair</td><td>2</td><td>900</td><td>80</td><td>23</td><td>first plank's inner long edge cut 22.5&deg; into the V; second trimmed 23&nbsp;mm</td></tr>
</table>
<h2>Material</h2>
<div class="sub" style="font-size:15px;"><ul>
<li>Untreated pine or hardwood. Untreated: it is a food bed.</li>
<li><b>35&nbsp;mm part-threaded screws</b> for the crossing and the side courses.</li>
<li>A <b>6&nbsp;mm or 10&nbsp;mm bolt</b> through each crossing if you want it to never move.</li>
<li>Stainless or coated only. Wood oil (Woodoc) outside and on the feet.</li>
</ul></div>
<div class="q"><b>Two rules that decide this build</b><ul>
<li><b>One saw setting for all four feet.</b> Cut every 33&deg; end off the same stop. One foot cut on its own and the box stands on three legs.</li>
<li><b>Lock the crossing.</b> A single screw lets the X scissor. Add 3-4 screws, or bolt it.</li></ul></div>
<div class="q"><b>Locked in from your build photos (14 Oct)</b><ul>
<li><b>Top = 300, inside corner to inside corner.</b> Your gauge to check every X comes out the same.</li>
<li><b>Feet cut at 33&deg;</b> so they sit flat. Method: clamp a plank, leg flush, one centre screw into the middle of the plank.</li>
<li><b>The two legs cross one on top of the other.</b> No notch - the upper leg lies full-thickness on the lower, so there is an inside leg and an outside leg.</li>
<li><b>Spacer blocks at the shoulder.</b> Small blocks fill the gap between the angled leg head and the underside of the first planks. Drawn from the ~60 and ~75&nbsp;mm marks in your shots.</li>
<li><b>One wall flush, one proud.</b> The back planks run <b>flush to the outside leg</b>; the front planks stand <b>23&nbsp;mm proud</b> (one plank thickness), as in your shots.</li>
</ul></div>
</div>

<div class="pg">
<h1 style="font-size:23px;">Cut list, drawn <span class="tag">what to cut</span></h1>
<div class="sub">Every cut in the build. Two angles hold the whole thing: <b>33&deg;</b> on the leg, <b>22.5&deg;</b> in the V, and the rest square.</div>
<div class="draw">{cutdiag_svg()}</div>
<h2>Where the planks sit</h2>
<div class="draw">{nest_svg()}</div>
<div class="cap"><b>End view: the pieces lie inside the V of the legs.</b> The trough is not a tray sitting on top - it drops down inside the X, both long sides leaning in at 22.5&deg; to a narrow bottom, and the leg tops stand proud above the rim. The lowest plank's bottom edge is cut at 22.5&deg; so it sits level; the next lands one thickness (23&nbsp;mm) higher, so trim 23&nbsp;mm off its edge and the tops come level.</div>
<div class="q"><b>The two angles that fool everyone</b><ul>
<li>33&deg; is the <b>leg</b> - the foot cut and the lean, one saw setting. Nothing else is 33&deg;.</li>
<li>22.5&deg; is the <b>V</b> - how far each side leans in, and the cut on the lowest plank's bottom edge to match it.</li>
<li>Each side above that is <b>scribed</b> off an offcut stood in the V, not set to a number.</li></ul></div>
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

<div class="pg">
<h1 style="font-size:23px;">Your build, 14 Oct <span class="tag">reference</span></h1>
<div class="sub">The four shots you sent. These are the ones the drawings answer to.</div>
<div class="refgrid">
<figure><img src="file:///workspace/plan/ref_joint.jpg"><figcaption><b>The X joint.</b> The upper leg lies on top of the lower - no notch. One screw through the centre.</figcaption></figure>
<figure><img src="file:///workspace/plan/ref_foot.jpg"><figcaption><b>The foot.</b> The 33&deg; cut sitting flat, and the crossing above it with the centre screw in.</figcaption></figure>
<figure><img src="file:///workspace/plan/ref_floor.jpg"><figcaption><b>The floor.</b> First planks laid across, sitting in the V of the two frames.</figcaption></figure>
<figure><img src="file:///workspace/plan/ref_top.jpg"><figcaption><b>Top view of the set.</b> Crossed legs on the tray, tape marks where you set the spread and the angle.</figcaption></figure>
</div>
</div>

</body></html>'''

open("/workspace/plan/herb-box-v4.html","w").write(html)
print("html", len(html), "tilt", TILT_DEG, "inner", round(2*half_inner,1), "vhalf", round(vhalf,1))
