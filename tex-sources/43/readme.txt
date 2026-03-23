================================================================================
On Observer-Dependent Torsion, Zitterbewegung, and Phase Accumulation:
A Supplement on SU(2) Teleparallel Geometry and Conceptual Implications
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: March 7, 2026
DOI: https://doi.org/10.5281/zenodo.18896784

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the supplementary note:

1. main.tex
   - Main LaTeX source file (single-file article)
   - Document class: article, 12pt, letterpaper
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
  amsmath, amssymb, graphicx, bm, physics, authblk, setspace,
  geometry, caption, hyperref, tabularx, ragged2e, booktabs

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

This supplementary note records interpretive considerations concerning the
possible role of observer-dependent torsion and internal phase dynamics in
the context of the 0-Sphere model. The discussion is motivated by the
line-integral-based framework developed in the companion works (the main
trilogy: zenodo.18067760, zenodo.18135855, zenodo.18203433), and by its
potential implications for Zitterbewegung, phase accumulation, and the
electron anomalous magnetic moment.

Attention is drawn to the mathematical structure of teleparallel geometry
on non-Abelian Lie groups, notably SU(2), as a concrete example of a space
exhibiting vanishing curvature but nonzero torsion (Weitzenbock connection).
No additional dynamical assumptions are introduced. The purpose of this note
is to clarify conceptual consistency and to delineate a possible interpretive
extension, without altering the quantitative results or claims of the main
text. The distinction between closed-loop and open-path line integrals,
central to the main trilogy, receives detailed treatment in its relation to
teleparallel structures.

Key topics include:
- Open-path vs. closed-loop line integrals: foundational distinction
- Discrete two-kernel (S^0) structure and phase-dependent energy localization
- Zitterbewegung velocity: Dirac prediction (c) vs. 0-Sphere prediction
  (v_ZB approximately 0.04047c, from gamma(v_ZB) = 1 + a)
- Anomalous magnetic moment as observer-dependent Lorentz contraction effect
- Teleparallel (Weitzenbock) geometry on SU(2): curvature = 0, torsion != 0
- Radiation gradient as effective torsion and phase-shift generator
- Thermodynamic irreversibility encoded in open-path integrals
- Scope and cautionary remarks: interpretive, not foundational

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This supplement builds upon and clarifies concepts from the main trilogy:

Primary references (the Line Integral Trilogy):
1. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo 2025)
   DOI: 10.5281/zenodo.18067760

2. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" (Zenodo 2026)
   DOI: 10.5281/zenodo.18135855

3. "Line Integrals as Fundamental Observables in Physics" (Zenodo 2026)
   DOI: 10.5281/zenodo.18203433

Foundational framework (0-Sphere Model):
4. "A Model of an Electron Including Two Perfect Black Bodies" (Zenodo 2018)
   DOI: 10.5281/zenodo.16759284

5. "Geometrical Confinement: Rest Mass and Zitterbewegung" (Zenodo 2026)
   DOI: 10.5281/zenodo.18356895

6. "Spin from Geometry: Emergence of Spin via Internal Berry Phase"
   (Zenodo 2025)
   DOI: 10.5281/zenodo.17765409

Contextual predecessor on torsion question:
7. "A Note on Derivative Hierarchy in Gauge Theory and Gravity" (Zenodo 2026)
   DOI: 10.5281/zenodo.18809117

This supplement serves as a conceptual bridge for readers of the main
trilogy, answering two questions not addressed there: (1) the geometric
origin of the spinorial theta/2 structure in the quartic energy terms, and
(2) the explicit comparison between the 0-Sphere velocity prediction
v_ZB approximately 0.04047c and the Dirac velocity-operator eigenvalue c.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive or establish:
- v_ZB approximately 0.04047c from gamma(v_ZB) = 1 + a (no free parameters)
- SU(2) teleparallel geometry as a mathematically controlled example of
  torsion encoding non-Abelian phase information without curvature
- Open-path integrals as thermodynamically irreversible, history-dependent
  observables distinct from closed-loop gauge-invariant phase phenomena
- Anomalous magnetic moment as observer-dependent Lorentz contraction of
  the internal photon-sphere circumference
- Radiation gradient F = -grad(U) as the classical mechanical origin of
  Zitterbewegung spatial oscillation

What the model CANNOT currently derive:
- A derivation of the fine-structure constant from first principles
- A modification of the Dirac equation or general relativity
- A claim that physical spacetime carries a Weitzenbock connection
- A claim that electrons "live on" an SU(2) manifold
- Definitive identification of the electron anomalous magnetic moment
  origin (the result is interpretive, not a formal derivation)

All interpretations in this supplement are explicitly labeled as
interpretive rather than derivational, maintaining the non-speculative
standard of the 0-Sphere Model series.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Research Summary (unnumbered)
  - Overview of motivations, scope, and key distinction

Section 1: Introduction
  - Line integrals as fundamental observables (main trilogy context)
  - Observer-dependent torsion as the central question
  - Open-path vs. closed-loop as the foundational distinction

Section 2: From Closed Loops to Open Paths: A Foundational Distinction
  2.1 Conventional Phase Phenomena: Closed Contours
      - Aharonov-Bohm effect, Berry phase, Wilson loops (closed contour form)
  2.2 The 0-Sphere Framework: Open Paths as Primary
      - Three-level comparison: cyclic vs. directional, parameter space vs.
        real space, background geometry vs. emergent spacetime
  2.3 Thermodynamic Irreversibility and Open Paths
      - Contrast with AB effect; entropic entrainment mechanism

Section 3: Discrete Two-Point Structure and Phase Accumulation
  3.1 The Two-Kernel Configuration Space
      - S^0 as configuration space; phase-driven hopping analogy
  3.2 Phase-Dependent Energy Localization
      - E_A = E_0 cos^4(theta/2), E_B = E_0 sin^4(theta/2)
  3.3 The Photon Sphere as Radiative Pathway
      - On-shell photons vs. sub-luminal collective envelope
  3.4 Line Integrals Over Discrete Segments
      - Phase accumulation as sum over finite contributions

Section 4: Zitterbewegung and Observer Dependence
  4.1 The Dirac Equation and Conventional Interpretation
      - nu_ZB = 2 m_e c^2 / h ~ 1.6e20 Hz; velocity eigenvalue c
  4.2 Reinterpretation: Radiation and Absorption as Energy States
      - Positive/negative energy as absorption/emission phase
  4.3 The Anomalous Magnetic Moment as Relativistic Circulation Effect
      - gamma(v_ZB) = 1 + a; circumference deficit interpretation
  4.4 From Known a to Predicted v_ZB
      - a_exp = 0.00115965218073(28); v_ZB approximately 0.04047c
      - Unverified prediction; concrete falsifiability criterion
  4.5 Observer Dependence and Frame Dependence
      - Comoving frame: g = 2; external frame: g = 2 + 2a

Section 5: Teleparallel Geometry on SU(2)
  5.1 Mathematical Structure
      - Weitzenbock connection; R^(W) = 0; T(e_a, e_b) = -epsilon_ab^c e_c
  5.2 Interpretive Role in the 0-Sphere Framework
      - Proof of concept only; not a physical claim about spacetime

Section 6: Radiation Gradient and an Interpretive Role of Torsion
  6.1 The Radiation Gradient as Force
      - dU_A/d(theta) proportional to sin(theta); F = -grad(U)
  6.2 Energy Conservation and Kinetic Conversion
      - Delta U_A = Delta U_B + Delta E_kin; work-energy theorem
  6.3 Torsion as Phase-Shift Generator
      - Radiation gradient as effective Weitzenbock torsion (interpretive)

Section 7: Relation to Line-Integral Observables
  - Compatibility with the main trilogy formalism
  - Torsion as interpretive layer, not competing description
  - Open-path character preserved; compatibility with established phenomena

Section 8: Scope and Cautionary Remarks
  - No new fundamental field; no modification of GR
  - Teleparallel SU(2) as mathematical illustration only
  - v_ZB prediction: falsifiable without adjustable parameters

Section 9: Discussion: Significance of This Supplement
  9.1 What the Trilogy Does and Does Not Address
      - Two unanswered questions: spinorial theta/2 origin; v_ZB vs. c
  9.2 Three Conceptual Contributions
      - Physical velocity distinction; torsion as geometric language;
        open-path vs. closed-loop systematic comparison
  9.3 Who Should Read This Supplement
      - Conceptual bridge for trilogy readers; graduate-level prerequisites

Section 10: Conclusion
  - Seven key points enumerated

Appendices:
  - Acknowledgments
  - Bibliography (16 entries: 9 Hanamura Zenodo, 7 external classics)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "On Observer-Dependent Torsion, Zitterbewegung, and Phase Accumulation:
  A Supplement on SU(2) Teleparallel Geometry and Conceptual Implications,"
  Zenodo (2026).
  DOI: 10.5281/zenodo.18896784

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (March 7, 2026)
  - Initial release
  - Foundational distinction: closed-loop vs. open-path line integrals
    (Sections 2, 7, 9)
  - Explicit comparison: Dirac v_ZB = c vs. 0-Sphere v_ZB ~ 0.04047c
    (Section 4)
  - Teleparallel geometry on SU(2) as proof-of-concept for torsion without
    curvature (Section 5)
  - Radiation gradient as effective torsion / phase-shift generator
    (Section 6)
  - Comprehensive scope and cautionary remarks (Section 8)

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
Document class: article, 12pt, letterpaper
Page layout: 2.5cm margins (all sides), a4paper
Line spacing: 1.5 (onehalfspacing)
Font: Computer Modern (LaTeX default)

Tables:
  None (no floating tables in this document)

Cross-references:
  - Section labels for internal navigation (sec:twokernel)
  - Equation numbering with \label and \ref
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
