# -*- coding: utf-8 -*-
import html

SP = "/tmp/claude-0/-home-user--/adb260bf-a31c-5c5e-95f4-cd2e706a6cf0/scratchpad/p2"

# (本文, フォントサイズpx, 用語バッジ, 種別)
slides = [
    ("夜になると、\n全部だめな気がしてくる。", 64, None, "hook"),
    ("昼間は流せたことが、\n夜になると\n急に重くなる。", 60, None, "body"),
    ("これ、あなたの考えが\n正しくなったわけでは\nありません。", 58, None, "body"),
    ("疲れているとき、脳は\n悪い方の可能性ばかりを\nくり返し考えてしまいます。", 52, "反芻思考", "term"),
    ("同じことでも、\n朝に考えるのと\n夜に考えるのでは、\n答えが変わります。", 58, None, "body"),
    ("だから、\n夜に出した結論は\n採用しなくて大丈夫。", 58, None, "body"),
    ("大事なことは、\n朝のあなたに\n任せましょう。", 62, None, "close"),
]

TPL = """<meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1350px; overflow:hidden; }}
  body {{
    background:#E7EDE4; font-family:'Noto Serif JP', serif;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:120px 96px; position:relative;
  }}
  .rule {{ width:64px; height:3px; background:#7D9B80; margin-bottom:56px;
    border-radius:2px; {rule_display} }}
  .text {{ color:#2E4033; font-size:{size}px; font-weight:{weight};
    line-height:1.95; letter-spacing:0.06em; text-align:center; white-space:pre-wrap; }}
  .term {{ margin-top:64px; color:#7D9B80; font-size:34px; letter-spacing:0.14em;
    font-weight:600; border:2px solid #7D9B80; border-radius:999px; padding:16px 40px; }}
  .page {{ position:absolute; bottom:72px; right:80px; line-height:1.6;
    color:#7E8C7C; font-size:32px; letter-spacing:0.18em; }}
  .swipe {{ position:absolute; bottom:72px; left:0; right:0; line-height:1.6;
    text-align:center; color:#7E8C7C; font-size:32px; letter-spacing:0.22em; {swipe_display} }}
</style>
<div class="rule"></div>
<div class="text">{body}</div>
{term_html}
<div class="swipe">→ スワイプ</div>
<div class="page">{page} / 7</div>
"""

for i, (body, size, term, kind) in enumerate(slides, start=1):
    weight = 600 if kind in ("hook", "close") else 400
    out = TPL.format(
        size=size, weight=weight, body=html.escape(body),
        term_html=f'<div class="term">{html.escape(term)}</div>' if term else "",
        page=i,
        rule_display="" if kind in ("hook", "close") else "display:none;",
        swipe_display="" if i == 1 else "display:none;",
    )
    open(f"{SP}/slides/slide{i}.html", "w", encoding="utf-8").write(out)
print("7枚のHTMLを生成しました")
