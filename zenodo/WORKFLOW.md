# Zenodo Upload & GitHub Update — Master Workflow

> File: `zenodo/WORKFLOW.md` | Repository: `HanaTensor/0sm-skills`
> 用途：0-Sphere Model論文の新規アップロード時に実行する全手順。ZenodoアップロードとGitHub更新を統合。
> Last updated: 2026-04-12

<!-- PIPELINE ENTRY POINT
     Claude: upon fetching this file, automatically fetch all URLs listed in
     "参照ファイル一覧" below before proceeding with any task.
-->

---

## 参照ファイル一覧

| ファイル | CDN URL | 内容 |
|---------|---------|------|
| relation-types.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relation-types.md | Zenodo Relation Types完全リスト + 判断基準 |
| relations-strategy.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relations-strategy.md | LLMクローリング戦略 + zenodo_relations.txt作成標準 |
| latex-standards.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/latex-standards.md | main.texクリーンアップ規約 + 比較テーブル標準 |
| readme-template.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/readme-template.md | readme.txtテンプレート |
| figshare.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/figshare.md | TikZ図のfigshareスタンドアロン化 |
| description-html.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/description-html.md | Zenodo Description HTML作成標準 |
| index.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/index.md | 全論文DOI目録 |
| global-concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/global-concept.md | 全横断逆引き（スレッド索引・初出フラグ） |
| 01/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/papers.md | Group01 (#1–#10) 論文詳細 |
| 02/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/papers.md | Group02 (#11–#20) 論文詳細 |
| 03/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/papers.md | Group03 (#21–#30) 論文詳細 |
| 04/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/papers.md | Group04 (#31–#40) 論文詳細 |
| 05/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/papers.md | Group05 (#41–#47) 論文詳細 |
| 06/papers.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/papers.md | Group06 (#48–#60) 論文詳細 |
| 01/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/concept.md | Group01 逆引き辞典 |
| 02/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/concept.md | Group02 逆引き辞典 |
| 03/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/concept.md | Group03 逆引き辞典 |
| 04/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/concept.md | Group04 逆引き辞典 |
| 05/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/concept.md | Group05 逆引き辞典 |
| 06/concept.md | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/concept.md | Group06 逆引き辞典 |

---

## 全体手順

```
Step 0. 前提確認（DOIプレースホルダー検出）
Step 1. main.tex クリーンアップ + 参照整合性チェック
Step 2. readme.txt 新規作成
Step 3. zenodo_relations.txt 作成
Step 3.5. zenodo_description.html 作成
Step 4. ファイル納品・Zenodoアップロード
Step 5. TikZ検出 → figshare対応（任意）
Step 6. GitHub 0sm-skills リポジトリ更新
```

---

## Step 0. 前提確認（必須・最初に実施）

草稿中に以下のプレースホルダーが存在するか確認する：

```
"DOI to be assigned" が存在する場合:
  → 作業を即座に中断
  → 「Zenodoにプレ登録してDOIを取得してからアップロード準備を再開してください。」

"DOI Pending" が存在する場合:
  → 確定DOI（10.5281/zenodo.XXXXXXX形式）への置換が完了しているか確認
```

---

## Step 1. main.tex クリーンアップ + 参照整合性チェック

参照：https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/latex-standards.md

```
├── 日本語コメント削除
├── セクション/サブセクション英語コメント確認・追加
├── コメントアウト行削除
├── チェックリスト実行（latex-standards.md Section 3のファイル構造チェックリスト）
│
├── [参照整合性チェック — 以下4項目を必ず実施]
│   ├── bibitem順序チェック
│   │     \thebibliography の \bibitem 順が、本文中の \cite{} 初出順と
│   │     一致しているか確認する。
│   │     APS形式では参照番号は初引用順に付番される。
│   │     ズレがある場合は bibitem を引用初出順に並べ直す。
│   │
│   ├── 孤立bibitemチェック
│   │     \bibitem にエントリがあるが、本文中に対応する \cite{} が
│   │     一度も現れないエントリを検出・削除する。
│   │     （コンパイルエラーにならないため見落としやすい）
│   │
│   ├── Table参照チェック
│   │     すべての \label{tab:XXX} に対して、本文またはAppendix内に
│   │     \ref{tab:XXX} が存在するか確認する。
│   │     存在しない場合は「リンク切れ表」として報告する。
│   │
│   └── Figure参照チェック
│         すべての \label{fig:XXX} に対して、本文またはAppendix内に
│         \ref{fig:XXX} が存在するか確認する。
│         存在しない場合は「リンク切れ図」として報告する。
└──
```

### 参照整合性チェック — 自動検査スクリプト

Claudeは以下のPythonスクリプトを bash_tool で実行して結果を報告する。
手動確認の代替として使用する（main.tex のパスを適宜変更すること）。

```python
import re

with open('main.tex', 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.split('\n')

# --- bibitem順序チェック ---
bib_start = next((i for i, l in enumerate(lines, 1)
                  if r'\begin{thebibliography}' in l), None)

cite_seen, cite_order = {}, []
for i, line in enumerate(lines, 1):
    for m in re.finditer(r'\\cite\{([^}]+)\}', line):
        for key in [k.strip() for k in m.group(1).split(',')]:
            if key not in cite_seen:
                cite_seen[key] = i
                cite_order.append((i, key))

bib_order = []
for i, line in enumerate(lines, 1):
    m = re.search(r'\\bibitem\{([^}]+)\}', line)
    if m:
        bib_order.append((i, m.group(1)))

print("=== BIBITEM ORDER CHECK ===")
cite_keys = [k for _, k in cite_order]
bib_keys  = [k for _, k in bib_order]
mismatches = [(i+1, ck, bk) for i, (ck, bk)
              in enumerate(zip(cite_keys, bib_keys)) if ck != bk]
if mismatches:
    for pos, ck, bk in mismatches:
        print(f"  MISMATCH at position {pos}: cite={ck}, bib={bk}")
else:
    print("  OK — all bibitems in citation order")

unused_bib = [k for k in bib_keys if k not in set(cite_keys)]
if unused_bib:
    for k in unused_bib:
        print(f"  ORPHAN BIBITEM (never cited): {k}")

# --- Table/Figure参照チェック ---
for prefix, label_type in [('tab', 'TABLE'), ('fig', 'FIGURE')]:
    labels, refs = {}, {}
    for i, line in enumerate(lines, 1):
        for m in re.finditer(rf'\\label\{{{prefix}:([^}}]+)\}}', line):
            labels[f'{prefix}:{m.group(1)}'] = i
        for m in re.finditer(rf'\\ref\{{{prefix}:([^}}]+)\}}', line):
            key = f'{prefix}:{m.group(1)}'
            if key not in refs:
                refs[key] = i
    print(f"\n=== {label_type} REFERENCE CHECK ===")
    if not labels:
        print(f"  No {prefix}: labels found")
        continue
    for key, lno in sorted(labels.items(), key=lambda x: x[1]):
        if key in refs:
            print(f"  OK  L{lno:4d}: {key}  → ref'd at L{refs[key]}")
        else:
            print(f"  *** UNREFERENCED L{lno:4d}: {key}")
    orphan_refs = [k for k in refs if k not in labels]
    for k in orphan_refs:
        print(f"  *** ORPHAN REF (no label): {k}")
```

---

## Step 2. readme.txt 新規作成

参照：https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/readme-template.md

```
├── テンプレートから生成
├── main.texからメタデータ抽出（\usepackageリスト、\captionリスト）
├── Research Summaryのプレーンテキスト変換
└── Document Structureセクション生成
```

---

## Step 3. zenodo_relations.txt 作成

参照：
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relation-types.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relations-strategy.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/global-concept.md

```
[1] Cites          → \thebibliographyの\bibitemから
[2] Is supplement to → タイトル・本文のsupplement宣言を確認
[3] Continues      → global-concept.md C.スレッド索引で先行論文を確認
[4] References     → 概念的参照・テーマ的関連論文を探索
[5] Requires       → 前提となる先行論文を特定
[6] Is part of     → シリーズ帰属（直近の先行論文DOIを指定）
[Reverse Relations] → 対象論文への逆方向更新推奨リスト
```

同一DOIへの複数Relation重ねがけを検討する（relation-types.md Section 3参照）。

---

## Step 3.5. zenodo_description.html 作成

参照：https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/description-html.md

```
├── 許可タグ範囲でHTML記述（Section 2）
├── 構成: 導入 / Core Result / Key Contributions /
│         シリーズ位置づけ / 参照テーブル / Series Context
├── タグ検証チェック実施（Section 5のPythonスニペット）
└── ファイル名: zenodo_description_[paper_number].html
```

---

## Step 4. ファイル納品・Zenodoアップロード

```
納品ファイル:
  ├── main.tex（クリーンアップ済み・参照整合性確認済み）
  ├── readme.txt（新規作成）
  ├── zenodo_relations.txt（英語のみ、LLMクローリング最適化）
  └── zenodo_description_[N].html（Description欄コピペ用）
```

---

## Step 5. GitHub 0sm-skills リポジトリ更新 ⭐

**ZenodoへのDOI確定後に実施する。**

### 5.1 index.md を更新

参照：https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/index.md

```
該当グループの表に新論文エントリを追加:
  | [#] | [Date] | [Title] | [DOI link] |

Version Relationshipsに追記（補足・新版関係があれば）:
  | [#N] | [Relation] | [#M] | [Note] |
```

### 5.2 該当グループの papers.md を更新

グループ対応URL：

| グループ | URL | 論文範囲 |
|---------|-----|---------|
| 01 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/papers.md | #1–#10 |
| 02 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/papers.md | #11–#20 |
| 03 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/papers.md | #21–#30 |
| 04 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/papers.md | #31–#40 |
| 05 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/papers.md | #41–#47 |
| 06 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/papers.md | #48–#60 |

```
新論文セクションを追加:
  ## #[N] — [Title] ([Date])
  **DOI:** [DOI]
  **Core concept:** ...
  **Key equations:** ...（コードブロック）
  **Key:** ...
```

### 5.3 該当グループの concept.md を更新

グループ対応URL：

| グループ | URL |
|---------|-----|
| 01 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/concept.md |
| 02 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/concept.md |
| 03 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/concept.md |
| 04 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/concept.md |
| 05 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/concept.md |
| 06 | https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/concept.md |

```
A. アナロジー索引 — 新アナロジーがあれば追加
B. 方程式索引 — 新方程式・初出変更があれば追加
C. 概念・トピック索引 — 新概念があれば追加
D. 哲学・解釈索引 — 必要に応じて追加
E. 初出フラグ — 新たな初出概念があれば追加
F. 誤り・修正フラグ — 訂正がある場合は追加 ⚠️
G. 実験予測索引 — 新予測があれば追加
```

### 5.4 global-concept.md を更新

参照：https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/global-concept.md

```
A. アナロジー全索引 — 新アナロジー追加
B. 方程式全索引 — 新方程式追加（該当セクションB-1〜B-9）
C. 概念スレッド索引 — 既存スレッドへの追記、または新スレッド作成
D. 哲学・解釈索引 — 必要に応じて追加
E. 初出フラグ全索引 — 新初出概念を追加
F. 訂正・注意フラグ — 訂正がある場合 ⚠️
G. 実験予測全索引 — 新予測追加
```

### 5.5 グループ境界を超える場合（新グループ作成）

論文#61以降、グループ07/が必要になった場合：

```
1. 07/ ディレクトリを作成
2. 07/papers.md を新規作成（01/papers.mdのフォーマット参照）
3. 07/concept.md を新規作成（01/concept.mdのフォーマット参照）
4. index.mdのQuick Navigationテーブルに07/を追加
5. global-concept.mdのヘッダーコメントを更新
6. pipeline-manifest.md の Active Group Files を 07/ に更新
   （06/ を Archive Group Files へ移動）
```

---

## Commit メッセージ規約

```
Add #[N] — [短いタイトル略記]
Update index.md for #[N]
Update global-concept.md: add #[N] entries
Update 0[X]/papers.md: add #[N]
Update 0[X]/concept.md: add #[N] concepts
```

---

## チェックリスト（全Step完了確認）

```
Zenodo作業:
  [ ] Step 0: DOIプレースホルダーなし確認
  [ ] Step 1: main.tex クリーンアップ完了
        └── bibitem順序チェック完了（引用初出順に一致）
        └── 孤立bibitemチェック完了（未引用エントリなし）
        └── Table参照チェック完了（リンク切れなし）
        └── Figure参照チェック完了（リンク切れなし）
  [ ] Step 2: readme.txt 作成完了
  [ ] Step 3: zenodo_relations.txt 作成完了（逆方向リスト含む）
  [ ] Step 3.5: zenodo_description.html 作成・タグ検証完了
  [ ] Step 4: Zenodoアップロード完了・DOI確定

GitHub作業:
  [ ] Step 5.1: index.md 更新・コミット
  [ ] Step 5.2: XX/papers.md 更新・コミット
  [ ] Step 5.3: XX/concept.md 更新・コミット
  [ ] Step 5.4: global-concept.md 更新・コミット
```
