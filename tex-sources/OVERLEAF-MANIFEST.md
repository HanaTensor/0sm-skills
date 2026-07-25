# Overleaf Sources Manifest

> Last updated: 2026-07-26 | 詳細な作業履歴は git log を参照（本ファイルは**現在状態と恒久規約のみ**を保持する）

## 配置規約（main.tex 二本立て・2026-07-19 確定）

各論文 #NN のトップ階層には **2 種類の tex を役割固定で置く**:

| ファイル | 役割 |
|---|---|
| `NN/main.tex` | **Zenodo 清書版のみ**（`0sm-zenodo-upload` skill で生成した納品物。英語コメント化・登録用メモ除去済み）。存在＝清書済みシグナル |
| `NN/main-overleaf.tex` | **Overleaf 原本**（日本語コメント込みの執筆版）。#1–#64 に常設。複数リビジョンある場合は最新 rK のコピー |
| `NN/overleaf/rK/` | Overleaf エクスポート zip の**不可変スナップショット**（図版・付随ファイル込み・無加工）。K = zip プレフィクス `NN-K` のリビジョン番号 |

- 複数リビジョン保有: #30（r1, r2）、#51（r1: 図版含む全量／r2: main.tex のみ → main-overleaf.tex は r2 由来）
- **#65–#68 は二本立て規約の例外**（2026-07-25 User 決定）: `main.tex` のみを置き `main-overleaf.tex` は持たない。理由＝この4本では**リポジトリが上流、Overleaf が下流**（User が repo の main.tex を Overleaf へ手動コピペする運用）。従来の #1–#64 は Overleaf が上流だったので原本保存に意味があったが、同じ物を2つ持つと drift の温床にしかならない
- #67 のみ図版を同梱: `67/fig1.tikz` `67/fig2.tikz` `67/fig3.tikz`（素の tikzpicture・pgfplots 不使用）

## 現在の状態（2026-07-26）

**#1–#64**: Zenodo 寄託済み・DOI 確定。`main.tex` は 63 論文全数完備。

**#65–#68**: **Zenodo 未寄託・DOI 未取得**。寄託順 **#65 → #66 → #67 → #68**。

| # | 内容 | 状態 |
|---|---|---|
| **65** | One Internal Oscillator（symplectic 複素構造・Dirac 静止解との等価性・quartic の幾何学的起源） | 前方依存ゼロ＝最初に寄託 |
| **66** | Dual-Model Deliberation Record（spin-2 セクターの二重モデル討議記録） | #63 までを引用 |
| **67** | Binding Energy, Composition, and the Residual β_ZB（等価原理2試験＋再出発宣言） | #65・#66 を引用 |
| **68** | The 0-Sphere Model: A Structural Overview（#1–#67 回顧＋冒頭に再出発宣言） | 最後に寄託＝#67 までカタログ可能 |

**DOI プレースホルダ**: #68 Group 08 に `[pending]` が計7箇所。**寄託時に4件とも差替が必須。**

**コンパイル検証（tectonic・2026-07-26）**: 4本とも PDF 生成 OK・エラー0・未定義参照0・**組版目視確認済み**（#65 202 KB／#66 313 KB／#67 302 KB／#68 357 KB）。

## 恒久的な決定事項

**総説の継承方針**（2026-07-25 User 決定）: 構造総説は改訂のたび**新しい通番と新しい DOI で寄託する**（同一 DOI の version 更新はしない）。理由＝Zenodo を時系列ライブラリとして構築するため。各総説は日付付きスナップショットであり、後続の総説が出た時点で supersede される。**次の総説を書く際は #68 を supersede する旨を明記すること。**

**tex 添付方針**（2026-07-19 User 談）: #1–#12 は viXra 期の PDF 寄託のみだった。現在は (1) 後続研究者が tex を DL して再現できる便宜、(2) PDF スキャンでは LLM が数式・図表を評価しにくく TikZ/LaTeX コードの保存に価値がある、という理由で Zenodo にも main.tex を添付する。未清書分の清書時は Zenodo レコードへの tex 追補もセットで行う。

**前提知識マップ（Sector/Tier 表）は不採用**（2026-07-19 User 決定）。難易度の事前宣言は読者バイアス・門前払いの要因になるため。用語集＝難易度を下げる、マップ＝難易度を宣言する、で前者のみ採用が正。**再提案しないこと。**

**組版**: tectonic のエラー0は「読める」を意味しない。**寄託前に必ず PDF ページを目視すること**（実例: #66 Table II の C3 行が Content 列と Status 列の混線で「maximum kinetic traction of the degener-」と読めていた）。狭い列の語間伸びには `array` パッケージの `>{\raggedright\arraybackslash}p{}` が本来の対処だが、起草規約が無断のパッケージ追加を禁じているため **User 承認待ち**。現状は列幅再配分＋`\tabcolsep` 拡大＋長文短縮で対処済み。

## 残タスクと未収録

- **#65–#68 の寄託と DOI 4件差替**（User 作業）
- **Zenodo tex 未収録は 32 レコード**（#1–15, #17–27, #29, #31–33, #49, #63）＝`ZENODO-TEX-BACKLOG.md` にチェックリスト。全件 upload-ready・品質統一済み。New version 作成＝version DOI 増の方針決定が先。#33 追補時は `fig_thermal.tex` / `fig_TotalHamiltonian.tex` も同梱要
- **`off-series/solar-neutrino-dna-recoils/`**: Overleaf 名「28-1 Solar Neutrino–Induced Nuclear Recoils as a Hypothetical Source of High-LET DNA Damage in Humans」。目録 #28（G/c² 次元整合）とは別物の系列外論文（生物物理）。番号衝突のため未採番のまま退避。採番は User 判断待ち
- **`tomonaga.md`** の扱い判断
