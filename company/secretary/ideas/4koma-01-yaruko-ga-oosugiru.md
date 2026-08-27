# 四コマ #01「やることが多すぎる」

作成日: 2026-08-27
テーマ: メンタルで悩みを抱える人が「悩み解決ってこんなに簡単なんだ」と前向きになれる
ターゲット: 治療が必要な人ではなく「ちょっと詰まっている人」

## 概要
「やることが多すぎてパンクしている」の正体は「数えていないこと」だった、という気づきの話。
紙に全部書き出したら3つしかなかった、というオチ。読んだ人が今日すぐ真似できるのが狙い。

## ネーム（構成とセリフ）

| コマ | 絵 | セリフ |
|---|---|---|
| 1 | 机に突っ伏すハル | ハル「やることが多すぎて、もう無理…」 |
| 2 | ノンが紙とペンを差し出す | ノン「じゃあ、全部書き出してみて」 |
| 3 | 書き終えて紙を見つめるハル | ハル「……あれ」 |
| 4 | 紙をこちらに向けて呆然 | ハル「3つしかない」 |

※4コマ目の紙には文字を描かせない。線だけの「箇条書きっぽい記号」にして、Canvaで必要なら文字を載せる。

## キャラクター設定（プロンプト固定ブロック）

生成のたびに、この2ブロックを**一字一句同じまま**先頭に貼る。

```
Character A (Haru, the one who is stuck):
A young woman in her late 20s, shoulder-length straight black hair with blunt bangs,
gentle tired eyes, wearing an oversized cream knit sweater.

Character B (Non, the friend):
A young woman in her late 20s, short wavy light-brown hair, calm confident expression,
wearing a simple navy button-up shirt.

Style:
Flat anime illustration style, clean bold line art, soft pastel color palette,
simple minimal room background, even flat lighting, no gradients.
Square 1:1 composition.
no text, no letters, no speech bubbles, no watermark
```

## 画像生成プロンプト（Gemini用）

### 手順0：まず基準画像を作る
2人が並んで立っているだけの画像を1枚生成し、**これを参照画像として4コマすべてに渡す。**
2キャラ出るので、ここを飛ばすと顔が毎コマ変わる。

```
[固定ブロック]

Scene: Haru and Non standing side by side in a plain room, full body, facing the viewer,
neutral relaxed pose, character reference sheet style.
```

### コマ1
```
[固定ブロック]

Scene: Haru slumped face-down on a wooden desk, arms sprawled, a laptop and scattered
sticky notes around her.
Expression: exhausted, overwhelmed.
Composition: slightly high angle, medium shot.
```

### コマ2
```
[固定ブロック]

Scene: Non standing beside the desk, holding out a blank sheet of paper and a pen
toward Haru. Haru lifts her head slightly and looks at the paper.
Expression: Non is calm and encouraging, Haru is puzzled.
Composition: two-shot, eye level, medium shot.
```

### コマ3
```
[固定ブロック]

Scene: Haru sitting upright at the desk, holding the sheet of paper with both hands,
staring down at it. Pen resting on the desk.
Expression: quiet surprise, eyes slightly wide.
Composition: bust-up shot, eye level.
```

### コマ4
```
[固定ブロック]

Scene: Haru turning the sheet of paper toward the viewer, holding it up with both hands.
The paper shows only three short blank bullet marks, no readable text.
Expression: blank, dumbfounded, mouth slightly open.
Composition: front-facing bust-up shot, eye level.
```

## Canva作業メモ
- 縦4段（1080×1350）か 2×2（1080×1080）。SNSなら 2×2 が読まれやすい
- フキダシは白・シンプルな楕円で統一。1〜3コマは小さめ、4コマ目だけ少し大きく
- フォントは丸ゴシック系（読みやすさ優先）
- 4コマ目の「3つしかない」は少し大きめの級数にして、オチを立てる

## 次のアクション
- [ ] 基準画像を1枚生成して、顔が気に入るまで作り直す
- [ ] 4コマ分を参照画像つきで生成
- [ ] Canvaで組んで書き出し
- [ ] 投稿してみて反応を見る（案B・案Cはストック済み）

## ストック（次回以降の案）
- **案B**: ぐるぐる考えてしまう人 → 声に出したら5秒で終わった
- **案C**: 完璧にやろうとして動けない人 → 60点で出したら「ありがとう」の一言だった
