# 0sm-skills — 0-Sphere Model reference repository

Satoshi Hanamura の 0-Sphere Model 論文系列（63本、#1–#64、#16 永久欠番）の参照リポジトリ。

## 現行構成（これだけ見ればよい）

| 場所 | 内容 | 正典性 |
|---|---|---|
| [index.md](index.md) | 全論文 DOI 表（公開向け） | baseline の `context/doi-canonical.md` の写し。齟齬時は baseline が正 |
| [wall-practice-index.md](wall-practice-index.md) | 壁練（構想議論）の入口: テーマ別発火チェーン・未解決問題台帳・トリガー語彙表 | skill `0sm-wall-practice` の fetch 先 |
| `tex-sources/NN/` | 論文 #NN の一次資料（main.tex=Zenodo清書版 / main-overleaf.tex=Overleaf原本 / overleaf/rK/=完全スナップショット / PDF / 図版 / readme。規約は [tex-sources/OVERLEAF-MANIFEST.md](tex-sources/OVERLEAF-MANIFEST.md)） | 一次資料の正典 |
| `workspace-baselines/` | curate workspace の完全スナップショット（最新 tar 1本で全引き継ぎ完結） | 個票・派生索引の正典 |

## Claude での使い方

- **壁練**: `wall-practice-index.md` を fetch（raw URL 推奨。jsDelivr はキャッシュ遅延あり）
- **curate / Zenodo 寄託**: skill `0sm-corpus-curate` / `0sm-zenodo-upload` を invoke（規約の正典はスキル側。本 repo にコピーを置かない）
- **原文精読**: `https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/NN/main.tex`（Zenodo 清書版。404 の番号は未清書 → `.../NN/main-overleaf.tex` に Overleaf 原本が必ずある）

## 旧構成（deprecated・attic 送り対象）

`01/`〜`07/`（グループ別 papers/concept）、`pipeline-manifest.md`、`global-concept.md`、`zenodo/`（skill 旧コピー）は
2026-04 以前の CDN-fetch 方式の遺産で、現在は更新されない。経緯と処分推奨は `CLEANUP.md` 参照。
