# 0SM 壁練インデックス (wall-practice index)

> Repository: `HanaTensor/0sm-skills` | Last updated: 2026-07-25 (#67 追加・総説を #68 へ移管)
> **用途**: skill `0sm-wall-practice` の起動時 fetch 先。テーマ → 発火チェーン → 必要論文 → 未解決問題 を連鎖特定する。
> DOI 全表は [index.md](index.md)。個票・派生索引は baseline tar（`workspace-baselines/` 最新版）の
> `context/papers/NNN.md`・`context/derived/{origins,keywords,open-questions}.md`。一次資料は `tex-sources/NN/main.tex`。

## §1 テーマ別発火チェーン

太字 = 現到達点。「テーマの議論には到達点 + 直近2〜3本を読む」が基本形。

| テーマ | チェーン | 常時前提 |
|---|---|---|
| 熱力学・E₀恒等式 | #1 → #18 → #22 → #33 → **#46** | #1 |
| スピン・二値性 | #2, #3 → #13, #19 → #26 → #38 → #48 → #50 → **#64** | #1 |
| AMM・γ・橋渡し | #10 → #21 → #47 → #48 → #61 → **#62** | #10 |
| 線積分存在論・Wilson線 | #29, #31 → #40, #41 → #45 → #54 → #55 → #56 → #63 → **#67**（出直しの起点として #29/#30/#31 に回帰） | #31 |
| 重力媒介・spin-2 | #34, #35 → #49 → #52 → #57 → #58 → #59 → #60 → #63 → #66 → **#67** | #24 |
| 計量創発・Synge | #23, #24 → #30 → #51 → #52 → #53 → #60 → **#63** | #24 |
| ゲージ U(1)/SU(2) | #17 → #19 → #26 → #48 → #55 → **#64** | #17 |
| 干渉・決定論 | #4 → #5 → #27 → **#38** | #1 |
| 真空エネルギー・Λ | #32 → #39 → **#46** | #31 |
| 非摂動性・方法論 | #36 → #42 → **#56** | — |
| トーション | #43 → #45 → **#63** | #29 |
| ニュートリノ・安定性（次期テーマ） | **#9** | #1 |

構造単位（三部作・companion 対・系列の正典）は baseline の `context/series-units.md`。

## §2 未解決問題台帳 (open questions)

議論の座標として使う。全量は baseline `context/derived/open-questions.md`（opens/closes の auto 集約）。

| ID | 問題 | 発生源 | 関連チェーン |
|---|---|---|---|
| OQ-1 | 速度レベル比残差: 2^(−1/4) vs 1/√2 のずれの起源 | #62 | AMM・γ |
| OQ-2 | A_μ の実体（ボトルネック: 接続の担い手は何か） | #63 | 線積分・ゲージ |
| OQ-3 | Ω_T（Thomas 渦）の rank-2 性の確立 — **#66 が源側に候補解**（固定カイラリティ＋運動量反転→トレースレス helicity±2、Landau–Yang 整合、質量ありJ=2 で Weinberg–Witten 圏外）。ただし **GR 輻射形式の輸入が代価**。残るのは Berry 曲率↔Riemann（#60 三角形の closure edge / O3）| #63, #66, #67 | 重力媒介・計量創発 |
| OQ-4 | 2経路収束と torsion 残差の整合 | #63 | トーション |
| OQ-5 | 平方根分岐の並行性・Wick 回転橋 | #64 | スピン二値性 |
| OQ-6 | 中性子 13.4 MeV 差の物理解釈（SU(3) ハドロン拡張） | #61–#62 系譜 | AMM・γ |
| OQ-7 | 安定性の起源3難点: 非対称二振動子の束縛／ω₁/ω₂↔a の橋／#9 整合 | #9, #50 | ニュートリノ・安定性 |
| OQ-8 | 検証予言の実験接続: ~~地平面凍結~~／Δν/ν≈5.29×10⁻¹⁰／ZB≈0.04c／可視性限界 ⟨V⟩=√2−1。**地平面凍結は #67 で撤回**（局所読みは LPI 係数2を要求 → Lange et al. 2021 の k_α=14(11)×10⁻⁹ で 10⁸ 倍排除。遠方観測者の記述としてのみ残り、GR と区別不能）| #22, #38, #59, #67 | 複数 |
| OQ-9 | **重力荷の種盲目性**: 重力荷は全エネルギーのみで、内部速度を含んではならない。#52 の残余 β_ZB は種依存（レプトン 0.0405 / 核子 0.898）で η(Ti,Pt)=3.13×10⁻⁵ を予言し 1.2×10¹⁰ 倍で排除される。#52 の完了機構は β_ZB を**消さ**ねばならない（必要因子はレプトン 24.7・核子 1.11 で定数ではありえない）。試験は η=0 が恒等式であること | #52, #61, #67 | 重力媒介 |
| OQ-10 | **ε₂ε₃ は 1/β_ZB を担えるか**: OQ-9 が要求する因子の住処の候補。ただし一次通過では逆向き（#49 の放出は Thomas 応力 ∝ β_ZB² が床を飽和して起きるため核子は放出が増える）。逃げ道は ε₂ε₃ が #34 の吸収側に属する場合。#34・#49 の精読のみで決着する**次の一手** | #34, #49, #67 | 重力媒介 |

## §3 トリガー語彙表

壁練依頼の語彙 → 入るべきチェーン。

| 語彙（例） | チェーン |
|---|---|
| 線積分, Wilson line/loop, holonomy, AB効果, Berry位相, 接続, connection | 線積分存在論・Wilson線 |
| 重力, spin-2, メディエータ, photon-sphere fragmentation, 四重極放射 | 重力媒介・spin-2 |
| 等価原理, WEP, Eötvös, MICROSCOPE, 組成依存, 束縛エネルギー, 重力荷, β_ZB, 種依存 | 重力媒介・spin-2（到達点 #67）|
| 局所位置不変性, LPI, k_α, 年周変調, 地平面凍結 | 重力媒介・spin-2（#67 で決着）|
| 計量, metric, Synge world function, helical, 固定端点 | 計量創発・Synge |
| スピン, 二値性, 4π/720°, SU(2), S³, Laplacian 平方根 | スピン・二値性 |
| AMM, g−2, γ方程式, bridge equation, 陽子 336 MeV, RMS | AMM・γ・橋渡し |
| E₀, 恒等式, 熱ポテンシャル, cos⁴/sin⁴, 零点エネルギー, 1/2因子 | 熱力学・E₀恒等式 |
| U(1), ゲージ, clock synchronization, fiber bundle, dual-frame | ゲージ U(1)/SU(2) |
| 二重スリット, 可視性, 干渉, 決定論, 不確定性 | 干渉・決定論 |
| 真空エネルギー, Λ, 宇宙定数 | 真空エネルギー・Λ |
| 非摂動, 微細構造定数 α, モノポール | 非摂動性・方法論 |
| torsion, teleparallel, semigroup, open-path | トーション |
| ニュートリノ, 振動, 安定性, 束縛 | ニュートリノ・安定性 |

キーワード → 論文番号の網羅逆引き（topic 統制語彙・タグ167・スレッド26・タイトル語302）は baseline `context/derived/keywords.md`。

## §4 起点参照（「この考察はどこで生まれたか」）

- **論文別の初出考察 + 下流伝播**: baseline `context/derived/origins.md`（例: 線積分三部作なら #29/#30/#31 の各セクションに、初出 articulation 名と continued/supplemented/required by の逆引きが揃う）
- **時系列の初出全量**: `derived/first-occurrences.md`（概念）/ `analogies.md`（類比）/ `equations.md`（方程式）
- **構造的転回（reframe/inversion 等）**: `derived/conceptual-moves.md`（手動 curate・Move 1–8）

## §5 セッション出口（skill `0sm-wall-practice` §4 と同一）

1. 論文化へ → `0sm-corpus-curate` → `latex-paper-drafting`/`revtex-aps-format` → `0sm-zenodo-upload`
2. 継続へ → `HANDOFF-wall-practice-YYYY-MM-DD.md` 次版出力
3. 本インデックスへの還流 → 新チェーン・新語彙・新 OQ の追記差分を提示（push は User）
