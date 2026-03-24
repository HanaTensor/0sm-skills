================================================================================
Line Integrals as Fundamental Observables in Physics:
A Unified Principle Behind the Aharonov-Bohm Effect, Berry Phase,
and Wilson Loops
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: January 10, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the above paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-2, APS/PRB format)
   - Document class: revtex4-2 (reprint, aps, prb)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-2, graphicx, bm, physics, hyperref, caption, microtype,
    ragged2e, booktabs, amsthm, listings, xcolor

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

In conventional physics, measurable quantities are often expressed as local
tensorial fields, such as electromagnetic tensors or spacetime curvature.
However, a wide range of phenomena -- including the Aharonov-Bohm effect,
Berry phase, Wilson loops, and energy transport in the 0-Sphere model --
demonstrates that physically observable effects can depend primarily on line
integrals accumulated along trajectories, rather than on local values alone.

This work identifies a unifying principle: physical observables correspond to
holonomies of connections or accumulated geometric phases along histories.
Local tensors and curvature emerge as secondary descriptors encoding
infinitesimal properties or noncommutativity of parallel transport. In the
0-Sphere two-kernel system, energy transport is mediated by thermal gradients
and captured entirely by line integrals of scalar potentials.

Key topics include:
- Aharonov-Bohm effect as gauge holonomy without local curvature
- Berry phase as geometric accumulation in parameter space
- Wilson loops as gauge-invariant observables in non-Abelian theories
- Thermal energy gradient in the 0-Sphere two-kernel system
- Scalar-potential interpretation: A = grad(phi), phi = T_e2 - T_e1
- Hierarchical reordering: connections over curvature, histories over points
- Coherent bridge: quantum interference, gauge invariance, gravitational dynamics

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper constitutes the third part of the Line Integral Trilogy:

Part I:
  "Geometric Structure of Spinorial Phase Accumulation along Thermal Geodesics"
  Zenodo (2025). DOI: 10.5281/zenodo.18067760
  Established why line integrals are the physically appropriate geometric
  objects in the 0-Sphere framework.

Part II:
  "From Curvature to Connection: Revisiting the Geometric Origin of
  Conservation Laws" Zenodo (2026). DOI: 10.5281/zenodo.18135855
  Showed that conservation laws emerge as geometric consistency conditions
  associated with accumulated connection and proper-time structure.

Part III (this paper):
  Advances a broader synthesis across quantum, gauge, and gravitational domains.

Additional 0-Sphere Model references:
  "Quantum Oscillations in the 0-Sphere Model: Bridging Zitterbewegung,
  Geodesic Paths, and Proper Time" Zenodo (2024).
  DOI: 10.5281/zenodo.17765017

  "A Noetherian Inversion: From Einsteinian Geometry to Emergent Symmetry"
  Zenodo (2025). DOI: 10.5281/zenodo.18064535

  "Spin from Geometry: Emergence of Spin via Internal Berry Phase"
  Zenodo (2025). DOI: 10.5281/zenodo.17765409

This paper is directly continued by #32 (Dissolution of the Vacuum Energy
Problem) and #33 (Geometrical Confinement), which apply the integral-based
ontology to cosmological and topological problems respectively.

================================================================================
KEY RESULTS
================================================================================

What the model CAN establish:
- Formal unification of AB effect, Berry phase, and Wilson loops under a
  single geometric principle (line integrals of connections)
- Explicit demonstration via 0-Sphere two-kernel thermal gradient:
    grad(T_e2 - T_e1) = E_0 sin(theta)
    A = grad(phi), phi = T_e2 - T_e1
- Hierarchical reordering: connections and histories are primary;
  curvature and local fields are derived
- Conceptual bridge between quantum interference, gauge invariance, and
  gravitational dynamics without modifying existing theories

What the model does NOT claim:
- Modification of empirical predictions of QM, gauge theory, or GR
- Derivation of new numerical predictions in this paper
- Replacement of any existing theoretical framework

The framework clarifies logical hierarchy rather than proposing theoretical
replacement.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Local tensorial formulations vs history-dependent observables
  - AB effect, Berry phase, Wilson loops as motivating examples
  - Synopsis of paper structure

Section 2: Line Integrals and the Nature of Physical Observables
  - Historical separation of AB, Berry, Wilson as artificial distinction
  - Line integral as minimal geometric structure for comparison of histories
  - Reordering: from local tensors to connection-centered descriptions

Section 3: Aharonov-Bohm Effect as Holonomy Without Curvature
  3.1 Analytical Formulation
      - Phase shift: Delta_phi = (q/hbar) oint A_mu dx^mu
      - Holonomy in regions of vanishing field strength
  3.2 Partial-Path Phase and Trajectory-Dependent Accumulation
      - Internal phase structure of 0-Sphere kernel
      - Delta_phi_segment formulation with path-length difference
  3.3 Open and Arbitrary Path Segments: Continuous Holonomy
      - Delta_phi(s) = (q/hbar) integral A.dl + k integral dL
      - Primacy of open paths over closed-loop requirement

Section 4: Berry Phase and the Primacy of Adiabatic Histories
  - gamma = oint A_i(lambda) d_lambda^i (Berry connection)
  - Holonomy over closed adiabatic path in parameter space
  - History-dependence as general principle beyond adiabatic QM

Section 5: Wilson Loops and Gauge-Invariant Line Integrals
  - W(C) = Tr P exp(i oint_C A_mu dx^mu)
  - Gauge-invariant observables from non-Abelian connections
  - Global information inaccessible to local field strengths

Section 6: From Gauge Holonomy to Gravitational Geometry
  - Structural mismatch: local tensors vs extended path-based measurement
  - Connection as primitive object; curvature as derived noncommutativity
  - Reorientation toward connection-based gravitational description

Section 7: Unifying Principle: Observables as Line Integrals
  - Common principle: observable = line integral of connection along path
  - "Quantum vs classical" distinction secondary to "point vs history"

Section 8: Bridging Line-Integral Observables to Gravitational Dynamics
  8.1 Thermal Energy Gradient Caused by Two Kernels
      - T_e1 = E_0 cos^4(omega*t/2), T_e2 = E_0 sin^4(omega*t/2)
      - grad(T_e2 - T_e1) = E_0 sin(theta)
      - Thermal geodesic equation with temperature-dependent metric
  8.2 Scalar-Potential Interpretation and Line Integrals
      - A = grad(phi), phi = T_e2 - T_e1
      - Endpoint-dependent line integral: boundary-value physics
  8.3 Implications for Gravitational and Gauge Theories
      - Gravitational observables as line integrals along proper-time paths

Section 9: Re-declaration of Principles: Line Integrals as Observables
  - Shift: locality to history, point fields to path-dependent quantities
  - Logical hierarchy clarification (not theoretical replacement)

Section 10: Conclusion
  - Structural lesson: observables are history-dependent line integrals
  - AB effect, Berry phase, Wilson loops, 0-Sphere system unified

Appendices:
  - (none)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Line Integrals as Fundamental Observables in Physics:
  A Unified Principle Behind the Aharonov-Bohm Effect, Berry Phase,
  and Wilson Loops,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.18203433

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (January 10, 2026)
  - Initial release
  - Third part of the Line Integral Trilogy (#29, #30, #31)
  - Establishes line integrals as universal fundamental observables
  - Unifies AB effect, Berry phase, Wilson loops, and 0-Sphere thermal dynamics
  - Proposes hierarchical reordering: connections and histories are primary

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a limited
supportive role for textual organization during document preparation.
All physical interpretations, methodological judgments, and philosophical
commitments remain the responsibility of the author.

The 0-Sphere model has been developed and presented continuously since 2018,
and its conceptual originality is independent of the use of any recent
computational tools. The line-integral-based formulation introduced in this
work was conceived, developed, and written entirely by the author.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: revtex4-2, reprint mode (APS/PRB)
Font: Computer Modern (LaTeX default)

Tables: (none)
Figures: (none)

Key equations:
  Delta_phi = (q/hbar) oint A_mu dx^mu               (AB phase)
  gamma = oint A_i(lambda) d_lambda^i                 (Berry phase)
  W(C) = Tr P exp(i oint_C A_mu dx^mu)               (Wilson loop)
  d^2x^mu/dtau^2 + Gamma^mu_nrho(T) dx^nu/dtau dx^rho/dtau = 0
                                                       (thermal geodesic)
  grad(T_e2 - T_e1) = E_0 sin(theta)                 (thermal gradient)

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref
  - Hyperlinked bibliography and DOI links

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

================================================================================
END OF README
================================================================================
