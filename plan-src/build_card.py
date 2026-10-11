import re, html
src = open('/workspace/piece-01-provenance.md').read().split('\n')
# body = paragraphs after title + italic line
paras = [p.strip() for p in '\n'.join(src[2:]).split('\n\n') if p.strip()]
body = "\n".join(f"<p>{html.escape(p)}</p>" for p in paras)
doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: 1000px 1500px; margin:0; }}
*{{box-sizing:border-box;}}
body{{margin:0;width:1000px;height:1500px;background:#f4efe6;color:#242018;
 font-family:"DejaVu Serif",Georgia,serif;padding:78px 84px;}}
.bar{{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:1.5px solid #b9ad97;padding-bottom:10px;margin-bottom:34px;}}
h1{{font-size:30px;letter-spacing:3px;margin:0;font-weight:600;text-transform:uppercase;}}
.tag{{font-family:"DejaVu Sans",Arial,sans-serif;font-size:13px;letter-spacing:1px;
 color:#8a1f14;border:1px solid #c9a08f;border-radius:10px;padding:3px 10px;}}
p{{font-size:20.5px;line-height:1.62;margin:0 0 20px 0;}}
.foot{{position:absolute;bottom:56px;left:84px;right:84px;display:flex;justify-content:space-between;
 font-family:"DejaVu Sans",Arial,sans-serif;font-size:12.5px;letter-spacing:1px;color:#7a7161;
 border-top:1px solid #d3c9b6;padding-top:10px;}}
</style></head><body>
<div class="bar"><h1>Provenance</h1><span class="tag">INVENTED HISTORY</span></div>
{body}
<div class="foot"><span>THE OFFCUT FEEDER</span><span>PIECE 01 &middot; MARK</span><span>2026-10-05</span></div>
</body></html>'''
open('provenance-card.html','w').write(doc)
print("wrote", len(doc))
