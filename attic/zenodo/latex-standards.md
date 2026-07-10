# LaTeX main.tex Standards

> File: `zenodo/latex-standards.md` | Repository: `HanaTensor/0sm-skills`
> 用途：0-Sphere Model論文のmain.texクリーンアップ規約。コメント形式、禁止事項、比較テーブル標準。

---

## 1. コメント規約

### セクション直前（`\section`）

```latex
% ========================================
% Section N: [Section Title in English]
% ========================================
\section{...}
```

### 非番号セクション（`\section*`）直前

```latex
% ========================================
% [Name] (e.g., Glossary, Acknowledgments, Bibliography)
% ========================================
\section*{...}
```

### サブセクション（`\subsection`）直前

```latex
% ----------------------------------------
% Subsection N.M: [Subsection Title]
% ----------------------------------------
\subsection{...}
```

### サブサブセクション（`\subsubsection`）直前

```latex
% ----------------------------------------
% Subsubsection N.M.K: [Subsubsection Title]
% ----------------------------------------
\subsubsection{...}
```

### テーブル（`\begin{table}`）直前

```latex
% ----------------------------------------
% Table N: [Table Description]
% ----------------------------------------
\begin{table}[...]
```

### ドキュメント構造区切り（プリアンブル標準）

```latex
% ========================================
% Document Class and Package Setup
% ========================================

% ========================================
% Page Layout Configuration
% ========================================

% ========================================
% Section Title Formatting
% ========================================

% ========================================
% Document Begin
% ========================================

% ========================================
% Title, Author, and Date
% ========================================

% ========================================
% Table of Contents
% ========================================

% ========================================
% Research Summary
% ========================================

% ========================================
% End of Document
% ========================================
```

---

## 2. 禁止事項

- **日本語コメントの全削除：** `%` に続く日本語テキストはすべて削除する
- **コメントアウト行の削除：** `%\date{\today}` のような不要なコメントアウト行は残さない
- **空コメントの禁止：** `%` のみの行は不要（空行で代替）

---

## 3. ファイル構造チェックリスト

main.texアップロード前に確認する項目：

- [ ] 日本語コメントがゼロであること
- [ ] 全セクションに英語コメントブロックがあること
- [ ] 全サブセクションに英語コメントブロックがあること
- [ ] テーブルにコメントブロックがあること
- [ ] `\label` と `\ref` の整合性
- [ ] DOIリンクが `\href{https://doi.org/...}{DOI: ...}` 形式であること
- [ ] **`DOI to be assigned` が草稿に残っていないこと**（残存する場合は作業中断 → DOI取得後に再開）
- [ ] `DOI Pending` が草稿に残っていないこと（確定DOIへ置換済みであること）
- [ ] `\date{}` が明示的な日付（`\today` ではない）であること
- [ ] 二重コンパイルで全参照が解決されること

---

## 4. 比較テーブルの作成要領（Supplement標準）

### 4.1 背景と目的

Supplement論文で2つの物理的枠組みを対比する際は、**独立したセクション内に比較テーブルを配置する**。テーブルは査読者にとって最もスキャンしやすい形式であり、誤読防止・理論輪郭の明示・将来論文への布石として機能する。

### 4.2 テーブルの配置構造

比較テーブルを含むセクションは以下の3部構成とする：

1. **概念的導入段落**（1段落）— 2つの対象が表面上類似しているが構造的に異なることを宣言する。疑問形を使わず平叙文で書く。
2. **テーブル本体** — 下記標準テンプレート参照。
3. **テーブル後の解説段落群** — `\paragraph` 見出しで層別に説明する。

### 4.3 テーブルのLaTeXコード標準

```latex
% ----------------------------------------
% Table N: [Table Title]
% ----------------------------------------
\begin{table}[h]
\centering
\textbf{Table N. [表題（テーブル上部に太字で表示）]}\\[6pt]
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Feature} & \textbf{[Case A]} & \textbf{[Case B]} \\[6pt]
\midrule\\[-4pt]
[行1の比較項目] & [Case A の内容] & [Case B の内容] \\[8pt]
[行2の比較項目] & [Case A の内容] & [Case B の内容] \\[8pt]
[数式を含む行]  & $\displaystyle\int ...$ & $\displaystyle\oint ...$ \\[12pt]
[最終行]        & [Case A の内容] & [Case B の内容] \\[4pt]
\bottomrule
\end{tabularx}
\caption{[キャプション文（テーブル下部）。両者に共通する構造と根本的差異を1〜2文で要約する。]}
\label{tab:[identifier]}
\end{table}
```

### 4.4 行間スペースの標準値

| 行の種類 | 末尾スペース |
|---------|------------|
| ヘッダー行（`\toprule` 直後） | `\\[6pt]` |
| `\midrule` 直後の調整 | `\\[-4pt]`（余分な空白を相殺） |
| 通常のデータ行 | `\\[8pt]` |
| 数式（`\displaystyle`）を含む行 | `\\[12pt]` |
| 最終データ行（`\bottomrule` 直前） | `\\[4pt]` |

**重要：**
- `\textbf{Table N. ...}\\[6pt]` — 表題はテーブル**上部**、太字
- `\caption{...}` と `\label{...}` — テーブル**下部**（`\end{tabularx}` の後）
- `\caption` の前に `\label` を置かない（参照番号がずれる）

### 4.5 標準7行カテゴリ（Supplement比較テーブル）

Paper #41のTable 1（Shapiro delay vs AB effect）を雛形として：

| 行カテゴリ | 記載内容の指針 |
|-----------|--------------|
| Field type | 各理論の基本的な幾何学的対象（計量・接続・曲率など） |
| Local curvature along path | 経路上の曲率の有無とその意味 |
| Observable | 実験的に測定される量（位相差・固有時差など） |
| Mathematical form | 線積分の具体的な数式表現 |
| Closed loop required | 測定に閉じたループが必要か否かとその理由 |
| Local force | 経路上に局所的な力が存在するか否か |
| Origin of effect | 効果の幾何学的・位相的起源の分類 |

### 4.6 テーブル後の解説段落標準構成

```latex
Table~\ref{tab:[identifier]} organizes these differences across
[N] levels, each of which corresponds to a distinct aspect of
[the comparison being made].

\paragraph{[Layer 1 name]: [declarative summary].}
[本文...]

\paragraph{[Layer 2 name]: [declarative summary].}
[本文...]
```

`\paragraph` 見出しの命名規則：
- ✅ `Physical level: local force and its absence.`
- ✅ `Observational level: a shared structure with an internal distinction.`
- ❌ `Physical level: Is there a local force?`（疑問形禁止）
- ❌ `What they share`（体言止め禁止）

### 4.7 テーブル追加時チェックリスト

- [ ] 表題が `\textbf{Table N. ...}\\[6pt]` 形式でテーブル上部にあること
- [ ] `\caption{}` がテーブル下部（`\end{tabularx}` の後）にあること
- [ ] `\label{}` が `\caption{}` の直後にあること
- [ ] `Table~\ref{tab:[identifier]}` で本文中から参照されていること
- [ ] `\paragraph` 見出しが平叙形であること（疑問形を含まない）
- [ ] readme.txtのTechnical Notes / Tablesセクションに追記されていること

---

*Last updated: 2026-03-22 | See also: `zenodo/readme-template.md`*
