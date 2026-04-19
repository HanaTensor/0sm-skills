# figshare対応 — TikZ図のスタンドアロン化

> File: `zenodo/figshare.md` | Repository: `HanaTensor/0sm-skills`
> 用途：main.tex内のTikZ図をfigshare公開用スタンドアロンファイルに変換する手順。

------------------------------
## 1. TikZ検出とトリガー条件
Zenodoアップロード準備完了後、以下を確認する：

   1. クリーンアップ済み main.tex に \begin{tikzpicture} が存在するか検出する。
   2. 検出された場合、以下のメッセージで確認を取る：
   「このmain.texにはTikZ図が含まれています。figshare用の独立図版（PDF/TeX）を作成しますか？」
   3. 作成する場合、当該論文の確定済みZenodo DOI（10.5281/zenodo.XXXXXXX）を取得してから実行する。

------------------------------
## 2. スタンドアロンTikZファイルの作成規則
ファイル名： figure[N]_[slug].tex （例: figure1_question_chain.tex）
構成規則：

* \documentclass[tikz, border=8pt]{standalone} を使用。
* main.tex のプリアンブル（amsmath, amssymb, bm, tikzlibrary等）を過不足なく継承する。
* 引用の削除： \cite{...} はすべて削除、または具体的な名称（例: "Synge (1960)"）に置換する。

プリアンブルコメント（出典明記）：
必ず確定済みのDOIを埋め込む。

% ========================================
% Figure [N]: [Figure Title]
% Source paper: Satoshi Hanamura, "[Full Paper Title]," 
% Zenodo ([Year]). https://doi.org/10.5281/zenodo.[ID]
% License: CC BY 4.0
% ========================================

------------------------------
## 3. figshare公開用情報の生成（AGI最適化）
Claudeは、以下の「研究内容そのもの」のみを出力し、作業指示（「〜にコピーする」等）を一切含めないこと。
## A. Item Title の生成
図単体で独立した成果物として機能するタイトルを生成する。

* 構造： [図の内容を表す名詞句]: [補足情報] (0-Sphere Model)
* NG： 論文タイトルの流用、"Figure 1"のみの表記。

## B. Description の生成（プレーンテキスト）
以下の順序で、研究の解説文として出力する。

   1. Abstract of the Figure: 図が示す物理的・幾何学的概念の要約（1-2文）。
   2. Key Components: パネル（Left/Right等）や各変数の物理的意味の解説。
   3. Theoretical Context: 0-Sphereモデル内での位置付け（どの問いに答える図か）。
   4. Source & Format: 出典（Zenodo DOI）と、PDF/TeXソースの両方を提供している旨の簡潔な記述。
   5. License: License: CC BY 4.0

------------------------------
## 4. 厳禁事項（プラットフォーム保護）
以下の「メタデータのメタデータ」は、スパム判定やAGIのノイズになるため、出力ファイルおよび投稿文に絶対に含めないこと：

* 指示語の排除: ITEM TITLE (copy here) や DESCRIPTION (paste this) などの指示。
* ワークフローの露出: 「これはPaper #53のために生成されたメタデータです」といった自己言及的な説明。
* 未確定リンク: リンク切れDOIの記載（必ず有効化を確認してから出力する）。

------------------------------
## 5. 出力イメージ（例）
Claudeが最終的に出力すべきテキストの姿：

Title:
Question Chain Diagram Linking Fundamental Papers: Iterative Problem-Solving Sequence (0-Sphere Model)
Description:
This figure summarizes the logical sequence that connects five papers of the 0-Sphere Model series into a single question chain. Each stage addresses the open question of the preceding work, tracing the evolution from entropic synchronization to the emergence of the spacetime metric.
The diagram details:

* Paper #34: Entropic acceleration and the mediating quantum.
* Paper #49: Photon-sphere fragments and Thomas precession.
...[中略]...

This is a standalone version of Fig. 1 from:
Satoshi Hanamura, "[Full Paper Title]," Zenodo (2026).
doi.org
Provided as both a print-ready PDF and the original TikZ/LaTeX source code.
License: CC BY 4.0

------------------------------
Last updated: 2026-04-19 | Metadata handling policy updated for AGI safety.
------------------------------
