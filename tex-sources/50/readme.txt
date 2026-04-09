================================================================================
Rotation from Scalar Oscillation: Emergence of Photon-Sphere Angular
Momentum from Phase-Staggered Kernel Dynamics in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: April 9, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for Paper #50 in the
0-Sphere Model series:

1. main.tex
   - Main LaTeX source file
   - Document class: revtex4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-2
    graphicx
    bm
    physics
    hyperref
    caption
    microtype
    ragged2e
    booktabs
    enumitem
    amsthm
    xcolor
    tikz (with libraries: arrows.meta, calc, 3d, shadings, positioning,
          decorations.pathmorphing, shapes.geometric)

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references,
      equation numbers, and hyperlinks.

Alternatively, use Overleaf with the following settings:
  - Main document: main.tex
  - Compiler: pdfLaTeX
  - TeX Live version: 2025
  - Compile mode: Normal
  - Stop on first error: ON (recommended)
  - Autocompile: ON (optional)

================================================================================
ABSTRACT
================================================================================

Spin is among the most fundamental properties of the electron, yet how purely
scalar (non-rotating) dynamics can generate it remains a foundational challenge.
Within the 0-Sphere Model, we demonstrate that angular momentum and a
Lorentz-invariant chirality emerge as collective properties of a phase-staggered
oscillator array, without any rotational degree of freedom postulated at the
level of any individual oscillator. The model's two thermodynamic kernels, A
and B, are scalar thermal potentials; no rotational degree of freedom is
postulated at the level of any single oscillator. Angular momentum is an
emergent collective property: the instantaneous locus of maximum amplitude
traces the unit circle, and the centroid of all oscillators traces a circle
of radius 1/2, linked to the zero-point energy floor of the energy identity.

The principal new results are three. First, the direction of circulation of
the photon sphere defines a Lorentz-invariant binary chi = sign(da/dt),
identified as chirality: the orientation of the continuous phase flow on S^1,
a topological invariant classified by pi_1(S^1) = Z. Second, the
frame-dependent projection of chi onto the propagation axis defines helicity h;
the helicity-flip condition is tied directly to v_ZB approximately 0.04c. Third,
the four Dirac spinor components correspond exactly to chi x spin = 2 x 2 = 4
states, with the electron/positron distinction carried by chi and the kernel
dynamics (Te_1, Te_2) forming a single continuous internal variable. Paper #47
identified three independent occurrences of 1/2 (Thomas coefficient, centroid
radius, spin quantum number) and predicted their common geometric origin would
be examined in a future paper; Section 7.4 of the present work provides that
answer: all three reflect the AM-GM constraint cos^2(theta) + sin^2(theta) = 1
acting at geometric, kinematic, and topological levels simultaneously.

Key topics include:
- Phase-staggered scalar oscillator array: bright-star locus and centroid circle
- Emergent angular momentum without circular force law
- Chirality chi = sign(da/dt) as Lorentz-invariant topological invariant
- Helicity as frame-dependent projection; helicity-flip condition
- Dirac spinor DOF audit: chi x spin = 4 states
- Three faces of 1/2 (geometric, kinematic, topological) unified via AM-GM
- Thomas precession as relativistic geometric correction, not generating principle
- Degrees-of-freedom resolution for electron and neutrino extension

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon and extends results from:

Primary references:
1. "A Model of an Electron Including Two Perfect Black Bodies" (Zenodo 2018)
   DOI: 10.5281/zenodo.16759284
   Role: Foundational energy identity and radiation gradient F(theta) = E_0 sin(theta)

2. "Coexistence of Positive and Negative-Energy States in the Dirac Equation"
   (Zenodo 2020)
   DOI: 10.5281/zenodo.17760132
   Role: 0-Sphere reinterpretation of Dirac Psi^(+/-) as Kernels A/B, extended here
         to a Lorentz-invariant theorem via chi = sign(da/dt)

3. "Redefining Electron Spin and AMM Through Harmonic Oscillation and Lorentz
    Contraction" (Zenodo 2023)
   DOI: 10.5281/zenodo.17764997
   Role: v_ZB ~ 0.04047c derived here as the kinematic controller of helicity

4. "Spin as a Real Vector: Geometric Origin of U(1) Gauge and SU(2) Periodicity"
   (Zenodo 2025)
   DOI: 10.5281/zenodo.17765238
   Role: Thomas precession vector Omega_T(t) connected to the phase stagger delta_b

5. "Spin from Geometry: Emergence of Spin via Internal Berry Phase" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765409
   Role: Berry phase -> spin mechanism; 4pi spinorial periodicity used in Sec. 5

6. "Geometric Origin of the One-Half Factor: Thermal Potential Energy Floor"
   (Zenodo 2026)
   DOI: 10.5281/zenodo.19010945
   Role: Energy floor cos^4 + sin^4 >= E_0/2 used directly in Sec. 2.3;
         centroid r = 1/2 is its spatial counterpart

7. "Rotational Lorentz Contraction as the Geometric Origin of the AMM: A Structural
    Correspondence with the Muon Lifetime Problem" (Zenodo 2026)
   DOI: 10.5281/zenodo.19120057
   Role: Three-1/2 open question first posed in #47 Sec. III.A; answered in Sec. 7.4

8. "Photon-Sphere Fragmentation as a Gravitational Mediator" (Zenodo 2026)
   DOI: 10.5281/zenodo.19393391
   Role: Arc-curvature of thermal geodesic justifies v x a != 0; used as input in Sec. 5

This paper introduces new results not present in any prior work:
- The emergent rotation of the bright-star locus from scalar oscillations (Sec. 2)
- The centroid circle r = 1/2 as the spatial counterpart to the energy floor (Sec. 2.3)
- Chirality chi = sign(da/dt) proved Lorentz-invariant via pi_1(S^1) = Z (Sec. 6.2)
- Helicity as observed rotation in the yz-plane; flip condition tied to v_ZB (Sec. 6.3)
- DOF audit: chi x spin = 4 = Dirac spinor dimension (Sec. 7.6)
- Unification of three 1/2 factors via common AM-GM constraint (Sec. 7.4)

================================================================================
KEY RESULTS
================================================================================

What the model CAN establish:
- Chirality chi = sign(da/dt) is topologically protected: orientation of S^1 phase
  flow, classified by pi_1(S^1) = Z, immune to Lorentz boosts
- Centroid of the phase-staggered oscillator array traces a circle of radius 1/2;
  this circle cannot collapse to zero (AM-GM constraint)
- Angular momentum from scalar potential gradient via transverse force in mode-space
- Thomas precession provides the relativistic window through which the internal
  topological structure becomes observable; net torque averages to zero per cycle
- Four Dirac spinor components = chi (2 values) x spin (2 values) = 4 states
- Kernel A/B pair is a single internal variable (one real phase theta), not two DOF
- Three 1/2 factors share the common algebraic root cos^2(theta) + sin^2(theta) = 1

What the model CANNOT currently establish:
- Forward derivation of v_ZB from Thomas precession independently of measured a_e
  (inverse route only: a_e -> v_ZB, as in Paper #10)
- Covariant formulation of the rotation plane for arbitrary propagation direction
  (the yz-plane assignment in Sec. 6 is frame-specific; companion paper #52)
- Algebraic isomorphism between chi = sign(da/dt) and the gamma^5 eigenvalue
  (structural analogy established; full isomorphism remains open)
- Quantitative radiation spectrum or superradiant amplification factors
  (outside the non-perturbative framework; see Sec. 7.6 scope note)
- Derivation of v_ZB = f(m_e) from first principles within the 0-Sphere framework
- K.E.(t) >= 0 guarantee for neutrino case (omega_A != omega_B): open constraint

The model's central quantitative prediction v_ZB ~ 0.04047c (from gamma(v_ZB) = 1 + a_e,
Paper #10) is used throughout as an established result and is not re-derived here.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  1.1 Relation to prior work and scope of new results (Table 1)

Section 2: Geometric Construction — The Phase-Staggered Oscillator Array
  2.1 Phase Evolution of the Oscillator Array (Fig. 1, n = 12, four phases)
  2.2 The bright-star locus (unit circle)
  2.3 The centroid locus and the 1/2 circle (Fig. 2, annotated frame)

Section 3: Angular Momentum from a Scalar Potential Gradient
  3.1 The apparent paradox
  3.2 Resolution: transverse force component in the mode-space
  3.3 Torque from the gradient (zero net torque over one revolution)

Section 4: Connection to E_0 and the Fourth-Power Structure
  4.1 The two-layer hierarchy (linear geometry vs. thermodynamic energy)
  4.2 Why the linear picture suffices for the angular momentum argument

Section 5: Thomas Precession as the Physical Origin of the Phase Stagger
  5.1 Thomas precession: rotation from sequential boosts
  5.2 Mapping Thomas precession onto the phase stagger
  5.3 Scalar source, rotational output: the Thomas mechanism (three steps)

Section 6: Chirality, Helicity, and the Electron-Positron Distinction
  6.1 Spatial setup: three planes, three roles (propagation x, rotation yz)
  6.2 Chirality: geodesic orientation (Lorentz invariant) (Table 2)
  6.3 Helicity: observed rotation in the yz-plane; Fig. 3 (electron/positron)
  6.4 Helicity flip and the v_ZB ~ 0.04c prediction
  6.5 Summary: chirality and helicity in 0-Sphere vocabulary

Section 7: Physical Interpretation
  7.1 Emergent circular motion
  7.2 Relation to Zitterbewegung
  7.3 Origin of the phase staggering
  7.4 Energy scale and internal dynamics
  7.5 Chirality and particle-antiparticle structure
  7.6 Summary of the physical picture

Section 8: Discussion
  8.1 Summary of the mechanism (five-step chain)
  8.2 Relation to the energy-identity companion paper (#46)
  8.3 On the suppression of visual intuition by the fourth power
  8.4 The three faces of 1/2 in the 0-Sphere Model (Table 3)
  8.5 Open questions (assessment table, Table 4)
  8.6 Degrees-of-freedom audit: why the reinterpretation does not require extra states

Section 9: Outlook

Acknowledgments
Bibliography (19 references: 14 Zenodo DOIs + 2 external textbooks +
             1 DOI pending #49 + 1 future paper #52 + Dirac 1928)

Appendix A: Dirac equation — four-component spinor structure and 0-Sphere reinterpretation
  A.1 Matrix form and four-component spinor
  A.2 At-rest solutions (p = 0)
  A.3 Plane-wave solutions (p != 0)
  A.4 Phase-momentum correspondence (4pi repeat structure)
  A.5 Three-layer reinterpretation (Table A.1)

Appendix B: Record of reasoning
  B.1 Purpose
  B.2 The degrees-of-freedom audit (resolution of apparent 6-DOF problem)
  B.3 The PMNS matrix: examined and rejected as a tool for the neutrino extension
  B.4 On the frequency ratio omega_A/omega_B: rational, irrational, sterile neutrino
  B.5 Summary table: DOF claims, status, and future tasks (Table B.1)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Rotation from Scalar Oscillation: Emergence of Photon-Sphere Angular
   Momentum from Phase-Staggered Kernel Dynamics in the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.[FILL: ID after pre-registration]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (April 9, 2026)
  - Initial release
  - New result: emergent angular momentum from phase-staggered scalar oscillators
  - New result: chirality chi = sign(da/dt) as Lorentz-invariant topological invariant
  - New result: helicity as frame-dependent projection; flip condition tied to v_ZB
  - New result: DOF audit chi x spin = 4 = Dirac spinor dimension
  - Answers open question of Paper #47: three faces of 1/2 share common AM-GM origin
  - Appendix B provides explicit record of reasoning for future extension work

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a limited
supportive role for textual organization and TikZ figure preparation during
document preparation. All physical interpretations, methodological judgments,
and philosophical commitments remain the responsibility of the author.

The scientific content, conceptual framework, and theoretical interpretations
presented in this document were conceived and developed by the author, who
assumes full responsibility for all claims and interpretations herein.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: revtex4-2 (reprint, APS/PRB format)
Page layout: REVTeX 4-2 default (two-column reprint)
Compiler: pdfLaTeX

TikZ figures (all generated from macros in the preamble):
  Fig. 1 — Four-panel phase-staggered oscillator array (oscframeSM macro, n=12)
  Fig. 2 — Annotated single frame a=30 degrees (oscframeanno macro)
  Fig. 3 — Photon-sphere rotation in yz-plane, electron and positron (yzplane macro)

Tables:
  Table 1 (tab:contributions)    — Map of contributions: prior series versus this paper
  Table 2 (tab:chiralhelicity)   — Chirality and helicity: QFT vs. 0-Sphere Model
  Table 3 (tab:assessment)       — Assessment of the chirality-helicity correspondence
  Table A.1 (tab:dirac_reinterpret) — Three-layer reinterpretation of the Dirac spinor
  Table B.1 (tab:dof_summary)    — Status of DOF claims and future research tasks

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref, indexed per section
  - Hyperlinked bibliography and DOI links

Compilation:
  - First pass: resolves most content
  - Second pass: resolves all cross-references and hyperlinks

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

If uploading to Overleaf, use these project settings:

Compiler Settings:
  Main document:       main.tex
  Compiler:            pdfLaTeX
  TeX Live version:    2025
  Compile mode:        Normal

Error Handling:
  Stop on first error: ON (recommended for debugging)
  Autocompile:         ON (optional, for real-time preview)

The document has been tested and compiles successfully with these settings.

================================================================================
END OF README
================================================================================
