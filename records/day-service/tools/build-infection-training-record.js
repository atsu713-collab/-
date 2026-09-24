const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, VerticalAlign, HeightRule, BorderStyle, PageBreak, Footer, Header, PageNumber,
  LevelFormat, TableLayoutType } = d;

const FONT = process.argv[2];
const OUT = process.argv[3];
const W = 9638; // A4 11906 - 左右20mm
const GRAY = 'E7E6E6';
const bd = { style: BorderStyle.SINGLE, size: 6, color: '000000' };
const borders = { top: bd, bottom: bd, left: bd, right: bd };

const r = (text, o = {}) => new TextRun({ text, font: { ascii: FONT, eastAsia: FONT, hAnsi: FONT }, size: o.size || 20, bold: o.bold });
const p = (text, o = {}) => new Paragraph({ children: [r(text, o)], alignment: o.align, spacing: { before: o.before || 0, after: o.after ?? 60, line: 300 } });
const h1 = (t) => new Paragraph({ children: [r(t, { size: 28, bold: true })], spacing: { before: 0, after: 160 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: '000000', space: 2 } } });
const h2 = (t) => new Paragraph({ children: [r(t, { size: 22, bold: true })], spacing: { before: 200, after: 100 } });
const brk = () => new Paragraph({ children: [new PageBreak()] });

function cell(text, width, o = {}) {
  const lines = Array.isArray(text) ? text : [text];
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders, rowSpan: o.rowSpan,
    verticalAlign: o.valign || VerticalAlign.CENTER,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 40, bottom: 40, left: 100, right: 100 },
    children: lines.map(t => new Paragraph({ children: [r(t, { size: o.size || 19, bold: o.bold })], alignment: o.align, spacing: { after: 0, line: 280 } })),
  });
}

// 記録表：rows = [区分, 項目, 値, 高さ]
const COLS = [1000, 2800, W - 1000 - 2800];
function recordTable(rows) {
  const groups = {};
  rows.forEach(x => groups[x[0]] = (groups[x[0]] || 0) + 1);
  const seen = {};
  const trs = [new TableRow({ tableHeader: true, children: [
    cell('区分', COLS[0], { fill: GRAY, bold: true, align: AlignmentType.CENTER }),
    cell('項目', COLS[1], { fill: GRAY, bold: true, align: AlignmentType.CENTER }),
    cell('記入欄', COLS[2], { fill: GRAY, bold: true, align: AlignmentType.CENTER })] })];
  for (const [g, item, val, h] of rows) {
    const ch = [];
    if (!seen[g]) { seen[g] = 1; ch.push(cell(g, COLS[0], { fill: GRAY, bold: true, align: AlignmentType.CENTER, rowSpan: groups[g] })); }
    ch.push(cell(item, COLS[1], { fill: 'F5F5F5' }));
    ch.push(cell(val, COLS[2], { valign: h > 700 ? VerticalAlign.TOP : VerticalAlign.CENTER }));
    trs.push(new TableRow({ cantSplit: true, height: { value: h || 520, rule: HeightRule.ATLEAST }, children: ch }));
  }
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: COLS, layout: TableLayoutType.FIXED, rows: trs });
}

const RC = [520, 1350, 1800, 2000, 1250, 1600, W - 520 - 1350 - 1800 - 2000 - 1250 - 1600];
function roster(rows, n) {
  const head = ['No.', '職種', '氏名', '参加方法', '受講日', '本人確認\n（署名等）', '備考'];
  const trs = [new TableRow({ tableHeader: true, children: head.map((t, i) => cell(t.split('\n'), RC[i], { fill: GRAY, bold: true, align: AlignmentType.CENTER, size: 18 })) })];
  for (let i = 0; i < n; i++) {
    const v = rows[i] || ['', '', '', '', '', ''];
    trs.push(new TableRow({ cantSplit: true, height: { value: 600, rule: HeightRule.ATLEAST },
      children: [cell(String(i + 1), RC[0], { align: AlignmentType.CENTER, size: 18 }), ...v.map((t, j) => cell(t, RC[j + 1], { size: 18 }))] }));
  }
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: RC, layout: TableLayoutType.FIXED, rows: trs });
}

const M = '参加方法の例：集合／オンライン／動画視聴／後日フォロー';

// 空欄
const blank = [
  ['基本情報', '事業所名', '', 560],
  ['基本情報', '事業所番号', '', 520],
  ['基本情報', '記録作成者（職種・氏名）', '', 520],
  ['基本情報', '記録作成日', '　　　　年　　月　　日', 520],
  ['研修概要', '研修名', '', 560],
  ['研修概要', '研修区分', '□定期研修　□新規採用時研修　□その他（　　　　　）', 520],
  ['研修概要', '実施日', '　　　　年　　月　　日（　　）', 520],
  ['研修概要', '実施時間', '　　：　　〜　　：　　（合計　　　分）', 520],
  ['研修概要', '実施方法', '□集合　□オンライン　□動画視聴　□その他（　　　　）', 520],
  ['研修概要', '実施場所', '', 520],
  ['研修概要', '講師・進行担当者（所属・職種・氏名）', '', 560],
  ['研修概要', '使用した資料・教材', '', 760],
  ['研修内容', '研修の目的', '', 900],
  ['研修内容', '研修内容（扱った項目を具体的に）', '', 1700],
  ['研修内容', '事業所の「感染症の予防及びまん延の防止のための指針」との関係（扱った章・項目）', '', 800],
  ['研修内容', '演習・実技の有無と内容', '□有　□無\n内容：'.split('\n'), 800],
  ['参加状況', '対象職員数', '　　　名', 480],
  ['参加状況', '参加者数', '　　　名', 480],
  ['参加状況', '参加者一覧', '別表「参加者名簿」のとおり', 480],
  ['参加状況', '欠席者数と、欠席者へのフォロー方法・実施日', ['欠席　　名', 'フォロー方法：', '実施日：　　　　年　　月　　日'], 900],
  ['振り返り', '理解度の確認方法', '□テスト　□アンケート　□口頭確認　□その他（　　　）', 520],
  ['振り返り', '理解度の確認結果', '', 900],
  ['振り返り', '参加者から出た主な意見・質問', '', 900],
  ['振り返り', '今後の課題・改善点', '', 900],
  ['振り返り', '次回研修の予定時期', '　　　　年　　月頃', 480],
  ['確認', '感染対策委員会への報告日', '　　　　年　　月　　日', 480],
  ['確認', '管理者確認（氏名・確認日）', ['氏名：', '確認日：　　　　年　　月　　日'], 600],
  ['添付', '添付資料', '□資料　□参加者名簿　□テスト・アンケート　□その他（　　　）', 520],
];

// 記入例
const ex = [
  ['基本情報', '事業所名', 'サンプル通所介護事業所A（架空）'],
  ['基本情報', '事業所番号', '0000000000（架空）'],
  ['基本情報', '記録作成者（職種・氏名）', '看護職員・見本 花子'],
  ['基本情報', '記録作成日', '20XX年6月12日'],
  ['研修概要', '研修名', '感染症の予防及びまん延の防止のための研修（定期）'],
  ['研修概要', '研修区分', '■定期研修　□新規採用時研修　□その他'],
  ['研修概要', '実施日', '20XX年6月10日（水）'],
  ['研修概要', '実施時間', '16：30〜17：30（合計60分）'],
  ['研修概要', '実施方法', '■集合　□オンライン　□動画視聴　□その他'],
  ['研修概要', '実施場所', '事業所内 機能訓練室'],
  ['研修概要', '講師・進行担当者（所属・職種・氏名）', '感染対策担当者・看護職員・見本 花子'],
  ['研修概要', '使用した資料・教材', '事業所の感染対策指針、手指衛生の手順書、嘔吐物処理の手順書、自作スライド'],
  ['研修内容', '研修の目的', '全職員が標準予防策を理解し、感染症が疑われる場合に手順どおり初期対応できるようにする'],
  ['研修内容', '研修内容（扱った項目を具体的に）', ['①標準予防策の考え方', '②手指衛生のタイミングと方法', '③個人防護具（手袋・マスク・エプロン）の着脱手順', '④嘔吐物の処理手順', '⑤利用者に発熱・下痢・嘔吐がみられた場合の報告経路']],
  ['研修内容', '事業所の「感染症の予防及びまん延の防止のための指針」との関係（扱った章・項目）', '指針「平常時の対策」「発生時の対応」「報告体制」の各項目'],
  ['研修内容', '演習・実技の有無と内容', ['■有　□無', '内容：嘔吐物処理キットを使った処理手順の実技、防護具の着脱練習']],
  ['参加状況', '対象職員数', '12名'],
  ['参加状況', '参加者数', '10名'],
  ['参加状況', '参加者一覧', '別表「参加者名簿」のとおり'],
  ['参加状況', '欠席者数と、欠席者へのフォロー方法・実施日', ['欠席 2名', 'フォロー方法：当日資料と録画を用いて個別に実施し、看護職員が理解度を確認', '実施日：20XX年6月15日・6月17日']],
  ['振り返り', '理解度の確認方法', '■テスト（5問）　■アンケート　□口頭確認　□その他'],
  ['振り返り', '理解度の確認結果', '参加者10名全員が5問中4問以上正答。防護具を外す順番の設問で誤答が3名あり、当日中に再説明した'],
  ['振り返り', '参加者から出た主な意見・質問', '「送迎車内で嘔吐があった場合の対応を知りたい」「処理キットの置き場所を増やしてほしい」'],
  ['振り返り', '今後の課題・改善点', '送迎車内での嘔吐時対応を手順書に追記する。処理キットを送迎車にも配置するか委員会で検討する'],
  ['振り返り', '次回研修の予定時期', '20XX年12月頃'],
  ['確認', '感染対策委員会への報告日', '20XX年6月24日'],
  ['確認', '管理者確認（氏名・確認日）', ['氏名：管理者・例示 一郎', '確認日：20XX年6月13日']],
  ['添付', '添付資料', '■資料　■参加者名簿　■テスト・アンケート　□その他'],
].map(x => [...x, 480]);

const exRoster = [
  ['管理者', '例示 一郎', '集合', '20XX/6/10', '署名済', ''],
  ['看護職員', '見本 花子', '集合', '20XX/6/10', '署名済', '講師'],
  ['介護職員', '仮名 次郎', '集合', '20XX/6/10', '署名済', ''],
  ['生活相談員', '試作 三恵', '集合', '20XX/6/10', '署名済', ''],
  ['介護職員', '架空 四季', '後日フォロー', '20XX/6/15', '署名済', '当日欠席のため録画で受講'],
];

const chk = (t) => new Paragraph({ children: [r('□　' + t)], indent: { left: 400, hanging: 400 }, spacing: { after: 60, line: 300 } });
const bul = (t, b) => new Paragraph({ numbering: { reference: 'bul', level: 0 }, children: [r(t, { bold: b })], spacing: { after: 80, line: 320 } });

const children = [
  // 1 空欄のひな形
  h1('感染症の予防及びまん延の防止のための研修の記録'),
  p('（通所介護）', { after: 120 }),
  recordTable(blank),
  brk(),
  h2('別表　参加者名簿'),
  p('研修名：　　　　　　　　　　　　　　　　　　　実施日：　　　　年　　月　　日', { after: 120 }),
  roster([], 18),
  p(M, { size: 17, before: 60 }),
  brk(),
  // 2 記入例
  h1('【記入例】感染症の予防及びまん延の防止のための研修の記録'),
  p('※記入例の事業所名・人名・番号・日付はすべて架空です。記入の粒度の参考としてご覧ください。■はチェックを入れた項目です。', { size: 18, after: 120 }),
  recordTable(ex),
  brk(),
  h2('【記入例】別表　参加者名簿（抜粋）'),
  p('研修名：感染症の予防及びまん延の防止のための研修（定期）　　実施日：20XX年6月10日', { after: 120 }),
  roster(exRoster, 5),
  brk(),
  // 3 確認ポイント
  h1('提出前の確認ポイント'),
  h2('記入漏れ'),
  ...['事業所名・記録作成者・記録作成日が記入されている',
    '実施日・実施時間（開始〜終了）・実施方法が記入されている',
    '研修区分（定期／新規採用時など）にチェックがある',
    '研修内容が「感染症研修」の一言ではなく、扱った項目が具体的に書かれている',
    '講師・進行担当者が記入されている',
    '対象職員数・参加者数が記入され、参加者名簿の人数と一致している',
    '欠席者がいる場合、フォローの方法と実施日が書かれている（「後日対応」だけで終わっていない）',
    '理解度の確認方法と結果が記入されている',
    '管理者確認欄に氏名と日付がある',
    '記載した添付資料（資料・参加者名簿など）が実際に綴じられている',
    '新規採用者がいた年度は、新規採用時の研修の記録があるか確認した',
    '当年度の研修回数が、各自治体の通知で求められる回数を満たしているか確認した'].map(chk),
  h2('不適切な表現・記載'),
  ...['利用者の氏名や病名など、研修記録に不要な個人情報を書いていない（事例は匿名化している）',
    '「特になし」「問題なし」だけで終わる欄がない（何を確認して問題がなかったのかが分かる）',
    '「全員理解した」など、確認方法の裏付けがない断定表現になっていない',
    '実施していない内容・参加していない職員を記録していない（実態と記録が一致している）',
    '日付の前後関係に矛盾がない（実施日より前に記録作成日・管理者確認日がない など）',
    '訂正は修正液等を使わず、二重線と訂正者・訂正日が分かる方法で行っている（事業所のルールがあればそれに従う）',
    '研修の記録と訓練の記録を混同していない（訓練は別様式で記録している）',
    '保存期間・保存方法について、各自治体の通知を確認した'].map(chk),
  // 4 免責文
  new Paragraph({ children: [], spacing: { after: 200 } }),
  h1('免責文'),
  bul('本様式は、通所介護事業所が記録を作成する際の参考として作成した空欄のひな形であり、法令への適合、監査・運営指導への対応、報酬の減算の回避、立入検査の通過を保証するものではありません。', true),
  bul('作成者は行政書士・社会保険労務士等の専門資格者ではなく、本様式は法的助言を目的とするものではありません。'),
  bul('運営基準は各自治体の条例・規則・通知等により定められ、改正されることがあります。実際の運用にあたっては、各自治体の通知を確認してください。判断に迷う場合は、指定権者（所管の自治体）や専門家にご相談ください。'),
  bul('記入例に記載した事業所名・人名・番号・日付等はすべて架空のものです。'),
  bul('本様式を共有・配布・見本として使う場合は、実在する利用者・職員の個人情報（氏名、病名、連絡先等）を書き込まないでください。実際の記録として使う場合は、事業所の個人情報保護のルールに従って管理してください。', true),
  bul('本様式の利用により生じたいかなる損害についても、作成者は責任を負いかねます。'),
];

const doc = new Document({
  styles: { default: { document: { run: { font: { ascii: FONT, eastAsia: FONT, hAnsi: FONT }, size: 20 } } } },
  numbering: { config: [{ reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '・', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 400, hanging: 400 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134, header: 567, footer: 567 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: [PageNumber.CURRENT, ' / ', PageNumber.TOTAL_PAGES], font: FONT, size: 16 })] })] }) },
    children,
  }],
});
Packer.toBuffer(doc).then(b => fs.writeFileSync(OUT, b));
