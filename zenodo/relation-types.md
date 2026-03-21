# Zenodo Relation Types — Complete Reference

> File: `zenodo/relation-types.md` | Repository: `HanaTensor/0sm-skills`
> 用途：ZenodoのRelated works入力フォームの全選択肢と、0-Sphere Model論文への適用判断基準。

---

## 1. Zenodo Relation Types — UI完全リスト

以下はZenodoの "Related works" 入力フォームに表示される全選択肢（UI画面スキャンに基づく）。

| Relation | 方向性 | カテゴリ | 使用場面 |
|----------|--------|----------|---------|
| **Is supplement to** | 本論文 → 補完先 | 補完 | 本論文が他論文の補遺・補足として書かれた場合 |
| **Is supplemented by** | 本論文 ← 補完元 | 補完 | 他論文が本論文を補足している場合 |
| **Cites** | 本論文 → 引用先 | 引用 | 本文中で `\cite` / `[N]` で正式引用した論文 |
| **Is cited by** | 本論文 ← 引用元 | 引用 | 他論文が本論文を引用している場合 |
| **References** | 本論文 → 参照先 | 参照 | Related Publications や言及したが正式引用でない論文 |
| **Is referenced by** | 本論文 ← 参照元 | 参照 | 他論文が本論文を参照している場合 |
| **Continues** | 本論文 → 先行 | 継続 | 本論文が先行研究を継続する場合 |
| **Is continued by** | 本論文 ← 後続 | 継続 | 他論文が本論文を継続する場合 |
| **Has version** | 本論文 ← 派生版 | バージョン | 本論文に別バージョンが存在する場合 |
| **Is new version of** | 本論文 → 旧版 | バージョン | 本論文が旧版の更新である場合 |
| **Is previous version of** | 本論文 → 新版 | バージョン | 本論文が新版の旧版である場合 |
| **Is version of** | 本論文 → 版元 | バージョン | 本論文がある版の一つである場合 |
| **Is part of** | 本論文 → 親 | 構成 | 本論文がシリーズや論文集の一部である場合 |
| **Has part** | 本論文 ← 子 | 構成 | 本論文が他の構成要素を含む場合 |
| **Describes** | 本論文 → 記述対象 | 記述 | 本論文がデータセット等を記述する場合 |
| **Is described by** | 本論文 ← 記述元 | 記述 | 他文書が本論文を記述する場合 |
| **Documents** | 本論文 → 文書化対象 | 記述 | 本論文が対象を文書化する場合 |
| **Is documented by** | 本論文 ← 文書化元 | 記述 | 他文書が本論文を文書化する場合 |
| **Compiles** | 本論文 → 編纂対象 | 編纂 | 本論文が他資料を編纂する場合 |
| **Is compiled by** | 本論文 ← 編纂元 | 編纂 | 他資料が本論文を編纂する場合 |
| **Reviews** | 本論文 → レビュー対象 | 評価 | 本論文が他論文をレビューする場合 |
| **Is reviewed by** | 本論文 ← レビュー元 | 評価 | 他論文が本論文をレビューする場合 |
| **Is source of** | 本論文 → 派生先 | 派生 | 本論文が他の成果物の元である場合 |
| **Is derived from** | 本論文 ← 派生元 | 派生 | 本論文が他の成果物から派生した場合 |
| **Is original form of** | 本論文 → 変形先 | 変形 | 本論文が変形版の原形である場合 |
| **Is variant form of** | 本論文 → 原形 | 変形 | 本論文が原形の変形版である場合 |
| **Is identical to** | 双方向同一 | 同一性 | 同一内容が別リポジトリにある場合 |
| **Obsoletes** | 本論文 → 廃止先 | 廃止 | 本論文が旧論文を置き換える場合 |
| **Is obsoleted by** | 本論文 ← 廃止元 | 廃止 | 本論文が新論文に置き換えられた場合 |
| **Is published in** | 本論文 → 掲載先 | 掲載 | ジャーナルや論文集に掲載された場合 |
| **Requires** | 本論文 → 必要先 | 依存 | 本論文が他資料を前提とする場合 |
| **Is required by** | 本論文 ← 必要元 | 依存 | 他資料が本論文を前提とする場合 |
| **Has metadata** | 本論文 → メタデータ | メタ | 本論文にメタデータ記録がある場合 |
| **Is metadata for** | 本論文 → メタデータ対象 | メタ | 本論文がメタデータとして機能する場合 |

---

## 2. 紐付け判断基準（0-Sphere Model論文用）

| 判断基準 | Relation |
|----------|----------|
| `\thebibliography` 内の `\bibitem` で引用 | **Cites** |
| Related Publications セクションに記載 | **References** |
| 本文中でDOIリンク付きで言及（`\bibitem` ではない） | **References** |
| 明示的に「本論文は〜の補遺である」とタイトル・本文に記載 | **Is supplement to** |
| 同シリーズの先行論文を概念的に発展・継続させている | **Continues** |
| 同テーマの論文をより詳細に展開した版 | **Is derived from** |
| 後続論文がすでに存在し、本論文をベースにしている | **Is source of** |
| 同一内容がviXra等の別リポジトリにも存在する | **Is identical to** |
| 本論文の理解に先行論文の読了が必要 | **Requires** |
| 0-Sphere Modelシリーズの一部（常に付与） | **Is part of** |

---

## 3. 同一DOIへの複数Relation付与パターン（推奨）

| DOI（論文）の性格 | 付与するRelations |
|-----------------|-----------------|
| 直接 `\bibitem` 引用 + 本論文の補完先 | Cites + Is supplement to |
| 直接 `\bibitem` 引用 + 継続発展元 | Cites + Continues |
| 概念参照 + 前提知識として必要 | References + Requires |
| 同シリーズ先行論文 + 継続 | Is part of + Continues |

---

*Last updated: 2026-03-22 | See also: `zenodo/relations-strategy.md`*
