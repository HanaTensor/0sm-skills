# 0-Sphere Model — Papers #31–#40 (High-Density Reference)

> Sub-file: `04/papers.md` | Parent: `index.md` | Concept: `04/concept.md`
> Period: Jan–Feb 2026 | Papers: #31–#40

---

## #31 — Line Integrals as Fundamental Observables in Physics: A Unified Principle (2026-01-10)

**DOI:** 10.5281/zenodo.18203433

**Core concept:** Unifying principle: Aharonov-Bohm effect, Berry phase, and Wilson loops all share the same mathematical structure — line integral of a connection. This is not coincidence but reveals a fundamental layer of physics where observables are histories, not field values.

**Three unified phenomena:**
```
Aharonov-Bohm: Δϕ = (e/ℏ)∮ A·dl     [EM phase, no local field]
Berry phase:   γ = ∮ A_Berry·dR       [geometric phase, parameter space]
Wilson loop:   W = Tr P exp(i∮ A·dl)  [gauge holonomy, QCD confinement]
```
All three: physically meaningful even where local curvature (field strength) vanishes.

**Key argument:** If the most fundamental quantum effects are integrals of connections along paths, then connection integrals — not local field values — are the primary carriers of physical information.

**0-Sphere model connection:**
```
Φ = ∫_γ ω   (connection one-form along internal worldline)
```
Unifies all three phenomena under single principle: physical observables = accumulated phase along histories.

**Operational significance:** Energy, momentum, charge measured through clocks, trajectories, and phase accumulation — not abstract field values at points.

---

## #32 — Dissolution of the Vacuum Energy Problem in an Integral-Based Ontology (2026-01-17)

**DOI:** 10.5281/zenodo.18275142

**Core concept:** Cosmological constant problem (10¹²⁰ discrepancy) dissolved at the level of principle — not resolved by dynamical mechanism. Vacuum energy is a category error arising from invalid reification of operator-ordering artifacts.

**The 5-step QFT derivation and where it fails:**
```
Step 1: Field quantization — uncontroversial
Step 2: Mode expansion via a_k, a†_k — uncontroversial
Step 3: Zero-point energy (1/2)ℏω_k per mode — uncontroversial
Step 4: Summation → E_vac ~ Λ⁴ — uncontroversial
Step 5: Gravitational coupling ⟨T_μν⟩_vac ~ ρ_vac g_μν — CATEGORY ERROR
```

**Why step 5 is invalid (integral-based ontology):**
- (1/2)ℏω_k = operator-ordering artifact (gauge-dependent, adding constant does not affect physics)
- Zero-point energies at spacetime points devoid of particles = no closed integral process
- Physical observables restricted to Φ = ∫_{γ_int} ω (worldline processes)
- Phase accumulation ≠ net energy flux → does not act as gravitational source

**Key distinction:**
```
Particle energy (E = mc²): localized, finite, gravitates → T^matter_μν ✓
Vacuum energy density (ρ_vac ~ Λ⁴): ubiquitous, divergent → category error ✗
```

**Cosmological constant Λ_obs:** Remains empirical input. Framework dissolves the vacuum energy problem but does NOT predict Λ_obs (explicitly acknowledged).

**Falsifiability:** Gravitational redshift/lensing from Casimir energy independent of plate mass would falsify this framework.

---

## #33 — Geometrical Confinement of Energy: A Topological Mechanism Underlying Rest Mass and Zitterbewegung (2026-01-24)

**DOI:** 10.5281/zenodo.18356895

**Core concept:** Rest mass and ZB emerge from topological confinement. S⁰ = {p₊, p₋} is totally disconnected; continuous energy transport requires embedding into arcwise connected domain D (photon sphere). supp(E) ⊂ D = confinement condition.

**Discrete localization:**
```
S⁰ = {p₊, p₋}                                           (III.1)
Discrete topology → any continuous map f: [0,1]→S⁰ is constant
No internal paths on S⁰ itself
```

**Embedding into domain D:**
```
i: S⁰ ↪ D   (D ⊂ ℝⁿ, compact, arcwise connected)         (IV.1)
D = photon sphere, diameter O(λ_C) = h/(mc) ≈ 2.426×10⁻¹² m
Geodesics in D: sin θ_A/sin θ_B = v_A/v_B  (Snell-type)  (IV.3)
S = ∫_{A}^{B} ds  (action minimized)                      (IV.4)
```

**Three Compton wavelength scales:**
```
Standard:    λ_C = h/(mc)  = 2.426×10⁻¹² m
Reduced:     λ̄_C = ℏ/(mc) = 3.86×10⁻¹³ m
ZB amplitude: λ_ZB = ℏ/(2mc) = 1.93×10⁻¹³ m
```

**ZB frequency (using λ_C):**
```
ν = βc/λ_C = 0.04047×c/λ_C ≈ 5.007×10¹⁸ Hz
τ_C = 1/ν ≈ 2.00×10⁻¹⁹ s (one cycle)
```

**Extreme limit — deformation retraction:**
```
λ_C → 0:  D ↘ {p}  (all paths degenerate)
           Radiative transport suppressed — geometric structure loss, not divergence
```

**Physical regime hierarchy:**
| Regime | Energy | Character |
|--------|--------|-----------|
| Visible–UV | ≲10 eV | Point-like electron |
| X-ray (Compton) | ~20 keV | Internal structure manifest, stable |
| Gamma-ray | ~250 keV | Stability threatened |
| Pair production | ≳511 keV | Electron no longer stable |

---

## #34 — Geometrical Confinement: Emergent Gravitational Dynamics Without Additional Mediators (2026-01-31)

**DOI:** 10.5281/zenodo.18437010

**Core concept:** First explicit derivation of gravitational-like phenomena from topological + thermodynamic principles. Atoms modeled as effective 0-Sphere subsystems. Entropic synchronization via real photon exchange → emergent drift/free-fall. No graviton needed.

**Entropic synchronization mechanism:**
```
Subsystem b (ν_b > ν_a) synchronizes with ambient network:
ΔE_sync = ℏ(ν_b − ν_a)                                  (II.3)
→ converted to translational KE: (1/2)mv²
→ drift toward synchronized ensemble = free-fall analog
```

**Metronome analogy:** Single metronome drifts toward synchronized group. Frequency mismatch energy converts to translational motion.

**Effective acceleration:**
```
g_eff = ΔE_sync/(m·Δx) = v_trans/Δt                     (III.6)
v_trans = √(2ΔE_sync/m) = √(2ℏΔν/m)                    (III.5)
Scaling: v_trans ∝ √(Δν)                                 (IV.5)
```

**ε₁ elimination — key innovation:**
```
Conventional: ε_total = ε₁ × ε₂ × ε₃ ~ 10⁻¹⁵  (implausible)
  ε₁ ~ 10⁻¹⁰ (internal energy → emitted photons)
0-Sphere:     ε₁ eliminated — ZB energy already in photon sphere
  ε_0-Sphere = ε₂ × ε₃ ~ 10⁻⁴–10⁻⁵
Improvement: ~10 orders of magnitude
```

**ZB energy budget (Earth-scale):**
```
E_ZB per electron ≈ 3.32×10⁻¹⁵ J
N_e (iron sphere, Earth mass) ≈ 1.7×10⁵¹
E_ZB,total ≈ 5.6×10³⁶ J  vs  E_grav ≈ 2.5×10³² J
Ratio ≈ 2.2×10⁴  (ZB energy exceeds gravitational binding by ~4 orders)
Required efficiency: ε ~ 7×10⁻⁵ (achievable with ε₁ eliminated)
```

**Simulation (Table I, idealized):** Δν = 1–10 MHz → g_eff = 9.6×10³–3.0×10⁴ m/s² (upper bounds; realistic with decoherence: 10⁻⁶–100 m/s²).

**Open questions:** Causality (light-crossing time ~21 ms vs local Δt ~10 μs), equivalence principle, 1/r² scaling emergence, mass/radius scaling.

---

## #35 — Detailed Exposition of the 0-Sphere Model Framework for Gravitational-Like Phenomena (2026-02-07)

**DOI:** 10.5281/zenodo.18511664

**Core concept:** Comprehensive reference paper for the gravitational-like phenomena framework. Full derivations, theoretical pathway, efficiency decomposition, Thomas precession spin derivation with corrected dimensional analysis.

**Theoretical pathway (α → g):**
```
α (fine-structure constant)
→ aₑ (anomalous magnetic moment: aₑ ≈ α/2π + higher order)
→ v_ZB (ZB velocity: γ=1+a → v_ZB≈0.04047c)
→ E_ZB (ZB energy: E_ZB = hν_ZB ≈ 3.32×10⁻¹⁵ J)
→ g_eff (effective gravitational acceleration via entropic synchronization)
```

**Complete efficiency decomposition:**
```
ε₁: internal energy → emitted photons (direction/quantization/coherence) ~10⁻¹⁰
ε₂: phase synchronization across subsystems
ε₃: synchronized gradients → translational motion
ε_total(conventional) = ε₁ × ε₂ × ε₃ ~ 10⁻¹⁵  (energetically implausible)
ε_total(0-Sphere) = ε₂ × ε₃ ~ 10⁻⁴–10⁻⁵  (ε₁ eliminated)
```

**Bicycle wheel analogy for γ=1+a:**
```
C_lab = 2πr,  C_rotating = 2πr/γ
ΔC/C_lab = γ − 1 ≈ a = aₑ/√2
```
Lorentz-contracted circumference of photon sphere → apparent excess angular momentum → AMM.

**Thomas precession derivation (corrected dimensionally):**
- Completes the correction begun in #28
- Confirms radius-independence
- Provides full derivation page 19

**Status:** Reference paper for #36 (methodological scope), #37 (gravitational PE).

---

## #36 — On the Non-Perturbative Nature of the 0-Sphere Model and the Fine-Structure Constant (2026-02-14)

**DOI:** 10.5281/zenodo.18603340

**Core concept:** Methodological manifesto. Non-perturbative (geometric) vs perturbative (QED) distinction. Explicit scope delimitation: what CAN and CANNOT be derived. α remains outside current scope.

**Non-perturbative derivation of v_ZB (no α dependence):**
```
a_exp = 0.00115965218073(28)           (experimental input only)
a = a_exp/√2 ≈ 0.00082008             (RMS-averaged)
γ(v_ZB^RMS) = 1 + a                   (geometric relation)
v_ZB^RMS = c√(1−1/(1+a)²) ≈ 0.04047c (closed-form prediction)
```
No α, no loop integrals, no virtual particles.

**Peak vs RMS velocities:**
```
v_ZB(t) = v_max|sin(ωt)|
γ_RMS = 1 + a_exp/√2 ≈ 1.00082008
γ_max = 1 + a_exp   ≈ 1.00115965
(γ_max−1)/(γ_RMS−1) = √2
v_RMS ≈ 0.04047c,  v_max ≈ 0.048c
v_max/v_RMS = 2^(1/4) = ⁴√2 ≈ 1.189
```

**Scope: CAN derive:**
1. v_ZB^RMS ≈ 0.04047c, v_ZB^max ≈ 0.048c (from a_exp + SR)
2. Geometric origin of g−2 (Lorentz contraction of photon sphere)
3. Spin-1/2 quantization (doubled frequency 2ω)
4. Energy conservation structure (Stefan-Boltzmann + phase)

**Scope: CANNOT currently derive:**
1. α ≈ 1/137 (no electric charge theory yet)
2. Electron rest mass m_e (identifies with E_ZB but not numerical value)
3. Lepton mass hierarchy (critical radius claims had dimensional error)
4. Strong and weak interactions (non-Abelian extension needed)

**QED vs 0-Sphere (Table 3, 7 aspects):**
- QED: perturbative in α, virtual photons, instrumentalist
- 0-Sphere: non-perturbative, real photons, realist

---

## #37 — Reinterpreting Gravitational Potential Energy as an Internal Line-Integral Quantity (2026-02-15)

**DOI:** 10.5281/zenodo.18637487
**Format:** REVTeX 4-2 (APS Physical Review B)

**Core concept:** mgh is not energy stored in space but energy stored in internal phase structure of the particle. Gravitational PE = differences in internal ZB frequency, accumulated as line integral along worldlines. Resolves circularity in classical definition.

**The circularity in classical definition:**
```
Object accelerates downward → has gravitational PE
Gravitational PE → associated with position in field
Gravitational field → defined by tendency to accelerate downward
→ closed logical loop
```

**Resolution — internal frequency identification:**
```
"Higher" = faster internal oscillation, less synchronized (operationally measurable)
"Lower"  = slower internal oscillation, more synchronized with surroundings
```

**Central derivation — ℏΔω = mgΔh:**
```
ΔΦ = gΔh
Δω = ω₀ΔΦ/c² = ω₀gΔh/c²
ω₀ = mc²/ℏ   (rest mass as internal frequency)
→ ℏΔω = ℏ(mc²/ℏ)(gΔh/c²) = mgΔh  ✓
```

**Numerical verification (electron, Δh = 1 m):**
```
ΔU_classical = m_e·g·Δh ≈ 8.9×10⁻³⁰ J
ΔE_int = ℏΔω             ≈ 8.9×10⁻³⁰ J   ✓  exact match
```

**GPS prediction (reused from #22):**
```
Δν = ν_ZB,sat − ν_ZB,Earth ≈ 2.64×10⁹ Hz
Fractional change ≈ 5.29×10⁻¹⁰
```

**Free fall as thermal geodesic (entropy-weighted action):**
```
S_thermal = ∫[L_geometric − T·S_internal] dτ
Free fall trajectory = entropy-maximizing path
```

**Comparison table (Table 1, 9 aspects):** Classical mechanics vs 0-Sphere for PE, "higher position," physical carrier, free-fall mechanism, conceptual circularity, GR correspondence, testability.

---

## #38 — Geometric Phase Structure of the 0-Sphere Model: Dual Degrees of Freedom within 2π Periodicity (2026-02-21)

**DOI:** 10.5281/zenodo.18718174
**Format:** REVTeX 4-2 (PRB)

**Core concept:** Establishes complete geometric phase structure. g=2 as topological invariant. Three coexisting phase periodicities. Realist Bloch sphere as antithesis to quantum superposition. EPR reality criterion.

**Three phase structures in one 2π cycle:**
```
Half-angle (θ/2): cos⁴(θ/2), period π  → Te₁, Te₂ (thermal PE)
Normal-angle (θ): (1/2)sin²(θ), period 2π → photon sphere KE (T^max/E₀ = 1/2)
Double-angle (2θ): (1/2)sin(2θ), period 4π → Thomas Ω_T (spinorial)
```
Note: T^max/E₀ = 1/2 (not 1) — thermodynamic consequence of Stefan-Boltzmann, not free parameter.

**Berry phase and g=2 (exact):**
```
Equatorial Bloch sphere trajectory → solid angle Ω = 2π sr
γ_intrinsic = Ω/2 = π
g_CM = 2γ/π = 2   [TOPOLOGICAL INVARIANT — no perturbative corrections]
g_lab = 2(1+a),   a = γ_anomalous/(2π)
```

**Gauge correspondence (phenomenological, not derivation):**
```
Period π  → s=2 → Gravity (spin-2 graviton)
Period 2π → s=1 → Electromagnetism U(1) (spin-1 photon)
Period 4π → s=1/2 → Weak SU(2) (spin-1/2 fermion)
```

**Spin-state classification (thermodynamic, primary):**
```
θ ∈ [0,π):  Kernel A radiation phase, ∂Te₁/∂t < 0 → spin-up
θ ∈ (π,2π]: Kernel A absorption phase, ∂Te₁/∂t > 0 → spin-down
θ = π:      transition point, spin unassigned
```

**Realist Bloch sphere (antithesis to superposition):**
```
Standard QM: Bloch sphere point = superposition |ψ⟩ = cos(θ/2)|0⟩ + e^{iφ}sin(θ/2)|1⟩
0-Sphere:    Bloch sphere = time-ordered deterministic trajectory of internal phase
             At any τ: definite point on trajectory (NOT simultaneous occupation of A and B)
```

**EPR reality criterion (Einstein, Podolsky, Rosen 1935):**
"If we can predict with certainty the value of a physical quantity without disturbing the system, there exists an element of physical reality."
→ Spin state in 0-Sphere = element of physical reality, determined by internal geometry prior to measurement.

**NOT a local hidden variable theory:** Internal phase θ is geometric, non-local quantity. Relationship to measurement involves non-local process. Not excluded by Bell's theorem. Correct label: **internal geometric realism**.

**Open question:** Electric charge generation/conservation in 0-Sphere → decisive criterion for final spin-state classification (kinematic alternative not fully closed).

---

## #39 — On Vacuum Energy, Integral Ontology, and the Cosmological Constant (2026-02-22)

**DOI:** 10.5281/zenodo.18727981
**Relation:** Supplementary note to #32

**Core concept:** Clarifies logical separation between (i) vacuum energy problem (addressed: category error) and (ii) origin of Λ_obs (open: 5 possibilities listed). Neither conflated nor confused.

**Category error diagnosis:**
```
Zero-point energy (1/2)ℏω_k:
  - Mathematical artifact of operator ordering
  - Gauge-dependent (Hamiltonian shift → no physical change)
  - Corresponds to NO closed integral process
  - Step 5 reification (→ gravitational source) = category error
```

**Gauge artifact analogy:**
```
A_μ(x):       gauge-dependent, only Wilson loops physical
Schwarzschild radius: coordinate artifact
(1/2)ℏω_k:   operator-ordering artifact — same logical status
```

**Λ_obs: 5 open possibilities (not resolved):**
1. Boundary conditions on global network of internal circulations
2. Collective statistical effects of vast number of processes
3. Topological contribution encoding global topology of emergent spacetime
4. Emergent parameter unrelated to vacuum structure (like viscosity in fluids)
5. Phase-frozen configurations (dynamically frozen internal states → background contribution)

**Casimir reinterpretation:** Boundary-dependent energy differences (not absolute vacuum energy density). No gravitational effect from Casimir energy detected independently of plate mass.

**Falsifiability (3 criteria):** Gravitational lensing from Casimir energy; spacetime curvature from vacuum state manipulation; cosmological evolution inconsistent with Λ=const. but consistent with field-theoretic vacuum dynamics.

---

## #40 — On the Derivative-Order Mismatch Between Gauge Theory and Gravity (2026-02-23)

**DOI:** 10.5281/zenodo.18736670
**Relation:** Supplement to line-integral trilogy (#29, #30, #31)

**Core concept:** Gauge theory and GR assign physical meaning to geometric objects at different derivative orders. Line integrals of connections provide common observational layer across both.

**The mismatch:**
```
Gauge theory:  Force = curvature F_μν = ∂_μA_ν − ∂_νA_μ  (1st derivative of connection)
GR:            Force = connection Γ^μ_νρ directly (0th order in connection, geodesic eq.)
```

**Summary table:**
| Aspect | Gauge Theory | General Relativity |
|--------|-------------|-------------------|
| Physical role of curvature | Physical force (E, B) | Source-related (mass-energy) |
| Physical role of connection | Auxiliary; holonomy | Force-like (geodesic equation) |
| Primary observable | Curvature locally; line integral globally | Connection/line integral |

**Harmonization via line integrals:**
```
Φ = ∫_γ ω   (generic connection one-form)
Gauge: ω = A_μ dx^μ         → Aharonov-Bohm phase
Gravity: ω = Γ^μ_ν = Γ^μ_νρ dx^ρ  → gravitational redshift, time dilation
```

**Pre-divergence layer:**
- Line integrals of connection definable PRIOR to any divergence requirement (∇^μG_μν=0)
- More primitive structural layer than Einstein's construction
- Conservation laws and divergence-free conditions = secondary/emergent

**Connection notation clarification:**
```
∫_γ Γ  [misleading — Γ^μ_νρ not tensors]
∫_γ ω  [correct — ω = Γ^μ_ν = Γ^μ_νρdx^ρ is matrix-valued one-form]
```
Not merely notational: one-form emphasizes curve-tied nature, not infinitesimal neighborhood.

---

## Cross-Paper Links (#31–#40)

| From | To | Connection |
|------|----|-----------|
| #31 (AB+Berry+Wilson unified) | #32, #37, #40 | Line integral ontology |
| #32 (vacuum energy dissolved) | #39 | #39 is supplement clarifying #32 |
| #33 (topological confinement) | #34 | #34 extends to gravitational phenomena |
| #34 (metronome/entropic sync) | #35 | #35 is comprehensive exposition of #34 |
| #34 (ε₁ elimination) | #35 | Full efficiency derivation in #35 |
| #35 (theoretical pathway α→g) | #36 | #36 clarifies scope (α outside) |
| #35 (bicycle wheel, γ=1+a) | #36 | Geometric derivation extended |
| #36 (v_ZB^peak/RMS distinction) | — | v_max=⁴√2·v_RMS (new result) |
| #37 (ℏΔω=mgΔh) | #22 | GPS Δν prediction reused |
| #38 (g=2 topological invariant) | #26 | Berry phase mechanism from #26 |
| #38 (realist Bloch sphere) | #27 | Determinism thread culmination |
| #38 (EPR criterion) | — | First explicit EPR citation in series |
| #39 (Λ_obs open) | #32 | Supplement: clarifies what #32 does NOT claim |
| #40 (derivative mismatch) | #29, #30, #31 | Conceptual bridge for line integral trilogy |
| #40 (pre-divergence layer) | #31, #32 | Layer below Einstein's construction |

---

*Period: Jan–Feb 2026 | Prev: `03/papers.md` | Next: `05/papers.md` (#41–#47+)*
