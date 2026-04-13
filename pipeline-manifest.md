## Active Group Files（現行グループ：07）

- [07/papers.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/papers.md)
- [07/concept.md](https://cdn.jsdelivr.net/gh/HanaTensor/0sm-skills@main/07/concept.md)

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
