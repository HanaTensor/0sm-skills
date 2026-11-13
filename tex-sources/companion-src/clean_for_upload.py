#!/usr/bin/env python3
"""Upload cleanup for 0SM main.tex (latex-standards.md of 0sm-zenodo-upload).
usage: clean.py in.tex out.tex "<header lines separated by |>"
"""
import re, sys

src, dst, header = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()

JP = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\u3000-\u303F\uFF00-\uFFEF]')
EQ = '% ' + '=' * 40
DA = '% ' + '-' * 40

# 1. strip any existing header comment block before \documentclass
s = s[s.index('\\documentclass'):]

# 2. translate preamble comments
trans = {
    '% 基本パッケージ': '% Basic packages',
    '% 量子力学記法': '% Quantum-mechanics notation',
    '% ハイパーリンク': '% Hyperlinks',
    '% キャプション設定': '% Caption settings',
    '% 数式番号をセクションごとに': '% Equation numbering by section',
    '% タイポグラフィ調整': '% Typography adjustments',
    '% マイクロタイポグラフィ': '% Microtypography',
    '% \\midrule、\\addlinespace、\\bottomruleを使う': '% Table rules (\\midrule, \\addlinespace, \\bottomrule)',
    '%   前 (block separator)': '%   space before (block separator)',
    '%                          後 (負値で run-in 維持)': '%                          space after (negative value keeps the heading run-in)',
    '% 色定義 (薄いブルー系 - 学術論文向け)': '% Colour definitions (light blue palette for listings)',
    '% Pythonスタイル定義': '% Python listing style',
}
for a, b in trans.items():
    s = s.replace(a, b)

# 3. remove commented-out LaTeX commands and empty comments
lines = []
for ln in s.split('\n'):
    st = ln.strip()
    if re.match(r'^%\s*\\[A-Za-z]', st):      # commented-out command
        continue
    if st == '%':                             # empty comment
        continue
    lines.append(ln)
s = '\n'.join(lines)

# 4. preamble block header and document-structure blocks
s = f"{EQ}\n% Document Class and Package Setup\n{EQ}\n" + s
s = s.replace('\\begin{document}', f"{EQ}\n% Document Begin\n{EQ}\n\\begin{{document}}", 1)
s = s.replace('\\title{', f"{EQ}\n% Title, Author, and Date\n{EQ}\n\\title{{", 1)
s = s.replace('\\begin{abstract}', f"{EQ}\n% Abstract\n{EQ}\n\\begin{{abstract}}", 1)
s = s.replace('\\begin{acknowledgments}', f"{EQ}\n% Acknowledgments\n{EQ}\n\\begin{{acknowledgments}}", 1)
s = s.replace('\\begin{thebibliography}', f"{EQ}\n% Bibliography\n{EQ}\n\\begin{{thebibliography}}", 1)
s = s.replace('\\end{document}', f"{EQ}\n% End of Document\n{EQ}\n\\end{{document}}", 1)

def plain(t):
    t = re.sub(r'\$([^$]*)\$', lambda m: m.group(1).replace('\\', ''), t)
    t = t.replace('\\\\', ' ').replace('~', ' ')
    t = re.sub(r'\\[A-Za-z]+\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\[A-Za-z]+', '', t)
    return re.sub(r'\s+', ' ', t).strip()

# 5. section / subsection / table / figure blocks
out, sec, sub, app, tab, fig = [], 0, 0, False, 0, 0
for ln in s.split('\n'):
    m = re.match(r'^\\(section|subsection)\{(.*)\}\s*$', ln)
    if ln.strip() == '\\appendix':
        app, sec = True, 0
    if m:
        kind, title = m.group(1), plain(m.group(2))
        if kind == 'section':
            sec += 1; sub = 0
            lab = f"Appendix {chr(64 + sec)}" if app else f"Section {sec}"
            out += [EQ, f"% {lab}: {title}", EQ]
        else:
            sub += 1
            lab = f"Appendix {chr(64 + sec)}.{sub}" if app else f"Subsection {sec}.{sub}"
            out += [DA, f"% {lab}: {title}", DA]
    if re.match(r'^\\begin\{table\*?\}', ln):
        tab += 1; out += [DA, f"% Table {tab}", DA]
    if re.match(r'^\\begin\{figure\*?\}', ln):
        fig += 1; out += [DA, f"% Figure {fig}", DA]
    out.append(ln)
s = '\n'.join(out)

# 6. caption text into the table/figure comment
def add_caption(s, env):
    pat = re.compile(r'(% ' + env + r' (\d+))\n(' + re.escape(DA) + r')\n(\\begin\{' + env.lower() + r'\*?\}.*?\\caption\{\\textbf\{(.*?)\}\})', re.S)
    return pat.sub(lambda m: f"{m.group(1)}: {plain(m.group(5))}\n{m.group(3)}\n{m.group(4)}", s)
s = add_caption(s, 'Table'); s = add_caption(s, 'Figure')

# 7. DOI links: \href{https://doi.org/X}{doi:X} -> {DOI: X}
s = re.sub(r'\\href\{https://doi\.org/([^}]*)\}\{(?:doi:|https://doi\.org/)?[^}]*\}', r'\\href{https://doi.org/\1}{DOI: \1}', s)

# 8. file header
hdr = [EQ] + ['% ' + h for h in header.split('|')] + [EQ, '']
s = '\n'.join(hdr) + s

bad = [l for l in s.split('\n') if l.lstrip().startswith('%') and JP.search(l)]
anyjp = [l for l in s.split('\n') if JP.search(l)]
open(dst, 'w', encoding='utf-8').write(s)
print('japanese comment lines left:', len(bad), '| japanese anywhere:', len(anyjp))
for l in anyjp[:5]: print('  ', l[:100])
print('sections', sec, 'tables', tab, 'figures', fig)
