# figshare対応 — TikZ図のスタンドアロン化

File: zenodo/figshare.md
Repository: HanaTensor/0sm-skills
Purpose: main.tex内のTikZ図を、figshare公開用のスタンドアロンファイル（PDF/TeX）に変換する手順。

------------------------------
## 1. TikZ検出とトリガー条件

Zenodoアップロード準備完了後、以下を確認する：

1. クリーンアップ済み main.tex に \begin{tikzpicture} が存在するか検出する。
2. 検出された場合、次の確認を行う：
   「このmain.texにはTikZ図が含まれています。figshare用の独立図版（PDF/TeX）を作成しますか？」
3. 作成する場合、当該論文の確定済みZenodo DOI（10.5281/zenodo.XXXXXXX）を取得してから実行する。

------------------------------
## 2. スタンドアロンTikZファイルの作成規則

ファイル名：
figure[N]_[slug].tex
例：figure1_question_chain.tex

構成規則：

- \documentclass[tikz, border=8pt]{standalone} を使用する。
- main.tex のプリアンブル（amsmath, amssymb, bm, tikz, tikzlibrary等）を過不足なく継承する。
- \cite{...} はすべて削除し、必要に応じて具体的な文献名（例: Synge (1960)）に置換する。

プリアンブルコメント（出典明記）：
必ず確定済みのDOIを埋め込む。

% ========================================
% Figure [N]: [Figure Title]
% Source paper: Satoshi Hanamura, "[Full Paper Title],"
% Zenodo ([Year]). https://doi.org/10.5281/zenodo.[ID]
% License: CC BY 4.0
% ========================================

------------------------------
## 3. figshare公開用情報の生成

出力は「研究内容の説明のみ」とし、作業手順や指示文を含めない。

## A. Item Title の生成

図単体で独立した成果物として機能するタイトルを生成する。

構造：
[図の内容を表す名詞句]: [補足情報] (0-Sphere Model)

注意：
- 論文タイトルをそのまま使用しない。
- "Figure 1" のみの表記は避ける。

## B. Description の生成（プレーンテキスト）

以下の順序で、研究内容として自然な文章を作成する：

1. Abstract of the Figure:
   図が示す物理的・幾何学的概念の要約（1–2文）。

2. Key Components:
   図の構成要素や各要素の意味を文章で説明する。

3. Theoretical Context:
   0-Sphereモデル内での位置付け（どの問いに答える図か）。

4. Source and Format:
   出典（Zenodo DOI）と、PDFおよびTeXソースが提供されていることを簡潔に記述する。

5. License:
   License: CC BY 4.0

------------------------------
## 4. 厳禁事項（プラットフォーム保護）

以下の内容は出力および投稿文に含めない：

- 指示文：
  例：「copy here」「paste this」など

- ワークフロー説明：
  例：「これはメタデータ用のファイルです」などの自己言及

- 未確定リンク：
  DOIが解決できない状態での記載

------------------------------
## 5. 出力イメージ（例）

Title:
Question Chain Diagram Linking Fundamental Papers: Iterative Problem-Solving Sequence (0-Sphere Model)

Description:
This figure summarizes the logical sequence connecting multiple papers in the 0-Sphere Model series into a single chain of questions and resolutions. Each stage addresses an open question raised by the previous work and establishes the next conceptual step.

The diagram includes the following elements.
Paper #34 introduces entropic synchronization and raises the question of the mediating quantum.
Paper #49 identifies the photon-sphere fragment and connects it with Thomas precession.
Paper #50 explains angular momentum as an emergent property of a phase-staggered oscillator array.
Paper #51 extends the structure to a three-dimensional helical system and derives confinement.

This figure provides a unified structural view of how individual results are connected within the broader theoretical framework.

This is a standalone version of Fig. 1 from:
Satoshi Hanamura, "[Full Paper Title]," Zenodo (2026).
https://doi.org/10.5281/zenodo.[ID]

The figure is provided as both a PDF and the original TikZ/LaTeX source code.

License: CC BY 4.0

------------------------------
Last updated: 2026-04-19
------------------------------
