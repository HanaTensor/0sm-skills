# 0sm-skills — 0-Sphere Model reference repository

Satoshi Hanamura の 0-Sphere Model 論文系列の参照リポジトリ。**寄託済み 63 本**（#1–#64、#16 永久欠番）＋**未寄託 4 本**（#65–#68）。

## 現行構成（これだけ見ればよい）

| 場所 | 内容 | 正典性 |
|---|---|---|
| [index.md](index.md) | 全論文 DOI 表（公開向け） | baseline の `context/doi-canonical.md` の写し。齟齬時は baseline が正 |
| [wall-practice-index.md](wall-practice-index.md) | 壁練（構想議論）の入口: §0 現在地（二前線）・§2 地雷・発火チェーン・課題台帳 | skill `0sm-wall-practice` の fetch 先。**状態の正典** |
| [trunks/](trunks/README.md) | 派生議論の起点となる自己完結セル（一幹＝一ファイル）。現在 T1 | 幹本体が正典。index に内容を複製しない |
| `tex-sources/NN/` | 論文 #NN の一次資料（main.tex=Zenodo清書版 / main-overleaf.tex=Overleaf原本 / overleaf/rK/=完全スナップショット / PDF / 図版 / readme。規約は [tex-sources/OVERLEAF-MANIFEST.md](tex-sources/OVERLEAF-MANIFEST.md)） | 一次資料の正典 |
| `workspace-baselines/` | curate workspace の完全スナップショット（最新 tar 1本で全引き継ぎ完結） | 個票・派生索引の正典 |
| `history/` | 大きな作業セッションの履歴文書（日付別） | 経緯の記録 |

## Claude での使い方

- **壁練**: `wall-practice-index.md` を fetch（raw URL 推奨。jsDelivr はキャッシュ遅延あり）→ **§0 現在地 → §2 地雷**の順に読む → テーマが幹に該当すれば `trunks/T<n>-*.md` を丸ごと読む
- **skill 本体の正典**: `skill-updates/0sm-wall-practice-SKILL.md`。org カタログ側へ反映するのは User の手作業（反映漏れがあると転換前の版が発火する）
- **curate / Zenodo 寄託**: skill `0sm-corpus-curate` / `0sm-zenodo-upload` を invoke（規約の正典はスキル側。本 repo にコピーを置かない）
- **原文精読**: `https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/NN/main.tex`（Zenodo 清書版。404 の番号は未清書 → `.../NN/main-overleaf.tex` に Overleaf 原本が必ずある）

## 旧構成（deprecated）

`attic/` 配下の `01/`〜`07/`（グループ別 papers/concept）、`pipeline-manifest.md`、`global-concept.md`、`zenodo/`（skill 旧コピー）は
2026-04 以前の CDN-fetch 方式の遺産で、現在は更新されない。**参照しないこと。**
