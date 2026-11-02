#!/usr/bin/env python3
"""Pedestal sink bird bath - one page layout sheet (proportions before the drawing)."""
import subprocess, pathlib, textwrap

OUT = pathlib.Path("/workspace/plan")
HTML = OUT / "sink-bath-proportions.html"
PDF = OUT / "sink-bath-proportions.pdf"

# ---- geometry for the elevation: mm scaled by S into a 360x400 viewBox ----
S = 0.35
CX = 150.0         # centre axis
G = 320.0          # ground datum (scaled)
RIM = G - 760 * S  # bowl rim y
BOWL_H = 150 * S
BOWL_W = 580 * S
BASE_W = 260 * S
STEM_TOP = 300 * S
BOWL_BOT = RIM + BOWL_H

def dim_v(x, y1, y2, label):
    mid = (y1 + y2) / 2
    return f'''
  <line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" class="dim"/>
  <line x1="{x-5}" y1="{y1}" x2="{x+5}" y2="{y1}" class="dim"/>
  <line x1="{x-5}" y1="{y2}" x2="{x+5}" y2="{y2}" class="dim"/>
  <text x="{x+6}" y="{mid+4}" class="dtext">{label}</text>'''

def dim_h(y, x1, x2, label):
    mid = (x1 + x2) / 2
    return f'''
  <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" class="dim"/>
  <line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" class="dim"/>
  <line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" class="dim"/>
  <text x="{mid}" y="{y-7}" class="dtext" text-anchor="middle">{label}</text>'''

bw, bw_bot = BOWL_W / 2, (BOWL_W - 60 * S) / 2
bowl = f'M {CX-bw} {RIM} L {CX+bw} {RIM} L {CX+bw_bot} {BOWL_BOT} L {CX-bw_bot} {BOWL_BOT} Z'
stem = (f'M {CX-STEM_TOP/2} {BOWL_BOT-3} L {CX+STEM_TOP/2} {BOWL_BOT-3} '
        f'L {CX+BASE_W/2} {G} L {CX-BASE_W/2} {G} Z')

elevation = f'''
<svg viewBox="0 0 360 400" class="fig">
  <line x1="14" y1="{G}" x2="300" y2="{G}" class="ground"/>
  <text x="16" y="{G-7}" class="gtext">ground</text>
  <path d="{bowl}" class="part"/>
  <path d="{stem}" class="part"/>
  <path d="M {CX-(BOWL_W-24)/2} {RIM+9} L {CX+(BOWL_W-24)/2} {RIM+9} L {CX+34} {BOWL_BOT-6} L {CX-34} {BOWL_BOT-6} Z" class="fill"/>
  <line x1="{CX-34}" y1="{RIM+13}" x2="{CX+34}" y2="{RIM+13}" class="water"/>
  <text x="{CX-bw-6}" y="{RIM+13}" class="note" text-anchor="end">water</text>
  <text x="{CX}" y="{BOWL_BOT-16}" class="note" text-anchor="middle">mortar bed</text>
  <line x1="{CX}" y1="20" x2="{CX}" y2="{G+8}" class="axis"/>
  {dim_v(CX+bw+16, RIM, BOWL_BOT, "150")}
  {dim_v(CX+bw+16, BOWL_BOT, G, "610")}
  {dim_v(CX+bw+58, RIM, G, "760")}
  {dim_h(G+20, CX-bw, CX+bw, "580")}
  {dim_h(G+44, CX-BASE_W/2, CX+BASE_W/2, "260")}
  <text x="{CX}" y="12" class="cap" text-anchor="middle">ELEVATION (mm)</text>
</svg>'''

plan = f'''
<svg viewBox="0 0 300 240" class="fig small">
  <text x="150" y="20" class="cap" text-anchor="middle">PLAN</text>
  <rect x="30" y="46" width="240" height="170" rx="16" class="part"/>
  <rect x="44" y="60" width="212" height="142" rx="10" class="inner"/>
  <rect x="44" y="150" width="212" height="52" class="fill"/>
  <text x="150" y="182" class="note" text-anchor="middle">sloped beach</text>
  <text x="150" y="200" class="note" text-anchor="middle">(one shallow end)</text>
  <circle cx="150" cy="120" r="16" class="drain"/>
  <text x="150" y="126" class="dtext" text-anchor="middle">drain</text>
  <text x="150" y="234" class="note" text-anchor="middle">keep the overflow slot open</text>
</svg>'''

BODY = f'''
<div class="sheet">
  <div class="kicker">Sheet 0 &middot; proportions before the drawing</div>
  <h1>Pedestal sink bird bath</h1>
  <p class="lede">A sink is the wrong depth for a bird. You don't fight that. You fill it:
  a bed of mortar and pebbles leaves a 30mm pan on top, rough underfoot, with one
  shallow end a bird can walk out of.</p>

  <div class="cols">
    <div class="figwrap">{elevation}<div class="caption">Height is the good news. Rim at 760 puts it
    in the 2.5&ndash;3ft band birds like, with cover behind it.</div></div>
    <div class="figwrap">{plan}<div class="caption">Slope one end of the bed, not the middle.
    A centre mound just hides the drain.</div></div>
  </div>

  <table>
    <tr><th>Number</th><th>Typical sink</th><th>What I use</th><th>Why</th></tr>
    <tr><td>Rim, ground to top</td><td>810</td><td>760</td><td>2.5&ndash;3ft: above cats, below cover</td></tr>
    <tr><td>Rim, across</td><td>560&ndash;610</td><td>your tape</td><td>the bowl is what you have, not a choice</td></tr>
    <tr><td>Rim, front to back</td><td>430&ndash;510</td><td>your tape</td><td>same</td></tr>
    <tr><td>Foot, across</td><td>240&ndash;280</td><td>your tape</td><td>sets the concrete pad</td></tr>
    <tr><td>Water depth</td><td>130&ndash;150 (the sink)</td><td>25&ndash;40</td><td>birds bathe in a puddle, not a pond</td></tr>
    <tr><td>Overflow slot</td><td>one, at the back</td><td>kept clear</td><td>it is your drain and your spillway</td></tr>
  </table>

  <div class="cols two">
    <div>
      <h2>Order of work</h2>
      <ol>
        <li>Set the sink on its side and tape the rim across, front to back, and the foot across. Photo it.</li>
        <li>Pour a pad 50mm bigger than the foot, 80mm thick, level. Bed the foot in while it is wet.</li>
        <li>Plug the drain from underneath with a disc of slate and mortar, or leave it open onto gravel.</li>
        <li>Fill the bowl to 30mm below the rim with a dry-ish mortar bed, then press pebbles into the top
            while it is still green. Rough is the point.</li>
        <li>Slope one end of the bed down to a wet edge so a bird can wade out, never a vertical wall.</li>
        <li>Cure three days, rinse twice, then let it rain once before you count it done.</li>
      </ol>
    </div>
    <div>
      <h2>What I won't print yet</h2>
      <p>A sealer or paint for the inside. Two sources online disagree and the ones I can read are
      selling a product. Pebbles and mortar don't need sealing. If you want colour, that is a question
      I answer when I have a maker's own data sheet, not a demo video.</p>
      <h2>Also true</h2>
      <p>Shade, within 3m of a shrub or fence, and nothing a cat can crouch behind. A bath in the open
      gets used once. One under cover gets used daily.</p>
    </div>
  </div>

  <div class="foot">Mark &middot; sheet 0 &middot; the drawing follows your two widths</div>
</div>'''

CSS = '''
@page { size: A4; margin: 12mm 12mm 10mm 12mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; color:#1d1b18; margin:0;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.sheet { width:100%; }
.kicker { font-family: Helvetica, Arial, sans-serif; font-size:9.5pt; letter-spacing:.14em;
          text-transform:uppercase; color:#8a6a3a; }
h1 { font-size:23pt; margin:2mm 0 1mm 0; font-weight:600; letter-spacing:-.01em; }
.lede { font-size:10.5pt; line-height:1.45; margin:0 0 4mm 0; max-width:135mm; color:#3a352e; }
.cols { display:flex; gap:6mm; align-items:flex-start; }
.cols.two > div { flex:1; }
.figwrap { flex:0 0 auto; }
.fig { width:66mm; height:auto; display:block; }
.fig.small { width:50mm; }
.caption { font-size:7.5pt; line-height:1.3; color:#5b5348; width:62mm; margin-top:1.5mm; }
svg .part { fill:#efe6d4; stroke:#3a332a; stroke-width:2; }
svg .inner { fill:#fbf8f1; stroke:#3a332a; stroke-width:1.4; }
svg .fill { fill:#cbb894; stroke:#7a6a4c; stroke-width:1.2; }
svg .water { stroke:#5f8ea8; stroke-width:2; stroke-dasharray:7 5; }
svg .ground { stroke:#3a332a; stroke-width:2.4; }
svg .axis { stroke:#b0483c; stroke-width:1; stroke-dasharray:10 4 2 4; }
svg .dim { stroke:#8a6a3a; stroke-width:1; }
svg .dtext { font-family: Helvetica, Arial, sans-serif; font-size:11px; fill:#6b5329; }
svg .note { font-family: Helvetica, Arial, sans-serif; font-size:10px; fill:#4a4338; }
svg .gtext { font-family: Helvetica, Arial, sans-serif; font-size:9px; fill:#6b6355; }
svg .cap { font-family: Helvetica, Arial, sans-serif; font-size:11px; letter-spacing:.16em; fill:#8a6a3a; }
svg .drain { fill:#fbf8f1; stroke:#3a332a; stroke-width:1.2; }
table { width:100%; border-collapse:collapse; margin:4mm 0 4mm 0; font-size:9pt; }
th { text-align:left; font-family: Helvetica, Arial, sans-serif; font-size:8pt; letter-spacing:.1em;
     text-transform:uppercase; color:#8a6a3a; border-bottom:1.5pt solid #3a332a; padding:0 2mm 1.5mm 0; }
td { padding:1.2mm 2mm 1.2mm 0; border-bottom:.4pt solid #d8cfbe; vertical-align:top; }
td:first-child { font-family: Helvetica, Arial, sans-serif; font-size:9pt; }
h2 { font-family: Helvetica, Arial, sans-serif; font-size:9pt; letter-spacing:.12em;
     text-transform:uppercase; color:#8a6a3a; margin:0 0 2mm 0; }
ol { margin:0 0 3mm 0; padding-left:5mm; font-size:9pt; line-height:1.38; }
ol li { margin-bottom:1.6mm; }
p { font-size:9pt; line-height:1.38; margin:0 0 2.5mm 0; }
.foot { font-family: Helvetica, Arial, sans-serif; font-size:8pt; color:#8a6a3a;
        border-top:.6pt solid #d8cfbe; padding-top:2mm; margin-top:2mm; }
'''

doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{BODY}</body></html>'
HTML.write_text(doc)
print("html", len(doc))

subprocess.run(["chromium", "--headless=new", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", f"--print-to-pdf={PDF}", str(HTML)],
               check=True, capture_output=True)
print("pdf", PDF.stat().st_size)

import fitz
d = fitz.open(PDF)
print("pages", d.page_count)
for i, p in enumerate(d):
    p.get_pixmap(dpi=140).save(f"/workspace/plan/sinkp{i+1}.png")
    print("png", i + 1)
