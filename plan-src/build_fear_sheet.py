#!/usr/bin/env python3
# Fear of Failure - 15 questions, one-page sheet (A4 portrait, phone-readable).
# Same visual language as the build guides: cream stock, oxblood accent, bullets.

ACTS = [
    ("Locate it", [
        "Name the one thing you're not doing because you might fail at it. The actual act, not the theme.",
        "Play the failure all the way to the last frame. What is that last frame?",
        "Who is in the room when it fails? Whose face do you see first?",
        "Say the outcome out loud as one sentence. Is it a loss, or a verdict on you?",
        "What does failing here actually cost: money, time, a person? Name the real thing, not the feeling.",
    ]),
    ("Weigh it", [
        "What is your evidence it would end that way? Split what you know from what you assume.",
        "Recall a time you failed at something. What did it actually cost you six months later?",
        "What did that failure hand you that success wouldn't have?",
        "What is the good-enough version of this, not the perfect one? Write it down.",
        "If you never try it, what does that cost you in a year? Price that too.",
    ]),
    ("Move", [
        "What are you protecting by not starting?",
        "What would you tell a friend standing exactly here?",
        "Write the headline you fear. Now write the headline most likely to actually run.",
        "What is the smallest first move that takes ten minutes or less?",
        "When will you do it, and who will you tell? You're reporting the attempt, not the result.",
    ]),
]

CSS = """
@page { size: A4 portrait; margin: 11mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:0; }
.head { border-bottom:3px solid #8a1f14; padding-bottom:6px; margin-bottom:9px; }
h1 { font-size:30px; margin:0; letter-spacing:0.2px; }
.kick { font-size:13px; text-transform:uppercase; letter-spacing:1.6px; color:#8a1f14; font-weight:700; margin:0 0 3px 0; }
.sub { font-size:14px; color:#444; margin-top:4px; line-height:1.3; }
.rule { background:#fff6e8; border:1px solid #e8d3a8; border-radius:4px; padding:7px 10px; font-size:13.5px; line-height:1.32; margin:0 0 10px 0; }
.act { margin-bottom:9px; page-break-inside:avoid; }
.acthead { display:flex; align-items:center; margin:0 0 4px 0; }
.badge { display:inline-block; background:#8a1f14; color:#fff; font-weight:800; font-size:13px;
         border-radius:4px; padding:2px 9px; margin-right:9px; letter-spacing:0.4px; }
.acttitle { font-size:17px; font-weight:800; color:#3a3a3a; letter-spacing:0.3px; }
.qs { margin:0; padding-left:0; list-style:none; }
.qs li { font-size:13.6px; line-height:1.33; padding:3.5px 0 3.5px 26px; position:relative; border-bottom:1px dotted #ddd; }
.qs li:last-child { border-bottom:none; }
.n { position:absolute; left:0; top:3.2px; font-weight:800; color:#8a1f14; font-size:13px; width:18px; text-align:right; }
.foot { margin-top:8px; border-top:2px solid #cfcfcf; padding-top:6px; font-size:13px; color:#3a3a3a; line-height:1.35; }
.foot b { color:#8a1f14; }
.sig { margin-top:5px; font-size:11.5px; color:#7a7a7a; letter-spacing:0.3px; }
"""

def build():
    p = []
    p.append('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>')
    p.append('<div class="head"><p class="kick">A walk, one page, 15 questions</p>')
    p.append('<h1>Fear of Failure</h1>')
    p.append('<p class="sub">Answer fast, in pen, one or two lines each. The first answer is usually the true one. Don\'t tidy it.</p></div>')
    p.append('<div class="rule">Work top to bottom. <b>Locate</b> the fear, <b>weigh</b> it against real evidence, then land on a <b>ten-minute move</b>. The questions do the work, not the prose.</div>')
    n = 1
    for i, (title, qs) in enumerate(ACTS, 1):
        p.append(f'<div class="act"><div class="acthead"><span class="badge">{i}</span><span class="acttitle">{title}</span></div><ul class="qs">')
        for q in qs:
            p.append(f'<li><span class="n">{n}</span>{q}</li>')
            n += 1
        p.append('</ul></div>')
    p.append('<div class="foot"><b>Do it on a walk if you can.</b> One question per pause. Answers come easier with your hands busy and nobody watching. '
             'You\'re reporting the attempt, not the result.</div>')
    p.append('<div class="sig">Mark 🛠️ &nbsp;·&nbsp; made with Paul</div>')
    p.append('</body></html>')
    return "\n".join(p)

if __name__ == "__main__":
    html = build()
    open("/workspace/plan/fear_sheet.html", "w").write(html)
    print("wrote /workspace/plan/fear_sheet.html", len(html), "bytes")
