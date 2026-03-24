================================================================================
A Supplementary Correction to the 0-Sphere Model:
Dimensional Consistency of G and c^2
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: September 23, 2025

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the above paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-1, APS format)
   - Document class: revtex4-1 (reprint, aps)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-1, graphicx, dcolumn, bm, hyperref, braket, caption,
    threeparttable, breqn, microtype, ragged2e, booktabs

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

This paper re-examines recent attempts to incorporate general relativistic
corrections into the description of lepton Zitterbewegung. A dimensional
inconsistency in the application of geodetic precession led to spurious claims
of a finite muon critical radius.

When the correct G and c^2 factors are restored, geodetic precession becomes
negligible at quantum scales (~10^-52 rad per orbit), leaving the critical
radius undefined. Thomas precession is then explored as an alternative: it
yields a nonzero correction (~10^-3 rad) but cancels its radius dependence,
also eliminating the notion of a critical radius.

Key topics include:
- Dimensional error in geodetic precession: omission of G/c^2 factor
- Correct geodetic formula: Delta_phi ~ 3*pi*G*M/(c^2*R) ~ 2.35e-34 rad at quantum scales
- Dimensionally consistent critical radius: R_crit ~ 2.55e-52 m (physically irrelevant)
- Thomas precession: Delta_phi_T = 2*pi*(gamma^2/(gamma+1))*beta^2 (radius-independent)
- Combined SR + Thomas: L/L0 = 1.000823 > 1 (no critical radius)
- Gravitomagnetic and semiclassical backreaction as possible future directions

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper is a supplementary correction to:

Primary target of correction:
  "Bridging Quantum Mechanics and General Relativity: A First-Principles
  Approach to Anomalous Magnetic Moments and Geodetic Precession" (#14)
  Zenodo (2025). DOI: 10.5281/zenodo.17765097

This paper corrects a dimensional inconsistency in #14 where G/c^2 factors
were omitted from the geodetic precession formula, leading to an overestimation
of the GR correction by ~27 orders of magnitude and a spurious muon critical
radius at 3.4e-25 m.

Version history of this paper:
  ver.1: DOI: 10.5281/zenodo.17149017
  ver.2: DOI: 10.5281/zenodo.17765448
  ver.3 (this file): DOI: 10.5281/zenodo.18636509  [September 23, 2025]

Other foundational references:
  "A Model of an Electron Including Two Perfect Black Bodies" (#1)
  Zenodo (2018). DOI: 10.5281/zenodo.16759284

================================================================================
KEY RESULTS
================================================================================

What this paper establishes:
- The muon critical radius reported in earlier work (#14) is not supported
  once correct G/c^2 factors are restored
- Geodetic precession at quantum scales: ~10^-52 rad (negligible)
- Dimensionally correct critical radius: R_crit ~ 2.55e-52 m (unphysical)
- Thomas precession magnitude: ~2 x Delta_phi_SR (correct order), but
  radius-independent -- cannot define critical radius
- Neither geodetic nor Thomas precession yields a meaningful instability
  scale for the muon

What remains open:
- Gravitomagnetic contributions from T_{0i} components may reintroduce
  R-dependence; requires controlled evaluation of linearized Einstein eqs.
- Semiclassical approach: computing <T_{mu nu}> for the oscillatory field
  configuration as source of linearized gravity

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Zitterbewegung and geodetic precession; motivation for the correction
  - Summary of dimensional error and its consequences

Section 2: Motivation
  - Full geodetic formula and its evaluation at muon mass/quantum scale
  - Result: ~10^-52 rad (negligible); previous claim of 3.4e-25 m unfounded

Section 3: Analysis and Alternatives
  - SR Lorentz contraction angle deficit
  - Thomas precession as natural alternative
  - Combined L/L0 = 1.0008 > 1: no critical radius

Section 4: Analysis and Detailed Derivations
  4.1 Special-Relativistic Angle Deficit (Lorentz Contraction)
  4.2 Geodetic Precession -- Correct Dimensional Form and Numerical Magnitude
  4.3 Thomas Precession: Derivation and Consequences
      - Exact: Omega_T = (gamma^2/(gamma+1)) * (v x a)/c^2
      - Crucial r-cancellation: Delta_phi_T = 2*pi*(gamma^2/(gamma+1))*beta^2
  4.4 Numerical Evaluation: SR vs Thomas for Electron and Muon
  4.5 Angle-Linear Composition and the Critical-Radius Condition
  4.6 Discussion of the Implication
  4.7 Paths Not Taken: Gravitomagnetism and Semi-Classical Backreaction

Section 5: Conclusion

Author's Note
  - Role of AI (ChatGPT 5.0) in identifying the dimensional error
  - Statement of independent authorship

Appendices:
  - (none)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "A Supplementary Correction to the 0-Sphere Model:
  Dimensional Consistency of G and c^2,"
  Zenodo (2025).
  https://doi.org/10.5281/zenodo.18636509

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 3.0 (September 23, 2025) [DOI: 10.5281/zenodo.18636509]
  - Current release
  - Comprehensive derivations of SR, geodetic, and Thomas precession angles
  - Full numerical evaluations for electron and muon (beta = 0.040472 / 0.040581)
  - Subsection structure with detailed angle-linear composition analysis
  - Discussion of gravitomagnetic and semiclassical alternatives

Version 2.0 [DOI: 10.5281/zenodo.17765448]
  - Intermediate revision

Version 1.0 [DOI: 10.5281/zenodo.17149017]
  - Initial release

================================================================================
ACKNOWLEDGMENTS
================================================================================

The dimensional inconsistency corrected in this paper was identified with
the assistance of ChatGPT 5.0 during a dimensional review. Earlier AI models
had not identified this issue.

The author acknowledges the use of large language models (LLMs) for
discussions, verification of dimensional consistency, and highlighting
potential gaps in the theoretical framework. All physical concepts,
interpretations, and final conclusions remain the sole responsibility of
the author.

The 0-Sphere model has been developed continuously since 2018, independently
of AI assistance. This research received no specific grant from funding agencies
in the public, commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: revtex4-1, reprint mode (APS)
Note: This paper uses revtex4-1 (not revtex4-2)
Font: Computer Modern (LaTeX default)

Tables: (none)
Figures: (none)

Key equations:
  Delta_phi_geodetic = 2*pi[1 - sqrt(1 - 3GM/(c^2*R))]    [Eq. 2.1]
  Delta_phi_SR = pi*(1 - 1/gamma)                           [Eq. 3.2]
  Omega_T = (gamma^2/(gamma+1)) * (v x a)/c^2              [Eq. 4.7]
  Delta_phi_T = 2*pi*(gamma^2/(gamma+1))*beta^2             [Eq. 4.9]
  R_crit = 3GM/(c^2*beta^2) ~ 2.55e-52 m  (muon)           [Eq. 4.5]

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

Compiler Settings:
  Main document:       main.tex
  Compiler:            pdfLaTeX
  TeX Live version:    2025
  Compile mode:        Normal

================================================================================
END OF README
================================================================================
