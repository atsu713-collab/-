# -*- coding: utf-8 -*-
"""
1週目の投稿画像を、デザイン仕様書どおりに生成するスクリプト。

使い方:
    python3 generate.py

仕様: company/secretary/ideas/2026-08-28-instagram-design-spec.md
文言: company/secretary/ideas/2026-08-28-week1-full-scripts.md

文言を直したいときは、下の CONTENT を編集して再実行してください。
テキスト中の **〜** はアクセント色（マスタード）になります。
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ---------- 仕様（デザイン仕様書と一致） ----------
BG        = "#1B2A41"   # 背景（濃紺）
BG_DARK   = "#141F30"   # 言い換え図鑑の1枚目（NG側）
FG        = "#F5F2EA"   # 文字（オフホワイト）
ACCENT    = "#E5B25D"   # アクセント（マスタード）
SUB       = "#8A94A6"   # 補助（グレー）
RULE      = "#3A4A63"   # 罫線

W, H      = 1080, 1350  # カルーセル・フィード 4:5
RW, RH    = 1080, 1920  # リール 9:16
MARGIN    = 80

FONT_DIR  = os.environ.get("NSJP_DIR", "/tmp/claude-0/-home-user--/7a81249a-1fe7-56a4-b8d8-d5859949cf8d/scratchpad/fonts")
OUT_DIR   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "week1")


def font(weight, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, f"NotoSansJP-{weight}.ttf"), size)


# ---------- 描画ヘルパ ----------
def runs(line):
    """**強調** を (text, is_accent) の並びに分解する"""
    out, buf, acc = [], "", False
    i = 0
    while i < len(line):
        if line[i:i + 2] == "**":
            if buf:
                out.append((buf, acc))
                buf = ""
            acc = not acc
            i += 2
        else:
            buf += line[i]
            i += 1
    if buf:
        out.append((buf, acc))
    return out


def draw_lines(d, x, y, lines, f, fill, lh, accent=ACCENT, center_w=None, stroke=0):
    """複数行を描く。center_w を渡すとその幅の中で中央揃え。戻り値は次のy"""
    for line in lines:
        segs = runs(line)
        total = sum(d.textlength(t, font=f) for t, _ in segs)
        cx = x if center_w is None else x + (center_w - total) / 2
        for t, is_acc in segs:
            d.text((cx, y), t, font=f, fill=(accent if is_acc else fill),
                   stroke_width=stroke, stroke_fill="#000000" if stroke else None)
            cx += d.textlength(t, font=f)
        y += lh
    return y


def save(img, name):
    os.makedirs(OUT_DIR, exist_ok=True)
    p = os.path.join(OUT_DIR, name)
    img.save(p, "PNG")
    print("  ", name)


# ---------- カルーセル ----------
def carousel_cover(name, label, heading, sub, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # シリーズラベル（縦バー＋文字）
    d.rectangle([MARGIN, 150, MARGIN + 8, 150 + 38], fill=ACCENT)
    d.text((MARGIN + 26, 150), label, font=font(500, 30), fill=SUB)
    # 見出し
    y = draw_lines(d, MARGIN, 430, heading, font(900, 96), FG, 134)
    # サブ
    if sub:
        draw_lines(d, MARGIN, y + 70, sub, font(500, 44), SUB, 70)
    # スワイプ誘導
    txt = "スワイプ →"
    f = font(500, 30)
    d.text((W - MARGIN - d.textlength(txt, font=f), H - MARGIN - 40), txt, font=f, fill=SUB)
    save(img, name)


def carousel_body(name, no, heading, body, page, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    y = 380
    if no:
        d.text((MARGIN, y), no, font=font(900, 72), fill=ACCENT)
        hx = MARGIN + d.textlength(no, font=font(900, 72)) + 24
    else:
        hx = MARGIN
    draw_lines(d, hx, y, [heading], font(700, 72), FG, 100)
    d.rectangle([MARGIN, y + 128, MARGIN + 360, y + 132], fill=RULE)
    draw_lines(d, MARGIN, y + 200, body, font(400, 46), FG, 83)
    f = font(400, 28)
    t = f"{page} / {total}"
    d.text((W - MARGIN - d.textlength(t, font=f), H - MARGIN - 36), t, font=f, fill=SUB)
    save(img, name)


def carousel_summary(name, heading, body, page, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([MARGIN - 20, 320, W - MARGIN + 20, H - 300], outline=RULE, width=3)
    draw_lines(d, MARGIN + 20, 400, [heading], font(900, 64), ACCENT, 100)
    draw_lines(d, MARGIN + 20, 560, body, font(400, 46), FG, 83)
    f = font(400, 28)
    t = f"{page} / {total}"
    d.text((W - MARGIN - d.textlength(t, font=f), H - MARGIN - 36), t, font=f, fill=SUB)
    save(img, name)


def carousel_cta(name, lines, page, total):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    draw_lines(d, MARGIN, H / 2 - 110, lines, font(700, 72), FG, 108, center_w=W - MARGIN * 2)
    f = font(400, 28)
    t = f"{page} / {total}"
    d.text((W - MARGIN - d.textlength(t, font=f), H - MARGIN - 36), t, font=f, fill=SUB)
    save(img, name)


# ---------- 言い換え図鑑（2枚組） ----------
def iikae(name, mark, lines, note, ng):
    img = Image.new("RGB", (W, H), BG_DARK if ng else BG)
    d = ImageDraw.Draw(img)
    d.text((MARGIN, 200), mark, font=font(900, 130), fill=(SUB if ng else ACCENT))
    y = draw_lines(d, MARGIN, 520, lines, font(900, 96), FG, 144)
    if note:
        d.rectangle([MARGIN, y + 70, MARGIN + 200, y + 74], fill=RULE)
        draw_lines(d, MARGIN, y + 130, note, font(400, 42), SUB, 72)
    f = font(500, 30)
    t = "言い換え図鑑"
    d.text((W - MARGIN - d.textlength(t, font=f), H - MARGIN - 40), t, font=f, fill=SUB)
    save(img, name)


# ---------- リールのテキストフレーム ----------
def reel(name, lines, size=72, tag=None):
    img = Image.new("RGB", (RW, RH), BG)
    d = ImageDraw.Draw(img)
    if tag:
        d.rectangle([MARGIN, 300, MARGIN + 8, 338], fill=ACCENT)
        d.text((MARGIN + 26, 300), tag, font=font(500, 30), fill=SUB)
    lh = int(size * 1.55)
    y = RH * 0.55 - (len(lines) * lh) / 2
    draw_lines(d, MARGIN, y, lines, font(900, size), FG, lh,
               center_w=RW - MARGIN * 2, stroke=0)
    save(img, name)


# =====================================================================
# 内容
# =====================================================================
def build():
    print("月曜｜言い換え図鑑 #01")
    iikae("01_mon_iikae01_a.png", "×", ["なんで", "やってないの？"], None, True)
    iikae("01_mon_iikae01_b.png", "○", ["どこで", "詰まってますか？"], ["原因を「人」ではなく", "「状況」に向ける聞き方です"], False)

    print("火曜｜リール メラビアンの誤用")
    R = "25_tue_reel_merabian"
    reel(f"{R}_01.png", ["「見た目が9割」って、", "実は**完全な誤用**です"], 68, "よくある誤解")
    reel(f"{R}_02.png", ["よく引用される", "言語7% 聴覚38% 視覚55%"], 62)
    reel(f"{R}_03.png", ["あの実験が調べたのは", "**言葉と表情が矛盾したとき**", "どちらを信じるか"], 58)
    reel(f"{R}_04.png", ["「好きだよ」と", "**不機嫌な顔**で言われたとき", "この場合に限った話です"], 58)
    reel(f"{R}_05.png", ["普段の会話の伝達比率とは", "まったく関係ありません"], 58)
    reel(f"{R}_06.png", ["中身は、ちゃんと", "**9割届いています**"], 68)

    print("水曜｜言い換え図鑑 #02")
    iikae("02_wed_iikae02_a.png", "×", ["前も", "言いましたよね"], None, True)
    iikae("02_wed_iikae02_b.png", "○", ["もう一度", "すり合わせ", "させてください"], ["過去を責めないと、", "話が前に進みます"], False)

    print("木曜｜リール 傍観者効果")
    R = "07_thu_reel_bystander"
    reel(f"{R}_01.png", ["その会議、", "**あなたのせい**で", "静かなわけじゃないです"], 62, "会議とチームの心理学")
    reel(f"{R}_02.png", ["心理学では", "**傍観者効果**と呼びます"], 66)
    reel(f"{R}_03.png", ["街で人が倒れたとき", "**通行人が多いほど**", "助けが遅れる"], 62)
    reel(f"{R}_04.png", ["理由は「誰かがやるだろう」", "責任が人数で薄まるから"], 56)
    reel(f"{R}_05.png", ["会議も同じ", "参加者が多いほど", "発言の責任は薄まります"], 60)
    reel(f"{R}_06.png", ["対策はひとつ", "**「◯◯さん、どう思いますか」**", "名指しするだけ"], 56)
    reel(f"{R}_07.png", ["会議を静かにしているのは、", "**人数**です"], 62)

    print("金曜｜リール コピー機実験")
    R = "19_fri_reel_copier"
    reel(f"{R}_01.png", ["「お願いが通る人」が", "やっている、", "**たった一言**"], 64, "今日から使える1手")
    reel(f"{R}_02.png", ["コピー機の順番を", "譲ってもらう実験"], 66)
    reel(f"{R}_03.png", ["①「先にコピーさせて」", "→ 承諾 **60%**"], 64)
    reel(f"{R}_04.png", ["②「**急いでいるので**、", "先にコピーさせて」", "→ **94%**"], 60)
    reel(f"{R}_05.png", ["③「**コピーを取りたいので**、", "先にコピーさせて」", "→ **93%**"], 56)
    reel(f"{R}_06.png", ["人は理由の中身ではなく", "**「理由の形」**に反応する"], 60)

    print("土曜｜カルーセル 認知の歪み")
    T = 10
    carousel_cover("14_sat_carousel_01.png", "働く自分の取扱説明書",
                   ["仕事で必要以上に", "落ち込む人の", "思考の癖**10個**"],
                   ["心理学では「認知の歪み」と", "呼ばれています"], T)
    carousel_body("14_sat_carousel_02.png", "①", "全か無か思考",
                  ["80点の資料を", "「失敗」と呼んでしまう"], 2, T)
    carousel_body("14_sat_carousel_03.png", "②", "過度の一般化",
                  ["1回の指摘を", "「いつも怒られる」に変換する"], 3, T)
    carousel_body("14_sat_carousel_04.png", "③", "心のフィルター",
                  ["9個の評価より、", "1個の指摘だけが残る"], 4, T)
    carousel_body("14_sat_carousel_05.png", "④", "心の読みすぎ",
                  ["既読スルー＝嫌われた、と", "決めてしまう"], 5, T)
    carousel_body("14_sat_carousel_06.png", "⑤", "べき思考",
                  ["「先輩なんだから", "完璧であるべき」"], 6, T)
    carousel_body("14_sat_carousel_07.png", "⑥", "レッテル貼り",
                  ["ミスした →", "「自分は無能だ」に飛躍する"], 7, T)
    carousel_body("14_sat_carousel_08.png", "", "⑦～⑩ はこの4つ",
                  ["拡大解釈 / 感情的決めつけ", "自己関連づけ / マイナス化思考"], 8, T)
    carousel_summary("14_sat_carousel_09.png", "【まとめ】",
                     ["落ち込んでいるのは事実ではなく、", "変換された「解釈」のほうです。", "",
                      "癖は、名前をつけて書き出すと", "威力が落ちていきます。"], 9, T)
    carousel_cta("14_sat_carousel_10.png",
                 ["この話が刺さる人に、", "そっと送ってください"], 10, T)


if __name__ == "__main__":
    build()
    print("\n完成:", OUT_DIR)
