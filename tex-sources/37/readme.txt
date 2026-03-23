================================================================================
Reinterpreting Gravitational Potential Energy
as an Internal Line-Integral Quantity in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: February 14, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for a theoretical physics paper
reinterpreting gravitational potential energy within the 0-Sphere model
framework:

1. main.tex
   - Main LaTeX source file (full manuscript with appendix)
   - Document class: revtex4-2 (APS Physical Review B format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
  graphicx, bm, physics, hyperref, caption, microtype, ragged2e,
  booktabs, amsthm, listings, xcolor, tikz

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

Gravitational potential energy is conventionally treated as a scalar function
assigned to spatial positions in classical mechanics and general relativity.
While operationally successful, this representation leaves unresolved the
ontological question of where such energy physically resides. This paper
proposes a reinterpretation within the 0-Sphere model framework in which
gravitational potential energy is not attributed to space itself, but instead
emerges from internal degrees of freedom of matter. These internal degrees are
geometrically described by a connection and accumulated through a line integral
along the particle's worldline.

Within this integral-based formulation, free fall is reinterpreted as the
geodesic evolution of internal phase history. A characteristic internal
oscillation velocity, v_ZB approximately 0.04047c, is uniquely determined from
the experimental value of the electron's anomalous magnetic moment without
adjustable parameters. The predicted gravitational redshift of the internal
oscillation frequency is numerically identical to the standard
general-relativistic result. The novelty lies not in modifying empirical
predictions, but in relocating gravitational potential energy from an abstract
spatial scalar field to accumulated internal phase evolution, providing an
internal dynamical ontology underlying the familiar expression E = mgh.

Key topics include:
- Reinterpretation of gravitational potential energy as internal phase dynamics
- Line-integral ontology replacing position-assigned scalar potentials
- Zitterbewegung velocity prediction from anomalous magnetic moment
- Gravitational redshift as internal frequency modulation
- Free fall as thermal geodesic motion via entropic synchronization
- Quantitative derivation showing hbar * Delta omega = mg * Delta h

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon and extends concepts from:

Primary references:
1. "Gravitational Redshift of Internal Quantum Clocks:
    A Zitterbewegung-Based Model" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765318

2. "Geometrical Confinement of Energy in the 0-Sphere Model:
    A Topological Mechanism Underlying Rest Mass, Zitterbewegung,
    and Gravitational-Like Phenomena" (Zenodo 2026)
   DOI: 10.5281/zenodo.18437010

3. "Line Integrals as Fundamental Observables in Physics:
    A Unified Principle Behind the Aharonov-Bohm Effect,
    Berry Phase, and Wilson Loops" (Zenodo 2026)
   DOI: 10.5281/zenodo.18203433

Foundational framework (energy conservation identity and spin):
4. "Redefining Electron Spin and Anomalous Magnetic Moment
    Through Harmonic Oscillation and Lorentz Contraction" (Zenodo 2024)
   DOI: 10.5281/zenodo.17764997

5. "Geometric Structure of Spinorial Phase Accumulation
    along Thermal Geodesics" (Zenodo 2025)
   DOI: 10.5281/zenodo.18067760

This paper synthesizes the gravitational redshift predictions from Ref. 1,
the entropic synchronization mechanism from Ref. 2, and the line-integral
ontology from Ref. 3 into a unified reinterpretation of gravitational
potential energy as an internal dynamical quantity.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:
- Exact correspondence hbar * Delta omega = mg * Delta h from gravitational
  redshift of internal Zitterbewegung frequency
- Characteristic velocity v_ZB approximately 0.04047c from anomalous magnetic
  moment without adjustable parameters
- Predicted frequency difference Delta nu approximately 2.64 x 10^9 Hz
  between Earth surface and GPS satellite altitude
- Variational principle for free fall as thermal geodesic motion
- Resolution of conceptual circularity in position-assigned potential energy

What the model CANNOT currently derive:
- Direct microscopic derivation of 1/r^2 gravitational scaling from internal
  phase synchronization networks
- Full non-Abelian treatment of the internal connection
- Explicit relationship between internal connection omega_mu and Christoffel
  symbols Gamma^mu_alpha_beta
- General-relativistic corrections to Zitterbewegung velocity (shown to be
  negligible at quantum scales but systematic treatment incomplete)
- Experimental verification of predicted Zitterbewegung velocity

This paper provides a conceptual reinterpretation with quantitative
predictions while acknowledging open problems in the microscopic foundation.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Conceptual problem of gravitational potential energy
  - Overview of the 0-Sphere reinterpretation
  - Connection to general-relativistic gravitational redshift

Section 2: Conceptual Problem of Position-Assigned Potentials
  - Circularity in classical potential energy definition
  - Comparison table: classical vs. 0-Sphere interpretation

Section 3: The 0-Sphere Model: Foundational Framework
  - Energy conservation identity E_0 = cos^4(theta) + sin^4(theta)
    + (1/2)sin^2(2*theta)
  - Zitterbewegung velocity from anomalous magnetic moment
  - Characteristic oscillation frequency

Section 4: Integral-Based Ontology and Internal Connections
  4.1 Integral-Based Ontology: Observables as Histories
  4.2 Internal Connection and Phase Accumulation
  4.3 Relation to Berry Phase, Wilson Loops, and Thermal Geodesics

Section 5: Gravitational Redshift as Internal Energy Modulation
  - Frequency shift between Earth surface and satellite altitude
  - Coordinate-time observation of Zitterbewegung velocity

Section 6: Reinterpreting mgh: Quantitative Analysis
  - Derivation of hbar * Delta omega = mg * Delta h
  - Numerical verification for electron at 1 m height difference
  - Entropic synchronization mechanism

Section 7: Free Fall as a Thermal Geodesic
  - Variational principle with entropy-weighted action
  - Comparison with GR geodesic equation
  - Inertial mass as internal phase coherence requirement

Section 8: Experimental Predictions and Verification
  - Optical atomic clock measurements
  - Trapped ion simulations
  - Attosecond spectroscopy and g-2 experiments

Section 9: Discussion
  - Relation to emergent gravity programs
  - Open questions on 1/r^2 scaling and proton structure
  - Cosmological constant implications

Section 10: Conclusion
  - Summary of main results and experimental targets

Appendices:
  A: Current Status of the Zitterbewegung Velocity Prediction

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Reinterpreting Gravitational Potential Energy
   as an Internal Line-Integral Quantity in the 0-Sphere Model,"
  Zenodo (2026).

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (February 14, 2026)
  - Initial release
  - Reinterpretation of gravitational potential energy as internal phase
    dynamics within the 0-Sphere model
  - Quantitative derivation of mgh from Zitterbewegung frequency modulation
  - Integral-based ontology with internal connection formalism
  - Thermal geodesic variational principle for free fall
  - Experimental predictions including Delta nu approximately 2.64 x 10^9 Hz

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
Document class: revtex4-2 (APS reprint format)
Page layout: APS Physical Review B default margins
Line spacing: APS reprint default
Font: Computer Modern (LaTeX default)

Tables:
  Table 1: Comparison of classical and 0-Sphere interpretations of
           gravitational potential energy
  Table 2: Status of Zitterbewegung velocity predictions in the 0-Sphere
           model (Revised February 2026)

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref (numbered by section)
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
