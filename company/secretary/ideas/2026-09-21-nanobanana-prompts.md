# ステッカー画像生成プロンプト（Nano Banana / Gemini）5パターン

作成日: 2026-09-21
用途: SUZURI・Etsyで販売する元データ作成。日本語版のみでスタート。

## 前提メモ（重要）
画像生成モデルは**日本語の文字描画が最も不得意**。漢字の画数が崩れる／
余分な文字が混入する／句読点がずれる、が高頻度で起きる。
そのため下記5パターンのうち **パターン4（文字なしで器だけ生成）を保険として必ず持つ**。
最終的な販売データは、パターン4の器に自分で文字を組むのが一番確実。

## 出力データの要件
- 背景透過PNG（生成物は白背景で出るので、あとで抜く）
- 長辺2000px以上を目標（SUZURIのステッカーテンプレートは出品前に必ず確認。外周の余白を確保）
- 生成後の必須チェック: ①1文字も崩れていないか ②句読点の位置 ③余分な文字が入っていないか
- 自分で文字を組む場合の商用可フォント: Zen Maru Gothic（丸ゴシック）／
  しっぽり明朝（細明朝）／Noto Sans JP

---

## パターン1 単体ステッカー・褒め群（丸ゴシック）
```
A minimalist die-cut sticker design, flat vector style, on a pure white background.

Text (render these exact Japanese characters and nothing else):
何もしてない。でも偉い

Typography: heavy rounded Japanese gothic typeface (maru gothic), generous letter spacing.
Set in 2 centered lines — line 1: 何もしてない。 line 2: でも偉い
Color: text in deep warm brown (#4A3728) on an off-white cream base (#F5F0E6)
Shape: horizontal rounded rectangle, 45:20 proportion, with a solid white die-cut border around the whole shape
Detail: one very small circle mark in the bottom-right corner, same brown
Style: clean, printable, flat. No gradients, no shadows, no illustration, no extra decoration, no additional text or characters.
Output: flat front-facing view, centered, high resolution.
```
※ Textの行を差し替えて使う: 何もしてない。でも偉い / 褒める人、いないので /
泣いたのも偉いです / 生きてるだけで手一杯 / 先に褒めておきます

## パターン2 単体ステッカー・告白群（細明朝）
```
A minimalist die-cut sticker design, flat vector style, on a pure white background.

Text (render these exact Japanese characters and nothing else):
気づいてほしかった

Typography: thin elegant Japanese serif typeface (mincho), wide letter spacing, single centered line.
Color: text in deep warm brown (#4A3728) on an off-white cream base (#F5F0E6)
Shape: horizontal rounded rectangle, 45:20 proportion, with a solid white die-cut border around the whole shape
Detail: one very small circle mark in the bottom-right corner, same brown
Style: clean, printable, flat, quiet. No gradients, no shadows, no illustration, no extra decoration, no additional text or characters.
Output: flat front-facing view, centered, high resolution.
```
※ Textの行を差し替えて使う: 気づいてほしかった / 期待、重いです / もう置いていかれてる

## パターン3 8案一覧シート（検討用・商品データには使わない）
```
A contact sheet showing 8 separate Japanese text stickers arranged in a clean 2 x 4 grid on a plain white background, with even spacing between them.

All 8 stickers share: off-white cream base (#F5F0E6), deep warm brown text (#4A3728), horizontal rounded rectangle shape with a white die-cut border, flat print style, no illustration.

Stickers 1-5 use a heavy rounded Japanese gothic typeface. Their texts are exactly:
1. 何もしてない。でも偉い
2. 褒める人、いないので
3. 泣いたのも偉いです
4. 生きてるだけで手一杯
5. 先に褒めておきます

Stickers 6-8 use a thin Japanese serif (mincho) typeface. Their texts are exactly:
6. 期待、重いです
7. もう置いていかれてる
8. 気づいてほしかった

Render only these Japanese characters. Do not add any other text, numbers, labels or decoration.
```
※ 8文字列を同時に描かせると崩れやすい。棚の統一感チェック用と割り切る。

## パターン4 器のみ生成（文字なし・保険であり本命）
```
An empty blank die-cut sticker template, flat vector style, on a pure white background.

Shape: horizontal rounded rectangle, 45:20 proportion, filled with a soft off-white cream color (#F5F0E6), surrounded by a clean solid white die-cut border with a subtle thin outline.
Detail: one very small deep-brown circle mark in the bottom-right corner.
Surface: very subtle matte paper texture, barely visible.

IMPORTANT: the sticker must be completely empty. Absolutely no text, no letters, no Japanese characters, no numbers, no symbols other than the small corner circle. No illustration, no gradient, no shadow.
Output: flat front-facing view, centered, high resolution.
```
→ これに自分でフォントを組んで文字を乗せる。文字化けリスクがゼロになる。

## パターン5 商品写真モックアップ（画像編集モードで使う）
完成したステッカーPNGを**アップロードしてから**下記を指示する。
```
Use the uploaded sticker image exactly as it is, without changing or redrawing its text.

Place it as a real applied sticker on the cover of a closed beige paper notebook, which lies on a light oak desk next to a white ceramic mug. Soft natural window light from the upper left, shallow depth of field, slight paper grain visible on the sticker surface.

The sticker should look physically applied: correct perspective, matching light, a very subtle edge shadow. Do not alter the sticker's text, colors, proportions or layout in any way.
Output: realistic product photograph, square crop.
```
※ 文字を再描画させないのがコツ。「as it is / do not alter the text」を必ず入れる。
※ 差し替え用シーン: 手帳／ノートPC天板／ステンレス水筒／洗面所の鏡

---

## 作業順序の推奨
1. パターン4で器を1枚だけ作り、気に入るまで詰める
2. パターン1・2で文字入りを試す（うまく描ければ工数が減る）
3. 崩れるならパターン4の器に自分で文字を組む（Zen Maru Gothic / しっぽり明朝）
4. 8枚そろったらパターン3で棚の統一感を確認
5. パターン5で商品写真を作る
