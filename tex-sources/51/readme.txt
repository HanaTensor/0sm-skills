================================================================================
Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of the
Spacetime Metric in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: November 25, 2026 (version 3; v2 May 29, 2026; v1 April 12, 2026)

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the above paper (Paper #51 in
the 0-Sphere Model series):

1. main.tex
   - Main LaTeX source file (REVTeX 4-2, APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (all included in standard TeX distributions):
    revtex4-2, graphicx, bm, physics, hyperref, caption, microtype,
    ragged2e, booktabs, enumitem, amsthm, listings, xcolor, tikz

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references,
      equations, and hyperlinks.

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

This paper presents a structural reconstruction of confinement and spacetime
geometry within the 0-Sphere framework. The companion paper (Paper #50)
established that the orientation of the thermal geodesic in the internal phase
space determines the electron/positron distinction as a Lorentz-invariant
binary chi = sign(da/dt). That analysis was confined to the transverse plane;
the propagation direction entered only as an external label.

The present paper extends the picture to three dimensions. Including the
longitudinal advance of the photon sphere converts the planar rotation into a
helix carrying two physically distinct velocity scales: the transverse
Zitterbewegung speed v_ZB approximately 0.04c, anchored to the anomalous
magnetic moment through gamma = 1 + a_e, and a longitudinal pitch speed
v_pitch approximately c, set by the Compton-scale kernel separation
Delta_x approximately lambda_C. The ratio v_pitch / v_ZB approximately 25
breaks the velocity uniformity assumed in the Dirac-Hestenes helical model;
both scales are derived from the two-kernel architecture without free
parameters.

Before the line integral can be defined, its foundational prerequisites ---
existence and uniqueness of the path --- must be secured. Starting from the
non-arcwise-connectivity of S^0 = {A, B}, a positively curved photon-sphere
geometry activates the Bonnet-Myers theorem, yielding a finite diameter bound
that defines the confinement domain D of Paper #33 without introducing it as
an external assumption. Non-antipodality of the kernels on S^n then ensures
uniqueness of the thermal geodesic, making the fixed-endpoint integral a
genuine two-point functional.

The half-turn arc between Kernel A and Kernel B defines a fixed-endpoint
phase accumulation functional S(x_A, x_B). It is the sum of a dynamical part
S_dyn = omega_ZB * integral of d tau, which is symmetric under exchange of the
endpoints and does not cancel on the return trip, and a geometric part
S_geo = integral of A_mu dx^mu of the Berry connection, which is antisymmetric
and carries spin and chirality. The dynamical part is a Hamilton principal
function of the arc; its square defines a world function
sigma_S = S_dyn^2 / (2 omega_ZB^2), and Synge's reconstruction theorem gives
g_mu_nu(x) = - partial_{A mu} partial_{B nu} sigma_S(x_A, x_B) at coincidence,
which reproduces eta_mu_nu exactly in flat spacetime.

Key topics include:
- Three-dimensional helical trajectory from two-kernel architecture
- Two-velocity-scale decomposition (v_ZB transverse, v_pitch longitudinal)
- Arcwise-connectivity prerequisite (S^0 not connected; S^n supplies embedding)
- Bonnet-Myers theorem applied to photon-sphere curvature: confinement as theorem
- Non-antipodality and uniqueness of the thermal geodesic
- Berry connection line integral along helical arc
- Phase accumulation functional S = S_dyn + S_geo (dynamical + Berry phase)
- World function sigma_S = S_dyn^2 / (2 omega_ZB^2); metric g = -dA dB sigma_S
- Flat-space consistency check closed exactly (g = eta)
- g = 2 from internal vs. external observer perspective
- Relation to Dirac-Hestenes helical model and perturbative QED

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper is the second in a closely coupled pair with Paper #50, and extends
the 0-Sphere line-integral programme established in Papers #29-#31.

Primary companion and foundation:
1. "Rotation from Scalar Oscillation: Emergence of Photon-Sphere Angular
   Momentum, Chirality, and Helicity from Phase-Staggered Kernel Dynamics
   in the 0-Sphere Model" (Zenodo, 2026)
   DOI: 10.5281/zenodo.19482145  [#50 — companion paper; required reading]

2. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo, 2025)
   DOI: 10.5281/zenodo.18067760  [#29 — line-integral foundation]

3. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18819682  [#30 — conservation laws as checksum]

4. "Line Integrals as Fundamental Observables: Holonomy, Phase Accumulation,
   and the 0-Sphere Two-Kernel System" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18203433  [#31 — universality of line integrals]

5. "Thermal Geodesics in the 0-Sphere Model: Extending General Relativity
   Through Internal Thermodynamic Structure" (Zenodo, 2025)
   DOI: 10.5281/zenodo.17765349  [#24 — thermal geodesic framework]

6. "Geometrical Confinement of Energy in the 0-Sphere Model: Rest Mass,
   Zitterbewegung, and Topological Stability" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18356895  [#33 — confinement domain D]

Foundational framework:
7. "A Model of an Electron Including Two Perfect Black Bodies" (Zenodo, 2018)
   DOI: 10.5281/zenodo.16759284  [#1 — central energy identity E_0]

This paper extends the two-dimensional chirality analysis of Paper #50 to
three dimensions, derives confinement as a geometric theorem via Bonnet-Myers
(promoting an assumption of #33), and proposes the spacetime metric as the
second functional derivative of the phase accumulation functional. The
line-integral foundations of Papers #29-#31 are used without re-derivation;
the thermal geodesic framework of #24 provides the geometric setting.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive in this paper:
- Helical trajectory geometry from two-kernel architecture (no free parameters)
- Two distinct velocity scales v_ZB approximately 0.04c (transverse) and
  v_pitch approximately c (longitudinal), from independent geometric origins
- v_pitch / v_ZB approximately 25 asymmetry ratio
- Arcwise-connectivity prerequisite: S^0 is not arcwise connected;
  S^n (n >= 1) supplies the required embedding
- Confinement domain D with |D| approximately lambda_C, as a theorem via
  Bonnet-Myers (promoted from assumption in #33)
- Kernel separation bounds: 0 < |x_A - x_B| <= pi * lambda_C
- Uniqueness of thermal geodesic from non-antipodality
- Decomposition of the phase functional into a symmetric dynamical part and an
  antisymmetric Berry part (version 3)
- World function sigma_S = S_dyn^2 / (2 omega_ZB^2) (version 3)
- Metric proposal: g_mu_nu = - partial_A partial_B sigma_S at coincidence
- Flat-space consistency: g = eta exactly (closed in version 3)
- g_internal = 2 (co-rotating frame), g_external = 2(1 + a_e) (lab frame)

What the model CANNOT currently derive (open tasks):
- Curved-spacetime evaluation with a rate of the internal clock supplied by the
  internal dynamics (otherwise the construction returns the metric that
  defined the proper time)
- Physical reading of the factor beta_ZB in omega_ZB = beta_ZB m_e c^2 / hbar
- Bridge equation between Berry curvature F_mu_nu and Riemann tensor of g_mu_nu
- Covariant definition of the rotation plane (inherited from #50)
- Forward derivation of v_ZB from Thomas precession alone (inherited from #10)
- Helical geometry for the neutrino case (omega_A != omega_B; Lissajous helix)
- Derivation of positive Ricci curvature K ~ lambda_C^{-2} from ZB dynamics
  (currently adopted as geometric modeling choice)

The scope of the metric-emergence proposal is that of a structurally motivated
conjecture whose flat-space limit is verified; a complete proof in curved
spacetime is deferred to subsequent work.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Long-range motivation: derivative-order mismatch between gauge theory and GR
  - Present paper as extension of companion #50 to three dimensions
  1.1 Relation to prior work and scope of new results
      - Table 1: Map of contributions (prior series vs. this paper)

Section 2: The Three-Dimensional Helical Trajectory
  2.1 From planar rotation to helix
      - Compton-scale kernel separation; SR and GR via proper time
  2.2 Two velocity scales and the asymmetry
      - v_ZB (transverse) from gamma = 1 + a_e; v_pitch (longitudinal) from
        Delta_x ~ lambda_C; v_pitch / v_ZB approximately 25
  2.3 Radiation gradient as the helical driving force
      - Radiation gradient of the kernel potential difference,
        F(theta) = grad(T_e2 - T_e1) = E_0 sin(theta), drives longitudinal propulsion

Section 3: Fixed-Endpoint Line Integral and Phase Accumulation
  3.1 S^0 is not arcwise connected
  3.2 The photon sphere supplies arcwise connectivity
  3.3 Compton scale, Bonnet-Myers, and the confinement domain
      - Ricci curvature lower bound K ~ lambda_C^{-2}; diam(S^n) <= pi * r ~ lambda_C
  3.4 Non-antipodality and uniqueness of the thermal geodesic
      - Logical chain: S^0 not connected -> S^n embedding -> Bonnet-Myers ->
        domain D -> non-antipodal -> unique geodesic -> S(x_A, x_B) well-defined
  3.5 Berry connection on the helical path
      - A_mu from Thomas precession; distinct from Christoffel symbols
  3.6 Phase accumulation functional
      - Antisymmetry under endpoint exchange; coincidence vanishing; S_s symmetrized

Section 4: Emergence of the Spacetime Metric from Phase Accumulation
  4.1 Phase accumulation and the world function
      - Why the linear phase is not a world function (degenerate Hessian;
        Maupertuis vs. Hamilton); sigma_S = S_dyn^2 / (2 omega_ZB^2)
  4.2 Metric proposal
      - g_mu_nu = - partial_{A mu} partial_{B nu} sigma_S at coincidence
      - Chain: internal clock -> dynamical phase -> world function
        -> Synge reconstruction
  4.3 Flat-space consistency check
      - g = eta exactly
  4.4 Relation to bi-tensor approaches in quantum gravity
      - Comparison with Kothawala (2023): minimum length from internal dynamics
        vs. imposed external parameter

Section 5: Discussion
  5.1 Relation to prior line-integral work (#29, #30, #31)
      - Table 2: The line-integral program (three prior works + this extension)
  5.2 Relation to Zitterbewegung and the Dirac equation
      - ZB frequency: 0-Sphere 5.0e18 Hz (X-ray) vs. Dirac 3.93e20 Hz (gamma)
      - gamma-matrix algebra as future derivation target, not input
  5.3 Internal and external observer: g=2 and the anomalous magnetic moment
      - g_internal = 2 (co-rotating), g_external = 2(1+a_e) (lab)
      - AMM as relativistic observation effect (analogy with muon lifetime)
      - Table 3: Comparison field-theoretic (#24) vs. line-integral ontology
  5.4 Relation to perturbative QED
      - Complementary geometric interpretation of a_e; not competing numerically
      - Table 4: Hierarchy of geodesic principles

Appendix A: Record of Reasoning
  A.1 Purpose
  A.2 The arcwise-connectivity argument: why it belongs in the main body
  A.3 The two-velocity decomposition: why it is new and why it matters
  A.4 The metric proposal: status and open problems
      - Table VII: Status of the metric-emergence proposal
  A.5 The gamma-matrix algebra: the question is ill-posed as stated
  A.6 Open problems inherited from the companion paper
  A.7 Corrections in version 3
      - Table VIII: Corrections made in version 3

Appendix B: Interpretational Status of the Photon-Sphere Curvature
  B.1 Historical and physical context of the Bonnet-Myers theorem
      - Table 6: Bonnet-Myers theorem vs. geodesic focusing in GR
  B.2 The question
  B.3 Adopted position: curvature from model geometry
  B.4 Alternative A: oscillatory dynamics as origin of positive curvature
  B.5 Alternative B: effective energy density via the strong energy condition
  B.6 Physical interpretation: permissible and impermissible statements
  B.7 Summary of modeling choices
      - Table 7: Interpretational status of the photon-sphere curvature assumption

Bibliography:
  - 17 papers from the 0-Sphere Model series (#1, #10, #22, #24, #29-#31,
    #33-#34, #36-#37, #40, #46, #50, #62, #65, #66)
  - 21 external references (Synge 1960, DeWitt 1965, Christensen 1976,
    Kothawala 2023, Schrodinger 1930, Hestenes 2010, Gerritsma 2010,
    Sakharov 1968, Jacobson 1995, Berry 1984, Van Vleck 1928, Morette 1951,
    Yukawa 1954/2021, de Broglie 1925, Breit 1928, Dirac 1928, Foldy-
    Wouthuysen 1950, Newton-Wigner 1949, Dirac 1958, Fizeau 1851, Laue 1907)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of
  the Spacetime Metric in the 0-Sphere Model,"
  Zenodo (2026), version 3.
  https://doi.org/10.5281/zenodo.24521440
  (version 2: https://doi.org/10.5281/zenodo.20388056)

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 3.0 (November 25, 2026)
  - Phase accumulation functional: version 2 stated antisymmetry under
    endpoint exchange for S as a whole and took the metric from the
    symmetrized combination S_s, which then vanishes identically. Version 3
    splits S into a symmetric dynamical part S_dyn = omega_ZB * int d tau and
    an antisymmetric Berry part S_geo = int A_mu dx^mu.
  - World function: the linear phase has a degenerate mixed second
    derivative and is not a world function (Maupertuis vs. Hamilton). The
    metric is taken from sigma_S = S_dyn^2 / (2 omega_ZB^2), with the sign
    g = - dA dB sigma. The flat-space check is closed exactly.
  - The circularity of the construction in curved spacetime is stated, and
    the factor beta_ZB in omega_ZB is recorded as an open item.
  - Numerical corrections: lambda_C = h/(m_e c) = 2.426e-12 m; Dirac ZB
    frequency 2 m_e c^2 / h = 2.47e20 Hz and ratio 2/beta_ZB = 49.42 (were
    3.93e20 Hz and about 80); v_ZB = 0.040472 c via gamma_v = 1 + a_e/sqrt(2)
    (was c sqrt(2 a_e) = 0.048 c); v_pitch = lambda_C nu_C = c (was
    Delta_x * omega_ZB).
  - New Appendix A.7 and Table VIII list the corrections. New references:
    #62, #65, #66, Berry 1984, Van Vleck 1928, Morette 1951, Yukawa.
  - Self-contained: the Dirac ZB frequency from the branch gap, the status
    of the eigenvalues +-c (Breit, Foldy-Wouthuysen, Newton-Wigner, Dirac),
    the invariant speed vs. the internal speed (Fizeau), the rest-energy
    frequency nu_C (de Broglie) and the root-mean-square factor are now
    explained in the paper; #62, #65, #66 are cited as "see also".
  - Acknowledgments: the two changes of substance proposed in working
    sessions with Claude Opus 5.5 (Anthropic) are stated.
  - Unchanged: arcwise-connectivity chain, Bonnet-Myers confinement,
    two-scale decomposition of the helix, metric-emergence programme.

Version 2.0 (May 30, 2026)
  - Section 2.3 (radiation gradient as the helical driving force): the
    helical driving force is corrected to the radiation gradient of the
    kernel potential difference, F(theta) = grad(T_e2 - T_e1) = E_0 sin(theta),
    following the foundational Paper #1. The earlier expression -- the
    gradient of the photon-sphere kinetic energy -- is withdrawn.
  - Energy-identity notation aligned to the half-angle (theta/2) convention
    of Paper #1 throughout.
  - Main results are unchanged: helical trajectory, two-velocity-scale
    decomposition, Bonnet-Myers confinement, and metric-emergence proposal.

Version 1.0 (April 12, 2026)
  - Initial release
  - Three-dimensional helical trajectory from two-kernel architecture
  - Two-velocity-scale decomposition (v_ZB transverse, v_pitch longitudinal)
  - Arcwise-connectivity prerequisite (S^0, S^n, Bonnet-Myers)
  - Confinement domain D derived as theorem (promotes assumption of #33)
  - Phase accumulation functional as generalized Synge world function
  - Metric-emergence proposal: g_mu_nu from second functional derivative

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a limited
supportive role for textual organization during document preparation.
All physical interpretations, methodological judgments, and philosophical
commitments remain the responsibility of the author.

The scientific content, conceptual framework, and theoretical interpretations
presented in this document were conceived and developed by the author, who
assumes full responsibility for all claims and interpretations herein.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: REVTeX 4-2 (reprint, APS/PRB)
Compiler: pdfLaTeX / TeX Live 2025

Tables (10 total, numbered as in the compiled PDF):
  Table I    (tab:contributions51)       — Map of contributions: prior series vs. this paper
  Table II   (tab:velocity_scales)       — The two velocity scales and comparison with Dirac
  Table III  (tab:lineintegral_program)  — The line-integral program (#29, #30, #31, present)
  Table IV   (tab:ontology_comparison)   — Field-theoretic (#24) vs. line-integral ontology
  Table V    (tab:geodesic_hierarchy)    — Hierarchy of geodesic principles
  Table VI   (tab:threewaves)            — Three waves of the 0-Sphere model
  Table VII  (tab:metric_status)         — Status of the metric-emergence proposal
  Table VIII (tab:v3corrections)         — Corrections made in version 3
  Table IX   (tab:bonnet_vs_focusing)    — Bonnet-Myers vs. geodesic focusing in GR
  Table X    (tab:curvature_choices)     — Interpretational status of photon-sphere curvature

Cross-references:
  - Section labels for internal navigation
  - Equation numbering by section with \label and \ref
  - Hyperlinked bibliography and DOI links (hyperref, colorlinks=true)

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

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