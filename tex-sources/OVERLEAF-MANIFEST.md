# Overleaf Sources Manifest

> Imported: 2026-07-19 | Source: Overleaf 全プロジェクト一括エクスポート「Overleaf Projects (67 items)」

## 配置規約(main.tex 二本立て・2026-07-19 確定)

各論文 #NN のトップ階層には **2 種類の tex を役割固定で置く**:

| ファイル | 役割 |
|---|---|
| `NN/main.tex` | **Zenodo 清書版のみ**(0sm-zenodo-upload スキル発火で生成した納品物。英語コメント化・登録用メモ除去済み)。未清書の番号には置かない — main.tex の有無が「Zenodo 清書済みか否か」のシグナル。 |
| `NN/main-overleaf.tex` | **Overleaf 原本**(日本語コメント込みの執筆版)。#1–#64 に常設。複数リビジョンある場合は最新 rK のコピー。**#65–#68 には置かない**(下記例外を参照)。 |
| `NN/overleaf/rK/` | Overleaf エクスポート zip の**不可変スナップショット**(図版・付随ファイル込み・無加工)。K = zip プレフィクス `NN-K` のリビジョン。 |

- 複数リビジョン保有: #30 (r1, r2)、#51 (r1: 図版含む全量 / r2: main.tex のみ → main-overleaf.tex は r2 由来)。
- **#65–#68 は二本立て規約の例外(2026-07-25 User 決定)**: `main.tex` のみを置き、`main-overleaf.tex` は持たない。理由 = この4本では**リポジトリが上流、Overleaf が下流**になったため(User が repo の main.tex を Overleaf へ手動コピペする運用)。従来の #1–#64 は Overleaf が上流だったので原本保存に意味があったが、#65–#67 で同じ物を2つ持つと drift の温床にしかならない。削除内訳: `66/main-overleaf.tex` は 07-19 改訂**前**の旧版だった(コード実体 542 行 vs main.tex 830 行、`\date` に archival revision 表記なし、本文が「outside the numbered corpus」= 採番矛盾の解消前、Appendix B–E 約 288 行と TikZ 重なり修正 693964c が欠落)。`67/main-overleaf.tex` は main.tex と完全一致のため冗長。いずれも git 履歴に残るので復元可能。
- **Zenodo 自動取得(2026-07-19)**: 各レコードの API(`zenodo.org/api/records/<id>/files/main.tex/content`)から公開版 main.tex を一括取得。#46, #51–62, #64 に新規設置、#28 は改訂公開版(Revised: 2026-02-13)へ更新、#30, #34–45, #47, #48, #50 は既存と完全一致を確認。
- **スキル清書(2026-07-19)**: #1–12, #63 の main.tex を 0sm-zenodo-upload スキル Step 1(latex-standards.md)で Overleaf 原本から生成(日本語コメント全削除・コメントアウト行削除・英語バナー挿入・明示日付。#1 は Overleaf 内の既存 main_cleanup.tex を採用、#2 は \today → February 24, 2019、#11 は \end{document} 後の作業メモ切除)。本文はコメント除去後のコード実体レベルで原本と一致検証済み。**この 13 本は Zenodo レコード側に tex 未収録**(PDF のみ)— レコード追補時は GitHub のこの main.tex をそのまま使える。
- **全 63 論文(#1–64、#16 欠番)に main.tex が揃った**。
- **コンパイル検証(2026-07-19)**: 全 13 本(#1–12, #63)を tectonic (XeTeX) で PDF 生成確認。互換修正 2 種を適用: hyperref 旧ドライバ指定(dvipdfm/pdftex)除去、#6 の caption `justification=center`→`centering`。#1/#3/#8 の EPS 図版は epstopdf 対応エンジン(Overleaf pdfLaTeX 等)が必要。
- **Zenodo レコードへの tex 追補**: 対象 32 レコードの一覧と手順は [`ZENODO-TEX-BACKLOG.md`](ZENODO-TEX-BACKLOG.md)。
- **規約統一(2026-07-19 追記)**: #13–15, #17–27, #29, #31–33, #49 の 19 本も規約統一+コンパイル検証済み(#13/#14/#49 はフル清書、#26 は破損スタブを原本から復旧)。#41, #48, #50 のみ Overleaf 版と実質同一のまま(Zenodo 公開版と一致しているため現状維持が正)。

## 特記事項

- **旧 99-1「Rethinking Particles as Spacetime Oscillators (Research Summary)」は採番せず破棄(2026-07-19)** — コーパスと全面重複のため(User 承認)。**#65 以降(#66–#68 含む)は通常の通番として今後の論文に使用する(欠番にしない)**。**通番を 2026-07-25 に再割当**(いずれも未寄託のため履歴不要・User 承認)。旧割当 #65=総説 / #66=討論記録 / #67=quartic を、まず **#65=quartic / #66=討論記録 / #67=総説** に変更し、同日さらに **#67=等価原理2試験 / #68=総説** へ移管(理由: #67 が #65・#66 を引用して成立するため後方参照とし、総説はバッチ最後に置いて #67 をカタログできるようにする=総説自身の設計意図どおり)。理由:(1) 総説が quartic 論文に実質依存するため、総説を最後に置けば全参照が後方参照になる;(2) 総説が #65・#66 を「in preparation」ではなく正規カタログ行として収録できる;(3) quartic は唯一の一次研究で前方参照ゼロ。**旧マニフェスト記述「#66 が #65 を参照するため」は誤り** — #66 の参考文献は #63 までで総説を引いていない(本文2箇所の番号参照のみ、#67 に更新済み)。
  - **#65 = One Internal Oscillator**(symplectic 複素構造・Dirac 静止解との等価性・quartic の幾何学的起源)— `65/main.tex`(旧 67/)。Prop.1: 輻射勾配関係+振動子運動エネルギー+保存則から $E_{A,B}=\frac14E_0(1\pm s_z)^2$ を一意導出、Stefan–Boltzmann 仮定不要。**Zenodo 未寄託**・寄託順 1 番目(前方依存ゼロ)。
  - **#66 = Dual-Model Deliberation Record**(Opus 4.8 × Fable 5)— `66/main.tex` 据置。総説への番号参照を #65→#67 に更新。**Zenodo 未寄託**・寄託順 2 番目。
  - **#67 = Binding Energy, Composition, and the Residual β_ZB**(等価原理2試験＋定式化の出直し宣言)— `67/main.tex` 新規。#52 の λ_C 相殺が届かなかった**束縛**と**組成**を検証: 束縛は合格(F=(E/c²)g·β_ZB、Ω_T=(v_ZB³/4ħc³)E ともに E に厳密線形=束縛エネルギー欠損を自動で担う)、**組成は不合格**(#61 の v_ZB^p≈0.898c により β_ZB が種依存 → η(Ti,Pt)=3.13×10⁻⁵ vs MICROSCOPE 2.7×10⁻¹⁵ = **1.2×10¹⁰ 倍で排除**)。E に非線形な読みは核束縛てこで 3.2×10¹¹ 倍排除。#62 と #63 の両立不能も決着(局所読みは LPI 係数2を要求、Lange et al. 2021 の k_α=14(11)×10⁻⁹ により **10⁸ 倍で排除** → **地平面凍結は遠方観測者の記述に降格＝GR との乖離点ではなくなる**)。診断=4症状は1つの不整合(内部運動学に重力荷を担わせる取り違え)。**線積分シリーズ #29/#30/#31 からの定式化再出発を宣言**、受け入れ条件4件。Dirac 側の副産物: ⟨β⟩=E/mc²(Hellmann–Feynman、Adkins 2008 で既知・先取権主張せず)→ 負エネルギー混入率 = B/2mc²。図3点は TikZ(`67/fig1–3.tikz`、pgfplots 不使用)。**Zenodo 未寄託**・寄託順 3 番目。
  - **#68 = The 0-Sphere Model: A Structural Overview** — `68/main.tex`(旧 67/、さらに旧 65/)。2026-07-25 Opus 5 改訂:§2.1 新設(quartic の二重被覆導出・SB を dual re-description に降格)、#61 の「disjoint empirical inputs」主張を撤回($1+a_p\equiv\mu_p/\mu_N$ より 336 MeV 一致は代数的恒等式)、γ/γ_v 二役を本文昇格、Synge 混合符号・次元・O18 署名問題・O19 先取り連続体・O20 輻射勾配関係を追加(全20課題)、#1–#67 対応に拡張、Group 08 新設。2026-07-25 追加改訂: #67 を収録(採番 detailbox・Group 08・Waves 節新設・Thread 5 延長・O21/O22 追加=全22課題)、**地平面凍結を「3つの実証的接点」から除去**(4箇所訂正: §3.5 内部時計・§8 capstone・O16・§15 まとめ)。**2026-07-25 再構成(User 決定)**: 冒頭に **Part 0「Where the Programme Stands」＋第1節『Conclusion and Outlook: A Restart Declaration』(6小節)** を新設し、genre を「現在地図」から**「再出発宣言＋#1–#67 の回顧リファレンス」**へ変更。副題を A Reader's Map → **A Retrospective ... and a Restart Declaration** に。宣言の骨子=(1) 媒介子構成ルートを**重力荷の定義としては**放棄(物理的描像としては保持)、(2) ε₂ε₃ 探索を打ち切り(レートで強さは直せない)、(3) 方法の絞り込み=**光子球内部の連続体＋線積分 → 二点幾何(Synge/van Vleck–Morette/Bonnet–Myers) → Einstein 方程式を整合条件として回復**、(4) **構築入力は全てコーパス内に所在特定済み**(表: #33 連続体／#51 well-defined 性＋光学計量恒等式／#57 a_ℓm／#24 T^(thermal) の組立指示・二度繰延／#30 場方程式の読み)、(5) 受け入れ条件4件(#67 由来、(i)(ii) は T^(thermal) が構成上満たす)、(6) 順序 N1–N4。**開放課題表(22件)は生きた台帳としてクローズ**し回顧記録化: 三分類(narrowed programme へ継承 10件／媒介子ルートと共に失効 5件／絞り込みの影響外 7件)＋**O19 の訂正**(#33+#51 により連続族の存在と 𝒮 の well-defined 性は既に解決、残るのは有限分離展開=N2)。新フロンティアは N1–N4。LLM 読者向け注記に「台帳はクローズ済み・地平面凍結は撤回済み」を追記。**Zenodo 未寄託**・寄託順 4 番目。
  - **DOI 未確定**: #65–#68 の DOI は Group 08 で `[pending]` プレースホルダ。**寄託時に4件とも差し替えが必須**。
  - **総説の継承方針(2026-07-25 User 決定)**: 構造総説は改訂のたびに**新しい通番と新しい DOI で寄託する**(同一 DOI の version 更新はしない)。理由 = Zenodo を時系列ライブラリとして構築するため。→ 各総説は日付付きスナップショットであり、後続の総説が出た時点で supersede される。この方針は #67 本文(採番 detailbox と §14.1 LLM 読者向け注記)にも明記済み=読者が「この地図は最新か」を判断できるようにするため。次の総説を書く際は #68 を supersede する旨を明記すること(#67 は未寄託のまま #68 へスロット移動したため、supersede 関係は発生していない)。
  - **#14/#17 訂正ログを全面化(2026-07-25)**: 誤りの正体を逆算により特定 = **質量を kg のまま挿入し、幾何学化質量 GM/c² を使わなかった**(G/c² = 7.4256×10⁻²⁸ m/kg の脱落)。再現: R_crit = 3M/β²(kg) → μ: 3.431×10⁻²⁵ m(#14 記載 3.43e-25)、τ: 5.715×10⁻²⁴ m(同 5.71e-24)。正: R_crit = 3GM/(c²β²) → 2.548×10⁻⁵² m(#28 記載 2.55e-52)。比 = c²/G = 1.347×10²⁷ = **27桁**。速度: β² → β² − 3m_e/R_crit = 0.00163002 → **0.040373c**(#14 記載 0.040374c、SR 値 0.040472c からの「精密化」)。正しい補正は 3Gm_e/(c²R) = 5.9×10⁻³³ で速度不変。**訂正後の半径に逃げ道なし** — 2.55×10⁻⁵² m は Planck 長の 10⁻¹⁷、模型自身の核間隔 λ_C/2 の 10⁻⁴⁰。#14 のレプトン崩壊の説明も臨界半径と共に失効。反映先 = #68 訂正ログ(#14 行を全面化・#17 行は継承元を指すのみに短縮)・Scope Boundaries・LLM 注記・index.md。**正準値は #10 の 0.04047c**。
  - **#1–#67 全数スキャン(2026-07-25)**: 撤回済み数値の伝播範囲を確定 = 速度 0.040374c は **8本**(#14/#15/#17/#20/#22/#23/#27/#37、#15 は要旨レベル)、臨界半径は **7本**(#14/#17/#20/#22/#23/#27/#37)、レプトン崩壊・世代の説明は **7本**(#14/#15/#20/#21/#23/#27/#37)。**過剰撤回への注意も記録**: #22 の重力変調予言 Δν/ν ≈ 5.29×10⁻¹⁰ は (dτ/dt)_地表 = 1−6.96e−10 と (dτ/dt)_衛星 = 1−1.67e−10 の**比**であり、内部速度の値が相殺するため**影響なし**(独立検算で一致)。撤回は #22 の引用ベースライン速度のみ。副次: ZB 速度の km/s 表記が論文間で不統一(12,133 #10/#11 正準 ／ 12,142 #15 = c≈3e5 の丸め ／ 12,108 #27 ／ 12,100 #36/#43)。
  - **N1 の前進(同スキャン)**: #24 §5.1 が既に ρ=Σa_ℓm Y_ℓm の展開と **ℓ=1 モーメント**(重心 r⃗_center = E⁻¹∫ρ r⃗ dΩ → 熱測地線)を持つ。**N1 = このモーメント階層を ℓ=1 から ℓ=2 へ延ばすこと**と再定義(#68 の N1 記述に反映)。ℓ=2 が四重極源であり、#57/#58 の spin-2 仕事と反対側から合流する。
  - コンパイル検証(tectonic・2026-07-25): #65 / #66 / #67 / #68 とも PDF 生成 OK・未定義参照 0・エラー 0(#67 = 305 KB、#68 = 346 KB[全数スキャン反映後])。
- **off-series/solar-neutrino-dna-recoils/** — Overleaf 名「28-1 Solar Neutrino–Induced Nuclear Recoils as a Hypothetical Source of High-LET DNA Damage in Humans」。目録 #28(G/c² 次元整合)とは別物の系列外論文(生物物理)。番号衝突のため未採番のまま退避。採番は User 判断待ち。
- 目録(index.md)の 63 論文 #1–#64(#16 欠番)は全て Overleaf 原本が揃った。

## 対応表(Overleaf プロジェクト → 配置先)

| zip | Overleaf プロジェクト名 | 配置先 |
|---|---|---|
| 1-4 | A Model of an Eletron Including Two Perfect Black Bodies (v4) | `1/overleaf/r4/` |
| 2-4 | A New Representation of Spin Angular Momentum (v4) | `2/overleaf/r4/` |
| 3-1 | Distinguishing of an electron's spin uniquely from two quantum states with Riemann surface guidance (v2) | `3/overleaf/r1/` |
| 4-2 | Perfect Contrast cannot be obtained in the Electron Double-Slit Experiment | `4/overleaf/r2/` |
| 5-1 | Transition Theory of An ElectronTraveling from Uncertain to Causal Basis (v1) | `5/overleaf/r1/` |
| 6-3 | Correspondence between 0-Sphere and the Electron Model | `6/overleaf/r3/` |
| 7-2 | Coexistence positive and negative-energy states in the Dirac equation with one electron | `7/overleaf/r2/` |
| 8-2 | Consideration of electron-positron pair annihilation by thermal oscillations and an inelastic collision | `8/overleaf/r2/` |
| 9-1 | Beyond the Standard Model: Neutrino Oscillations and the Search for New Physics | `9/overleaf/r1/` |
| 10-3 | Redefining Electron Spin and Anomalous Magnetic Moment Through Harmonic Oscillation and Lorentz Contraction | `10/overleaf/r3/` |
| 11-1 | Quantum Oscillations in the 0-Sphere Model: Bridging Zitterbewegung, Geodesic Paths, and Proper Time Through Radiative Energy Transfer | `11/overleaf/r1/` |
| 12-1 | Radiation-Mediated Quantum Tunneling: A Zitterbewegung Perspective | `12/overleaf/r1/` |
| 13-1 | Unified Spin Dynamics: From Pseudovector Nature to Relativistic Constraints | `13/overleaf/r1/` |
| 14-1 | Bridging Quantum Mechanics and General Relativity: A First-Principles Approach | `14/overleaf/r1/` |
| 15-1 | Spin-Induced Inertial Resistance in Electrons: A Gyroscopic Interpretation Based on General Relativity | `15/overleaf/r1/` |
| 17-1 | From Clock Synchronization to Electromagnetism: A Realist Construction of U(1) Gauge Theory | `17/overleaf/r1/` |
| 18-1 | Time-Dependent Mass in the 0-Sphere Model:  A Hamiltonian Approach to Thermal Modulation | `18/overleaf/r1/` |
| 19-1 | Spin as a Real Vector from Internal Photon-Sphere Motion: Geometric Origin of U(1) Gauge and SU(2) Periodicity | `19/overleaf/r1/` |
| 20-1 | Emergent Conservation Laws from Internal Geometry: A Noetherian Reinterpretation in the 0-Sphere Model | `20/overleaf/r1/` |
| 21-1 | Anomalous Magnetic Moments Without Fields: A Geometric and Observer-Dependent Interpretation | `21/overleaf/r1/` |
| 22-1 | Gravitational Redshift of Internal Quantum Clocks: A Zitterbewegung-Based Model | `22/overleaf/r1/` |
| 23-1 | From Zero-Sphere to Emergent Spacetime: A Minimalist Background-Independent Framework for Temporal and Spatial Genesis | `23/overleaf/r1/` |
| 24-1 | Thermal Geodesics in the 0-Sphere Model: Extending General Relativity through Internal Thermodynamic Structure | `24/overleaf/r1/` |
| 25-1 | A Noetherian Inversion: From Einsteinian Geometry to Emergent Symmetry | `25/overleaf/r1/` |
| 26-1 | Spin from Geometry: Emergence of Spin via Internal Berry Phase in the 0-Sphere Electron Model | `26/overleaf/r1/` |
| 27-2 | Challenging the Uncertainty Principle: A Deterministic Interpretation of Measurement and Reality in Quantum Mechanics | `27/overleaf/r2/` |
| 28-1 | A Supplementary Correction to the 0-Sphere Model: Dimensional Consistency of G and c² | `28/overleaf/r1/` |
| 28-1 | Solar Neutrino--Induced Nuclear Recoils as a Hypothetical Source of High-LET DNA Damage in Humans | `off-series/solar-neutrino-dna-recoils/` |
| 29-1 | Geometric Structure of Spinorial Phase Accumulation along Thermal Geodesics | `29/overleaf/r1/` |
| 30-1 | From Curvature to Connection: Revisiting the Geometric Origin of Conservation Laws | `30/overleaf/r1/` |
| 30-2 | From Curvature to Connection: Revisiting the Geometric Origin of Conservation Laws | `30/overleaf/r2/` |
| 31-1 | Line Integrals as Fundamental Observables in Physics: A Unified Principle Behind the Aharonov–Bohm Effect, Berry Phase, and Wilson Loops | `31/overleaf/r1/` |
| 32-1 | Dissolution of the Vacuum Energy Problem in an Integral-Based Ontology: The 0-Sphere Model Perspective | `32/overleaf/r1/` |
| 33-1 | Geometrical Confinement of Energy in the 0-Sphere Model: A Topological Mechanism Underlying Rest Mass and Zitterbewegung | `33/overleaf/r1/` |
| 34-1 | 34-1　Geometrical Confinement of Energy in the 0-Sphere Model: A Topological Mechanism Underlying Rest Mass, Zitterbewegung, and Gravitational-Like | `34/overleaf/r1/` |
| 35-1 | Detailed Exposition of the 0-Sphere Model Framework for Gravitational-Like Phenomena | `35/overleaf/r1/` |
| 36-1 | On the Non-Perturbative Nature of the 0-Sphere Model and the Fine-Structure Constant: A Supplement on Non-Perturbative Features | `36/overleaf/r1/` |
| 37-1 | Reinterpreting Gravitational Potential Energy as an Internal Line-Integral Quantity in the 0-Sphere Model | `37/overleaf/r1/` |
| 38-1 | Electron Interference from Internal Geometry:  Two-Kernel SU(2) Structure, Quartic Energy Flow, and an Intrinsic Visibility Limit | `38/overleaf/r1/` |
| 39-1 | On Vacuum Energy, Integral Ontology, and the Cosmological Constant Supplementary Note on the Logical Status of Λ in the 0-Sphere Model | `39/overleaf/r1/` |
| 40-1 | On the Derivative-Order Mismatch Between Gauge Theory and Gravity: A Supplement on Curvature, Connection, and Physical Correspondence | `40/overleaf/r1/` |
| 41-1 | A Note on Derivative Hierarchy in Gauge Theory and Gravity: A Historical Supplement on Connection, Curvature, and Line-Integral Observables | `41/overleaf/r1/` |
| 42-1 | On the Non-Perturbative Nature of the 0-Sphere Model and Magnetic Monopole Absence: A Supplement on Conceptual Analysis | `42/overleaf/r1/` |
| 43-1 | On Observer-Dependent Torsion, Zitterbewegung, and Phase Accumulation: A Supplement on SU(2) Teleparallel Geometry and Conceptual Implications | `43/overleaf/r1/` |
| 44-1 | On Internal Energy Stabilization, Charge Localization, and Superradiant Rephasing | `44/overleaf/r1/` |
| 45-1 | Open-Path Spinorial Transport in the 0-Sphere Model and the Status of Torsion: Holonomy Sufficiency and the Possibility of Emergent Semigroup | `45/overleaf/r1/` |
| 46-1 | Geometric Origin of the One-Half Factor: Thermal Potential Energy Floor and the Zero-Point Energy in the 0-Sphere Model (CF Note) | `46/overleaf/r1/` |
| 47-1 | Rotational Lorentz Contraction as the Geometric Origin of the Anomalous Magnetic Moment: A Structural Correspondence with the Muon Lifetime Probl | `47/overleaf/r1/` |
| 48-1 | Geometric Origin of g = 2 in the 0-Sphere Model: U(1) Fiber Bundle and Dual-Frame Phase Decomposition | `48/overleaf/r1/` |
| 49-1 | Photon-Sphere Fragmentation as a Gravitational Mediator: Radiation-Gradient Ejection in the π-Cycle of the 0-Sphere Model | `49/overleaf/r1/` |
| 50-1 | Rotation from Scalar Oscillation: Emergence of Photon-Sphere Angular Momentum from Phase-Staggered Kernel Dynamics in the 0-Sphere Model | `50/overleaf/r1/` |
| 51-1 | Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of the Spacetime Metric in the 0-Sphere Model | `51/overleaf/r1/` |
| 51-2 | Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of the Spacetime Metric in the 0-Sphere Model | `51/overleaf/r2/` |
| 52-1 | Directional Decomposition of Force Types in the 0-Sphere Helical Geometry: Gravity, Electromagnetism, and Spin as Three Projections of a Single | `52/overleaf/r1/` |
| 53-1 | From Gravitational Mediation to the Emergence of Spacetime: A Conceptual and Mathematical Supplement to Papers #49, #50, and #51 | `53/overleaf/r1/` |
| 54-1 | Maxwell Electrodynamics as a Derived Low-Energy Limit of the 0-Sphere Line-Integral Ontology | `54/overleaf/r1/` |
| 55-1 | Four Functions of the Open Wilson Line in the 0-Sphere Model: Phase-History Carrier, Gauge Localization, Holonomy Composition, and Boundary Data | `55/overleaf/r1/` |
| 56-1 | The Framework Boundary: How Local-Field and Directed-Path Descriptions Diverge in the 0-Sphere Model —with Application to Microscopic Time Revers | `56/overleaf/r1/` |
| 57-1 | Spherical Harmonic Imprinting and the Physical Identity of Phase Information: Microscopic Mechanism of Gravitational Coupling in the 0-Sphere Mod | `57/overleaf/r1/` |
| 58-1 | Spin-2 Structure of the Gravitational Mediator: Phase-Stable Pair Emission and Quadrupole Radiation in the 0-Sphere Model | `58/overleaf/r1/` |
| 59-1 | Proton-Trapped Electron as the Generator of Spin-2 Gravitational Radiation: Coulomb Confinement, ZB Axis Locking, and the Separation of Gravitati | `59/overleaf/r1/` |
| 60-1 | The Berry–Synge–Bonnet–Myers Triangle: Structural Conditions for the Unification of Gauge and Gravitational Sectors in the 0-Sphere Model | `60/overleaf/r1/` |
| 61-1 | Application of the γ-Equation to the Proton: A Parameter-Free Hadronic Mass Scale | `61/overleaf/r1/` |
| 62-1 | The Bridge Equation γ = 1 + a from First Principles: Representation Duality of the Anomalous Moment and the Geometric Origin of the Root-Mean-Squ | `62/overleaf/r1/` |
| 63-1 | From Line Integral to Covariant Derivative: A Reader’s Map of the Bridge from the 0-Sphere Model to Riemannian Curvature | `63/overleaf/r1/` |
| 64-1 | The Square Root of the Hyperspherical Laplacian: A Geometric Foundation for Spin Two-Valuedness on S³ in the 0-Sphere Model | `64/overleaf/r1/` |
| 99-1 | Rethinking Particles as Spacetime Oscillators: (Research Summary) | 破棄(未採番) |
