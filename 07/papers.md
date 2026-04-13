# 0-Sphere Model Papers: Group 06 (#48–, Mar 2026–)

**Coverage:** Papers #48–#51 (March–April 2026)
**Parent Index:** index.md
**Preceded by:** 05/papers.md (#41–#47)
**Theme:** Fiber Bundle Formalization, Gauge Symmetry Correspondence, Gravitational Mediation, Metric Emergence

---

## Overview

Group 06 opens with the formal fiber bundle proof of the g-factor structure, establishing the U(1) principal bundle framework that organizes the Berry phase results of Groups 02–05. Papers in this group elevate structural correspondences (gauge symmetry, gravitational mediator) from phenomenological observations to rigorous derivations, and culminate in the three-dimensional helical trajectory and the emergence of the spacetime metric from internal phase accumulation.

Development arc (so far):

1. U(1) fiber bundle formalization of g = 2 and dual-frame decomposition (#48)
2. Photon-sphere ejection mechanism as gravitational mediator; Thomas precession via Tomonaga framing; geometric UV cutoff (#49)
3. Scalar oscillation → angular momentum emergence; Lorentz-invariant chirality χ = sign(da/dt); frame-dependent helicity h = χ·sign(p_x); flip-impossibility at m → 0 (#50)
4. Three-dimensional helical trajectory; arcwise-connectivity prerequisite; Bonnet–Myers confinement as theorem; spacetime metric emergence from Berry connection (#51)

---

## Paper #48: Geometric Origin of g = 2 in the 0-Sphere Model: U(1) Fiber Bundle and Dual-Frame Phase Decomposition

**Date:** 2026-03-28 · **DOI:** 10.5281/zenodo.19227518 · **Type:** Structural Clarification Note (Supplement to #26 + #38)

### Core Concept

Establishes the geometric phase structure of the 0-Sphere Model via a three-step logical chain: (1) the 2π periodicity of the internal state is uniquely determined by the single-valuedness requirement; (2) this periodicity defines a principal U(1) fiber bundle P = S¹ × U(1); (3) the Berry connection on this bundle yields a non-trivial holonomy γ_intrinsic = π, geometrically necessitating g_CM = 2 as a topological invariant.

### Three-Step Logical Chain (Core Argument)

```
Step 1: 2π period uniquely selected
  T(θ) = (E₀/2)sin²θ has period π (scalar)
  |ψ(θ)⟩ = cos(θ/2)|A⟩ + sin(θ/2)|B⟩ requires 2π (spinor)
  → Period π is physically distinct (orthogonal), 4π redundant → 2π unique

Step 2: 2π → S¹ → U(1) bundle
  Base: M = S¹ ≅ ℝ/(2πℤ)
  Fiber: U(1) = {e^{iφ} | φ ∈ ℝ}
  Total: P = S¹ × U(1)

Step 3: Berry connection → holonomy
  A_θ(θ) = (1/2)cos θ
  γ_intrinsic = Ω/2 = π  (boundary term = arg(-1) = π)
  → g_CM = 2γ/π = 2 (exact, topologically protected)
```

### Dual-Frame Decomposition

γ_total = γ_intrinsic + γ_anomalous = π + a·2π

g_lab = 2(1 + a),  a := γ_anomalous/(2π)

Source: Lorentz projection (Thomas precession + Lorentz contraction) distorts the equatorial trajectory on the Bloch sphere into a perturbed ellipse. The anomalous arc a·2πr is the "hidden segment" in the CM frame, generating γ_anomalous.

### Foucault Pendulum as Prototype Holonomy (New Analogy)

| Foucault Pendulum | 0-Sphere Model |
|---|---|
| Equator (φ = 0) | CM frame (proper time τ) |
| Zero precession at equator | γ_intrinsic = π, g_CM = 2 exactly |
| Geographic latitude φ | Lorentz boost by v_ZB/c |
| Small latitude φ ≪ 1 | Small lab-frame correction a_e ≈ 0.00116 |
| Precession 2π sin φ | γ_anomalous |

### Key Equations

```
Berry connection:   A_θ(θ) = (1/2)cos θ
Holonomy (real gauge): γ = ∫A_θ dθ + arg⟨ψ(0)|ψ(2π)⟩ = 0 + π = π
g-factor definition:  g := 2γ/π → g_CM = 2
Dual-frame:          γ_total = π + a·2π,  g_lab = 2(1+a)
Bridge equation:     γ_L = 1 + a  (from #10, formalized here)
```

### Three-Periodicity / Gauge Symmetry Correspondence (Phenomenological)

| Function | Period T | s = 2π/T | Correspondence |
|---|---|---|---|
| cos⁴(θ/2) | 4π | 1/2 | SU(2) fermion |
| (1/2)sin²(θ) | 2π | 1 | U(1) EM (photon) |
| (1/2)sin(2θ) = Ω_T | π | 2 | Spin-2 candidate |

Note: spin-2 assignment conditional on spin-state classification branch point (Section VII E).

### Triple Coincidence: Three Routes to 1/2ℏω

1. **QM**: [x̂, p̂] = iℏ → uncertainty principle floor
2. **0-Sphere Hamiltonian**: cos⁴(θ/2)+sin⁴(θ/2) ≥ 1/2 (trigonometric identity)
3. **Centroid geometry**: AM–GM on (u,v)=(cos²θ/2, sin²θ/2) → r ≥ 1/2

All three arrive at E₀/2 = (1/2)ℏω through independent logical paths. First identified as a "unified triple coincidence" in this paper.

### Thermodynamic Classification: Algebraic Selection

The kinematic classification (spin assigned by sgn(Ω_T)) is excluded by internal algebraic consistency: it implies T_spin = π, giving g = 2·2γ/π = 4, contradicting the topologically established g_CM = 2. The thermodynamic classification ([0,π) = spin-up, (π,2π] = spin-down) is the unique internally consistent assignment.

### What the Model Can and Cannot Derive

**Can:**
- γ_intrinsic = π as formal topological invariant
- g_CM = 2 as theorem (not postulate)
- g_lab = 2(1+a) structural decomposition
- Foucault analogy with quantitative bridge equation γ_L = 1+a
- Three-periodicity gauge symmetry correspondence (phenomenological)
- Thermodynamic classification selected by algebraic consistency
- Triple coincidence for 1/2ℏω

**Cannot (open tasks):**
- First-principles calculation of γ_anomalous from internal geometry
- δA(θ; v/c) functional form
- Forward chain: Thomas precession → v_ZB → a_e (remains open from #47)
- Gauge field equations from internal phase structure
- Electric charge generation and EM coupling (internal structure)

### Harmonic Oscillator Reinterpretation (Fig. 5)

E_n = (n + 1/2)ℏω reinterpreted: ground state n=0 ↔ geometric minimum E₀/2. Each n→n+1: absorption of photon-sphere quantum. Each n→n-1: ejection (gravitational mediator conjecture, Paper #49).

### Relation Chain

Is supplement to #26 + #38 · Continues #26 + #38 + #47 + #35 · References #47 + #10 + #44 · Requires #1 + #26 + #35 + #38 · Is part of #47

---

## Paper #49: Photon-Sphere Fragmentation as a Gravitational Mediator: Radiation-Gradient Ejection in the π-Cycle of the 0-Sphere Model

**Date:** 2026-04-04 · **DOI:** 10.5281/zenodo.19393391 · **Type:** Research Paper

### Core Concept

This paper identifies the microscopic gravitational-mediation mechanism left open in Paper #34, and provides the physical ejection mechanism whose existence Paper #48 established as a prerequisite for a full spin-2 derivation. The physical basis is Thomas precession understood in the kinematic sense formulated by Tomonaga: whenever a body undergoes accelerated motion at relativistic speed, its proper coordinate frame rotates relative to the laboratory frame even under parallel-axis transport. In the 0-Sphere model, the photon sphere is continuously accelerated by the radiation gradient F = E₀sinθ, and Zitterbewegung sustains this oscillation at v_ZB ≈ 0.04c; Thomas precession therefore naturally arises as a structural feature of the internal dynamics, rather than being introduced as an additional assumption.

### Thomas Precession: Tomonaga Framing (Revised from #19)

The critical conceptual revision established in this paper:

| | Old framing (#19 context) | New framing (#49) |
|---|---|---|
| **Cause** | Arc-connected geodesic path → v × a ≠ 0 | Relativistic accelerated motion → Thomas precession (Tomonaga's physical interpretation) |
| **Primary driver** | Geometric path curvature | Radiation gradient F = E₀sinθ |
| **v × a ≠ 0** | Explanation | Concrete expression of the above |
| **Reference** | — | Tomonaga, *The Story of Spin* (1997), pp.42–43 |

See also: `tomonaga.md` (repository root) for full framing, anti-pattern, and cross-references.

### Key Equations

```
Radiation gradient (Paper #1, re-applied):
  F(θ) = d(Te₂ − Te₁)/dθ = E₀sinθ

Photon-sphere KE profile (π-cycle):
  E_ph(θ) = (E₀/2)sin²θ    [peaks at θ = π/2]

Ejection threshold:
  E_ph(π/2) = E₀/2 = E_bind
  [n = 0: threshold exactly saturated, no emission]
  [n ≥ 1: surplus nℏω above floor → fragment ℏω ejected per n → n−1]

Thomas angular velocity (established #19, Tomonaga-framed here):
  Ω_T(θ) = −(v₀²ω / 4c²) sin(2θ) ê_z    [period = π]

UV cutoff:
  Mode n has n+1 antinodes → n+1 ejection opportunities per A→B traversal
  n bounded above by n_max (Compton-scale well geometry) → self-energy sum finite
```

### Key Results

**Thomas-Precession Ejection Mechanism.** The photon sphere is perpetually accelerated by the radiation gradient at v_ZB ≈ 0.04c. Thomas precession, as physically interpreted by Tomonaga, naturally arises, generating angular momentum Ω_T that peaks at θ = π/2 and constitutes the outward centrifugal-like stress driving fragment ejection.

**Closure of Paper #34's Three Open Questions.**
- (i) Mediating quantum: photon-sphere fragment ejected at θ = π/2
- (ii) Ejection mechanism: photon-sphere KE saturates geometric binding floor E₀/2
- (iii) Near-neighbor character: follows from Compton-scale photon-sphere size

**Physical Ejection Mechanism for Paper #48's Spin-2 Candidate.** The ejected fragment carries the π-periodic phase structure of Ω_T through a kinetic-stress balance derived independently of kinematic spin-cycle counting. Rank-2 tensor proof remains an open task.

**Fourth Independent Route to Zero-Point Energy.** The geometric floor E₀/2 is precisely the ejection threshold. This adds a physical ejection interpretation to the three routes of Papers #46 and #48 → four-fold coincidence established.

**Structural Ultraviolet Cutoff.** Re-absorption of an ejected fragment constitutes the 0-Sphere counterpart of a QED self-energy loop. Because n is bounded above by n_max (Compton-scale well geometry), the self-energy sum is naturally finite — a structural Debye-type cutoff requiring no regularization.

**Quantum Harmonic Oscillator Reinterpretation.** E_n = (n + 1/2)ℏω is reproduced identically: n counts external photons absorbed; zero-point energy is algebraically fixed by the quartic kernel structure. Empirical predictions unchanged.

**ZB-Driven Cascade and Cooling.** The cascade n → n−1 → ··· → 0 provides a microscopic origin of cooling of isolated matter. Gravity is proposed as the macroscopic consequence of neighboring subsystems exchanging ejected fragments and drifting toward phase synchronization.

### Open Tasks (10 items)

| # | Question | Status |
|---|---|---|
| (i) | Quantitative ejection probability | Qualitative threshold; rate model pending |
| (ii) | Spherical harmonic mode assignments for n | Open conjecture |
| (iii) | 1/r² long-range scaling | Inherited from #34 |
| (iv) | Equivalence principle in composite systems | Scaling argument; derivation pending |
| (v) | Relation to general relativity (metric emergence) | → addressed in #51 |
| (vi) | Rank-2 tensor proof for ejected fragment | Physical mechanism established; tensor structure open |
| (vii) | Re-excitation dynamics and Planck spectrum recovery | Open |
| (viii) | Quantitative Thomas-precession outward stress | Geodesic geometry and force mapping pending |
| (ix) | Quantitative determination of n_max | Existence proved; value requires v_ZB(n) derivation |
| (x) | Coupling between internal ZB modes and atomic Coulomb potential | New open question |

### Relation Chain

Is supplement to #34 + #48 · Continues #34 + #46 + #48 · Requires #1 + #19 + #33 + #34 + #46 + #48 · References #32 (UV cutoff context), #35 (gravitational network)

---

## Paper #50: Rotation from Scalar Oscillation: Emergence of Photon-Sphere Angular Momentum, Chirality, and Helicity from Phase-Staggered Kernel Dynamics in the 0-Sphere Model

**Date:** 2026-04 · **DOI:** 10.5281/zenodo.19482145 · **Type:** Research Paper

### Core Concept

Establishes that angular momentum, chirality, and helicity all emerge from the scalar phase dynamics of the two-kernel system. The central mechanism is phase-staggered kernel oscillation: when oscillators on the unit circle have staggered phases, their combined centroid traces a rotation whose orientation is determined geometrically. The Lorentz-invariant chirality χ = sign(da/dt) provides the geometric origin of the electron/positron distinction.

### Phase-Staggered Oscillator Array → Angular Momentum

Centroid of N oscillators with phases staggered by 2π/N traces a circle of radius 1/2 (AM-GM bound: u + v = 1 → |r| ≥ 1/2), identical to the kernel energy floor E₀/2 of Paper #46. The active (bright-star) kernel traces the unit circle; the centroid minimum establishes the structural identity between spatial geometry and thermal PE.

### Key Equations and Results

```
Chirality (Lorentz-invariant):  χ := sign(da/dt)
  χ = +1: phase advancing → CCW rotation in yz-plane (electron)
  χ = −1: phase retreating → CW rotation (positron)

Helicity (frame-dependent):     h := χ · sign(p_x)
  Lorentz boost along x reverses sign(p_x), flips h, leaves χ invariant

Centroid lower bound:           |r_centroid| ≥ 1/2  (AM-GM ↔ E₀/2)

Flip-impossibility at m → 0:
  v_ZB = c√(1 − γ^{−2}), γ = 1 + a_e → v_ZB → 0 as m → 0
  → χ-flip energetically forbidden → massless particles have fixed helicity

DOF audit:  χ × spin = 2 × 2 = 4  (matches Dirac spinor)
  ω_A ≠ ω_B (neutrino): genuine 2 internal DOF
```

### Thomas Precession Justification

Delegated to Paper #49 (Tomonaga framing). The yz-plane rotation is driven by the radiation gradient F = E₀sinθ via Thomas precession; used here without re-derivation.

### What the Model Can and Cannot Derive

**Can:** χ as Lorentz-invariant binary; h = χ·sign(p_x) decomposition; centroid ≥ 1/2; flip-impossibility at m → 0; DOF count 4 = χ × spin.

**Cannot (open tasks):** Covariant rotation-plane definition (yz fixed for x-propagation); v_ZB from first principles (inherited from #10); neutrino Lissajous-helix for ω_A ≠ ω_B.

### Relation Chain

Continues #49 + #48 + #24 · Requires #1 + #49 + #10 + #24 · References #46 (AM-GM identity) · Is part of #49

---

## Paper #51: Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of the Spacetime Metric in the 0-Sphere Model

**Date:** 2026-04-12 · **DOI:** 10.5281/zenodo.19489126 · **Type:** Research Paper

### Core Concept

Extends the two-dimensional chirality analysis of Paper #50 to three dimensions, derives confinement as a geometric theorem via the Bonnet–Myers theorem, and proposes the spacetime metric as the second functional derivative of the phase accumulation functional — identified as a generalized Synge world function. Arcwise connectivity of the photon sphere is established as the rigorous prerequisite for the fixed-endpoint line integral.

### Three-Dimensional Helical Trajectory

```
x(τ) = v_pitch · τ,   y(τ) = cos(ω_ZB τ),   z(τ) = sin(ω_ZB τ)

Two velocity scales (no free parameters):
  v_ZB   ≈ 0.04c   (transverse)  from γ = 1 + a_e
  v_pitch ~ c      (longitudinal) from Δx ~ λ_C and ω_ZB
  Ratio: v_pitch / v_ZB ≈ 25   (breaks Dirac–Hestenes uniform-speed assumption)

ZB frequency: ν_ZB = v_ZB / λ_C ≈ 5.0 × 10¹⁸ Hz  (X-ray, vs Dirac gamma-ray)
```

### Arcwise-Connectivity Chain (Logical Prerequisites)

```
S⁰ = {A, B} not arcwise connected
  → no line integral ∫_A^B A_μ dx^μ possible in S⁰ alone

S^n (n ≥ 1) arcwise connected → photon sphere supplies minimal embedding

Ric ≥ K ~ λ_C^{−2}  →  Bonnet–Myers:  diam(S^n) ≤ π λ_C
  → confinement domain D of #33 derived as theorem (not assumption)

Energy floor E₀/2 (#46):  |x_A − x_B| > 0  (arc-length collapse prevented)
  Combined:  0 < |x_A − x_B| ≤ π λ_C

A, B non-antipodal on S^n → unique thermal geodesic
  → S(x_A, x_B) is a well-defined two-point functional
```

### Phase Accumulation Functional and Metric Emergence

```
S(x_A, x_B) := ∫_{Γ_ext} A_μ dx^μ   (Berry connection, unique helical arc)

Synge identification:
  S(x_A, x_B)  ↔  σ(x_A, x_B)   (Synge world function)
  S(x, x) = 0,   S(x_B, x_A) = −S(x_A, x_B)

Symmetrized:  S_s = (1/2)[S(x_A,x_B) + S(x_B,x_A)]

Metric proposal:
  g_μν(x) = ∂_{Aμ} ∂_{Bν} S_s(x_A, x_B) |_{x_A = x_B = x}

Flat-space check:  A_μ = const → S ∝ L(x_A,x_B) → g_μν = η_μν  ✓

Observer duality:
  g_internal = 2  (co-rotating frame; Dirac value, exact)
  g_external = 2(1 + a_e)  (lab frame; a_e as relativistic observation effect)
```

### Status of Metric Proposal

| Item | Status |
|---|---|
| S satisfies Synge axioms | ✓ Established |
| Flat-space limit: η_μν recovered | ✓ Established |
| Synge reconstruction theorem applies | ✓ Established |
| Existence and uniqueness of Γ_ext | ✓ Established (§3) |
| Explicit ∂_A ∂_B S_s beyond flat space | △ Open |
| Bridge equation F_μν ↔ R^ρ_{σμν} | △ Open |

### What the Model Can and Cannot Derive

**Can:** Helical trajectory with two scales; arcwise-connectivity prerequisites; confinement domain D as theorem (promotes #33 assumption); kernel separation bounds 0 < |x_A − x_B| ≤ π λ_C; S(x_A,x_B) as generalized Synge world function; metric proposal; flat-space consistency; g_internal = 2 vs g_external = 2(1+a_e).

**Cannot (open tasks):** Explicit mixed second derivatives beyond flat-space; bridge equation F_μν ↔ R^ρ_{σμν}; covariant rotation-plane (inherited from #50); v_ZB from first principles (inherited); neutrino Lissajous helix; positive Ricci curvature K ~ λ_C^{−2} from ZB dynamics (currently modeling postulate).

### Relation Chain

Is supplement to #50 · Continues #50 + #29 + #30 + #31 + #40 · Requires #50 + #29 + #31 + #33 + #24 + #1 · References #46 (energy floor → lower bound), #36 (non-perturbative scope) · Is part of #50

---

## Cross-Paper Connections (Group 06)

**From Group 05 AMM arc (#10→#35→#36→#47) to #48:**
#47 established ΔL=|γ_L−1|×L₀; #48 embeds this into the U(1) fiber bundle as γ_anomalous = a·2π.

**From Group 03 Berry phase arc (#26) to #48:**
#26 established Berry phase → spin; #48 formally proves the U(1) bundle and holonomy γ_intrinsic = π.

**Zero-point energy four-fold coincidence (#32→#46→#48→#49):**
#32 dissolved QFT vacuum energy; #46 gave geometric origin of 1/2ℏω; #48 adds centroid geometry route (triple coincidence); #49 adds ejection threshold (four-fold coincidence).

**From #34 gravitational program to #49:**
#34 left the mediating quantum unspecified. #49 closes all three open questions (mediating quantum, ejection mechanism, near-neighbor character).

**From #48 spin-2 candidate to #49:**
#48 requested independent physical ejection mechanism; #49 provides it. Rank-2 tensor proof remains open.

**From #49 Thomas precession to #50 chirality:**
#49 established the rotation mechanism (radiation gradient → Thomas precession → Ω_T). #50 identifies the rotation orientation sign(da/dt) as the Lorentz-invariant chirality χ, and separates it from the frame-dependent helicity h = χ·sign(p_x).

**From #50 planar rotation to #51 helix and metric:**
#50 analyzed the 2D transverse plane. #51 adds the longitudinal advance (v_pitch ~ c), derives confinement via Bonnet–Myers (promoting #33's assumption to theorem), and extracts the spacetime metric from the phase accumulation functional.

**Line-integral program culmination (#29→#30→#31→#51):**
#29 established the open-arc spinorial integral; #30 conservation laws as geometric conditions; #31 demonstrated universality. #51 is the culmination: helical extension + g_μν from ∂_A ∂_B S_s.

---

## Citation Format

```
Hanamura, S. (2026). [Title]. Zenodo. https://doi.org/10.5281/zenodo.[ID]
```

| # | Short Title | Zenodo DOI |
|---|---|---|
| 48 | g=2 U(1) Fiber Bundle / Dual-Frame | 10.5281/zenodo.19227518 |
| 49 | Photon-Sphere Fragmentation / Gravitational Mediator | 10.5281/zenodo.19393391 |
| 50 | Rotation from Scalar Oscillation / Chirality & Helicity | 10.5281/zenodo.19482145 |
| 51 | Helical Trajectory / Fixed-Endpoint Line Integral / Metric | 10.5281/zenodo.19489126 |

---

**Last Updated:** 2026-04-12
**Papers Covered:** #48–#51 (4 papers)
**Time Period:** March–April 2026
**Thematic Arc:** Fiber bundle formalization · U(1) holonomy proof · Dual-frame g-factor · Foucault analogy · Triple/quadruple coincidence · Gauge symmetry correspondence · Thomas-precession ejection · Photon-sphere fragment as gravitational mediator · Geometric UV cutoff · Angular momentum from scalar oscillation · Lorentz-invariant chirality · Frame-dependent helicity · Three-dimensional helix · Arcwise connectivity · Bonnet–Myers confinement as theorem · Spacetime metric from Berry connection
