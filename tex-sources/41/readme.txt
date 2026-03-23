================================================================================
A Note on Derivative Hierarchy in Gauge Theory and Gravity:
A Historical Supplement on Connection, Curvature, and Line-Integral Observables
================================================================================

Author: Satoshi Hanamura
Email:  hana.tensor@gmail.com
Date:   February 28, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for a supplementary note providing
a historical and conceptual clarification of the structural distinction between
gauge theories and general relativity:

1. main.tex
   - Main LaTeX source file (article, single file, no external figures)
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
      table numbering, and hyperlinks.

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

This supplementary note provides a historical and conceptual clarification of a
structural distinction between gauge theories and general relativity that has
remained largely implicit in the literature. Although both frameworks are
formulated using connections and curvature, the correspondence between geometric
objects and physical observables differs systematically by one derivative order.

In gauge theories, curvature is directly identified with physical forces, while
observable effects such as phase shifts arise through line integrals of the
connection. In contrast, general relativity assigns force-like significance to
the connection itself, while curvature primarily encodes mass-energy
distributions through the Einstein equations.

The purpose of this Supplement is not to modify established field equations or
propose new dynamics, but to make this derivative-order mismatch explicit and to
situate it within its historical development from Einstein to Yang-Mills. By
emphasizing line integrals and accumulated phase as a common observational layer,
the discussion clarifies how these otherwise distinct theoretical structures can
be placed on equal footing without conceptual tension.

A structural comparison of the Aharonov-Bohm effect and the Shapiro time delay
is presented in tabular form, illustrating how both arise as line-integral
observables yet differ fundamentally in their geometric and physical origins:
the Shapiro delay is reducible to local geometry accumulated along geodesics,
while the Aharonov-Bohm phase is a global topological property of the gauge
connection, irreducible to any local quantity along the paths traversed.

Key topics include:
- Derivative-order mismatch between gauge theory and general relativity
- Historical development from Einstein (1916) to Yang-Mills (1954)
- Connection vs. curvature as carriers of physical observables
- Line integrals as a missing observational layer
- Structural comparison: Shapiro delay vs. Aharonov-Bohm effect
- Position of the 0-Sphere model within this historical context
- Open question: formal classification of line-integral observables
  relative to holonomy and Wilson loops

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This Supplement builds upon and clarifies concepts from:

Primary references (formally cited):
1. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo, 2025)
   DOI: https://doi.org/10.5281/zenodo.18067760

2. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" (Zenodo, 2026)
   DOI: https://doi.org/10.5281/zenodo.18135855

3. "Line Integrals as Fundamental Observables in Physics: A Unified
   Principle Behind the Aharonov-Bohm Effect, Berry Phase, and Wilson
   Loops" (Zenodo, 2026)
   DOI: https://doi.org/10.5281/zenodo.18203433

Historical references (non-Zenodo):
4. A. Einstein, Annalen der Physik 49, 769 (1916)
5. H. Weyl, Sitzungsberichte der Preussischen Akademie (1918)
6. E. Cartan, Ann. Sci. Ecole Norm. Sup. 40, 325 (1923)
7. C. N. Yang and R. L. Mills, Physical Review 96, 191 (1954)
8. Y. Aharonov and D. Bohm, Physical Review 115, 485 (1959)
9. I. I. Shapiro, Physical Review Letters 13, 789 (1964)

This Supplement serves as a historical and conceptual companion to the three
Zenodo references listed above. It clarifies why line-integral-based approaches
are not ad hoc reinterpretations but articulate explicitly what remained implicit
throughout the development of modern field theory.

================================================================================
KEY RESULTS
================================================================================

What this Supplement establishes:
- Explicit identification of the derivative-order mismatch between gauge
  theory and general relativity as a structural principle
- Historical tracing of when and why this mismatch was normalized rather
  than examined (Einstein -> Weyl -> Cartan -> Yang-Mills)
- Line integrals as the missing observational layer common to both theories
- Three-tier structural comparison (physical, geometric, observational) of
  the Shapiro delay and Aharonov-Bohm effect, with comparison table

What this Supplement does not claim:
- No new field equations or dynamical modifications are proposed
- No unification of gauge theory and gravity at the level of symmetry
- No formal classification of line-integral observables relative to
  holonomy and Wilson loops (identified as future work in Section 9)

The contribution is interpretive rather than dynamical: making explicit a
structural distinction that was present throughout the history of modern
field theory, yet never articulated as an organizing principle.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Research Summary (unnumbered, before Section 1)
  - Plain-language overview of the derivative-order mismatch and its
    historical and conceptual significance

Section 1: Introduction
  - Motivation: derivative-order mismatch as an unspoken structural feature
  - Scope: historical and interpretive, not dynamical
  - Relation to the 0-Sphere model and prior Zenodo publications

Section 2: Historical Context and Conceptual Motivation
  - Overview of the historical trajectory from Einstein to Yang-Mills
  - Why the mismatch remained an unspoken structural feature

Section 3: Historical Perspective: From Einstein to Yang-Mills
  3.1 Einstein: Gravity as Connection, Curvature as Source
      - Christoffel symbols govern geodesics; curvature encodes sources
      - Derivative-order assignment implicit from the outset
  3.2 Weyl: The First Attempt at Unification
      - Scale connection and anticipated gauge ideas
      - Mismatch treated as problem to eliminate, not feature to preserve
  3.3 Cartan: Structural Clarity without Observational Emphasis
      - Full geometric hierarchy made explicit mathematically
      - Observational priority of line integrals left undetermined
  3.4 Yang-Mills: Curvature as Force
      - Curvature unambiguously identified with physical field strength
      - Mismatch with GR normalized rather than examined

Section 4: Why the Mismatch Remained Unspoken
  - Absence of a common observational language
  - Implicit bias toward local, differential observables

Section 5: Connection as First Derivative and Curvature as Second Derivative
  5.1 Metric, Connection, and Their Derivative Structure
      - Christoffel symbols and the geodesic equation
  5.2 Curvature as a Second-Derivative Object and Tidal Effects
      - Riemann tensor and the geodesic deviation equation
  5.3 Einstein Field Equations and the Role of Curvature
      - G_mu_nu = 8 pi G T_mu_nu; curvature encodes sources
      - Comparison with gauge field strength F_mu_nu
  5.4 Implications for Line-Integral-Based Observables
      - Why gravitational observables arise as worldline integrals

Section 6: Line Integrals as a Missing Observational Layer
  - Gauge holonomy and gravitational time dilation as shared structure
  - Extended comparison: gravitational lensing (Shapiro delay) vs.
    Aharonov-Bohm effect
  - Topological non-locality vs. geometric accumulation distinguished

Section 7: Comparative Structure of Line-Integral Observables
  - Table 1: seven-feature structural comparison of the Shapiro delay
    and the Aharonov-Bohm effect (field type, local curvature, observable,
    mathematical form, closed loop requirement, local force, origin)
  - Three-tier analysis: physical, geometric, observational levels
  - Derivative-order mismatch reappears as a distinction within the
    observational layer itself
  - Bridge to future work: holonomy, Wilson loops, formal classification

Section 8: Position of the 0-Sphere Model
  - The model articulates explicitly what remained implicit historically
  - Line-integral-based observational framework accommodates both
    gauge-theoretic and gravitational phenomena

Section 9: Conclusion
  - Summary of the derivative-order mismatch as a defining feature
  - Line integrals as missing observational layer
  - Open question: Wilson loops and holonomy vs. line-integral layer
    as future direction for formal classification

Acknowledgments (unnumbered)
Bibliography (9 references: 3 Zenodo DOIs + 6 historical)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "A Note on Derivative Hierarchy in Gauge Theory and Gravity:
   A Historical Supplement on Connection, Curvature, and
   Line-Integral Observables,"
  Zenodo (2026).
  DOI: [to be assigned upon upload]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (February 28, 2026)
  - Initial release
  - 9 sections including Section 7 (structural comparison table) and
    Section 9 (conclusion with open question on holonomy/Wilson loops)
  - Table 1: seven-feature structural comparison of Shapiro delay and
    Aharonov-Bohm effect
  - Bibliography: 9 references (3 Zenodo DOIs + 6 historical, including
    Shapiro 1964)

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
Page layout: 2.5cm margins (all sides)
Line spacing: 1.5 (onehalfspacing)
Font: Computer Modern (LaTeX default)

Tables:
  Table 1 (Section 7): Comparative structure of the Shapiro delay and the
    Aharonov-Bohm effect as line-integral observables
    (7 features x 2 cases, using tabularx + booktabs)

Cross-references:
  - \label{tab:comparison} -> \ref{tab:comparison} in Section 7 body text
  - \label{sec:conclusion} -> \ref{sec:conclusion} in Section 7 closing
  - Hyperlinked DOIs in bibliography (hyperref package)

Compilation:
  - First pass: resolves most content
  - Second pass: resolves all cross-references and hyperlinks

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
