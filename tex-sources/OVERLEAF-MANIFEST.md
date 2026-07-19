# Overleaf Sources Manifest

> Imported: 2026-07-19 | Source: Overleaf 全プロジェクト一括エクスポート「Overleaf Projects (67 items)」

## 配置規約(main.tex 二本立て・2026-07-19 確定)

各論文 #NN のトップ階層には **2 種類の tex を役割固定で置く**:

| ファイル | 役割 |
|---|---|
| `NN/main.tex` | **Zenodo 清書版のみ**(0sm-zenodo-upload スキル発火で生成した納品物。英語コメント化・登録用メモ除去済み)。未清書の番号には置かない — main.tex の有無が「Zenodo 清書済みか否か」のシグナル。 |
| `NN/main-overleaf.tex` | **Overleaf 原本**(日本語コメント込みの執筆版)。全番号に常設。複数リビジョンある場合は最新 rK のコピー。 |
| `NN/overleaf/rK/` | Overleaf エクスポート zip の**不可変スナップショット**(図版・付随ファイル込み・無加工)。K = zip プレフィクス `NN-K` のリビジョン。 |

- 複数リビジョン保有: #30 (r1, r2)、#51 (r1: 図版含む全量 / r2: main.tex のみ → main-overleaf.tex は r2 由来)。
- **Zenodo 自動取得(2026-07-19)**: 各レコードの API(`zenodo.org/api/records/<id>/files/main.tex/content`)から公開版 main.tex を一括取得。#46, #51–62, #64 に新規設置、#28 は改訂公開版(Revised: 2026-02-13)へ更新、#30, #34–45, #47, #48, #50 は既存と完全一致を確認。
- **スキル清書(2026-07-19)**: #1–12, #63 の main.tex を 0sm-zenodo-upload スキル Step 1(latex-standards.md)で Overleaf 原本から生成(日本語コメント全削除・コメントアウト行削除・英語バナー挿入・明示日付。#1 は Overleaf 内の既存 main_cleanup.tex を採用、#2 は \today → February 24, 2019、#11 は \end{document} 後の作業メモ切除)。本文はコメント除去後のコード実体レベルで原本と一致検証済み。**この 13 本は Zenodo レコード側に tex 未収録**(PDF のみ)— レコード追補時は GitHub のこの main.tex をそのまま使える。
- **全 63 論文(#1–64、#16 欠番)に main.tex が揃った**。
- **コンパイル検証(2026-07-19)**: 全 13 本(#1–12, #63)を tectonic (XeTeX) で PDF 生成確認。互換修正 2 種を適用: hyperref 旧ドライバ指定(dvipdfm/pdftex)除去、#6 の caption `justification=center`→`centering`。#1/#3/#8 の EPS 図版は epstopdf 対応エンジン(Overleaf pdfLaTeX 等)が必要。
- **Zenodo レコードへの tex 追補**: 対象 32 レコードの一覧と手順は [`ZENODO-TEX-BACKLOG.md`](ZENODO-TEX-BACKLOG.md)。
- **規約統一(2026-07-19 追記)**: #13–15, #17–27, #29, #31–33, #49 の 19 本も規約統一+コンパイル検証済み(#13/#14/#49 はフル清書、#26 は破損スタブを原本から復旧)。#41, #48, #50 のみ Overleaf 版と実質同一のまま(Zenodo 公開版と一致しているため現状維持が正)。

## 特記事項

- **旧 99-1「Rethinking Particles as Spacetime Oscillators (Research Summary)」は採番せず破棄(2026-07-19)** — コーパスと全面重複のため(User 承認)。**#65 以降(#66, #67 含む)は通常の通番として今後の論文に使用する(欠番にしない)**。#65 = The 0-Sphere Model: A Structural Overview — 2026-07-19 改訂完了・`65/main.tex` 設置済み(#1–#64 対応・DOI 最新化・tectonic コンパイル検証済・**Zenodo 未寄託**)。#66–67 は将来用の空スキャフォールド。
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
