# デザイン仕様（全投稿共通）

画像は `source/gen.py` で生成しています。テキストを差し替えて実行すれば同じデザインで作れます。

## 配色：ウォームベージュ

| 用途 | 色 |
|---|---|
| 背景 | `#F2EBE3` |
| 本文 | `#4A4038` |
| アクセント（罫線） | `#C0A490` |
| ページ番号・補助 | `#94897E` |
| 用語バッジ 背景 / 文字 | `#E8DDD1` / `#9B7F68` |

## フォント：Zen Maru Gothic（丸ゴシック）

| 用途 | ウェイト |
|---|---|
| フック・締めのスライド | 700 |
| 本文スライド | 500 |

Google Fonts から取得できます。

## レイアウト

| 項目 | 値 |
|---|---|
| サイズ | 1080 × 1350（4:5） |
| 余白 | 上下120px / 左右92px |
| 行間 | 2.0 |
| 字間 | 0.05em |
| 1枚あたりの行数 | 2〜4行 |

---

## この配色・フォントを選んだ理由

読み手が落ち込んでいる状態を前提に選定しています。

### 色

- **彩度の低さが色相そのものより重要。** 同じ「落ち着く色」でも、鮮やかな青は逆に覚醒度を上げてしまう。淡く彩度を落とした色であれば、多くの色相で鎮静効果が出る
- **温かいニュートラル（ベージュ系）は心拍とコルチゾールを下げる**とされる
- **赤・黒・鮮やかな黄は避ける。** 赤は心拍を上げ、黒は不安を強め、鮮やかな黄は感覚を過剰に刺激する
- 本文も純黒ではなく `#4A4038`（茶みのある濃色）にしている。純黒はコントラストが強すぎて目が疲れるため
- 青系（ミストブルー）も候補だったが、鎮静効果がある一方で「悲しみ」「冷たさ」の連想があるため、落ち込んでいる人向けには温かい色を選んだ

### フォント

- **丸ゴシック体は「やさしさ」「安心」「安全」の印象を与える**とされる
- 明朝体は「落ち着き」「信頼」を与えるが、線が細く繊細なため、疲れているときは読みづらい
- 丸ゴシックは「子どもっぽい」印象になりやすいが、Zen Maru Gothic は落ち着いた設計で大人向けの内容にも耐える

### 参考

- [Colors That Calm the Mind: What Psychology and Cognitive Science Reveal](https://blog.cognifit.com/colors-that-calm-the-mind-what-psychology-and-cognitive-science-reveal/)
- [Calming Colors: Psychology Behind Soft Blues and Greens](https://villahealingcenter.com/calming-colors-psychology/)
- [Colors and Mental Health: How Hues Affect Anxiety & Mood](https://villahealingcenter.com/colors-and-mental-health/)
- [フォントが与える印象 心理を考慮したフォントの選び方](https://321web.link/fonts-impression/)
- [「ゴシック体」と「明朝体」の特徴と人に与える印象](https://www.togu.co.jp/column/detail/120)
