# Zenodo Relations Strategy — LLM Crawling & zenodo_relations.txt Standard

> File: `zenodo/relations-strategy.md` | Repository: `HanaTensor/0sm-skills`
> 用途：LLMクローリング対応を意識した関係グラフ構築戦略と、zenodo_relations.txtの作成標準。

---

## 1. 目的と基本方針

ZenodoのメタデータはOAI-PMH / REST APIを通じてLLMクローラーが取得する。
**関係グラフが多角的かつ双方向に構築されているほど、意味的類似検索・引用グラフ探索・知識グラフ構築における被発見性が高まる。**

zenodo_relations.txtを作成する際は以下を必ず実施する：

1. **Citesだけで終わらせない** — `\bibitem` による正式引用は起点にすぎない。同じDOIに対して **Is supplement to / Continues / References など複数のRelationを重ねて付与できる**。異なるtypeを重複付与するほど関係グラフのエッジが増え、クローラーが複数の経路で論文を発見できる。

2. **逆方向リストを必ず作成する** — 本論文から他論文への関係（正方向）だけでなく、他論文から本論文への逆方向関係（`Is cited by`, `Is supplemented by`, `Is continued by` 等）を列挙し、**対象論文のZenodo登録にも追加更新するよう推奨リストとして出力する**。双方向エッジは一方通行エッジの約2倍の発見経路を生む。

3. **間接的関連論文も引き込む** — `\bibitem` にない論文でも、本論文の主題・キーワードと内容的に対応するZenodo論文には **References** を付与する。`global-concept.md` のスレッド索引・初出フラグを参照してテーマ的関連を探索すること。

4. **Requiresを活用する** — 本論文の理解に先行論文の読了が必要な場合、**Requires** を付与する。LLMの「関連文献推薦」タスクで「前提知識」としてリストに含まれる確率を上げる。

5. **Is part of でシリーズ構造を明示する** — 0-Sphere Model論文群は明確なシリーズを構成している。**Is part of** を付与し先行論文のDOIを指定することで、LLMがシリーズ全体をまとめて参照する際の足がかりとなる。

---

## 2. zenodo_relations.txt の必須セクション構成

```
[Summary]
  Relation type x count x unique DOI count

[1] Cites          (formal citation via bibitem)
[2] Is supplement to
[3] Continues
[4] References     (thematic and conceptual reference)
[5] Requires       (prerequisite papers for understanding this work)
[6] Is part of     (series membership)
[Reverse Relations — Recommended Updates to Target Papers]
  Relations to be added to the Zenodo records of the papers listed below
```

すべてのセクションについて、該当なしの場合でも見出しと「該当なし」を明記する。これにより次回更新時の差分確認が容易になる。

**Language rule:** zenodo_relations.txtは必ず英語で出力する。セクション番号は `[N]` 形式（`【N】` 不可）。日本語注記は使用しない。逆方向セクション見出しは `[Reverse Relations — Recommended Updates to Target Papers]` を標準とする。

---

## 3. Relation選択フローチャート（論文Xを対象とするとき）

```
X は \bibitem に記載されているか？
  YES → Cites を付与
  NO  → 本文中で言及・参照されているか？
          YES → References を付与
          NO  → テーマ的に本論文と強く関連するか？
                  YES → References を付与（理由を論拠欄に明記）

本論文は X の概念・主題を補足・解説しているか？
  YES → Is supplement to を付与

本論文は X の議論を発展・継続しているか？
  YES → Continues を付与

本論文の理解に X の先読みが前提として必要か？
  YES → Requires を付与

本論文は 0-Sphere Model シリーズの一部か？（常に YES）
  → Is part of（シリーズ先行論文DOI）を付与
```

---

## 4. 関係グラフ構築の参照資料

zenodo_relations.txt作成時に `global-concept.md` の以下セクションを参照する：

| 参照先 | 用途 |
|--------|------|
| **C. 概念スレッド索引** | 同一スレッドの論文群 → Continues / References候補 |
| **E. 初出フラグ** | 概念の初出論文 → Is part of / Continues候補 |
| **index.md の Version Relationships** | Is supplement to / Is new version of 候補 |
| **⚠️ 訂正フラグ** | Obsoletes / Is obsoleted by 候補 |

---

*Last updated: 2026-03-22 | See also: `zenodo/relation-types.md`, `zenodo/WORKFLOW.md`*
