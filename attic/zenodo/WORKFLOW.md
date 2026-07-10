# Zenodo Upload & GitHub Update — Master Workflow

> File: `zenodo/WORKFLOW.md` | Repository: `HanaTensor/0sm-skills`
> 用途：0-Sphere Model論文の新規アップロード時に実行する全手順。ZenodoアップロードとGitHub更新を統合。
> Last updated: 2026-04-25

---

## 参照ファイル一覧

| ファイル | 内容 |
|---------|------|
| [relation-types.md](relation-types.md) | Zenodo Relation Types完全リスト + 判断基準 |
| [relations-strategy.md](relations-strategy.md) | LLMクローリング戦略 + zenodo_relations.txt作成標準 |
| [latex-standards.md](latex-standards.md) | main.texクリーンアップ規約 + 比較テーブル標準 |
| [readme-template.md](readme-template.md) | readme.txtテンプレート |
| [description-html.md](description-html.md) | Zenodo Description HTML作成標準 |
| [../index.md](../index.md) | 全論文DOI目録 |
| [../global-concept.md](../global-concept.md) | 全横断逆引き（スレッド索引・初出フラグ） |
| [../XX/papers.md](../01/papers.md) | 該当グループの論文詳細 |
| [../XX/concept.md](../01/concept.md) | 該当グループの逆引き辞典 |

---

## 全体手順

```
Step 0. 前提確認（DOIプレースホルダー検出）
Step 1. main.tex クリーンアップ
Step 2. readme.txt 新規作成
Step 3. zenodo_relations.txt 作成
Step 3.5. zenodo_description.html 作成
Step 4. ファイル納品・Zenodoアップロード
Step 5. GitHub 0sm-skills リポジトリ更新
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

## Step 1. main.tex クリーンアップ

参照：[latex-standards.md](latex-standards.md)

```
├── 日本語コメント削除
├── セクション/サブセクション英語コメント確認・追加
├── コメントアウト行削除
└── チェックリスト実行（Section 3のファイル構造チェックリスト）
```

---

## Step 2. readme.txt 新規作成

参照：[readme-template.md](readme-template.md)

```
├── テンプレートから生成
├── main.texからメタデータ抽出（\usepackageリスト、\captionリスト）
├── Research Summaryのプレーンテキスト変換
└── Document Structureセクション生成
```

---

## Step 3. zenodo_relations.txt 作成

参照：[relation-types.md](relation-types.md)、[relations-strategy.md](relations-strategy.md)、[../global-concept.md](../global-concept.md)

```
[1] Cites          → \thebibliographyの\bibitemから
[2] Is supplement to → タイトル・本文のsupplement宣言を確認
[3] Continues      → global-concept.md C.スレッド索引で先行論文を確認
[4] References     → 概念的参照・テーマ的関連論文を探索
[5] Requires       → 前提となる先行論文を特定
[6] Is part of     → シリーズ帰属（直近の先行論文DOIを指定）
[Reverse Relations] → 対象論文への逆方向更新推奨リスト
```

同一DOIへの複数Relation重ねがけを検討する（[relation-types.md Section 3](relation-types.md)参照）。

---

## Step 3.5. zenodo_description.html 作成

参照：[description-html.md](description-html.md)

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
  ├── main.tex（クリーンアップ済み）
  ├── readme.txt（新規作成）
  ├── zenodo_relations.txt（英語のみ、LLMクローリング最適化）
  └── zenodo_description_[N].html（Description欄コピペ用）
```

TikZを使用する論文の場合、`fig_*.tikz` 等の外部図表ファイルがあれば main.tex と同じアーカイブに同梱する。

---

## Step 5. GitHub 0sm-skills リポジトリ更新 ⭐

**ZenodoへのDOI確定後に実施する。**

### 5.1 index.md を更新

ファイル：[../index.md](../index.md)

```
該当グループの表に新論文エントリを追加:
  | [#] | [Date] | [Title] | [DOI link] |

Version Relationshipsに追記（補足・新版関係があれば）:
  | [#N] | [Relation] | [#M] | [Note] |
```

### 5.2 該当グループの papers.md を更新

ファイル：`XX/papers.md`（論文番号からグループを特定）

```
グループ対応表:
  01/papers.md → #1–#10
  02/papers.md → #11–#20
  03/papers.md → #21–#30
  04/papers.md → #31–#40
  05/papers.md → #41–#47
  07/papers.md → #48–#60（現在#48–）※06/は欠番
  ※ #61を超えたら 08/papers.md を新規作成

新論文セクションを追加:
  ## #[N] — [Title] ([Date])
  **DOI:** [DOI]
  **Core concept:** ...
  **Key equations:** ...（コードブロック）
  **Key:** ...
```

### 5.3 該当グループの concept.md を更新

ファイル：`XX/concept.md`

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

ファイル：[../global-concept.md](../global-concept.md)

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

論文#61（または次のグループ境界）を追加する場合：

```
1. 08/ ディレクトリを作成
2. 08/papers.md を新規作成（01/papers.mdのフォーマット参照）
3. 08/concept.md を新規作成（01/concept.mdのフォーマット参照）
4. index.mdのQuick Navigationテーブルに08/を追加
5. global-concept.mdのヘッダーコメントを更新
6. pipeline-manifest.md の Active Group Files を 08/ に差し替え、07/ を Archive へ移動
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
