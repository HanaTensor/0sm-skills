# readme.txt Template

> File: `zenodo/readme-template.md` | Repository: `HanaTensor/0sm-skills`
> 用途：Zenodoアーカイブ同梱用readme.txtの新規作成テンプレート。`[PLACEHOLDER]` を論文固有の情報に置換する。

---

## テンプレート本文

```text
================================================================================
[FULL TITLE OF THE PAPER]
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: [Month Day, Year]

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the [document type description]:

1. main.tex
   - Main LaTeX source file ([brief description])
   - Document class: article, 12pt, letterpaper
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
  [LIST ALL PACKAGES FROM \usepackage IN main.tex]

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references,
      equations, and hyperlinks.

Alternatively, use Overleaf with the following settings:
  - Main document: main.tex
  - Compiler: pdfLaTeX
  - TeX Live version: 2025
  - Compile mode: Normal
  - Stop on first error: ON (recommended)
  - Autocompile: ON (optional)

================================================================================
ABSTRACT
================================================================================

[RESEARCH SUMMARY FROM THE PAPER - plain text version, no LaTeX markup.
 Replace special characters:
   alpha  for  α
   gamma  for  γ
   approximately  for  ≈
   hbar  for  ℏ
   omega  for  ω
 Keep to 1-2 paragraphs summarizing core contribution.]

Key topics include:
- [TOPIC 1]
- [TOPIC 2]
- [TOPIC 3]
- [...]

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This [document type] builds upon and clarifies concepts from:

Primary references:
1. "[Full Title]" (Zenodo [Year])
   DOI: 10.5281/zenodo.[ID]

2. "[Full Title]" (Zenodo [Year])
   DOI: 10.5281/zenodo.[ID]

[IF APPLICABLE:]
Foundational framework ([framework description]):
3. "[Full Title]" (Zenodo [Year])
   DOI: 10.5281/zenodo.[ID]

[BRIEF STATEMENT OF HOW THIS DOCUMENT RELATES TO PREVIOUS WORK]

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:
- [RESULT 1]
- [RESULT 2]
- [...]

What the model CANNOT currently derive:
- [LIMITATION 1]
- [LIMITATION 2]
- [...]

[CONCLUDING STATEMENT ON SCOPE AND INTEGRITY]

================================================================================
DOCUMENT STRUCTURE
================================================================================

[LIST ALL SECTIONS AND SUBSECTIONS:]

Section 1: [Title]
  - [Brief description]

Section 2: [Title]
  2.1 [Subsection Title]
  2.2 [Subsection Title]
  [...]

[...]

Appendices:
  - [List non-numbered sections: Glossary, Acknowledgments, Bibliography, etc.]

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "[FULL TITLE],"
  Zenodo ([Year]).
  https://doi.org/10.5281/zenodo.[ID]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 ([Month Day, Year])
  - Initial release [brief description of content]
  [LIST KEY FEATURES/CONTRIBUTIONS]

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a limited
supportive role for textual organization during document preparation.
All physical interpretations, methodological judgments, and philosophical
commitments remain the responsibility of the author.

The scientific content, conceptual framework, and theoretical interpretations
presented in this document were conceived and developed by the author, who
assumes full responsibility for all claims and interpretations herein.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: article, 12pt, letterpaper
Page layout: 2.5cm margins (all sides)
Line spacing: 1.5 (onehalfspacing)
Font: Computer Modern (LaTeX default)

Tables:
  [LIST ALL TABLES WITH NUMBERS AND DESCRIPTIONS]

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref
  - Hyperlinked bibliography and DOI links

Compilation:
  - First pass: resolves most content
  - Second pass: resolves all cross-references and hyperlinks

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

If uploading to Overleaf, use these project settings:

Compiler Settings:
  Main document:       main.tex
  Compiler:            pdfLaTeX
  TeX Live version:    2025
  Compile mode:        Normal

Error Handling:
  Stop on first error: ON (recommended for debugging)
  Autocompile:         ON (optional, for real-time preview)

The document has been tested and compiles successfully with these settings.

================================================================================
END OF README
================================================================================
```

---

## 作成時の注意事項

1. **文字エンコーディング：** UTF-8。本文中では特殊文字を避けASCII表現を使用
2. **行幅：** 80文字程度で折り返し（可読性確保）
3. **セクション区切り：** `=` 80文字のライン
4. **パッケージリスト：** main.texの `\usepackage` 行から自動抽出
5. **テーブルリスト：** main.texの `\caption` から自動抽出
6. **参照リスト：** `\thebibliography` およびRelated Publicationsから抽出

---

*Last updated: 2026-03-22 | See also: `zenodo/latex-standards.md`*
