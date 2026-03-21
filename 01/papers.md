# 0-Sphere Model — Papers #1–#10 (High-Density Reference)

> Sub-file: `01/papers.md` | Parent: `index.md` | Concept: `01/concept.md`
> Period: 2018–2023 | Papers: #1–#10 (10 papers, #8=2021, #9–#10=2023)

---

## #1 — A Model of an Electron Including Two Perfect Black Bodies (2018-11)

**DOI:** 10.5281/zenodo.16759284
**Original:** viXra:1811.0312v3
**Zenodo label:** [1 Essential]

**Core concept:** Foundation paper establishing the complete 0-Sphere Model architecture. Electron = 2 bare electrons (spinors, perfect black bodies) + 1 virtual photon (real photon captured by fine structure constant α ≈ 1/137).

**Central energy conservation identity (first appearance — cited in all subsequent papers):**
```
E₀ = E₀[cos⁴(ωt/2) + sin⁴(ωt/2) + (1/2)sin²(ωt)]
Te₁ = E₀·cos⁴(ωt/2)        — Spinor 1 thermal potential energy
Te₂ = E₀·sin⁴(ωt/2)        — Spinor 2 thermal potential energy
γ*_KE = (1/2)E₀·sin²(ωt)   — Virtual photon kinetic energy
```

**Temperature gradient driving force:**
```
grad(Te₂ − Te₁) = E₀·sin(θ)   where θ = ωt
u_γ* = −E₀·sin(θ)              velocity potential of virtual photon
```
Gradient drives virtual photon as simple harmonic oscillator between ±a.

**Key physical assumptions:**
- Perfect black body: emissivity ε = 1 required for charge conservation (if ε < 1, bare electrons vanish)
- Perfect fluid: irrotational, no viscosity (required for continuous oscillation without dissipation)
- Hydrostatic equilibrium analogy: electron ≈ Sun (pressure-gradient force vs electromagnetic centering force)
- Zero-point energy: system achieves (1/2)E₀ at phase sin²(ωt) = 1

**Spinor superposition (720° rotation):**
```
Four states cycling in phases between nπ: |↑↑⟩, |↓↑⟩, |↑↓⟩, |↓↓⟩
Spinors: 720° periodicity (θ/2 dependence)
Vector:  360° periodicity (θ dependence)
```

**Key innovation:** Eliminates self-energy divergence by maintaining non-zero distance between interacting particles. Quartic dependence cos⁴, sin⁴ from Stefan-Boltzmann law (black-body radiation ∝ T⁴).

---

## #2 — A New Representation of Spin Angular Momentum (2018-12)

**DOI:** 10.5281/zenodo.16783727
**Original:** viXra:1812.0472v3
**Zenodo label:** [2 Supplement]

**Core concept:** Slinky spring analogy for electron spin angular momentum during linear motion. Extends the dual-spinor oscillation model of #1 to translational motion with discrete spatial steps.

**Architecture:**
- Each translational step = one Compton wavelength = radius of virtual photon
- Two spinors at positions ±a exchange thermal PE via virtual photon
- Linear progression resembles a Slinky descending stairs: CoM advances one step per oscillation cycle

**Spatial discretization:**
```
Spinor 1 positions: x_e1 = 2nr       (n = 0, 1, 2, ...)
Spinor 2 positions: x_e2 = (2n+1)r   (n = 0, 1, 2, ...)
Te₁ = ∫ E₀·cos⁴(ωt/2)·δ(x − 2nr) dx
Te₂ = ∫ E₀·sin⁴(ωt/2)·δ(x − (2n+1)r) dx
```

**Stern-Gerlach explanation:**
- Magnetic field gradient ≈ tilted staircase perpendicular to direction of motion
- Slinky shifts laterally (left or right) as it descends inclined stairs
- Spin-up vs spin-down = direction of lateral shift under gradient

**Key conclusion:** Spin angular momentum emerges from discrete step-wise energy transfer between two thermal spots, not from intrinsic rotation of a point particle.

---

## #3 — Uniquely Distinguishing an Electron's Spin via Riemann Surface (2019-03)

**DOI:** 10.5281/zenodo.17759634
**Original:** viXra:1904.0273

**Core concept:** Riemann surface w → √z represents the two-state spin system. Magnetic field disconnects Riemann domains to select eigenstate.

**Two-domain architecture:**
```
D₀ (0π to 2π): Te₁ spin = |↑⟩, Te₂ spin = |↑⟩
D₁ (2π to 4π): Te₁ spin = |↓⟩, Te₂ spin = |↓⟩
Analytic continuation connects D₀ and D₁ → superposition of four states
```

**Phase-dependent spin states:**
```
|↑↑⟩: (4n+0)π < θ < (4n+1)π
|↓↑⟩: (4n+1)π < θ < (4n+2)π
|↓↓⟩: (4n+2)π < θ < (4n+3)π
|↑↓⟩: (4n+3)π < θ < (4n+4)π
```

**Measurement mechanism:**
- Magnetic field gradient disconnects domains: D₀ ∩ D₁ = ∅
- Disconnection eliminates |↑↓⟩ and |↓↑⟩ transition paths
- Fixes spin to either |↑↑⟩ or |↓↓⟩ (eigenstate selection)

**Key conclusion:** Spin uniquely determined at θ = nπ (one spinor holds all energy, other is zero). Superposition exists only while Riemann surface domains remain connected.

---

## #4 — Perfect Contrast Cannot Be Obtained in the Electron Double-Slit (2019-06)

**DOI:** 10.5281/zenodo.17759699
**Original:** viXra:1907.0259

**Core concept:** Explains Tonomura's observation that electron interference fringes never achieve perfect visibility P_vis = 1, while photon double-slit achieves P_vis = 1.

**The visibility problem:**
```
Photon double-slit: P_vis = 1 (perfect dark fringes, p_min = 0)
Electron double-slit: P_vis < 1 (ambiguous troughs, p_min > 0)
P_vis ≡ (p_max − p_min)/(p_max + p_min)
```

**0-Sphere explanation:**
```
|ψ(x)|² = (A·cos²θ·J₀(kr₁) + A·sin²θ·J₀(kr₂))²
A_spinor1 = A·cos²θ,  A_spinor2 = A·sin²θ   (phase-dependent weights)
```

**Phase-dependent amplitude ratios:**
```
θ = 0π:   100:0  → single spinor only → no interference
θ = π/4:  50:50  → equal amplitudes  → P_vis = 1 (photon-like)
θ = π/2:  0:100  → single spinor only → no interference
```

**Amplitude order hierarchy:**
```
Spinor energy:    4th order — cos⁴(θ/2), sin⁴(θ/2)
Spinor amplitude: 2nd order — cos²(θ/2), sin²(θ/2)
Vector energy:    2nd order — sin²(θ)
Vector amplitude: 1st order — sin(θ)
```

**Prediction:** C₆₀ fullerene and helium atom experiments also show P_vis < 1 (confirmed by references). Verification: control electron phase at biprism to intentionally vary visibility.

---

## #5 — Transition Theory from Uncertain to Causal Basis (2019-09)

**DOI:** 10.5281/zenodo.17759726
**Original:** viXra:1909.0435

**Core concept:** Thermal potential energy gradients convert random walk into deterministic electron trajectory. "Uncertainty principle" → "certainty principle."

**Random walk (no gradient):**
```
Bare electron at origin: equal probability p = q = 1/2 left or right
Step size = virtual photon radius (Compton wavelength)
Characteristic function: peiθ + qe−iθ = cos θ (when p = q = 1/2)
Position probability: Pn(j) = (1/2π)∫[cos θ]ⁿ e^(−ijθ) dθ
```

**Deterministic motion (with gradient):**
- Another electron at coordinate A creates temperature gradient
- Second law: electron moves toward lower thermal PE → p = 1

**2D lattice extension:**
```
Random: electron at O, neighbor at A → moves to B, C, or D with p = 1/3 each
Causal: electrons occupy A, B, D → electron at O must move to C with p = 1
```

**Key conclusion:** Uncertainty arises from incomplete thermal information, not fundamental randomness. This paper is the seed of the determinism thread continued in #25 and #27.

---

## #6 — Correspondence Between a 0-Sphere and the Electron Model (2020-01)

**DOI:** 10.5281/zenodo.17759908
**Original:** viXra (2020)

**Core concept:** Formal naming convention paper. S⁰ = {−a, +a} as the minimal nontrivial topology underlying the electron model.

**Key definitions:**
- S⁰ = two disconnected points = {Spinor A at −a, Spinor B at +a}
- Minimal geometric structure sufficient for all electron dynamics
- Perfect black body condition (ε = 1): physically equivalent to charge conservation

**Key insight:** If emissivity ε < 1, bare electrons gradually lose energy and vanish — charge conservation requires exactly ε = 1. This connects the thermodynamic assumption to a fundamental conservation law.

---

## #7 — Coexistence of Positive and Negative-Energy States in the Dirac Equation (2020-06)

**DOI:** 10.5281/zenodo.17760132
**Original:** viXra:2007.0051

**Core concept:** Reinterprets Dirac equation's negative-energy solutions as internal energy exchange between two spinors in one electron. Eliminates need for antiparticles or time reversal.

**The reallocation:**
```
Traditional: Ψ = (Ψ⁽⁺⁾, Ψ⁽⁻⁾)ᵀ = (particle, antiparticle)ᵀ         where p = 0
0-Sphere:    Ψ = (Ψ⁽⁺⁾, Ψ⁽⁻⁾)ᵀ = (Spinor 1/Te₁, Spinor 2/Te₂)ᵀ  where p_γ* = 0
```

Key substitution: conventional free-particle momentum p → virtual photon momentum p_γ*.

**Dirac equation at rest (p_γ* = 0):**
```
Ψ⁽⁺⁾_u: E = +mc² — Spinor 1 in radiation state (∂m_Te1/∂t < 0, losing energy)
Ψ⁽⁻⁾_u: E = −mc² — Spinor 2 in absorption state (∂m_Te2/∂t > 0, gaining energy)
```

**Phase-dependent states:**
```
θ = 0π, 4π:  Ψ⁽⁺⁾_u = (1,0,0,0)ᵀ — Spinor 1 at +a holds all energy
θ = π:       Ψ⁽⁻⁾_u = (0,0,0,1)ᵀ — Spinor 2 at −a holds all energy
θ = 2π:      Ψ⁽⁺⁾_d = (0,1,0,0)ᵀ — Spinor 1 at +a holds all energy
θ = 3π:      Ψ⁽⁻⁾_d = (0,0,1,0)ᵀ — Spinor 2 at −a holds all energy
```

**Key conclusion:** "We do not have to eliminate the negative sign of the energy nor to consider reversing the time t → −t." Positive/negative energy states arise naturally from phase-dependent internal energy exchange.

---

## #8 — Consideration of Electron-Positron Pair Annihilation (2021-07)

**DOI:** 10.5281/zenodo.17760445

**Core concept:** Annihilation requires simultaneous satisfaction of two independent conditions: Feynman (phase alignment) AND Pauli (anti-symmetry). Riemann surface domain intersection = physical event of annihilation.

**Two conditions:**
```
Feynman condition: phase alignment between electron and positron oscillations
Pauli condition:   anti-symmetry requirement (spinor states must be anti-parallel)
Annihilation: both conditions satisfied simultaneously → Riemann domain intersection
```

**Post-annihilation photons:** Composed of spinor pairs from the original electron-positron system. Time-reversal interpretation of positron: positron = electron running backward in phase (not time).

---

## #9 — Beyond the Standard Model: Neutrino Oscillations (2023-04)

**DOI:** 10.5281/zenodo.17764952

**Core concept:** Neutrino flavor oscillation emerges geometrically from Lissajous curve trajectories when two internal spinors have different angular frequencies (ω₁ ≠ ω₂).

**Framework comparison:**
```
Standard Model: |νℓ⟩ = Σᵢ Uℓᵢ|νᵢ⟩  (PMNS mixing matrix, probabilistic)
0-Sphere Model: Neutrino = two spinors with ω_ν₁ ≠ ω_ν₂
                Oscillation pattern = Lissajous curve in 2D space
                T = 2π/|ω_ν₁ − ω_ν₂|
```

**Flavor → frequency ratio correspondence:**
- Electron neutrino νₑ: specific ω_ν₁/ω_ν₂ region
- Muon neutrino νμ: different frequency ratio region
- Tau neutrino ντ: third frequency ratio region

**Beyond Standard Model implications:**
- No seesaw mechanism required (neutrino masses from frequency differences)
- CP violation: phase difference between ω_ν₁ and ω_ν₂ (geometric origin)
- Sterile neutrinos: additional frequency modes ω_ν₃, ω_ν₄ naturally accommodated

**Testable prediction:** Neutrino beam spatial distribution ≠ straight line → Lissajous spatial pattern detectable by long-baseline detector arrays (NOvA, T2K, DUNE).

---

## #10 — Redefining Electron Spin and AMM Through Harmonic Oscillation and Lorentz Contraction (2023-09)

**DOI:** 10.5281/zenodo.17764997
**Updated:** June 2024

**Core concept:** Spin emerges from Thomas precession with SHM. Anomalous magnetic moment caused by rotational Lorentz contraction. First quantitative prediction of ZB velocity.

**Thomas precession with SHM (corrects uniform-circular-motion assumption):**
```
vγ* = v₀·cos(ωt)            virtual photon velocity
aγ* = −v₀ω·sin(ωt)          virtual photon acceleration
Ω = (1/2c²)[aγ* × vγ*] = −(1/4c²)v₀²ω·sin(2ωt)
```

Double angle sin(2ωt) → half-circumference (π) generates angular velocity equivalent to one full rotation (2π) → natural spin-1/2.

**AMM via Lorentz contraction (Einstein 1912 rotating coordinate system):**
```
γ = 1 + a                          [FIRST APPEARANCE — bridge equation]
L/L₀ = 1/(1 + √(1/2)·aₑˣᵖ)
aₑˣᵖ = 0.00115965218059(13)        (experimental input)
```

**ZB velocity prediction (first appearance):**
```
β² = (v_ZB/c)² = 0.00163798087
v_ZB ≈ 0.04047c = 12,133 km/s     [KEY PREDICTION]
ν_ZB = βc/λ_Compton ≈ 5.007×10¹⁸ Hz
```

**GR correction (geodetic precession, Schwarzschild metric):**
```
Δφ_geodetic = 2π[1 − √(1 − 3M/R)]
L/L₀ = 1/(1 + √(1/2)·aₑˣᵖ − Δφ_geodetic/2π)
v_ZB(SR+GR) ≈ 0.040374c
```

**Electron size predictions:**

| r_electron (m) | v_ZB/c |
|----------------|--------|
| 10⁻²² | 0.040472 |
| 10⁻²⁵ | 0.040134 |
| 10⁻²⁶ | 0.036950 |

→ If v_ZB ≈ 0.0400c measured, electron radius is between 10⁻²⁵ to 10⁻²⁶ m.

**QED comparison:**

| Property | QED | 0-Sphere |
|----------|-----|---------|
| Spin origin | Intrinsic | Thomas precession + SHM |
| AMM calculation | Perturbative series in α | Single geometric formula |
| Zitterbewegung | Superluminal (c) | Subluminal (~0.04c) |
| Electron size | Point particle | 10⁻²⁵–10⁻²⁶ m |

---

## Cross-Paper Links (#1–#10)

| From | To | Connection |
|------|----|-----------|
| #1 (central identity) | **All papers** | Always cite as foundation when introducing 0-Sphere Model |
| #6 (S⁰ naming) | All papers | "0-Sphere" naming convention throughout series |
| #7 (Dirac ± reinterpretation) | #26 (Appendix V.B,H), #33 (Appendix H2), #38 | ±energy = thermal emission/absorption phases |
| #10 (γ=1+a, v_ZB) | #13–#47 | Quantitative foundation used in all subsequent papers |
| #4 (P_vis < 1) | #38 | Electron interference visibility revisited with Berry phase |
| #5 (determinism) | #25, #27 | Anti-Copenhagen determinism thread |
| #3 (Riemann surface) | #8 | Domain intersection = annihilation mechanism |
| #9 (Lissajous ω₁≠ω₂) | Speculative: quarks, dark matter | Frequency generalization principle |

---

*Period: 2018–2023 | Next: `02/papers.md` (#11–#20)*
