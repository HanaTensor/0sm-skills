# 0-Sphere Model Concept Index: Group 05 (#41–#47, Feb–Mar 2026)

**Coverage:** Papers #41–#47 (February–March 2026)
**Parent Index:** index.md · global-concept.md
**Preceded by:** 04/concept.md (#31–#40)
**Theme:** Structural Clarifications, Torsion, Stability, Lorentz Contraction

---

## New Analogies (Group 05)

| Analogy | Paper | Keyword |
|---------|-------|---------|
| **ミュオン寿命↔電子AMM** | #47 | ΔL=\|γ_L−1\|×L₀で統一。ミュオン: v≈c, γ≈29。電子: v_ZB≈0.04c, γ_L−1=a_e≈10⁻³ |
| **Weitzenböck接続 (SU(2))** | #43 | R=0かつT≠0の数学的実例。ねじれ「あり」かつ曲率「なし」のコントロールされた証明 |
| **4レベル概念階層** | #44 | 接続+固有時→線積分→創発EM→曲率（#31由来を#44が明示） |

---

## New Equations (Group 05)

### G05-1. Kernel Energy Floor（基礎恒等式の新帰結）

| 方程式 | 初出 | 用途 |
|--------|------|------|
| `cos⁴θ + sin⁴θ ≥ 1/2 = E₀/2`  (for all θ) | **#46** | AM-GMによる熱PEの幾何学的下限。ゼロ点エネルギー対応 |
| 等号: θ = π/4 + nπ/2 のとき | #46 | 光子球KEが最大 (E₀/2) になるタイミングと一致 |
| power 2n → floor = 2^(1−n) × E₀ | #46 | n=2 のみが 1/2 を与える（Stefan-Boltzmann固有性） |
| `E₀ ≈ 20.7 keV` | **#46** | ℏω = E₀識別からの数値予測 |

### G05-2. Muon-AMM 統一方程式

| 方程式 | 初出 | 用途 |
|--------|------|------|
| `ΔL = \|γ_L − 1\| × L₀` | **#47** | ミュオン寿命と電子AMMの統一恒等式 |
| `L/L₀ = 1/γ_L ≈ 1/(1+a_e)` | **#47** | 回転Lorentz収縮による弧長短縮 |
| `√(1−v_ZB²/c²) = 1/(1+a_e^exp/√2)` | **#47** | RMS補正付き逆算 |
| `v_ZB² / c² = 0.001638 → v_ZB ≈ 0.04047c` | #47 | (#10の結果を明示的に再導出) |

### G05-3. Torsion関係

| 方程式 | 初出 | 用途 |
|--------|------|------|
| `R^(W) = 0,  T(e_a,e_b) = −ε_abc e_c ≠ 0` | **#43** | Weitzenböck接続 on SU(2) |
| `K_int(A,B) = exp(iω₀L_int/v_ZB)` | **#45** | 内部伝播核。K(B,A)=K(A,B)⁻¹（群可逆） |

### G05-4. Thomas歳差（#47で明示的再構成）

```
v_γ*(t) = v₀ cos(ωt)
Ω(t) = −(v₀²ω / 4c²) sin(2ωt)     ← double-angle構造 → g=2の幾何学的起源
```

---

## New Concept Threads (Group 05)

### G05-T1. ねじれ・幾何構造スレッド

```
#43: Weitzenböck SU(2) (R=0, T≠0) の数学的実例
      開放的経路vs閉ループの系統的比較（初出）
      v_ZB≈0.04047c vs Dirac ±c（初めての明示的比較）
  ↓
#45: 4π周期性はねじれを強制しない（SU(2)正則群で十分）
     有向弧長L_spin(A,B)の未解決問題を定式化
     位相Δφ(A,B) = 内部ゲージ接続と同定
```

### G05-T2. AMM構造的起源スレッド（#10からの到達点）

```
#10: 逆算 a_e → v_ZB ≈ 0.04c （初出）
  ↓
#35: 自転車ホイール類比（AMM as Lorentz収縮）
  ↓
#36: v_ZB^RMS vs peak 区別
  ↓
#47: ΔL=|γ_L−1|×L₀でミュオン寿命と統一（明示的補足）
     順方向鎖 Thomas → v_ZB → a_e は未解決
```

### G05-T3. ゼロ点エネルギー二部構成スレッド

```
#32: QFT真空エネルギーの巨大さを「カテゴリーエラー」として溶解（負の結果）
  ↓
#46: 残存する1/2ℏωの幾何学的起源（正の結果）
     AM-GM: cos⁴θ+sin⁴θ ≥ E₀/2 → 幾何学的下限
```

---

## Extensions of Existing Threads

### C-1 スピン理論スレッドへの追加

```
…→ #38 (g=2位相的不変量) → #47 (g=2幾何学的起源をdouble-angle Thomas歳差から明示化)
```

### C-3 線積分存在論スレッドへの追加

```
…→ #40 (微分次数ミスマッチ)
   → #41 (歴史的補足: 欠落していた観測層の明示)
   → #43 (開放的経路vs閉ループ最初の系統的比較)
   → #45 (ホロノミー十分性: 内部ゲージ接続への帰着)
```

### C-6 真空エネルギー・宇宙定数スレッドへの追加

```
#32 (カテゴリーエラー) → #39 (Λ_obsは別問題) → #46 (残存1/2ℏωの幾何的起源)
```

---

## New First Occurrences (Group 05)

| 概念・量 | 初出 |
|---------|------|
| 磁気単極不在の構造的説明（エネルギー恒等式非対称性から） | **#42** |
| 電荷=単極量（単項）/ 磁化=双極量（対項）の識別 | **#42** |
| 開放的経路vs閉ループの系統的比較（最初の明示） | **#43** |
| Dirac v_ZB=±c vs 0-Sphere v_ZB≈0.04047c の明示的対比 | **#43** |
| Weitzenböck接続 SU(2) as torsion proof-of-concept | **#43** |
| K_int(A,B) = exp(iω₀L_int/v_ZB) 内部伝播核 | **#45** |
| 有向弧長L_spinの未解決問題を定式化 | **#45** |
| cos⁴θ+sin⁴θ ≥ E₀/2（kernel energy floor） | **#46** |
| 1/2ℏωの幾何学的起源（AM-GM from energy identity） | **#46** |
| E₀ ≈ 20.7 keV（ZBエネルギー量子の数値予測） | **#46** |
| Stefan-Boltzmann n=2固有性（power 2nのfloor = 2^(1−n)） | **#46** |
| ΔL = \|γ_L−1\|×L₀（統一恒等式） | **#47** |
| 回転Lorentz収縮→AMM（明示的補足） | **#47** |
| ミュオン寿命と電子AMMの構造的対応 | **#47** |
| RMS補正 1/√2（調和振動子のpeak vs average） | **#47（明示化）** (#14由来) |

---

## New Experimental Predictions (Group 05)

| 予測 | 論文 | 状況 |
|------|------|------|
| E₀ ≈ 20.7 keV（ZBエネルギー量子） | #46 | 未測定 |
| ミュオン寿命と電子AMM: 同一のΔL構造（実験的確認は#47の前提） | #47 | 既知現象の構造的再解釈 |
| 順方向鎖 Thomas歳差 → v_ZB（a_eとは独立に） | #47 | 未解決（open task） |

---

## Scope and Methodology Notes (Group 05)

**共通の方法論的立場（全7論文）:**

- すべて「補足」「構造的明確化ノート」「概念的明確化」として自己定義
- 新しい力学方程式・新しい実験予測（#46, #47除く）を導入しない
- 「working structural hypothesis」という表現が#42に明示
- #44は「技術的内容は#33+#34+#35を読めばこの論文を読む必要なし」と明示

**#44 vs #35 の重複に注意:**

#35（Detailed Exposition）はすでに#33+#34の包括的技術的展開を含む。#44は概念的ナビゲーション地図として設計されており、#35を読んだ場合は#44は不要。

**#47 の未解決タスクに注意:**

#47は逆算（a_e → v_ZB）を確立しているが、順方向鎖（Thomas歳差のみから v_ZB を独立に導出）は未解決。この完成が「構造的対応」を「確認された物理的等価性」に昇格させる。

---

## Paper Character Summary

| # | 性格 | 読む必要がある場合 | スキップできる場合 |
|---|------|-------------------|------------------|
| 41 | 歴史・解釈的補足 | #40の歴史的文脈を知りたい | 技術的内容のみ必要な場合 |
| 42 | 構造仮説（磁気単極） | 磁気単極不在の0-Sphere的説明が必要 | #36+#33で十分な場合 |
| 43 | 開放経路vs閉ループ明示 | ねじれ問題・Dirac比較が必要 | — |
| 44 | 概念地図 | シリーズのナビゲーションが必要 | #35を読んだ場合 |
| 45 | 幾何構造問題 | ねじれの論理的強制性を知りたい | — |
| 46 | 数学的定理+予測 | 1/2ℏωの幾何的起源・E₀値が必要 | — |
| 47 | 構造的対応（定量的） | AMM-muon統一・v_ZBの逆算が必要 | — |

---

**Last Updated:** 2026-03-22
**Papers Covered:** #41–#47 (7 papers)
**Thematic Arc:** Structural clarifications — derivative hierarchy · monopole absence · torsion geometry · stability synthesis · holonomy · zero-point energy floor · AMM-muon structural correspondence
