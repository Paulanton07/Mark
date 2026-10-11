#!/usr/bin/env python3
# Paul's own planter box - build guide v3 (phone-readable A4 portrait).
# Draws Paul's spec: stacked 800x400 frame rings (long 800 OUTSIDE, short 400
# captured INSIDE, screwed from outside) held between four 600-tall corner legs.
# v3 adds Paul's real assembly: build the rings, stack them, screw the four legs
# from INSIDE the corners (box upside down), rip one 90x800 plank into two ~45
# rebate rails screwed underneath, turn over, then lay NINE 400-long floor boards
# across the bottom with gaps for drainage. Two products off one footprint:
# 3 rings deep (240 trough) and 2 rings (160).
# Pages: views / cut+material / picture sequence / steps 1-5 / steps 6-10.

# ---- Paul's numbers (mm) ----
LONG  = 800.0     # long plank length = o/a length (outside)
T     = 23.0      # plank thickness
PW    = 80.0      # plank width = one frame course high
SHORT = 400.0     # short plank length, captured between the longs
OUTW  = SHORT + 2*T          # 446 o/a width
H     = 600.0     # leg length = o/a height
LEGW  = 80.0      # leg width
LEGT  = 2*T       # leg thickness = two planks face-to-face (46)
NF_TALL  = 3      # rings deep - tall version
NF_SHORT = 2      # rings deep - short version
TROUGH_TALL  = NF_TALL*PW    # 240
TROUGH_SHORT = NF_SHORT*PW   # 160
FLOOR_T = T
FLOOR_BOARDS = 9      # Paul: nine 400-long boards across the bottom (space by eye)
FLOOR_BW = 80.0       # board width = the 80 stock; ~4 mm gaps across the interior
REB_W = 45.0          # rebate rail width = a 90mm plank ripped down the middle
REB_L = LONG          # rails run the full length
REB_T = T

# ---- drawing helpers ----
S = 0.50
M = 70
TOPL = 26

def gx(x, ox=M): return ox + x*S
def gy(z, oy, Ht=H): return oy + (Ht - z)*S

CSS = """
@page { size: A4 portrait; margin: 10mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:0; }
h1 { font-size: 26px; margin:0 0 3px 0; }
h2 { font-size: 16px; text-transform:uppercase; letter-spacing:1px; color:#5a5a5a; margin:11px 0 4px 0; border-bottom:2px solid #cfcfcf; padding-bottom:3px;}
.sub { font-size:15px; color:#444; margin-bottom:6px; line-height:1.32; }
.draw { text-align:center; margin:5px 0 1px 0; }
.draw svg { display:block; margin:0 auto; }
.part { fill:#efe8dc; stroke:#2a2a2a; stroke-width:1.1; }
.part2 { fill:#e3d9c6; stroke:#2a2a2a; stroke-width:1.1; }
.leg { fill:#d9c9ad; stroke:#2a2a2a; stroke-width:1.2; }
.hidden { fill:#ffffff; stroke:#9a9a9a; stroke-width:0.8; stroke-dasharray:3 3; }
.liner { stroke:#2f6f8a; stroke-width:2.2; fill:none; stroke-dasharray:5 3; }
.soil { fill:#cfe3c2; opacity:0.55; stroke:#7a9a5a; stroke-width:0.8; }
.ground { stroke:#2a2a2a; stroke-width:1.8; }
.dim { stroke:#7a7a7a; stroke-width:0.8; }
.dimtxt { fill:#222; font-size:12px; text-anchor:middle; dominant-baseline:middle; paint-order:stroke; stroke:#ffffff; stroke-width:5px; }
.dimtxt.v { text-anchor:start; }
.vt { text-anchor:start; font-size:14px; font-weight:bold; fill:#3a3a3a; letter-spacing:0.4px; }
.cap { font-size:14px; color:#444; margin:2px auto 8px auto; max-width:690px; line-height:1.28; text-align:center; }
table { width:100%; border-collapse:collapse; font-size:16px; }
th,td { text-align:left; padding:5px 6px; border-bottom:1px solid #ddd; vertical-align:top; }
th { color:#5a5a5a; font-weight:700; text-transform:uppercase; font-size:13px; letter-spacing:0.4px;}
.q { font-size:15px; background:#fff6e8; border:1px solid #e8d3a8; padding:8px 10px; margin-top:9px; border-radius:3px; }
.tag { display:inline-block; font-size:13px; border:1px solid #999; border-radius:3px; padding:2px 8px; margin-left:8px; color:#555; vertical-align:middle; }
.steps td { padding:7px; line-height:1.3; font-size:16px; }
.steps th { font-size:13px; }
.num { font-weight:800; color:#8a1f14; text-align:center; font-size:18px; }
.hl { fill:#f4b183; stroke:#a8410f; stroke-width:1.3; }
.hline { stroke:#a8410f; stroke-width:2.4; fill:none; }
.oil { fill:#f6d9a8; stroke:#a87b1f; stroke-width:1; opacity:0.55; }
.future { fill:#ffffff; stroke:#c9c9c9; stroke-width:1; stroke-dasharray:3 3; }
.steps_grid { display:grid; grid-template-columns:1fr 1fr; gap:6px 9px; }
.tile { border:1px solid #ddd; border-radius:5px; padding:5px 7px 6px 7px; }
.tile svg { display:block; margin:1px auto 3px auto; }
.tnum { display:inline-block; font-weight:800; color:#fff; background:#8a1f14; border-radius:3px; font-size:12px; padding:1px 7px; }
.tcap { font-size:13px; line-height:1.22; color:#222; }
.pg { page-break-before: always; }
"""

# ---------- FRONT ELEVATION (long 800 face) ----------
def front_svg(nf):
    w = gx(LONG) + 150
    h = gy(0, TOPL) + 46
    e = []
    oy = TOPL + H*S
    def X(x): return gx(x)
    def Y(z): return oy - z*S
    e.append(f'<line x1="{X(0)-16:.1f}" y1="{Y(0):.1f}" x2="{X(LONG)+16:.1f}" y2="{Y(0):.1f}" class="ground"/>')
    tb = H - nf*PW
    # trough courses (long planks over the full width; their ends hide behind the legs)
    for i in range(nf):
        z0 = tb + i*PW
        e.append(f'<rect x="{X(0):.1f}" y="{Y(z0+PW):.1f}" width="{LONG*S:.1f}" height="{PW*S:.1f}" class="part"/>')
    # rebate rails under the bottom, running the full length (seen as a band)
    e.append(f'<rect x="{X(0):.1f}" y="{Y(tb):.1f}" width="{LONG*S:.1f}" height="{REB_T*S:.1f}" class="part2"/>')
    # floor board ends: nine ticks across, gaps between them (drainage)
    x0f, x1f = T, LONG-T
    pitch = (x1f-x0f)/FLOOR_BOARDS
    bw = FLOOR_BW
    for j in range(FLOOR_BOARDS):
        bx = x0f + j*pitch + (pitch-bw)/2
        e.append(f'<rect x="{X(bx):.1f}" y="{Y(tb+REB_T+FLOOR_T):.1f}" width="{bw*S:.1f}" height="{FLOOR_T*S:.1f}" class="part2"/>')
    # legs LAST, so they read as the OUTER members at the corners (Paul's correction)
    for x0 in (0.0, LONG-LEGW):
        e.append(f'<rect x="{X(x0):.1f}" y="{Y(H):.1f}" width="{LEGW*S:.1f}" height="{H*S:.1f}" class="leg"/>')
    # soil level line
    e.append(f'<line x1="{X(LEGW):.1f}" y1="{Y(H-20):.1f}" x2="{X(LONG-LEGW):.1f}" y2="{Y(H-20):.1f}" class="soil"/>')
    # dim: o/a length
    yb = Y(0)+30
    e.append(f'<line x1="{X(0):.1f}" y1="{yb:.1f}" x2="{X(LONG):.1f}" y2="{yb:.1f}" class="dim"/>')
    for xx in (0.0, LONG):
        e.append(f'<line x1="{X(xx):.1f}" y1="{yb-5:.1f}" x2="{X(xx):.1f}" y2="{yb+5:.1f}" class="dim"/>')
    e.append(f'<rect x="{(X(0)+X(LONG))/2-40:.1f}" y="{yb-9:.1f}" width="80" height="18" fill="#fff"/>')
    e.append(f'<text x="{(X(0)+X(LONG))/2:.1f}" y="{yb:.1f}" class="dimtxt">800 o/a</text>')
    # dim: leg width
    e.append(f'<line x1="{X(0):.1f}" y1="{Y(H)+22:.1f}" x2="{X(LEGW):.1f}" y2="{Y(H)+22:.1f}" class="dim"/>')
    e.append(f'<text x="{X(LEGW/2):.1f}" y="{Y(H)+34:.1f}" class="dimtxt">80</text>')
    # dim: trough depth (right)
    xd = X(LONG)+40
    e.append(f'<line x1="{xd:.1f}" y1="{Y(tb):.1f}" x2="{xd:.1f}" y2="{Y(H):.1f}" class="dim"/>')
    e.append(f'<rect x="{xd+3:.1f}" y="{(Y(tb)+Y(H))/2-9:.1f}" width="52" height="18" fill="#fff"/>')
    e.append(f'<text x="{xd+4:.1f}" y="{(Y(tb)+Y(H))/2:.1f}" class="dimtxt v">{nf*PW:.0f}</text>')
    # dim: height o/a
    xh = X(LONG)+96
    e.append(f'<line x1="{xh:.1f}" y1="{Y(0):.1f}" x2="{xh:.1f}" y2="{Y(H):.1f}" class="dim"/>')
    e.append(f'<rect x="{xh+3:.1f}" y="{(Y(0)+Y(H))/2-9:.1f}" width="52" height="18" fill="#fff"/>')
    e.append(f'<text x="{xh+4:.1f}" y="{(Y(0)+Y(H))/2:.1f}" class="dimtxt v">600</text>')
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">' + "".join(e) + \
           f'<text x="{M}" y="18" class="vt">FRONT ELEVATION (800 face)</text></svg>'

def front_wh(nf):
    return (gx(LONG)+150, gy(0, TOPL)+46)

# ---------- SIDE ELEVATION (446 end face) ----------
def side_svg(nf):
    w = gx(OUTW) + 150
    h = gy(0, TOPL) + 46
    e = []
    oy = TOPL + H*S
    def X(x): return gx(x)
    def Y(z): return oy - z*S
    e.append(f'<line x1="{X(0)-16:.1f}" y1="{Y(0):.1f}" x2="{X(OUTW)+16:.1f}" y2="{Y(0):.1f}" class="ground"/>')
    tb = H - nf*PW
    # short-plank courses (400 wide) between the legs
    for i in range(nf):
        z0 = tb + i*PW
        e.append(f'<rect x="{X(LEGT):.1f}" y="{Y(z0+PW):.1f}" width="{SHORT*S:.1f}" height="{PW*S:.1f}" class="part"/>')
    # rebate rails seen end-on: one block at each long wall, screwed underneath
    e.append(f'<rect x="{X(0):.1f}" y="{Y(tb):.1f}" width="{T*S:.1f}" height="{REB_T*S:.1f}" class="part2"/>')
    e.append(f'<rect x="{X(OUTW-T):.1f}" y="{Y(tb):.1f}" width="{T*S:.1f}" height="{REB_T*S:.1f}" class="part2"/>')
    # floor boards span the depth, seen here as one recessed band
    e.append(f'<rect x="{X(LEGT):.1f}" y="{Y(tb+REB_T+FLOOR_T):.1f}" width="{(OUTW-2*LEGT)*S:.1f}" height="{FLOOR_T*S:.1f}" class="part"/>')
    # legs LAST, end-on, the outer members at each corner
    for x0 in (0.0, OUTW-LEGT):
        e.append(f'<rect x="{X(x0):.1f}" y="{Y(H):.1f}" width="{LEGT*S:.1f}" height="{H*S:.1f}" class="leg"/>')
    # dims width
    yb = Y(0)+30
    e.append(f'<line x1="{X(0):.1f}" y1="{yb:.1f}" x2="{X(OUTW):.1f}" y2="{yb:.1f}" class="dim"/>')
    for xx in (0.0, OUTW):
        e.append(f'<line x1="{X(xx):.1f}" y1="{yb-5:.1f}" x2="{X(xx):.1f}" y2="{yb+5:.1f}" class="dim"/>')
    e.append(f'<rect x="{(X(0)+X(OUTW))/2-40:.1f}" y="{yb-9:.1f}" width="80" height="18" fill="#fff"/>')
    e.append(f'<text x="{(X(0)+X(OUTW))/2:.1f}" y="{yb:.1f}" class="dimtxt">446 o/a</text>')
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">' + "".join(e) + \
           f'<text x="{M}" y="18" class="vt">SIDE ELEVATION (end face)</text></svg>'

def side_wh(nf):
    return (gx(OUTW)+150, gy(0, TOPL)+46)

# ---------- PLAN VIEW (the assembly key) ----------
def plan_svg():
    w = gx(LONG) + 90
    h = gx(OUTW) + 90
    ox, oy = 50, 48
    def X(x): return ox + x*S
    def Y(y): return oy + y*S
    e = []
    # long planks front/back (full 800, horizontal bands)
    e.append(f'<rect x="{X(0):.1f}" y="{Y(0):.1f}" width="{LONG*S:.1f}" height="{T*S:.1f}" class="part"/>')
    e.append(f'<rect x="{X(0):.1f}" y="{Y(OUTW-T):.1f}" width="{LONG*S:.1f}" height="{T*S:.1f}" class="part"/>')
    # short planks captured inside (400 long, vertical bands at the ends)
    e.append(f'<rect x="{X(0):.1f}" y="{Y(T):.1f}" width="{T*S:.1f}" height="{SHORT*S:.1f}" class="part2"/>')
    e.append(f'<rect x="{X(LONG-T):.1f}" y="{Y(T):.1f}" width="{T*S:.1f}" height="{SHORT*S:.1f}" class="part2"/>')
    # legs at four corners
    for cx in (0.0, LONG-LEGW):
        for cy in (0.0, OUTW-LEGT):
            e.append(f'<rect x="{X(cx):.1f}" y="{Y(cy):.1f}" width="{LEGW*S:.1f}" height="{LEGT*S:.1f}" class="leg"/>')
    # dims
    yb = Y(OUTW)+30
    e.append(f'<line x1="{X(0):.1f}" y1="{yb:.1f}" x2="{X(LONG):.1f}" y2="{yb:.1f}" class="dim"/>')
    e.append(f'<rect x="{(X(0)+X(LONG))/2-40:.1f}" y="{yb-9:.1f}" width="80" height="18" fill="#fff"/>')
    e.append(f'<text x="{(X(0)+X(LONG))/2:.1f}" y="{yb:.1f}" class="dimtxt">800 o/a</text>')
    e.append(f'<line x1="{X(LONG)+26:.1f}" y1="{Y(0):.1f}" x2="{X(LONG)+26:.1f}" y2="{Y(OUTW):.1f}" class="dim"/>')
    e.append(f'<rect x="{X(LONG)+28:.1f}" y="{(Y(0)+Y(OUTW))/2-9:.1f}" width="42" height="18" fill="#fff"/>')
    e.append(f'<text x="{X(LONG)+29:.1f}" y="{(Y(0)+Y(OUTW))/2:.1f}" class="dimtxt v">446</text>')
    # inner 400 note
    e.append(f'<text x="{X(LONG/2):.1f}" y="{Y(OUTW/2):.1f}" class="dimtxt" style="font-size:14px;">400 inner clear (short plank inside)</text>')
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">' + "".join(e) + \
           f'<text x="{50}" y="22" class="vt">PLAN (top view) - one frame ring</text></svg>'

def plan_wh():
    return (gx(LONG)+90, gx(OUTW)+90)

# ---------- FLOOR DETAIL (nine boards, gaps for drainage) ----------
def floor_svg():
    w = gx(LONG) + 70
    h = gx(OUTW) + 66
    ox, oy = 40, 40
    def X(x): return ox + x*S
    def Y(y): return oy + y*S
    e = []
    # ring opening between the long walls
    e.append(f'<rect x="{X(T):.1f}" y="{Y(T):.1f}" width="{(LONG-2*T)*S:.1f}" height="{(OUTW-2*T)*S:.1f}" class="hidden"/>')
    # rebate rails: dashed, run the length under the board ends
    e.append(f'<rect x="{X(0):.1f}" y="{Y(T):.1f}" width="{LONG*S:.1f}" height="{REB_W*S:.1f}" class="hidden"/>')
    e.append(f'<rect x="{X(0):.1f}" y="{Y(OUTW-T-REB_W):.1f}" width="{LONG*S:.1f}" height="{REB_W*S:.1f}" class="hidden"/>')
    # nine boards across the length, gaps between (400 long each, spanning the depth)
    x0f, x1f = T, LONG-T
    pitch = (x1f-x0f)/FLOOR_BOARDS
    bw = FLOOR_BW
    for j in range(FLOOR_BOARDS):
        bx = x0f + j*pitch + (pitch-bw)/2
        e.append(f'<rect x="{X(bx):.1f}" y="{Y(T):.1f}" width="{bw*S:.1f}" height="{(OUTW-2*T)*S:.1f}" class="part"/>')
    yb = Y(OUTW)+28
    e.append(f'<line x1="{X(0):.1f}" y1="{yb:.1f}" x2="{X(LONG):.1f}" y2="{yb:.1f}" class="dim"/>')
    e.append(f'<rect x="{(X(0)+X(LONG))/2-58:.1f}" y="{yb-9:.1f}" width="116" height="18" fill="#fff"/>')
    e.append(f'<text x="{(X(0)+X(LONG))/2:.1f}" y="{yb:.1f}" class="dimtxt">9 boards, gaps for drainage</text>')
    return f'<svg width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}">' + "".join(e) + \
           f'<text x="{40}" y="22" class="vt">FLOOR (nine 400 boards, gaps between)</text></svg>'

def floor_wh():
    return (gx(LONG)+70, gx(OUTW)+66)

# ---------- progressive build tiles (front view) ----------
TILE_CAP = {
 "1":"Four legs. Two planks each, 600 long, screwed from the inside.",
 "2":"The frame rings: long 800 outside, short 400 captured inside.",
 "3":"Screw the rings: 60 mm from outside, through the long into the short.",
 "4":"Stack the rings on a table, one on top of the other.",
 "5":"Four legs on the OUTSIDE corners, screwed from inside. Box is upside down now.",
 "6":"Rip one 90x800 plank down the middle: two rails about 45 wide.",
 "7":"Screw the two rails underneath. That makes the rebate.",
 "8":"Turn it over. Nine 400 boards in the bottom, gaps between for drainage.",
 "9":"Liner over the floor and up the sides. Untreated only.",
 "10":"Oil outside and the feet. Position, fill, plant.",
}

def tile_svg(step, nf=3):
    step = int(step)
    w, h = 150, 120
    xmin, xmax = -16, LONG + 16
    zmin, zmax = -22, H + 12
    s = min((w-12)/(xmax-xmin), (h-12)/(zmax-zmin))
    ox = (w - (xmax-xmin)*s)/2 - xmin*s
    oy = (h - (zmax-zmin)*s)/2 + zmax*s
    X = lambda x: ox + x*s
    Y = lambda z: oy - z*s
    def rc(x0,x1,z0,z1,cls):
        return f'<rect x="{X(x0):.1f}" y="{Y(z1):.1f}" width="{(x1-x0)*s:.1f}" height="{(z1-z0)*s:.1f}" class="{cls}"/>'
    E = []
    tb = H - nf*PW
    def legs(hl=False):
        for x0 in (0.0, LONG-LEGW):
            E.append(rc(x0, x0+LEGW, 0, H, 'hl' if hl else 'leg'))
    def rings(cls='part'):
        for i in range(nf):
            z0 = tb + i*PW
            E.append(rc(0, LONG, z0, z0+PW, cls))
    if step == 1:
        legs(True)                                   # make the four legs
    elif step == 2:
        E.append(rc(0, LONG, tb, tb+PW, 'hl'))       # one ring: long outside...
        E.append(rc(0, T, tb+PW, tb+PW+SHORT*0.62, 'part2'))
        E.append(rc(LONG-T, T, tb+PW, tb+PW+SHORT*0.62, 'part2'))
    elif step == 3:
        E.append(rc(0, LONG, tb, tb+PW, 'hl'))       # ...screwed from outside
        for xx in (16, LONG-16):
            E.append(f'<line x1="{X(xx):.1f}" y1="{Y(tb+PW/2):.1f}" x2="{X(xx+22):.1f}" y2="{Y(tb+PW/2):.1f}" class="hline"/>')
    elif step == 4:
        rings('hl')                                  # stack the rings on a table
        E.append(f'<line x1="{X(-10):.1f}" y1="{Y(tb):.1f}" x2="{X(LONG+10):.1f}" y2="{Y(tb):.1f}" class="ground"/>')
    elif step == 5:
        rings(); legs(True)                          # legs on the corners, inside
    elif step == 6:
        for zc in (208.0, 330.0):                    # rip one plank into two rails
            E.append(rc(0, LONG, zc, zc+REB_W, 'hl'))
    elif step == 7:
        rings(); legs()
        E.append(rc(0, LONG, tb-REB_T, tb, 'hl'))    # rails underneath make the rebate
    elif step == 8:
        rings(); legs()
        E.append(rc(0, LONG, tb-REB_T, tb, 'part2'))
        x0f, x1f = T, LONG-T
        pitch = (x1f-x0f)/FLOOR_BOARDS
        bw = pitch*0.72
        for j in range(FLOOR_BOARDS):
            bx = x0f + j*pitch + (pitch-bw)/2
            E.append(rc(bx, bx+bw, tb, tb+FLOOR_T, 'hl'))
    else:
        rings(); legs()
        E.append(rc(0, LONG, tb-REB_T, tb, 'part2'))
        E.append(rc(T, LONG-T, tb, tb+FLOOR_T, 'part'))
        hlc = 'hline' if step == 9 else 'liner'
        E.append(f'<line x1="{X(LEGW+3):.1f}" y1="{Y(tb):.1f}" x2="{X(LEGW+3):.1f}" y2="{Y(H-4):.1f}" class="{hlc}"/>')
        E.append(f'<line x1="{X(LONG-LEGW-3):.1f}" y1="{Y(tb):.1f}" x2="{X(LONG-LEGW-3):.1f}" y2="{Y(H-4):.1f}" class="{hlc}"/>')
        if step >= 10:
            E.append(rc(0, LONG, tb, H, 'oil'))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{"".join(E)}</svg>'

def tiles_html(nf=3):
    out = ['<div class="steps_grid">']
    for n in TILE_CAP:
        out.append(f'<div class="tile"><span class="tnum">{n}</span>{tile_svg(n,nf)}<div class="tcap">{TILE_CAP[n]}</div></div>')
    out.append('</div>')
    return "\n".join(out)

# ---------- steps ----------
STEPS = [
 ("1","<b>Make the four legs.</b> Two planks 600&times;80 per leg, eight planks in all. Glue them and screw from the <b>inside</b> of each leg with 35&nbsp;mm screws, so they grip but cannot break through the two planks. Use the smooth-shank (part-threaded) screws here so they clamp the two planks tight (see the screw tip on the material page). Keep the ends flush; stand each leg on its end and check it does not rock.","Two planks screwed together make one stiff post from narrow stock. Screwing from the inside hides the heads and 35&nbsp;mm stops short of the 46&nbsp;mm thickness, so nothing breaks through the outside face. A smooth shank pulls the two planks together like a clamp; flush ends so the leg sits flat and the rim comes out level."),
 ("2","<b>Build the frame rings.</b> For each ring: lay the two long 800 planks outside, drop the two short 400 planks between them at the ends, flush top and bottom. Long planks run outside, short planks captured inside.","This is the ring that makes the box. Long outside means the screw heads and the end grain of the short planks are hidden on the outside where you screw."),
 ("3","<b>Screw the rings.</b> Drive 60&nbsp;mm screws from outside, through the long plank, into the end grain of the short plank. Two per end, pilot first, especially in the short ends.","60&nbsp;mm from outside reaches through the 23&nbsp;mm long plank and deep into the short end, so it clamps hard. Screwing from outside keeps the fixings off the inside face where the soil and liner sit."),
 ("4","<b>Stack the rings.</b> Lay the rings one on top of the other on a table, tight and flush, and check the corners are square and the stack does not rock.","Working flat on a table keeps the stack true. Square and flushed now, and the legs will pull it up straight."),
 ("5","<b>Fit the legs.</b> Stand the four legs on the four corners of the stack, on the <b>outside</b> of the rings so each leg runs the full height and the rings sit between them. Screw each leg from the <b>inside</b> of the corner, 35&nbsp;mm, so it cannot break through. The box is one unit now, sitting upside down.","Legs on the outside corners make them the outer frame; the rings nest inside them. Screwed from inside, the heads stay hidden and 35&nbsp;mm never breaks the 46&nbsp;mm leg. Upside down is the easiest way to land four legs on square and keep the rings flush between them."),
 ("6","<b>Rip the rail plank.</b> Take one plank 90&times;800 and rip it down the middle, so you have two rails about 45&nbsp;mm wide.","One board split in two gives a matched pair of rails, thin enough to step the floor down without eating the planting depth."),
 ("7","<b>Screw the rails underneath.</b> With the box still upside down, fix one rail under each long side, set in a little from the outer face. These two rails form the rebate the floor drops onto.","The rails sit proud of the underside by 23&nbsp;mm, which is exactly the rebate the boards rest in. Set in from the edge so they hide under the box and leave the leg feet clear."),
 ("8","<b>Turn it over and lay the floor.</b> Turn the box right way up. Cut nine boards 400 long and lay them across the bottom, resting on the two rebate rails, spaced by eye with an even gap between each. Screw the two end boards down.","Nine boards fill the bottom with gaps between, so water drains through instead of pooling on the soil. Boards run across the short way, so each is fixed only at its two ends. Gaps about finger-width; space them by eye."),
 ("9","<b>Line it.</b> Staple geotextile over the floor and up the inside of the walls to within 20&nbsp;mm of the rim. Fold the corners. Untreated timber only.","The liner keeps soil in and water moving, and keeps wet soil off bare timber. Untreated because it is a food bed and birds and hands touch it."),
 ("10","<b>Oil and place.</b> Wood oil on the outside faces, the rim and the leg feet, two coats. Set it level on clear ground, fill with free-draining mix, plant.","Outside and feet is where the weather sits. Clear, level feet spread the load and stop one corner sitting wet."),
]

def steps_table(rows):
    out = ['<table class="steps"><tr><th style="width:24px;">#</th><th style="width:48%;">Step</th><th>Why</th></tr>']
    for n, s, why in rows:
        out.append(f'<tr><td class="num">{n}</td><td>{s}</td><td>{why}</td></tr>')
    out.append('</table>')
    return "\n".join(out)

# ---------- cut lists ----------
def cut_table(nf):
    trough = nf*PW
    rows = [
      ("Long plank (frame)", str(2*nf), "800", "80", "23"),
      ("Short plank (frame)", str(2*nf), "400", "80", "23"),
      ("Leg plank", "8", "600", "80", "23"),
      ("Rebate rail (rip one 90&times;800 plank in two)", "2", "800", "45", "23"),
      ("Floor board", str(FLOOR_BOARDS), str(int(SHORT)), "80", "23"),
      ("Liner (geotextile)", "1", "1200", "500", "&mdash;"),
    ]
    out = ['<table><tr><th>Part</th><th>Qty</th><th>Length</th><th>Width</th><th>Thick</th></tr>']
    for r in rows:
        out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append('</table>')
    return out[0] + "".join(out[1:])

fw, fh = front_wh(NF_TALL)
sw, sh = side_wh(NF_TALL)
plw, plh = plan_wh()
flw, flh = floor_wh()

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<h1>Planter Box <span class="tag">your build &middot; drawn v5</span></h1>
<div class="sub">Your numbers. Stacked frame rings held between four corner legs. Long planks 800 run <b>outside</b>, short planks 400 are captured <b>inside</b>, screwed from the outside. The build order is the trick: rings first, stacked, then the four legs screwed from inside the corners with the box upside down. Two 45&nbsp;mm rails ripped from one plank go underneath to form a rebate, and <b>nine 400&nbsp;mm boards</b> lay across it as a drained floor. Two sizes off the same footprint: <b>three rings deep (240 trough)</b> and <b>two rings deep (160 trough)</b>, same 600 legs. Shown three rings, 600&times;446&times;600 outside. Dimensions in mm.</div>

<div class="draw">{front_svg(NF_TALL)}</div>
<div class="cap"><b>Front.</b> The four legs are the <b>outer</b> members, full height at the corners. The long 800 planks stack in courses <b>between</b> the legs; their ends run behind the legs, so the frame is set inside the leg. Trough sits in the top of the legs, rim flush at 600. Floor and rebate rails sit at the bottom of the trough.</div>

<div class="draw">{side_svg(NF_TALL)}</div>
<div class="cap"><b>End.</b> Overall 446 (the 400 short planks sit inside the two 23&nbsp;mm longs, so 400&nbsp;+&nbsp;46). The legs run full height on the outside at the corners; the short planks sit between them.</div>

<div class="pg">
<div class="draw">{plan_svg()}</div>
<div class="cap"><b>Plan, one ring.</b> Legs are the four corner posts; the ring is built between them, long planks outside, short planks captured inside. Get this ring right and the box is right.</div>

<div class="draw">{floor_svg()}</div>
<div class="cap"><b>Floor.</b> Nine 400&nbsp;mm boards across the top of the two rebate rails, even gaps between. That gap is the drainage.</div>
</div>

<div class="pg">
<h2>Cut list &mdash; three rings (240 trough)</h2>
{cut_table(3)}
<div class="q"><b>Two rings instead:</b> drop one long and one short pair, and shorten the trough to 160. Everything else, legs included, is identical. The six long and six short planks give you <b>two</b> boxes if you go two rings each.</div>
<h2>Material</h2>
<div class="sub" style="font-size:15px;"><b>Untreated pine</b> (heat-treated crate stock is fine) or hardwood. Untreated because it is a food bed. <b>60&nbsp;mm</b> screws for the frames, driven from outside. <b>35&nbsp;mm</b> screws for the legs, driven from the inside of each corner. One extra <b>90&times;800</b> plank, ripped down the middle for the two rebate rails. Stainless or coated only. Geotextile liner. Wood oil (Woodoc) outside and on the legs.</div>
<div class="q"><b>Tip from Paul &mdash; use screws with a shank, not fully-threaded.</b> There are two sorts: one where the thread runs the whole length, and one where the thread stops about three-quarters up and the top of the shank is <b>smooth</b>. Take the smooth-shank (part-threaded) sort. When you drive it through the first plank into the second, the smooth top turns in the first plank without gripping it, while the thread bites the second and pulls it in &mdash; so the screw works like a <b>clamp</b>, closing the two planks together. A fully-threaded screw grips both planks at once and can hold them apart instead of pulling them tight. This is the one to use on every two-plank joint here: the legs (two planks face to face) and the rebate rails. Most people never notice the difference.</div>
<h2>Drainage</h2>
<div class="sub" style="font-size:15px;">Nine boards with gaps between, sitting on the rebate rails; the liner goes over them. Water leaves the soil through the gaps and out of the bottom. Clear, level feet keep the base off wet ground.</div>
</div>

<div class="pg">
<h1 style="font-size:24px;">The build at a glance <span class="tag">picture sequence</span></h1>
<div class="sub">Ten steps, front view, in order. Highlighted part is what you add that step. Wording follows.</div>
{tiles_html(NF_TALL)}
</div>

<div class="pg">
<h1 style="font-size:24px;">How it goes together <span class="tag">steps 1&ndash;5</span></h1>
{steps_table(STEPS[0:5])}
</div>

<div class="pg">
<h1 style="font-size:24px;">How it goes together <span class="tag">steps 6&ndash;10</span></h1>
{steps_table(STEPS[5:10])}
</div>

</body></html>'''

open("/workspace/plan/planter-box-v5.html","w").write(html)
print("html", len(html))
