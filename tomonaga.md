# Thomas Precession in the 0-Sphere Model: Physical Framing
# Based on Tomonaga's "The Story of Spin" (スピンはめぐる)
# Created: 2026-04-03 | Updated: 2026-04-05
# Applies to: #10, #19, #47, #48, #49, #50, #51, #52 and all subsequent papers

---

## 0. Origin: Paper #10 and the Conceptual Gap It Left Open

Paper #10 (DOI: 10.5281/zenodo.17764997) is the first paper in the series to apply the Thomas precession formula within the 0-Sphere model. Understanding what #10 did — and what it left unresolved — is essential for understanding why Papers #19 and #49 were necessary.

### What #10 established

Thomas proved that a coordinate system co-moving with an accelerating body, when observed from the lab frame, rotates with angular velocity:

    Omega = (1/2c^2) [a x v]                         [Thomas_Eq1 in #10]

The conventional spin picture uses this with constant acceleration (uniform circular motion), giving a constant Omega. #10 replaced this assumption: instead of constant acceleration, the photon sphere undergoes simple harmonic motion, so

    v(t) = cos(omega*t)      (velocity)
    a(t) = -sin(omega*t)     (acceleration, the time-derivative of v)

Substituting into the Thomas formula:

    Omega = (1/2c^2) [(-sin*omega*t) x (cos*omega*t)]
          = -(1/4c^2) sin(2*omega*t)

**Key result:** the cross product of cosine and sine produces a double-angle sin(2ωt). The angular velocity therefore has period π, half that of the displacement. This is the first derivation in the series of the doubled-periodicity structure underlying g = 2, and it explains why a single electron can take both up-spin and down-spin values over time.

### What #10 left unresolved — the "straight-line" problem

The photon sphere travels between Kernel A and Kernel B. This appears to be motion along a line. But if the motion were truly one-dimensional, then v and a would always be parallel or antiparallel, giving v × a = 0 and Omega_T = 0. No Thomas precession would occur.

#10 avoided this problem by writing v and a as scalar SHM functions (cosine and sine) without specifying their spatial directions. The calculation is mathematically correct — cosine and sine are orthogonal functions — but the physical reason why the velocity and acceleration vectors point in perpendicular spatial directions was never given. The paper implicitly assumed v ⊥ a without justifying why the A→B path curves in three-dimensional space.

This gap — why does v × a ≠ 0 for a photon sphere moving between two fixed points? — remained open from #10 through #48 and is recorded as open task (viii) in Paper #49.

### Additional error corrected in #19

In #10, Omega_T is written as a scalar, missing the unit vector ê_z. Paper #19 (DOI: 10.5281/zenodo.17765238) corrected this to the vector form:

    Omega_T(t) = -(v_0^2 * omega / 4c^2) sin(2*omega*t) * e_z

### The development chain

    #10: SHM substitution → double-angle sin(2ωt) → g=2 basis
         [PROBLEM: scalar Omega; v⊥a assumed but not explained]
      ↓
    #19: vector correction (e_z added)
         [PROBLEM: v⊥a still assumed, not derived]
      ↓
    #49: Correct causal framing established — Thomas precession arises from accelerated
         motion as kinematic inevitability; v×a≠0 is its concrete expression.
         WHY the geodesic curves (and the magnitude of curvature):
         --> OPEN TASK (item viii)
      ↓
    #50: Phase-staggered oscillator picture — angular momentum is a
         COLLECTIVE EMERGENT property; Thomas precession is the
         relativistic WINDOW making it observable, not the generator.
         Chirality χ = sign(da/dt) is the Lorentz-invariant seed.
         v⊥a is confirmed to follow from arc-curvature of geodesic
         (citing #49 as established input).

---

## 0.1 Paper #50: The Deeper Resolution

Paper #50 ("Rotation from Scalar Oscillation," companion to #49) directly addresses the question that the development chain from #10 to #49 left as an open task: how does a system of purely SCALAR (linear) oscillators produce angular momentum, and what is the physical origin of the condition v⊥a?

### The phase-staggered oscillator picture

Consider n radial oscillation axes, uniformly distributed in angle, with oscillation amplitude P_k(a) = cos(a - b_k), where b_k = kπ/n. Each oscillator moves strictly along its own radial axis — no circular motion at any individual level. Nevertheless, as the global phase parameter a increases, the locus of maximum amplitude sweeps around the unit circle: an emergent rotation from purely linear constituents.

The centroid of all oscillators traces a circle of radius 1/2 — not approximately, but exactly in the continuum limit. This 1/2 radius is the SAME constraint as the AM-GM energy floor E₀/2 established in #46: both follow from cos²θ + sin²θ = 1 under the AM-GM inequality.

### The revised role of Thomas precession (#50 Section 5 "Remark")

This is the key conceptual shift established in #50:

  OLD picture (implicit in #10→#49):
    Thomas precession GENERATES angular momentum.

  NEW picture (#50):
    Angular momentum exists as a TOPOLOGICAL INVARIANT of the S¹ phase flow,
    independently of any relativistic correction.
    Thomas precession is the RELATIVISTIC WINDOW through which this
    topologically existing angular momentum becomes observable in the lab.

  Specifically (#50 Section 7.1, item 4):
    "Thomas precession provides the relativistic geometric correction through
    which the phase-space rotation becomes observable in the laboratory frame.
    It does not generate the circular structure — that structure exists at
    the topological level of the S¹ phase flow independently of any
    relativistic correction — but it quantifies the physical scale of the
    phase stagger δb = π/n in terms of v_ZB, and it accounts for the
    accumulation of a_e per internal cycle."

  In the Newtonian limit (v_ZB/c → 0):
    - Topological structure SURVIVES: the S¹ phase flow, chirality χ,
      4π periodicity all remain
    - Relativistic quantification DISAPPEARS: Ω_T → 0, a_e → 0,
      phase stagger becomes unmeasurable externally

### Why v⊥a: the chirality connection

Paper #50 explicitly cites #49 for the v×a≠0 derivation and provides the clearest statement of its origin (#50 Series Context, L.41-46):

  "This is why Ω_T ≠ 0 for a purely linear 1D oscillator in the 0-Sphere
  Model: NOT because linear motion alone generates angular momentum (it does
  not; for a pendulum v ∥ a → Ω_T = 0), but because the arc-connected
  geodesic topology gives v ⊥ a via geometric curvature."

The deeper origin is chirality: χ = sign(da/dt), the orientation of the phase flow on S¹. When the thermal geodesic is traversed forward (A→B), da/dt > 0 and the curvature of the arc enforces a transverse acceleration component. This is the SAME geometric fact as v⊥a, viewed from the level of the phase flow rather than the instantaneous velocity vectors.

### Chirality χ = sign(da/dt): Lorentz-invariant seed

#50 defines:

    χ = sign(da/dt) = orientation of phase flow on S¹
                    = winding number sign of the directed geodesic
                    = classified by π₁(S¹) = ℤ

  χ = +1: forward geodesic A→B, Kernel A dominant, CCW rotation in yz-plane
          → electron, h = +1/2
  χ = -1: backward geodesic B→A, Kernel B dominant, CW rotation in yz-plane
          → positron, h = -1/2

χ is Lorentz invariant (Lorentz boosts preserve the orientation of directed
curves). Helicity h is the frame-dependent projection of χ onto the
propagation axis; it flips when an observer overtakes the particle.

The electron/positron distinction arises from the traversal direction, not
from any pre-assigned quantum number or charge.

### The three faces of 1/2 (#50 Section 7.4 — answering #47's open question)

Paper #47 identified three independent occurrences of 1/2 in the 0-Sphere
framework and predicted that their common geometric origin would be examined
in a future paper. Paper #50 provides that answer:

  (1) GEOMETRIC: centroid radius = 1/2
      The centroid of the phase-staggered array traces a circle of radius
      exactly 1/2. Same as the AM-GM energy floor:
      cos⁴θ + sin⁴θ ≥ E₀/2.

  (2) KINEMATIC: Thomas precession coefficient 1/2
      Ω_T ≈ (1/2)(v/c²) × a. Without this factor, predicted spin-orbit
      splitting of hydrogen would be twice the observed value.

  (3) TOPOLOGICAL: spin quantum number s = 1/2 (4π holonomy)
      A spinor returns to its original value only after 4π rotation,
      not 2π. The π-periodicity of the oscillation axis space generates
      this 4π spinorial holonomy.

  Common root: all three reflect the constraint cos²θ + sin²θ = 1 under
  AM-GM, which simultaneously:
    → prevents centroid from collapsing to origin (geometric 1/2)
    → halves effective angular velocity via Thomas mechanism (kinematic 1/2)
    → imposes π-periodicity of axis space → 4π holonomy (topological 1/2)

### 4 Dirac spinor components = χ × spin = 2 × 2

The four Dirac spinor components correspond exactly to:
  χ ∈ {+1, −1}  (chirality: geodesic direction → electron/positron)
  × spin ∈ {+1/2, −1/2}  (internal angular momentum from arc-curvature)
  = 4 states

---

## 1. Source: Tomonaga's Explanation (朝永振一郎「スピンはめぐる」)

Nobel Laureate Sin-Itiro Tomonaga's description of Thomas precession, which provides the physical foundation for how the 0-Sphere model treats Thomas precession:

---

『トーマスのやった計算は恐ろしくややこしいので、ここでお話しするにはしんどすぎます。しかしとにかく、"電子が静止していて核が回っている座標系"というのをそう簡単に扱ってはいかん、ということなのです。電子が等速運動をしているなら、そういう座標系は実験室系からローレンツ変換で簡単に与えられます。しかし電子に加速度があると面倒なことが起こる。確かに電子がじっとしている座標系は存在しています。詳しくいうと、電子の上に原点を載せながら電子と一緒に動いてゆく座標系がそれです。しかし、原点が電子と一緒に動いている、というだけでは座標系は一つに決まりません。つまりその時、x, y, z軸の向きをどうとるかが問題です。そこで、原点が電子と一緒に動いてゆく、という条件の他に、x, y, z軸が常に並行に移動してゆく、といった条件をつける必要があるでしょう。ところがこの"平行"ということは、等速運動の電子に対しては明白なのですが、電子に加速度があると、それほど明白なことではない。こういう点にトーマスは気づいたのです。

　そこでまずトーマスは、座標軸の平行な移動とは何か、ということを論じました。そして、軸の平行な移動とは、各瞬間ごとに、その瞬間での軸が無限小時間前の軸と平行になっていることだ、と結論しました。電子と一緒に動く原点を持ち、かつこの意味において並行に移動してゆく軸を持つ座標系は、電子の固有座標系とでもいうべきものです。トーマスは、この系の軸を実験室系からみると、電子に加速度があるときには、それは決して平行に移動していなくて、そこには"回転"が伴っていることを導いたのです。彼はしんどい計算をやって、固有座標系の軸が、実験室系からみると

    Omega = 1/(2c^2) [a x v]

という角速度で回転していることを見つけたのです。』

---

## 2. Core Principle (Tomonaga's Key Insight)

Thomas precession is NOT caused by the spatial path being curved. It is a kinematic inevitability of relativistic ACCELERATED motion:

  - For uniform motion: the rest frame is unambiguously given by a Lorentz transformation from the lab frame.
  - For accelerated motion: even when the coordinate axes are transported "in parallel" (each instant parallel to the infinitesimally preceding instant), the axes as seen from the lab frame are NOT in parallel transport — they rotate.
  - This rotation appears whenever v x a != 0, i.e., whenever acceleration has a component perpendicular to the velocity.

The formula:   Omega_T = -(1/2c^2)(a x v)

is the angular velocity of this rotation as seen from the lab frame.

Note on the 1D case (Tomonaga's pendulum example): for a purely rectilinear oscillator, v ∥ a at all times, so v × a = 0 and Omega_T vanishes identically. This is why a simple pendulum or a spring along a single axis produces no Thomas precession. The A→B thermal geodesic of the 0-Sphere model differs because it curves in 3D space, yielding a centripetal acceleration component perpendicular to the velocity. This is precisely the condition that #10 implicitly assumed (v = cosωt, a = -sinωt as orthogonal functions) without deriving from first principles. The quantitative justification of why this curvature exists — and what its magnitude is — remains open task (viii) of Paper #49.


## 3. Causal Chain in the 0-Sphere Model

CORRECT order (established in #49):

  [1] Radiation gradient F = E_0 sin(theta)
        --> photon sphere is continuously ACCELERATED
            throughout the A->B traversal (Paper #1)

  [2] ZB sustains this oscillation at v_ZB ≈ 0.04c (relativistic)

  [3] Because the photon sphere is perpetually accelerated at relativistic speed, Thomas precession — in the sense explained by Tomonaga — naturally arises as a structural feature of the 0-Sphere internal dynamics, rather than being introduced as an additional assumption.

  [4] The radiation gradient acts within the geometry of the internal thermal phase space:
        --> a(t) = -v_0 * omega * sin(omega*t) * e_y  (transverse)
        --> v(t) =  v_0 * cos(omega*t)         * e_x
        --> v x a = -(v_0^2 * omega / 2) sin(2*omega*t) * e_z  != 0
            (as realized in the present construction)

  [5] Substituting into Thomas formula:
        --> Omega_T = -(v_0^2 * omega / 4c^2) sin(2*omega*t) * e_z
            (established in Paper #19)

  [6] Quantitative derivation of the transverse geometry of the thermal geodesic from first principles:
        --> OPEN TASK (item viii, Paper #49 Section 7)


## 4. Anti-Pattern (AVOID this explanation order)

  WRONG:
    Path is arc-connected in 3D space
      --> thermal geodesic has geometric curvature
        --> acceleration has transverse component
          --> v x a != 0
            --> Thomas precession

  CORRECT (Tomonaga's physical interpretation):
    Photon sphere undergoes accelerated motion (radiation gradient)
      --> Thomas precession naturally arises (kinematic inevitability,
          as explained by Tomonaga): proper frame rotates in lab frame
          even under parallel-axis transport
        --> v x a != 0 expresses this concretely
          --> Omega_T = -(v_0^2*omega/4c^2) sin(2*omega*t) * e_z


## 5. Reference Implementation — Verbatim from Paper #49 main.tex

The following passages are taken verbatim from Paper #49 (main.tex v4, DOI: 10.5281/zenodo.19393391). LaTeX markup is stripped for readability; equation labels and citation keys are shown in brackets.

---

### 5-1. Introduction (Section 1, paragraph beginning L.550)

"The justification is provided by Thomas precession, understood in the sense made precise by Tomonaga [Tomonaga1997]: whenever a body undergoes *accelerated* motion in a relativistic regime, its proper coordinate frame rotates relative to the laboratory frame---even under the condition that the axes are transported 'in parallel.' This rotation is not a consequence of the spatial path being curved; it is a kinematic inevitability of relativistic accelerated motion. The angular velocity of this rotation is

    Omega_T = -(1/2c^2)(v x a),                    [eq:cross_product]

which is non-zero whenever the acceleration has a component perpendicular to the velocity (as realized in the present construction)."

---

### 5-2. Section 3.2.1 (sec:ejection_thomas)

"In a pure one-dimensional oscillator (e.g., a pendulum), the velocity v and acceleration a are always parallel or antiparallel; their cross product v x a = 0, and the Thomas angular velocity vanishes identically. The 0-Sphere model is categorically different: the photon sphere is continuously accelerated throughout the A->B traversal by the radiation gradient [hanamura01], and Zitterbewegung sustains this oscillation at v_ZB ≈ 0.04c. Because the photon sphere is perpetually accelerated at relativistic speed, Thomas precession---in Tomonaga's sense [Tomonaga1997]---naturally arises as a structural feature of the 0-Sphere internal dynamics, rather than being introduced as an additional assumption. The radiation gradient acts within the geometry of the internal thermal phase space; the resulting acceleration

    a(t) = -v_0 * omega * sin(omega*t) * e_y

is transverse to the instantaneous velocity

    v(t) = v_0 * cos(omega*t) * e_x,

so that their cross product is non-zero (as realized in the present construction):

    Omega_T(theta) = -(v_0^2 * omega / 4c^2) sin(2*theta) * e_z,   [eq:thomas_AV]

generates angular momentum throughout the A->B traversal. Because v_ZB ≈ 0.04c, the factor v_0^2/c^2 ≈ 1.6 x 10^{-3} is small but non-negligible---a purely Newtonian oscillator at the same frequency would produce no such term. This angular momentum---a kinematic consequence of the radiation-gradient-driven ZB acceleration, not of circular rotation---is here interpreted as giving rise to an outward centrifugal-like stress on the photon-sphere structure, peaking where |Omega_T| is extremal. The quantitative derivation of the transverse geometry of the thermal geodesic from first principles is an open task recorded as item (viii) in Section 7."

---

### 5-3. Key Phrases Established in Paper #49

The following expressions are canonical within the series from #49 onward:

  - "Thomas precession, understood in the sense made precise by Tomonaga"
    [Introduction: attribution formula]

  - "Thomas precession---in Tomonaga's sense---naturally arises as a structural feature of the 0-Sphere internal dynamics, rather than being introduced as an additional assumption."
    [Section 3.2.1: the operative claim]

  - "a kinematic consequence of the radiation-gradient-driven ZB acceleration, not of circular rotation"
    [Section 3.2.1: disambiguation from rotation]

  - "This rotation is not a consequence of the spatial path being curved; it is a kinematic inevitability of relativistic accelerated motion."
    [Introduction: the anti-pattern negation]

  - "(as realized in the present construction)"
    [Recurring phrase marking the concrete realization of the general principle]


## 6. Cross-References

  Paper #10: FIRST application of Thomas precession in the series. SHM substitution (v=cosωt, a=−sinωt) → double-angle sin(2ωt) → g=2 basis. Omega_T written as scalar (missing ê_z); v⊥a assumed but not explained. DOI: 10.5281/zenodo.17764997
  Paper #19: Vector correction (ê_z added to Omega_T). DOI: 10.5281/zenodo.17765238
  Paper #47: Thomas precession → g=2 geometric basis (double-angle, ΔL identity); three independent 1/2 factors identified (derivation of common origin deferred)
  Paper #48: π-periodicity of Omega_T → spin-2 candidate
  Paper #49: Ejection mechanism via Thomas-precession stress; Tomonaga's physical interpretation first introduced in series; open task (viii) records the missing quantitative derivation of v⊥a. DOI: 10.5281/zenodo.19393391
  Paper #50: Phase-staggered oscillator picture; Thomas precession as relativistic window (not generator) of angular momentum; chirality χ = sign(da/dt) as Lorentz-invariant seed; three faces of 1/2 unified (answering #47's open question); 4 Dirac components = χ × spin = 2 × 2
  Paper #51: Helical trajectory with two velocity scales (v_ZB transverse, v_pitch longitudinal); Bonnet-Myers confinement theorem; Synge world function identification; g_μν emergence. Thomas precession direction (ê_z) is the cross-product of the helix's two kinematic directions (ê_x and ê_y).
  Paper #52: Directional decomposition — ê_x (velocity) → gravity, ê_y (acceleration) → EM, ê_z = ê_x×ê_y → Thomas precession/spin. The ê_z assignment is ESTABLISHED from #19; the ê_x and ê_y assignments are structural proposals. Key results: (a) deterministic ZB axis drift Δφ=2πa_e per cycle from non-closing orbit; (b) turning-point asymmetry → F=mg without ensemble averaging; (c) λ_C cancellation is geometric (ê mediates both internal lever arm and external gradient); (d) a_e reinterpreted as the essential tolerance enabling a particle to interact with its environment ("hard stone → soft antenna"). Appendices A/B/C provide pedagogical derivations (equivalence principle, scanning mechanism, Ising contrast).

  global-concept.md Section B-3: Thomas precession equation index
  global-concept.md Section C-10: photon-sphere ejection thread (#34→#48→#49)


## 7. Bibliographic Reference

S. Tomonaga, "The Story of Spin," translated by T. Oka, University of Chicago Press, Chicago (1997), pp. 42-43. Originally published in Japanese as "Spin wa Meguru," Misuzu Shobo, Tokyo (1974); new ed. (2010).

Zenodo citation key: Tomonaga1997
