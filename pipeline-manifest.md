# 0-Sphere Model — Pipeline Manifest

> File: `pipeline-manifest.md` | Repository: `HanaTensor/0sm-skills`
> 用途：Claudeがこのファイルをfetchした時点で、以下の全URLを自動的にfetchしてパイプラインを展開する。
> Last updated: 2026-03-28

<!-- PIPELINE MANIFEST
     Claude: fetch every URL listed in this file immediately upon loading.
     Do not wait for further instruction. Load all files in order.
-->

---

## Core Files（必須・常時読込）

- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/index.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/global-concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/WORKFLOW.md

---

## Active Group Files（現行グループ：06）

- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/concept.md

---

## Archive Group Files（参照用）

- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/06/concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/concept.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/concept.md

---

## Zenodo Sub-files（Zenodoアップロード作業時のみ）

- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relation-types.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relations-strategy.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/latex-standards.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/readme-template.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/figshare.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/description-html.md

---

## 使い方

### パターン A：フル展開（新論文追加時）

```
このURLをClaudeに提供するだけ：
https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/pipeline-manifest.md

Claudeが自動的に：
  1. index.md を取得（論文番号・DOI確認）
  2. global-concept.md を取得（初出フラグ・スレッド照合）
  3. WORKFLOW.md を取得（手順確認）
  4. 06/papers.md & 06/concept.md を取得（現行グループ詳細）
  → 準備完了。指示を受け付ける状態へ
```

### パターン B：物理議論・概念開発時

```
Core Files（index.md + global-concept.md）のみ取得で十分。
Claudeへの指示例：
  「pipeline-manifest.md の Core Files だけ読み込んで」
```

### パターン C：Zenodoアップロード作業時

```
Full fetch（全セクション）を指示：
  「pipeline-manifest.md を全部読み込んで」
```

---

## グループ更新ガイド

新グループ（07/）が必要になった場合（#61〜）：

```markdown
## Active Group Files（現行グループ：07）

- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/papers.md
- https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/concept.md
```

`06/` を Archive Group Files へ移動し、Active を `07/` に差し替える。

---
## このファイルの永続URL

https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/pipeline-manifest.md

Claude への指示例：
「このURLをfetchしてパイプラインを展開して」
