# -*- coding: utf-8 -*-
import html, sys, os

SP = "/tmp/claude-0/-home-user--/adb260bf-a31c-5c5e-95f4-cd2e706a6cf0/scratchpad/new"

BG, INK, ACCENT, SUB = "#F2EBE3", "#4A4038", "#C0A490", "#6F6357"

POSTS = {
"p1": [
    ("言われた一言が、\n何日も抜けない。", 70, None, "hook"),
    ("楽しかったことは\nすぐ忘れてしまうのに、\n\nちくっとした一言だけ、\nやけに鮮明に覚えている。", 52, None, "body"),
    ("これ、\nあなたが気にしすぎだから\nではありません。", 54, None, "body"),
    ("脳には、\n危険な情報を優先して\n記憶する性質があります。", 52, "ネガティビティ・バイアス", "term"),
    ("「褒め言葉より\n批判が残る」のは、\n生き延びるために\n必要だった機能。\n\n今も、そのまま働いています。", 46, None, "body"),
    ("つまり、\n\n忘れられないのは\n心が弱いからではなく、\n脳がちゃんと働いている証拠。", 48, None, "body"),
    ("覚えてしまう自分を、\n責めなくて大丈夫です。", 60, None, "close"),
],
"p2": [
    ("夜になると、\n全部だめな気がしてくる。", 58, None, "hook"),
    ("昼間は流せたことが、\n夜になると\n急に重くなる。", 54, None, "body"),
    ("これ、あなたの考えが\n正しくなったわけでは\nありません。", 52, None, "body"),
    ("疲れているとき、脳は\n悪い方の可能性ばかりを\nくり返し考えてしまいます。", 48, "反芻思考", "term"),
    ("同じことでも、\n朝に考えるのと\n夜に考えるのでは、\n答えが変わります。", 52, None, "body"),
    ("だから、\n夜に出した結論は\n採用しなくて大丈夫。", 54, None, "body"),
    ("大事なことは、\n朝のあなたに\n任せましょう。", 58, None, "close"),
],
}

TPL = """<meta charset="utf-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:1080px; height:1350px; overflow:hidden; }}
  body {{
    background:%s; font-family:'Zen Maru Gothic', sans-serif;
    display:flex; flex-direction:column; align-items:center; justify-content:center;
    padding:120px 92px; position:relative;
  }}
  .rule {{ width:72px; height:4px; background:%s; margin-bottom:60px;
    border-radius:99px; {rule_display} }}
  .text {{ color:%s; font-size:{size}px; font-weight:{weight};
    line-height:2.0; letter-spacing:0.05em; text-align:center; white-space:pre-wrap; }}
  .term {{ margin-top:64px; color:#9B7F68; font-size:32px; letter-spacing:0.12em;
    font-weight:700; background:#E8DDD1; border-radius:999px; padding:18px 42px; }}
  .page {{ position:absolute; bottom:84px; right:88px; line-height:1.4;
    color:#4A4038; font-size:44px; font-weight:700; letter-spacing:0.10em; }}
  .swipe {{ position:absolute; bottom:88px; left:0; right:0; line-height:1.4;
    text-align:center; color:#5F554C; font-size:36px; font-weight:500; letter-spacing:0.18em; {swipe_display} }}
</style>
<div class="rule"></div>
<div class="text">{body}</div>
{term_html}
<div class="swipe">→ スワイプ</div>
<div class="page">{page} / 7</div>
""" % (BG, ACCENT, INK)

for key, slides in POSTS.items():
    d = f"{SP}/{key}"
    os.makedirs(d, exist_ok=True)
    for i, (body, size, term, kind) in enumerate(slides, start=1):
        out = TPL.format(
            size=size, weight=700 if kind in ("hook", "close") else 500,
            body=html.escape(body),
            term_html=f'<div class="term">{html.escape(term)}</div>' if term else "",
            page=i,
            rule_display="" if kind in ("hook", "close") else "display:none;",
            swipe_display="" if i == 1 else "display:none;",
        )
        open(f"{d}/slide{i}.html", "w", encoding="utf-8").write(out)
print("14枚のHTMLを生成しました")
