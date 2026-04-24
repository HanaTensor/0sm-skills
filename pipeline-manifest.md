# 0-Sphere Model — Pipeline Manifest

> File: `pipeline-manifest.md` | Repository: `HanaTensor/0sm-skills`
> 用途：Claudeがこのファイルをfetchした時点で、以下の全URLを自動的にfetchしてパイプラインを展開する。
> Last updated: 2026-04-25

<!-- PIPELINE MANIFEST
     Claude: fetch every URL listed in this file immediately upon loading.
     Do not wait for further instruction. Load all files in order.
-->

<!-- NOTE: グループ番号について
     06/ は欠番。
     過去に誤って "06/papers.md" というスラッシュ込みのファイル名をリポジトリ直下に作成したため、
     jsDelivr CDN が @main/06/ パスに誤った404レスポンスをキャッシュした。
     パージ後も汚染が残留したため、06/ を使用せず 07/ へ繰り上げた（2026-04-14）。
     現行グループは 07/（論文 #48–）。
-->

<!-- NOTE: figshareについて
     著者のfigshareアカウント凍結により、今後figshare関連作業は行わない（2026-04-25）。
     zenodo/figshare.md はリポジトリから削除済み。
     WORKFLOW.md の旧Step 5（TikZ→figshare対応）も削除済み。
-->

---

## Core Files（必須・常時読込）

- [index.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/index.md)
- [global-concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/global-concept.md)
- [zenodo/WORKFLOW.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/WORKFLOW.md)

---

## Active Group Files（現行グループ：07）

- [07/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/papers.md)
- [07/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/concept.md)

---

## Archive Group Files（参照用）

- [05/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/papers.md)
- [05/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/05/concept.md)
- [04/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/papers.md)
- [04/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/04/concept.md)
- [03/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/papers.md)
- [03/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/03/concept.md)
- [02/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/papers.md)
- [02/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/02/concept.md)
- [01/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/papers.md)
- [01/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/01/concept.md)

---

## Zenodo Sub-files（Zenodoアップロード作業時のみ）

- [zenodo/relation-types.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relation-types.md)
- [zenodo/relations-strategy.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/relations-strategy.md)
- [zenodo/latex-standards.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/latex-standards.md)
- [zenodo/readme-template.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/readme-template.md)
- [zenodo/description-html.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/zenodo/description-html.md)

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
  4. 07/papers.md & 07/concept.md を取得（現行グループ詳細）
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

新グループ（08/）が必要になった場合（#61〜）：

```markdown
## Active Group Files（現行グループ：08）

- [08/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/08/papers.md)
- [08/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/08/concept.md)
```

`07/` を Archive Group Files へ移動し、Active を `08/` に差し替える。

---

## このファイルの永続URL

https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/pipeline-manifest.md

Claude への指示例：
「このURLをfetchしてパイプラインを展開して」
