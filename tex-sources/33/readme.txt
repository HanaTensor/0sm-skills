================================================================================
Geometrical Confinement of Energy in the 0-Sphere Model:
A Topological Mechanism Underlying Rest Mass and Zitterbewegung
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: January 24, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source files for the above paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-2, APS/PRB format)
   - Document class: revtex4-2 (reprint, aps, prb)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

2. fig_TotalHamiltonian.tex
   - TikZ figure: energy conservation and internal dynamics in the 0-Sphere model
   - Included via \input{} in main.tex (Appendix H)

3. fig_thermal.tex
   - TikZ figure: spatiotemporal energy distribution within a single electron
   - Included via \input{} in main.tex (Appendix A)

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-2, graphicx, bm, physics, hyperref, caption, microtype,
    ragged2e, booktabs, amsmath, tikz (libraries: arrows.meta, calc,
    3d, shadings, positioning)

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

This paper presents a geometrical interpretation of the 0-Sphere model in which
thermal potential energy -- identified with rest mass energy -- is localized at
two discrete energy kernels, while admissible radiative transport is constrained
by an embedding into a higher-dimensional arcwise connected region interpreted
as a photon sphere.

Although the 0-sphere itself is totally disconnected, its embedding into this
compact domain permits continuous paths that support circulation of thermal
potential energy between kernels via Zitterbewegung oscillations derived from
the Dirac equation. This construction establishes a topological mechanism in
which rest mass and Zitterbewegung emerge from geometric confinement rather than
from dynamical binding or symmetry-based conservation laws. The resulting
confinement is topological rather than dynamical, restricting radiative
processes to a finite region and ensuring energy conservation without invoking
dynamical equations of motion or Noether-type symmetries.

Key topics include:
- Topological confinement via embedding S^0 into arcwise connected domain D
- Rest mass energy as thermally localized quantity at discrete 0-sphere kernels
- Zitterbewegung as real internal oscillation constrained by photon sphere
- Energy conservation: E0[cos^4(omega*tau/2)+sin^4(omega*tau/2)+(1/2)sin^2(omega*tau)]
- Deformation retraction as mechanism for extreme-limit transport suppression
- Snell-type thermal geodesics within the photon sphere
- Three Compton wavelength scales and predicted frequency hierarchy

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon and clarifies concepts from:

Primary references (Line Integral Trilogy):
1. "Geometric Structure of Spinorial Phase Accumulation along Thermal Geodesics"
   Zenodo (2025). DOI: 10.5281/zenodo.18067760

2. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" Zenodo (2026). DOI: 10.5281/zenodo.18135855

3. "Line Integrals as Fundamental Observables in Physics: A Unified Principle
   Behind the Aharonov-Bohm Effect, Berry Phase, and Wilson Loops"
   Zenodo (2026). DOI: 10.5281/zenodo.18203433

Foundational 0-Sphere Model papers:
4. "From Zero-Sphere to Emergent Spacetime" Zenodo (2025).
   DOI: 10.5281/zenodo.17765336

5. "From Clock Synchronization to Electromagnetism: U(1) Gauge Theory"
   Zenodo (2025). DOI: 10.5281/zenodo.17765136

6. "Redefining Electron Spin and AMM Through Harmonic Oscillation and
   Lorentz Contraction" Zenodo (2024). DOI: 10.5281/zenodo.17764997

7. "A Model of an Electron Including Two Perfect Black Bodies" Zenodo (2018).
   DOI: 10.5281/zenodo.16759284

Additional references:
8. "Thermal Geodesics: Extending GR Through Internal Thermodynamic Structure"
   Zenodo (2025). DOI: 10.5281/zenodo.17765349

9. "Spin from Geometry: Emergence of Spin via Internal Berry Phase"
   Zenodo (2025). DOI: 10.5281/zenodo.17765409

10. "Coexistence of Positive and Negative-Energy States in the Dirac Equation"
    Zenodo (2020). DOI: 10.5281/zenodo.17760132

11. "Bridging QM and GR: AMM and Geodetic Precession" Zenodo (2025).
    DOI: 10.5281/zenodo.17765097

12. "Dissolution of the Vacuum Energy Problem in an Integral-Based Ontology"
    Zenodo (2026). DOI: 10.5281/zenodo.18275142

This paper provides the topological confinement foundation underlying the
internal energy circulation described in prior 0-Sphere work. The framework is
extended in paper #34 (DOI: 10.5281/zenodo.18437010) to gravitational phenomena.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:
- Topological origin of rest mass confinement: supp(E) subset D
- Zitterbewegung as geometric consequence of embedding, not dynamical artifact
- Energy conservation from Stefan-Boltzmann quartic structure
- Snell-type geodesics as admissible radiative paths within photon sphere
- Zitterbewegung frequency: nu approx 5.007e18 Hz (beta = 0.04047, lambda_C)
- Extreme-limit behavior: deformation retraction replaces divergence with
  topological degree-of-freedom loss
- Physical energy regime: X-ray (Compton, ~20 keV) as natural domain

What the model CANNOT currently derive:
- Absolute value of electron rest mass m_e
- Origin of fine-structure constant alpha
- Extension to strong and weak interactions
- Non-Abelian generalization of topological confinement

The confinement condition supp(E) subset D is purely geometric: it does not
require equations of motion, Noether-type symmetries, or dynamical laws.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Motivation for topological approach to rest mass and Zitterbewegung
  - Relation to line integral trilogy and prior 0-Sphere work

Section 2: Motivation and Conceptual Overview
  - Line integrals as primary observables; ontological reversal
  - Three core innovations: ontological reversal, dimensional emergence,
    vacuum energy dissolution

Section 3: Discrete Localization on the 0-Sphere
  - S^0 = {p+, p-} with discrete topology
  - No internal continuous paths; necessity of external embedding

Section 4: Embedding into an Arcwise Connected Region
  - Inclusion map i: S^0 -> D (photon sphere)
  - Thermal geodesics and Snell-type refraction

Section 5: Topological Confinement of Thermal Potential Energy
  - supp(E) subset D as geometric confinement condition
  - Energy conservation as topological consequence

Section 6: Extreme Limits and Degeneracy of Transport
  - Deformation retraction: D -> {p} in high-energy limit
  - Suppression of transport without divergence

Section 7: Discussion and Outlook
  - Implications for singularity resolution
  - Connection to quantum gravity approaches

Appendices:
  A. What is the 0-sphere
  B. Thermal energy gradient caused by two kernels
  C. On Continuous Maps from Connected Domains to the 0-Sphere
  D. Deformation Retraction: Formal Definition
  E. Physical Scale of the Photon Sphere
  F. Compton Wavelength Scales in Zitterbewegung
  G. Length Scale Selection in Frequency Predictions
  H. Mathematical Foundation from Internal Energy Dynamics
     H.1 Energy Conservation in the Dual-Kernel System
     H.2 Reinterpretation of Positive and Negative Energy States
     H.3 Derivation of the Sinusoidal State Function from Temperature Gradients

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Geometrical Confinement of Energy in the 0-Sphere Model:
  A Topological Mechanism Underlying Rest Mass and Zitterbewegung,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.18356895

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (January 24, 2026)
  - Initial release
  - Establishes topological confinement mechanism for rest mass and ZB
  - Introduces photon sphere as arcwise connected embedding domain
  - Derives Zitterbewegung frequency from beta=0.04047c and Compton scale
  - Analyzes extreme-limit deformation retraction

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
Document class: revtex4-2, reprint mode (APS/PRB)
Font: Computer Modern (LaTeX default)

Tables:
  Table 1: Hierarchy of Compton wavelength scales and their physical roles
  Table 2: Frequency predictions using different length scales
  Table 3: Energy scale hierarchy (X-ray through pair production)

Figures (TikZ, inline):
  Fig. 1: Topological embedding of the 0-sphere (S^0 in D, path w(tau))
  Fig. 2: Deformation retraction in the extreme limit
  Fig. 3: Geometric comparison of the 0-sphere and 1-sphere
  Fig. 4: Spatiotemporal energy distribution (fig_thermal.tex)
  Fig. 5: Energy conservation and internal dynamics (fig_TotalHamiltonian.tex)

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
