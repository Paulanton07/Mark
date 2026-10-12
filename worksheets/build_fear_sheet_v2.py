#!/usr/bin/env python3
# Fear of Failure - answerable one-page-per-act worksheet (A4 portrait, phone-readable).
# v2: Paul's read - needs white space, room to write. Same palette as the guides.

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
@page { size: A4 portrait; margin: 10mm 11mm; }
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", Arial, sans-serif; color:#191919; margin:0; padding:0; font-size:13.5px;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
.head { border-bottom:3px solid #8a1f14; padding-bottom:5px; margin-bottom:8px; }
h1 { font-size:27px; margin:0; letter-spacing:0.2px; }
.kick { font-size:12px; text-transform:uppercase; letter-spacing:1.5px; color:#8a1f14; font-weight:700; margin:0 0 2px 0; }
.sub { font-size:13px; color:#444; margin-top:3px; line-height:1.28; }
.rule { background:#fff6e8; border:1px solid #e8d3a8; border-radius:4px; padding:6px 10px; font-size:12.5px; line-height:1.3; margin:0 0 8px 0; }
.runhead { display:flex; align-items:center; margin:0 0 6px 0; border-top:2px solid #8a1f14; padding-top:6px; }
.runhead.first { border-top:none; padding-top:0; }
.badge { display:inline-block; background:#8a1f14; color:#fff; font-weight:800; font-size:12.5px;
         border-radius:4px; padding:2px 9px; margin-right:9px; letter-spacing:0.4px; }
.acttitle { font-size:16px; font-weight:800; color:#3a3a3a; letter-spacing:0.3px; }
.acthint { font-size:11.5px; color:#888; font-style:italic; margin-left:auto; }
.q { margin:0 0 4px 0; page-break-inside:avoid; }
.qtext { font-size:13.5px; line-height:1.3; padding-left:24px; position:relative; }
.qtext .n { position:absolute; left:0; top:0; font-weight:800; color:#8a1f14; font-size:13px; width:17px; text-align:right; }
.ans { margin:2px 0 5px 24px; }
.ans .ln { height:7mm; border-bottom:1px solid #d6d6d6; }
.ans .ln:last-child { border-bottom:1px solid #c9c9c9; }
.foot { margin-top:6px; border-top:2px solid #cfcfcf; padding-top:6px; font-size:12.5px; color:#3a3a3a; line-height:1.34; }
.foot b { color:#8a1f14; }
.sig { margin-top:4px; font-size:11px; color:#7a7a7a; letter-spacing:0.3px; }
.movebox { margin-top:12px; border:2px solid #8a1f14; border-radius:5px; padding:10px 12px; background:#fff6e8; page-break-inside:avoid; }
.movebox h2 { font-size:16px; margin:0 0 2px 0; color:#8a1f14; }
.movebox p { font-size:12.5px; color:#444; margin:0 0 8px 0; line-height:1.3; }
.mline { border-bottom:1.4px solid #999; height:9mm; margin:0 0 2mm 0; }
.mlab { font-size:12px; color:#3a3a3a; font-weight:700; margin:0 0 1mm 0; }
"""

def build():
    p = []
    p.append('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS + '</style></head><body>')
    p.append('<div class="head"><p class="kick">A walk &middot; 15 questions &middot; 10 minutes</p>')
    p.append('<h1>Fear of Failure</h1>')
    p.append('<p class="sub">Answer fast, in pen or on the line. One or two lines each. The first answer is usually the true one. Don\'t tidy it.</p></div>')
    p.append('<div class="rule">Work top to bottom. <b>Locate</b> the fear, <b>weigh</b> it against real evidence, then land on a <b>ten-minute move</b>. The questions do the work, not the prose.</div>')
    n = 1
    for i, (title, qs) in enumerate(ACTS, 1):
        first = ' first' if i == 1 else ''
        p.append(f'<div class="runhead{first}"><span class="badge">{i}</span><span class="acttitle">{title}</span>'
                 + (f'<span class="acthint">do these {len(qs)} first</span>' if False else '') + '</div>')
        for q in qs:
            p.append(f'<div class="q"><div class="qtext"><span class="n">{n}</span>{q}</div><div class="ans"><div class="ln"></div><div class="ln"></div></div></div>')
            n += 1
    p.append('<div class="movebox"><h2>Your ten-minute move</h2>'
             '<p>The one act from question 14. Small enough to start before you can talk yourself out of it.</p>'
             '<div class="mlab">I will &nbsp;:</div><div class="mline"></div>'
             '<div class="mlab">In the next ten minutes, at &nbsp;:</div><div class="mline"></div>'
             '<div class="mlab">I will tell &nbsp;:</div><div class="mline"></div></div>')
    p.append('<div class="foot"><b>Do it on a walk if you can.</b> One question per pause. Answers come easier with your hands busy and nobody watching. '
             'You\'re reporting the attempt, not the result.</div>')
    p.append('<div class="sig">Mark \U0001f6e0\ufe0f &nbsp;&middot;&nbsp; made with Paul</div>')
    p.append('</body></html>')
    return "\n".join(p)

if __name__ == "__main__":
    html = build()
    open("/workspace/plan/fear_sheet_v2.html", "w").write(html)
    print("wrote /workspace/plan/fear_sheet_v2.html", len(html), "bytes")
