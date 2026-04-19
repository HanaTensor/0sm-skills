# figshare対応 — TikZ図のスタンドアロン化

> File: `zenodo/figshare.md` | Repository: `HanaTensor/0sm-skills`
> 用途：main.tex内のTikZ図をfigshare公開用スタンドアロンファイルに変換する手順。

---

## 1. TikZ検出とトリガー条件

Zenodoアップロード準備（WORKFLOW.mdのStep 0〜4）が完了した後、以下を確認する：

1. クリーンアップ済み `main.tex` に `\begin{tikzpicture}` が存在するか検出する
2. 検出された場合、以下のメッセージで確認を取る：

```
このmain.texにはTikZ図が含まれています。
figshare用の独立ファイルを作成しますか？
```

3. 作成しない場合 → 作業完了
4. 作成する場合 → 以下の手順を実行する

**前提条件：** 当該論文のZenodo DOI（`10.5281/zenodo.XXXXXXX`）が確定済みであること。DOIが未確定の場合は、Zenodoプレ登録・DOI取得後に作成する。

---

## 2. スタンドアロンTikZファイルの作成規則

**ファイル名：** `figure[N]_[slug].tex`

- `[N]` は論文中の図番号（Fig. 1 → `1`）
- `[slug]` は図の内容を表す2〜4単語のsnake_case（例: `structural_comparison`）

**documentclassとプリアンブル：**

```latex
\documentclass[tikz, border=8pt]{standalone}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{bm}
\usepackage{tikz}
\usetikzlibrary{...}  % main.texと同一のライブラリ
```

**main.texとの差分（必須処理）：**

| 項目 | main.tex | スタンドアロン |
|------|----------|--------------|
| documentclass | revtex4-2等 | standalone[tikz, border=8pt] |
| `\newcommand{\figXxx}{...}` ラッパー | あり | 廃止、tikzpictureを直接配置 |
| `\cite{...}` 参照 | あり | **削除する**（bibliography非存在のため） |
| 出典記載 | bibliography | プリアンブルコメントに確定DOIを直接記載 |
| カスタムマクロ | あり | main.texと同一のものをそのまま転記 |

**プリアンブルコメント標準：**

`[ID]` には当該論文の確定済みZenodo DOI番号（数字部分）を埋め込む。プレースホルダーのまま納品しない。

```latex
% ========================================
% Figure [N]: [Figure Title]
%
% Source paper:
%   Satoshi Hanamura,
%   "[Full Paper Title],"
%   Zenodo ([Year]). https://doi.org/10.5281/zenodo.[ID]
%
% License: CC BY 4.0
% ========================================
```

**コンパイル確認：** 作成後、必ずpdflatexでコンパイルし、エラーゼロ・PDF生成を確認してから納品する。

**納品ファイル：** `.tex` と `.pdf` の2点セット

---

## 3. figshare Item titleの作成規則

figshareのItem titleは**図単体の成果物**として検索・引用される前提で記述する。論文タイトルをそのまま転記しない。

**構造：**
```
[図の内容を表す名詞句]: [補足情報] ([モデル名/シリーズ名])
```

**判断基準：**
- 図として何が描かれているかを先頭に置く
- 論文サブタイトル（"Structural Clarification Note" 等）は含めない
- シリーズ帰属は末尾に括弧書きで添える（キーワード検索対応）
- 70〜120文字程度を目安とする

**例：**
```
Structural Correspondence Between Muon Lifetime Extension and Electron
Anomalous Magnetic Moment: Unified Lorentz-Factor Diagram (0-Sphere Model)
```

---

## 4. figshare Descriptionの作成規則

figshareはMarkdown・HTMLタグを表示に通さない実装が多いため、**プレーンテキスト**で記述する。

**構成（段落順）：**

1. **概要文**（1文）— 図が何を示しているかを平叙文で
2. **パネル説明**（パネル数に応じた段落）— Left/Right/Bottom等のラベルを先頭に
3. **統一原理の説明**（1段落）— 図の底部・中央にある統一式・記号の意味
4. **出典表記**（固定フォーマット）— 論文タイトル、著者名、DOIリンク
5. **ファイル内容の説明**（1文）— PDF + .texソースの両提供である旨
6. **ライセンス**（1行）— `License: CC BY 4.0`

通常のメタデータ（OKなもの）
Figshare が期待しているのはこういう内容：
研究の要約
何を示しているデータか
手法や結果の説明
DOIや関連論文の参照
👉 “研究内容を説明するための情報”
metadata about metadata（問題になりやすいもの）

書かないもの
「この内容をfigshareのフィールドにコピーする」
「アップロード方法の説明」
「このメタデータがどう構成されているか」
「この投稿がどういう意図で作られているか（内部構造の解説）」
👉 “メタデータの使い方・作り方を説明している”

**出典表記の固定フォーマット：**

```
This figure is Fig. [N] of:
Satoshi Hanamura, "[Full Paper Title]," Zenodo ([Year]).
https://doi.org/10.5281/zenodo.[ID]

The figure was produced as a standalone TikZ/LaTeX file
(pdfLaTeX, TeX Live 2025) and is provided both as PDF
and as the original .tex source.
```

---

*Last updated: 2026-03-22 | See also: `zenodo/WORKFLOW.md`*
