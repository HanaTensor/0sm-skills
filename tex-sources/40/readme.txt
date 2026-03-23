================================================================================
On the Derivative-Order Mismatch Between Gauge Theory and Gravity:
A Supplement on Connection, Curvature, and Line-Integral Observables
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: February 23, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the supplementary note on
derivative-order structure in gauge theory and general relativity:

1. main.tex
   - Main LaTeX source file (single-file article, 12 sections + appendices)
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
  amsmath, amssymb, graphicx, bm, physics, authblk, setspace, geometry,
  caption, hyperref, tabularx, ragged2e, booktabs

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

This supplementary note clarifies a structural distinction between gauge
theories and general relativity: the correspondence between mathematical
objects and physical quantities differs by one derivative order.

In gauge theories, curvature two-forms represent physical forces (electric
and magnetic fields), while observable phase effects arise through line
integrals of the connection. In general relativity, the connection itself
governs gravitational motion, whereas curvature relates to mass-energy
distributions through the Einstein equations.

This derivative-order mismatch does not signal an inconsistency but reflects
differing choices of which geometric objects are assigned direct physical
significance. The note systematically unpacks this frequently compressed
observation and shows how line integrals of connections provide a common
observational layer across both frameworks.

The discussion emphasizes that the 0-Sphere model naturally accommodates
this mismatch by treating line integrals between discrete points as
fundamental observables, thereby harmonizing gauge-theoretic and gravitational
descriptions at the level of accumulated phase.

Key topics include:
- Derivative-order mismatch between gauge theory and general relativity
- Physical roles of connection and curvature in each framework
- Line integrals as a unified observational layer
- Pre-divergence layer of gravitational theory
- Harmonization via the 0-Sphere model

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This supplementary note builds upon and clarifies concepts from the
Line Integral Trilogy:

1. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo, 2025)
   DOI: 10.5281/zenodo.18067760

2. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18135855

3. "Line Integrals as Fundamental Observables in Physics: A Unified Principle
   Behind the Aharonov-Bohm Effect, Berry Phase, and Wilson Loops"
   (Zenodo, 2026)
   DOI: 10.5281/zenodo.18203433

This note serves as a conceptual bridge to the trilogy by systematically
unpacking the derivative-order mismatch that motivates a line-integral-based
ontology. It does not introduce new physical results but clarifies the
geometric and interpretive context in which the 0-Sphere model operates.

================================================================================
KEY RESULTS
================================================================================

What this note establishes:
- Systematic unpacking of the derivative-order mismatch between gauge
  theory (curvature = force) and gravity (connection = force)
- Identification of line integrals as a common observational layer
  independent of this mismatch
- Clarification of the "pre-divergence layer" of gravitational theory,
  where line integrals of connections can be defined prior to any
  divergence-free requirement
- Notation clarification: Gamma as a matrix-valued one-form suitable
  for line integration, not as a local tensor field

What this note does not claim:
- No new physical predictions beyond the trilogy
- No modification of established gauge theory or general relativity
- No resolution of the mismatch (it is a structural feature, not a flaw)

The derivative-order mismatch is treated as a structural feature to be
accounted for rather than a problem to be resolved.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Research Summary (page 2)

Section 1:  Introduction
  - Motivation for clarifying the derivative-order mismatch
  - Relation to the Line Integral Trilogy

Section 2:  Forces and Potentials in Classical Field Theory
  - Hierarchy of potentials and forces; Aharonov-Bohm background

Section 3:  Gauge Theory: Connection and Curvature
  - Vector potential as connection; F_munu as curvature and physical force
  - Global phase effects via line integrals

Section 4:  Einstein's Reformulation of Gravity
  - Metric tensor as gravitational potential; geometric interpretation

Section 5:  Connection and Motion in General Relativity
  - Geodesic equation; connection as force-like object
  - Cartan's reformulation

Section 6:  Curvature and Source in Gravitational Theory
  - Einstein field equations; curvature as source quantity

Section 7:  Derivative-Order Mismatch
  - Explicit statement of the mismatch; Table 1 summary
  - Local vs. global observational hierarchy in gauge theory

Section 8:  Harmonization via Line Integrals in the 0-Sphere Model
  - Phi = integral_gamma omega as common observational framework
  - Discrete two-point structure; conceptual and interpretive harmonization

Section 9:  Implications for Line-Integral-Based Interpretations
  - Accumulated phase as primary observable
  - Coherent framework across derivative-order levels

Section 10: Line Integrals and the Pre-Divergence Layer of Gravitational Theory
  - Historical context of Einstein's divergence-free construction
  - Pre-divergence layer: line integrals prior to local field equations

Section 11: Remark on Connection Notation and Line Integrals
  - Gamma as matrix-valued one-form; omega notation
  - Distinction between local coefficients and geometric one-form

Section 12: Conclusion

Appendices:
  - Acknowledgments
  - Bibliography (9 references)

Tables:
  - Table 1: Observational Roles of Connection and Curvature in Gauge
    Theory and Gravity (derivative-order summary)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "On the Derivative-Order Mismatch Between Gauge Theory and Gravity:
  A Supplement on Connection, Curvature, and Line-Integral Observables,"
  Zenodo (2026).

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (February 23, 2026)
  - Initial release
  - Systematic clarification of derivative-order mismatch
  - Introduction of pre-divergence layer concept
  - Notation section on connection one-forms and line integrals
  - Table summarizing connection/curvature roles in both frameworks

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
  Table 1: Observational Roles of Connection and Curvature in Gauge Theory
           and General Relativity (table*, full-width, top of page)

Cross-references:
  - Section labels for internal navigation
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
