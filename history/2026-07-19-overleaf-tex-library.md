# 作業履歴 2026-07-19 — Overleaf 原本収蔵と tex ライブラリ化

> 対象コミット: `09ed0fb` → `6dbd1b3` → `48bcb41`(3件・main 直コミット)
> 作業者: User (Satoshi Hanamura) + Claude Code (Fable 5)

## 背景と目的

Overleaf に保存されていた全論文プロジェクトを GitHub(`tex-sources/`)へ整理・収蔵し、
論文 tex の「ライブラリ化」を確立した。動機は 2 つ:

1. **後続研究者への便宜** — tex があれば図表・数式込みで再現・検証・引用ができる。
   PDF のみの寄託とは保存物としての性格が変わる。
2. **AI 可読性** — PDF スキャンでは LLM が数式・図表を評価しにくい。
   LaTeX/TikZ コードは数式が一意に読め、図は「幾何の構成手順」として読めるため、
   壁練スキル等で AI が原文を読みに行く本コーパスの運用ではほぼ必須の下部構造。

(#1–#12 は viXra 期に PDF をアップロードしただけで、当時は tex ライブラリ化を
想定していなかった。上記の考えに基づき方針を改めた。)

## 実施内容

### 1. Overleaf 全 67 プロジェクトの一括収蔵(`09ed0fb`)

- ソース: Overleaf 一括エクスポート「Overleaf Projects (67 items)」(zip 67 本)。
- 各論文 #NN に `tex-sources/NN/overleaf/rK/` を新設し、zip の中身を**無加工格納**
  (K = zip プレフィクス `NN-K` のリビジョン)。目録 63 論文 #1–#64(#16 欠番)の原本が全て揃った。
- 複数リビジョン: #30 (r1, r2)、#51 (r1: 図版含む全量 / r2: main.tex のみ)。
- 既存のトップ階層 main.tex(Zenodo 清書版)は一切上書きしていない。

**採番判断(User 指示 + 判定)**:

- 旧 Overleaf 名「99-1 Rethinking Particles as Spacetime Oscillators (Research Summary)」は
  **99 番を廃止し #67 (REV-02)** として保存。中身は 2025-04-13 付・#1–#14 期の研究総括で、
  現行の #65「The 0-Sphere Model: A Structural Overview」(REV-01・未収蔵)への合流ではなく
  歴史的スナップショットとして独立保存が適切と判定。経緯は `tex-sources/67/NOTE.md`。
- 「28-1 Solar Neutrino–Induced Nuclear Recoils …」は目録 #28 と番号衝突する**系列外論文**
  (生物物理)のため、未採番のまま `tex-sources/off-series/solar-neutrino-dna-recoils/` へ退避。
  採番は User 判断待ち。

### 2. main.tex 二本立て規約の確定(`6dbd1b3`)

User の運用(Overleaf 執筆版に日本語コメント → 0sm-zenodo-upload スキル発火で清書版生成)を
そのまま構造に写した:

| ファイル | 役割 |
|---|---|
| `NN/main.tex` | **Zenodo 清書版のみ**。有無がそのまま「清書済みシグナル」 |
| `NN/main-overleaf.tex` | **Overleaf 原本**(日本語コメント込み)。全番号に常設 |
| `NN/overleaf/rK/` | zip スナップショット(図版込み・不可変アーカイブ) |

初回コミットで行った「未清書番号への raw main.tex 昇格コピー」はこの規約と矛盾するため取り消し。

### 3. Zenodo 公開版 main.tex の API 一括取得(`48bcb41`)

- 63 レコードを `zenodo.org/api/records/<id>` で走査 → **31 レコードに main.tex 収録**を確認。
- 全 31 本を `…/files/main.tex/content` からダウンロードし、LaTeX 構造検証のうえ配置:
  - **新規設置**: #46, #51–62, #64(14 本)
  - **更新**: #28(公開版は Revised: 2026-02-13 付。repo 側は改訂前だった)
  - **一致検証**: #30, #34–45, #47, #48, #50(16 本が公開版とバイト一致 =
    repo 清書版が公開版の忠実な写しであることを機械的に裏付け)

### 4. #1–12, #63 のスキル清書(同日追記)

0sm-zenodo-upload スキル Step 1(latex-standards.md)を発火し、Overleaf 原本
(`main-overleaf.tex`)から 13 本の cleaned main.tex を生成・設置:

- 適用規約: 日本語コメント全削除(204 行)+コメントアウト命令削除(62 行)+
  英語バナー(Section/Subsection/Appendix/Bibliography 等)挿入+明示日付+空コメント禁止。
- 個別判断: #1 は Overleaf 内に在った既存 `main_cleanup.tex`(著者清書・date: March 10, 2019)を採用。
  #2 は `\date{\today}` → February 24, 2019(原本コメントに残る著者記録)。
  #11 は `\end{document}` 後に付いていた日本語の文献作業メモを切除。
- 検証: 全 13 本で「コメント除去後のコード実体」が原本と完全一致(機械照合)+
  環境対応・ref/label 整合・日本語ゼロを確認。ローカルに LaTeX toolchain が無いため
  コンパイル検証は未実施(Overleaf での二重コンパイル確認を推奨)。

### 5. コンパイル検証・#67 清書・追補チェックリスト(同日追記)

- **実コンパイル検証**: tectonic (XeTeX) + Ghostscript を導入し、全 14 本
  (#1–12, #63, #67)の PDF 生成に成功。これに伴う互換修正 2 種を本体へ適用:
  hyperref の旧ドライバ指定(dvipdfm×11 / pdftex×1)を除去して自動検出化、
  #6 の caption 廃止指定 `justification=center` → `centering`(いずれも本文非接触)。
  #1/#3/#8 の EPS 図版は tectonic 単体では埋め込めず事前変換で検証
  (Overleaf pdfLaTeX では epstopdf 自動変換で問題ない)。
- **#67 清書**: 同一規約で cleaned main.tex を生成・検証・設置。
  → **全 64 番号(#1–64, #67)に main.tex が揃った**。
- **Zenodo 追補チェックリスト**: tex 未収録レコードは #1–12/#63 だけでなく
  #13–15, #17–27, #29, #31–33, #49 を含む **32 件**と判明。一覧・手順・
  DOI バージョン方針の注意を `tex-sources/ZENODO-TEX-BACKLOG.md` に整備(User 手作業用)。
- 小掃除: `tex-sources/12/[#12]main.tex`(Overleaf 原本と同一の冗長コピー)を削除。

### 6. Zenodo 追補対象の残り 19 本を規約統一(同日追記)

追補対象 32 レコードのうち未検証だった #13–15, #17–27, #29, #31–33, #49 を処理:

- **#13, #14**: 日本語コメント残存・バナー無しだったため Overleaf 原本からフル清書。
- **#26**: 既存 main.tex が **41 行の破損スタブ**(プリアンブル途中で切断・
  `\end{document}` 欠落)と判明 → Overleaf 原本(680 行)からフル清書で復旧。
  今回の点検が無ければ破損ファイルを Zenodo に上げるところだった。
- **#49**: 未清書相当だったためフル清書。
- **残り 15 本**: 既存の英訳コメントを保持したまま規約統一(コメントアウト命令・
  空コメント除去、バナー統一、旧ドライバ指定除去)。
- **全 19 本を tectonic で実コンパイル検証**(#33 は `\input` される
  fig_thermal.tex / fig_TotalHamiltonian.tex 併用で成功 → Zenodo 追補時も同梱要)。
  本文はコメント除去後のコード実体レベルで各ソースと一致検証済み。

### 7. 旧 99-1(一時 #67)の廃棄判定(同日追記)

User の依頼で「Rethinking Particles as Spacetime Oscillators (Research Summary)」
(2025-04-13、#1–#14 期総括)の存続価値をコーパス全体と照合して判定:

- 主要主張 12 項目すべてがコーパスに既出かつ上位互換あり(γ=1+a → #62 が専用論文、
  臨界半径 → #14/#47、ZB 速度 → 24 論文、E₀ 恒等式 → 44 論文、対消滅 → #8、
  シーソー/バスケットボール比喩まで #9/#15 に既出)。固有の科学的内容ゼロ。
- 総括機能は #65 Structural Overview 下書き(全論文目録・9 概念スレッド・依存図・
  ロードマップ収載)が完全上位互換。
- 2025-04 時点の陳腐化記述(RMS/√2 の旧定式化、muon g-2 4.2σ 等)を含む。

→ **廃棄確定**(User 承認)。`tex-sources/67/` を削除し、**#66・#67 は欠番として空き**。
復元は commit `d415dcb` に一式あり。この文書の過去セクションにある「#67」への言及は
廃棄前の経緯として原文のまま残す。

## 結果と現在地

- 清書済み `main.tex`: **63 論文全数(#1–64、#16 欠番)**。うち 32 本
  (#1–15, #17–27, #29, #31–33, #49, #63)は今日コンパイル検証済み。
  **Zenodo 追補対象 32 件はすべて upload-ready で品質統一済み**(`ZENODO-TEX-BACKLOG.md` 参照)。
- 採番状況: #16 永久欠番、#65 = Structural Overview(REV-01・未収蔵)、#66・#67 = 空き。
- 残る User 手作業: (1) Zenodo 32 レコードへの tex 追補(DOI バージョン方針の
  統一決定が先)、(2) #65/#66 の Overleaf エクスポート提供、
  (3) off-series(Solar Neutrino)の採番判断。
- 注記: #13, #14, #41, #48–50 の main.tex は Overleaf 版と実質同一(清書工程未経過の可能性)。
- 規約・対応表の正典: [`tex-sources/OVERLEAF-MANIFEST.md`](../tex-sources/OVERLEAF-MANIFEST.md)
- 宙ぶらりん: #65(Structural Overview REV-01)・#66 は本エクスポート未収録で `tex-sources/65` `66` は未作成。

## 参照

- 収蔵規模: 519 ファイル・約 180MB(`09ed0fb`)
- ローカルクローン: `~/Desktop/0sm-skills`
- 原文精読 URL: `https://raw.githubusercontent.com/HanaTensor/0sm-skills/main/tex-sources/NN/main.tex`
  (404 = 未清書 → `NN/main-overleaf.tex` に原本が必ずある)
