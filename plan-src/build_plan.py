#!/usr/bin/env python3
# The Offcut Feeder - one-page dimensioned plan generator.
# Model units: millimetres. d = depth axis, l = length axis, z = up from tray base.
import math

W, L, H, T, FLOOR, PITCH, OH = 145, 340, 50, 18, 18, 25, 15
HALF = W / 2.0
SLOPE = math.tan(math.radians(PITCH))
APEX = 198
RIDGE_U = APEX - T
def eave_u(d):   # roof underside height directly above d
    return RIDGE_U - abs(d - HALF) * SLOPE
ROOF_LOW = RIDGE_U - (HALF + OH) * SLOPE
ROOF_L = L + 2 * 20
ROD_Z = 170

def dl(x1, y1, x2, y2, label, vert=False):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="dim"/>'
            f'<line x1="{x1:.1f}" y1="{y1-5:.1f}" x2="{x1:.1f}" y2="{y1+5:.1f}" class="dim"/>'
            f'<line x1="{x2:.1f}" y1="{y2-5:.1f}" x2="{x2:.1f}" y2="{y2+5:.1f}" class="dim"/>'
            f'<text x="{(x1+x2)/2:.1f}" y="{(y1+y2)/2:.1f}" '
            f'transform="rotate({"90" if vert else "0"} {(x1+x2)/2:.1f} {(y1+y2)/2:.1f})" class="dimtxt">{label}</text>')

# ---------- END ELEVATION (looking along length) ----------
S1 = 1.38
ex = lambda d: 34 + (d + OH) * S1
ey = lambda z: 18 + (APEX - z) * S1
g = []
g.append(f'<polygon points="{ex(0):.1f},{ey(FLOOR):.1f} {ex(W):.1f},{ey(FLOOR):.1f} {ex(W):.1f},{ey(eave_u(W)):.1f} {ex(HALF):.1f},{ey(RIDGE_U):.1f} {ex(0):.1f},{ey(eave_u(0)):.1f}" class="part fill"/>')
g.append(f'<rect x="{ex(0):.1f}" y="{ey(FLOOR):.1f}" width="{W*S1:.1f}" height="{FLOOR*S1:.1f}" class="fill2"/>')
g.append(f'<line x1="{ex(-OH):.1f}" y1="{ey(ROOF_LOW):.1f}" x2="{ex(HALF):.1f}" y2="{ey(RIDGE_U):.1f}" class="line2"/>')
g.append(f'<line x1="{ex(W+OH):.1f}" y1="{ey(ROOF_LOW):.1f}" x2="{ex(HALF):.1f}" y2="{ey(RIDGE_U):.1f}" class="line2"/>')
g.append(f'<polygon points="{ex(-OH):.1f},{ey(ROOF_LOW):.1f} {ex(HALF):.1f},{ey(RIDGE_U):.1f} {ex(HALF):.1f},{ey(APEX):.1f} {ex(-OH):.1f},{ey(ROOF_LOW+T):.1f}" class="part fill"/>')
g.append(f'<polygon points="{ex(W+OH):.1f},{ey(ROOF_LOW):.1f} {ex(HALF):.1f},{ey(RIDGE_U):.1f} {ex(HALF):.1f},{ey(APEX):.1f} {ex(W+OH):.1f},{ey(ROOF_LOW+T):.1f}" class="part fill"/>')
g.append(f'<rect x="{ex(HALF-10):.1f}" y="{ey(APEX):.1f}" width="{20*S1:.1f}" height="{20*S1:.1f}" class="part fill"/>')
g.append(f'<circle cx="{ex(HALF):.1f}" cy="{ey(ROD_Z):.1f}" r="3.5" class="hole"/>')
g.append(f'<line x1="{ex(-OH)-14:.1f}" y1="{ey(0):.1f}" x2="{ex(W+OH)+14:.1f}" y2="{ey(0):.1f}" class="ground"/>')
g.append(dl(ex(0), ey(0)+38, ex(W), ey(0)+38, str(W)))
g.append(dl(ex(-OH), ey(0)+58, ex(W+OH), ey(0)+58, f"{W+2*OH}"))
g.append(f'<line x1="{ex(W)+20:.1f}" y1="{ey(0)-5:.1f}" x2="{ex(W)+20:.1f}" y2="{ey(H)+5:.1f}" class="dim"/>'
         f'<line x1="{ex(W)+16:.1f}" y1="{ey(0):.1f}" x2="{ex(W)+24:.1f}" y2="{ey(0):.1f}" class="dim"/>'
         f'<line x1="{ex(W)+16:.1f}" y1="{ey(H):.1f}" x2="{ex(W)+24:.1f}" y2="{ey(H):.1f}" class="dim"/>'
         f'<text x="{ex(W)+26:.1f}" y="{(ey(0)+ey(H))/2:.1f}" class="dimtxt">{H}</text>')
g.append(f'<line x1="{ex(W)+52:.1f}" y1="{ey(0)-5:.1f}" x2="{ex(W)+52:.1f}" y2="{ey(APEX)-5:.1f}" class="dim"/>'
         f'<line x1="{ex(W)+48:.1f}" y1="{ey(0):.1f}" x2="{ex(W)+56:.1f}" y2="{ey(0):.1f}" class="dim"/>'
         f'<line x1="{ex(W)+48:.1f}" y1="{ey(APEX):.1f}" x2="{ex(W)+56:.1f}" y2="{ey(APEX):.1f}" class="dim"/>'
         f'<text x="{ex(W)+58:.1f}" y="{(ey(0)+ey(APEX))/2:.1f}" class="dimtxt">{APEX}</text>')
end_svg = "\n".join(g)

# ---------- SIDE ELEVATION (looking along depth) ----------
S2 = 1.00
sx = lambda l: 30 + (l + 20) * S2
sy = lambda z: 18 + (APEX - z) * S2
s = []
s.append(f'<rect x="{sx(0):.1f}" y="{sy(H):.1f}" width="{L*S2:.1f}" height="{H*S2:.1f}" class="part fill"/>')
s.append(f'<line x1="{sx(0):.1f}" y1="{sy(FLOOR):.1f}" x2="{sx(L):.1f}" y2="{sy(FLOOR):.1f}" class="line2"/>')
s.append(f'<rect x="{sx(0):.1f}" y="{sy(APEX):.1f}" width="{T*S2:.1f}" height="{APEX*S2:.1f}" class="part fill"/>')
s.append(f'<rect x="{sx(L-T):.1f}" y="{sy(APEX):.1f}" width="{T*S2:.1f}" height="{APEX*S2:.1f}" class="part fill"/>')
s.append(f'<rect x="{sx(T):.1f}" y="{sy(RIDGE_U):.1f}" width="{(L-2*T)*S2:.1f}" height="{20*S2:.1f}" class="part fill"/>')
s.append(f'<polygon points="{sx(-20):.1f},{sy(ROOF_LOW):.1f} {sx(L+20):.1f},{sy(ROOF_LOW):.1f} {sx(L+20):.1f},{sy(ROOF_LOW+T):.1f} {sx(-20):.1f},{sy(ROOF_LOW+T):.1f}" class="part fill"/>')
s.append(f'<line x1="{sx(-20):.1f}" y1="{sy(APEX):.1f}" x2="{sx(L+20):.1f}" y2="{sy(APEX):.1f}" class="line2"/>')
s.append(f'<line x1="{sx(0):.1f}" y1="{sy(H):.1f}" x2="{sx(L):.1f}" y2="{sy(H):.1f}" class="line2"/>')
for l in (60, 120, 220, 280):
    s.append(f'<circle cx="{sx(l):.1f}" cy="{sy(FLOOR/2):.1f}" r="2.6" class="hole"/>')
s.append(f'<line x1="{sx(T):.1f}" y1="{sy(ROD_Z):.1f}" x2="{sx(L-T):.1f}" y2="{sy(ROD_Z):.1f}" class="rod"/>')
s.append(f'<rect x="{sx(0)-3:.1f}" y="{sy(ROD_Z)-4:.1f}" width="7" height="8" class="part fill"/>')
s.append(f'<rect x="{sx(L)-4:.1f}" y="{sy(ROD_Z)-4:.1f}" width="7" height="8" class="part fill"/>')
s.append(f'<line x1="{sx(-20)-14:.1f}" y1="{sy(0):.1f}" x2="{sx(L+20)+14:.1f}" y2="{sy(0):.1f}" class="ground"/>')
s.append(dl(sx(0), sy(0)+38, sx(L), sy(0)+38, str(L)))
s.append(dl(sx(-20), sy(0)+58, sx(L+20), sy(0)+58, str(ROOF_L)))
side_svg = "\n".join(s)

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 landscape; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:9mm; }}
h1 {{ font-size: 19px; margin:0 0 1px 0; }}
h2 {{ font-size: 10px; text-transform:uppercase; letter-spacing:1px; color:#6b6b6b; margin:11px 0 3px 0; border-bottom:1px solid #d8d8d8; padding-bottom:2px;}}
.sub {{ font-size:10px; color:#555; margin-bottom:5px;}}
.wrap {{ display:flex; gap:14px; align-items:flex-start; }}
.views {{ flex: 0 0 520px; }}
.side {{ flex: 1 1 auto; font-size:10px; }}
svg {{ display:block; }}
.part {{ fill:#efe8dc; stroke:#2a2a2a; stroke-width:1; }}
.fill2 {{ fill:#dcd2c2; stroke:#2a2a2a; stroke-width:1; }}
.line2 {{ stroke:#2a2a2a; stroke-width:0.9; fill:none;}}
.hole {{ fill:#fff; stroke:#2a2a2a; stroke-width:0.9;}}
.rod {{ stroke:#b23b2e; stroke-width:2.4; }}
.ground {{ stroke:#2a2a2a; stroke-width:1.6; }}
.dim {{ stroke:#7a7a7a; stroke-width:0.7; }}
.dimtxt {{ fill:#333; font-size:9px; text-anchor:middle; dominant-baseline:middle; }}
.vt {{ text-anchor:start; font-size:9px; fill:#6b6b6b; }}
.note {{ font-size:9px; fill:#8a1f14; text-anchor:middle; }}
.cap {{ font-size:9px; color:#666; margin-top:2px; }}
table {{ width:100%; border-collapse:collapse; font-size:9.5px; }}
th,td {{ text-align:left; padding:2px 3px; border-bottom:1px solid #e4e4e4; }}
th {{ color:#6b6b6b; font-weight:600; text-transform:uppercase; font-size:8px; letter-spacing:0.4px;}}
.q {{ font-size:9.5px; background:#fff6e8; border:1px solid #e8d3a8; padding:5px 7px; margin-top:8px;}}
.tag {{ display:inline-block; font-size:8.5px; border:1px solid #999; border-radius:8px; padding:0 5px; margin-left:6px; color:#555;}}
</style></head><body>
<h1>The Offcut Feeder <span class="tag">Mark &middot; piece 01 &middot; v1</span></h1>
<div class="sub">Hanging platform feeder from untreated Baltic pine. No glue. One tool-free joint. Comes apart to clean. Dimensions in mm.</div>
<div class="wrap">
  <div class="views">
    <svg width="520" height="356" viewBox="0 0 520 356">
      {end_svg}
      <text x="34" y="12" class="vt">END ELEVATION</text>
    </svg>
    <div class="cap">Roof pitch 25&deg;. Eave 146, ridge 180. Tray 145 wide, walls 50 deep.</div>
    <svg width="520" height="288" viewBox="0 0 520 288">
      {side_svg}
      <text x="34" y="12" class="vt">SIDE ELEVATION</text>
    </svg>
    <div class="cap">Red line: M6 stainless rod through both end walls and the ridge beam, wing nut each end &mdash; the one joint. Undo it and the roof lifts off.</div>
  </div>
  <div class="side">
    <h2>Cut list</h2>
    <table>
      <tr><th>Part</th><th>Qty</th><th>L</th><th>W</th><th>T</th></tr>
      <tr><td>End wall / gable</td><td>2</td><td>198</td><td>145</td><td>18</td></tr>
      <tr><td>Tray floor</td><td>1</td><td>340</td><td>145</td><td>18</td></tr>
      <tr><td>Tray long wall</td><td>2</td><td>304</td><td>50</td><td>18</td></tr>
      <tr><td>Roof panel</td><td>2</td><td>380</td><td>100</td><td>18</td></tr>
      <tr><td>Ridge cap</td><td>1</td><td>380</td><td>20</td><td>20</td></tr>
      <tr><td>Ridge beam (clamp)</td><td>1</td><td>304</td><td>20</td><td>20</td></tr>
    </table>
    <div class="sub" style="margin-top:3px;">End-wall top edge cut to the 25&deg; pitch: 146 at the eaves, 180 at the ridge. Roof panels mitred at the ridge.</div>

    <h2>Material</h2>
    <div><b>Untreated</b> Baltic pine, 38 &times; 150 &times; 900, resawn to two 18&nbsp;mm boards. Nothing treated touches this.</div>

    <h2>Hardware &amp; finish</h2>
    <div>M6 stainless threaded rod &times; 350, 2 wing nuts, 2 washers &mdash; the one joint.<br>
    Stainless screws 4&times;40, approx 22.<br>
    Woodoc sealer, all faces, 2 coats. Tray interior left bare.</div>

    <h2>Water &amp; service</h2>
    <div>Roof overhang 15&nbsp;mm eaves, 20&nbsp;mm gables. 4 &times; &Oslash;6 drain holes. 50&nbsp;mm walls hold seed above the wet line.<br>
    Rod out &rarr; roof off &rarr; tray lifts out. No tools.</div>

    <h2>Hanging</h2>
    <div>&Oslash;8 hole through the ridge cap at centre, cord or chain. ~2&nbsp;m up, ~3&nbsp;m clear of trees.</div>

    <h2>Basis</h2>
    <div style="font-size:9px;">Proportions after published platform-feeder plans (Cabin Life covered seed tray; Birdwatching-Bliss long tray). Squirrel clearance 6&ndash;8&nbsp;ft from jump-offs, 5&ndash;6&nbsp;ft up (Cabin Life). Untreated wood for bird contact surfaces; treated avoided (NestWatch nest-box guidance; NPIC on CCA leaching).</div>

    <div class="q"><b>Set:</b> untreated Baltic pine (Paul's call). The treated truss offcut is out &mdash; it leaches on a food surface in the weather. Untreated pine needs re-oiling yearly.</div>
  </div>
</div>
</body></html>'''

open("/workspace/plan/offcut-feeder-plan.html", "w").write(html)
print("wrote html", len(html))
print("ROOF_LOW", round(ROOF_LOW,1), "eave_u(0)", round(eave_u(0),1), "RIDGE_U", RIDGE_U)
