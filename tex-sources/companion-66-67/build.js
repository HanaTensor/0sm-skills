// Build a companion record (.docx) from a content module.
// usage: node build.js content-ja.js out.docx
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType,
  Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle,
  LevelFormat, Footer, PageNumber,
} = require('docx');

const content = require(path.resolve(process.argv[2]));
const out = process.argv[3];
const lang = content.lang;
const FONT = lang === 'ja'
  ? { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: 'Yu Mincho', cs: 'Times New Roman' }
  : { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: 'Yu Mincho', cs: 'Times New Roman' };
const HFONT = lang === 'ja'
  ? { ascii: 'Arial', hAnsi: 'Arial', eastAsia: 'Yu Gothic', cs: 'Arial' }
  : { ascii: 'Arial', hAnsi: 'Arial', eastAsia: 'Yu Gothic', cs: 'Arial' };

const PAGE_W = 11906, MARGIN = 1300; // A4
const TEXT_W = PAGE_W - 2 * MARGIN;

const run = (t, o = {}) => new TextRun({ text: t, font: FONT, size: 21, ...o });
const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
const borders = { top: border, bottom: border, left: border, right: border };

function para(text, o = {}) {
  return new Paragraph({ children: [run(text, o.run || {})], spacing: { after: 140, line: 330 }, alignment: AlignmentType.JUSTIFIED, ...(o.p || {}) });
}

function quote(text, who) {
  const kids = [run(text, { italics: lang !== 'ja' })];
  const ps = [new Paragraph({
    children: kids, indent: { left: 567, right: 340 }, spacing: { before: 60, after: 60, line: 320 },
    border: { left: { style: BorderStyle.SINGLE, size: 12, color: '2E5A88', space: 8 } },
  })];
  if (who) ps.push(new Paragraph({ children: [run(who, { size: 18, color: '555555' })], indent: { left: 567 }, spacing: { after: 160 } }));
  return ps;
}

function table(headers, rows, ratios) {
  const tot = ratios.reduce((a, b) => a + b, 0);
  const widths = ratios.map(r => Math.floor(TEXT_W * r / tot));
  widths[widths.length - 1] += TEXT_W - widths.reduce((a, b) => a + b, 0);
  const cell = (t, w, head) => new TableCell({
    borders, width: { size: w, type: WidthType.DXA },
    shading: head ? { fill: 'DCE6F1', type: ShadingType.CLEAR } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: [run(t, { size: 19, bold: !!head })], spacing: { line: 280 } })],
  });
  return new Table({
    width: { size: TEXT_W, type: WidthType.DXA }, columnWidths: widths,
    rows: [new TableRow({ tableHeader: true, children: headers.map((h, i) => cell(h, widths[i], true)) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, widths[i], false)) }))],
  });
}

const children = [];
children.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun({ text: content.title, font: HFONT, size: 36, bold: true })], alignment: AlignmentType.LEFT }));
if (content.subtitle) children.push(new Paragraph({ children: [run(content.subtitle, { size: 24, color: '2E5A88' })], spacing: { after: 120 } }));
for (const line of content.byline) children.push(new Paragraph({ children: [run(line, { size: 19, color: '444444' })], spacing: { after: 40 } }));
children.push(new Paragraph({ children: [], spacing: { after: 200 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '2E5A88', space: 4 } } }));

for (const b of content.blocks) {
  const [k] = b;
  if (k === 'h1') children.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun({ text: b[1], font: HFONT })] }));
  else if (k === 'h2') children.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun({ text: b[1], font: HFONT })] }));
  else if (k === 'p') children.push(para(b[1]));
  else if (k === 'q') children.push(...quote(b[1], b[2]));
  else if (k === 'ul') for (const it of b[1]) children.push(new Paragraph({ numbering: { reference: 'bul', level: 0 }, children: [run(it)], spacing: { after: 80, line: 320 } }));
  else if (k === 'ol') for (const it of b[1]) children.push(new Paragraph({ numbering: { reference: 'num-' + (b[2] || 'a'), level: 0 }, children: [run(it)], spacing: { after: 80, line: 320 } }));
  else if (k === 'table') { children.push(table(b[1], b[2], b[3])); children.push(new Paragraph({ children: [], spacing: { after: 160 } })); }
  else if (k === 'note') children.push(new Paragraph({ children: [run(b[1], { size: 18, color: '555555' })], spacing: { after: 160, line: 300 } }));
}

const numRefs = ['a', 'b', 'c', 'd', 'e', 'f'].map(x => ({
  reference: 'num-' + x,
  levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 340 } } } }],
}));

const doc = new Document({
  creator: 'Satoshi Hanamura',
  title: content.title,
  styles: {
    default: { document: { run: { font: FONT, size: 21 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: HFONT, size: 36, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 0, after: 120 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 28, bold: true, color: '1F3864' }, paragraph: { spacing: { before: 360, after: 140 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HFONT, size: 24, bold: true, color: '2E5A88' }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 567, hanging: 284 } } } }] },
    ...numRefs,
  ] },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: 16838 }, margin: { top: 1300, bottom: 1300, left: MARGIN, right: MARGIN } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(out, buf); console.log('wrote', out); });
