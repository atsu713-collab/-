# -*- coding: utf-8 -*-
import os, html

SP = "/tmp/claude-0/-home-user--/adb260bf-a31c-5c5e-95f4-cd2e706a6cf0/scratchpad"

# (本文, フォントサイズpx, 注釈, 種別)
slides = [
    ("言われた一言が、\n何日も抜けない。", 78, None, "hook"),
    ("楽しかったことは\nすぐ忘れてしまうのに、\n\nちくっとした一言だけ、\nやけに鮮明に覚えている。", 58, None, "body"),
    ("これ、\nあなたが気にしすぎだから\nではありません。", 62, None, "body"),
    ("脳には、\n危険な情報を優先して\n記憶する性質があります。", 58, "ネガティビティ・バイアス", "term"),
    ("「褒め言葉より批判が残る」のは、\n生き延びるために\n必要だった機能。\n\n今も、そのまま働いています。", 50, None, "body"),
    ("つまり、\n\n忘れられないのは\n心が弱いからではなく、\n脳がちゃんと働いている証拠。", 54, None, "body"),
    ("覚えてしまう自分を、\n責めなくて大丈夫です。", 68, None, "close"),
]

TPL = """<meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1350px; overflow:hidden; }}
  body {{
    background:{bg};
    font-family:'Noto Serif JP', serif;
    display:flex; flex-direction:column;
    align-items:center; justify-content:center;
    padding:120px 96px;
    position:relative;
  }}
  .rule {{
    width:64px; height:3px; background:{accent};
    margin-bottom:56px; border-radius:2px;
    {rule_display}
  }}
  .text {{
    color:#33302B;
    font-size:{size}px;
    font-weight:{weight};
    line-height:1.95;
    letter-spacing:0.06em;
    text-align:center;
    white-space:pre-wrap;
  }}
  .term {{
    margin-top:64px;
    color:{accent};
    font-size:34px;
    letter-spacing:0.14em;
    font-weight:600;
    border:2px solid {accent};
    border-radius:999px;
    padding:16px 40px;
  }}
  .page {{
    position:absolute; bottom:64px; right:80px;
    color:#A9A296; font-size:26px; letter-spacing:0.16em;
    font-family:'Noto Serif JP', serif;
  }}
  .swipe {{
    position:absolute; bottom:62px; left:0; right:0;
    text-align:center; color:#A9A296;
    font-size:28px; letter-spacing:0.2em;
    {swipe_display}
  }}
</style>
<div class="rule"></div>
<div class="text">{body}</div>
{term_html}
<div class="swipe">→ スワイプ</div>
<div class="page">{page} / 7</div>
"""

for i, (body, size, term, kind) in enumerate(slides, start=1):
    bg = "#F4F1EA"
    accent = "#7A8B7F"
    weight = 600 if kind in ("hook", "close") else 400
    rule_display = "" if kind in ("hook", "close") else "display:none;"
    swipe_display = "" if i == 1 else "display:none;"
    term_html = f'<div class="term">{html.escape(term)}</div>' if term else ""
    out = TPL.format(
        bg=bg, accent=accent, size=size, weight=weight,
        body=html.escape(body), term_html=term_html,
        page=i, rule_display=rule_display, swipe_display=swipe_display,
    )
    with open(f"{SP}/slides/slide{i}.html", "w", encoding="utf-8") as f:
        f.write(out)

print(f"{len(slides)} 枚のHTMLを生成しました")
