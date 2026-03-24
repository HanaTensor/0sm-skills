================================================================================
From Clock Synchronization to Electromagnetism:
A Realist Construction of U(1) Gauge Theory
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: June 1, 2025

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source and figure files for the above paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-1, APS format)
   - Document class: revtex4-1 (reprint, aps)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

2. f-TotalHamiltonian.png
   - Figure 1: Energy conservation and hierarchical phase structure in the
     0-Sphere electron model
   - Shows cos^4(phi/2), sin^4(phi/2), (1/2)sin^2(phi), H(phi)=1
   - Illustrates coexistence of 4*pi periodicity (fermionic kernels) and
     2*pi periodicity (bosonic photon sphere) within a unified framework

Note: references.bib is included for reference but the bibliography is
      embedded inline in main.tex via \begin{thebibliography}.

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages:
    revtex4-1, graphicx, dcolumn, bm, hyperref, braket, caption,
    threeparttable, breqn, microtype

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: main.tex and f-TotalHamiltonian.png must be in the same directory.
      The .bib file is not needed for compilation (bibliography is inline).

================================================================================
ABSTRACT
================================================================================

This paper proposes a realist reinterpretation of U(1) gauge symmetry in
electromagnetism. In conventional formulations, gauge transformations are
treated as mathematical redundancies. Here, they are grounded in the internal
phase dynamics of electrons within the 0-Sphere model.

Central thesis: U(1) gauge freedom emerges from the physical degree of freedom
associated with each electron's internal temporal phase theta(t). The gauge
potential A_mu is reinterpreted not as a formal artifact, but as a geometric
synchronization mechanism coordinating internal clocks across an ensemble of
phase-bearing particles.

Key elements:
- v_ZB = 0.040374c: Zitterbewegung velocity from first principles (SR + GR)
- Energy conservation: E0[cos^4(omega*t/2) + sin^4(omega*t/2)
                         + (1/2)sin^2(omega*t)]
- 4*pi periodicity (omega*t/2 terms): fermionic spin
- 2*pi periodicity (omega*t term): bosonic gauge/photon sphere
- U(1) gauge transformation: theta(x) --> theta(x) + alpha(x)
  = resetting internal phase of particle at spacetime point x
- Snell's law for internal energy transport:
  sin(theta_A)/sin(theta_B) = v_A/v_B
- Discrete U(1) fiber bundle assigned per electron (vs. continuous field)
- Non-Abelian structure potentially emergent from multiple phase modes

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon:

1. "A Model of an Electron Including Two Perfect Black Bodies" (#1, 2018)
   Cited as hanamura2018
   DOI: 10.5281/zenodo.16759284

2. "Redefining Electron Spin and AMM" (#10, 2023)
   Cited as hanamura2023
   DOI: 10.5281/zenodo.17764997

3. "Quantum Oscillations in the 0-Sphere Model" (#11, 2024)
   Cited as hanamura2024quantum
   DOI: 10.5281/zenodo.17765017

4. "Bridging QM and GR: AMM and Geodetic Precession" (#14, 2025)
   Cited as hanamura2025bridging
   DOI: 10.5281/zenodo.17765097

This paper is thematically related to #19 (Spin as a Real Vector, SU(2)/U(1)
unification) and #20 (Noetherian Reinterpretation), which further develop
the internal phase geometry program.

================================================================================
KEY RESULTS
================================================================================

Realist gauge interpretation:
- Gauge freedom = freedom in choosing phase origin of internal clock
- A_mu = synchronization field ensuring phase coherence across particles
- gauge transformation theta(x) --> theta(x) + alpha(x): physically real
  (resets internal phase, not just mathematical redundancy)

Geometric foundations:
- Snell's law in internal phase space: governs TPE energy transport
- Geodesic motion = path of least action in internal phase space
- Discrete U(1) fiber bundle per electron (not continuous over spacetime)
- Differentiable manifold arises from photon sphere trajectory within electron

Harmonic hierarchy:
- omega*t/2 (4*pi): fermionic kernel dynamics / spin-1/2
- omega*t (2*pi): bosonic photon sphere / gauge
- Same internal clock theta(t) governs both layers
- Bridge between spin and gauge without independent gauge symmetries

Prediction: v_ZB = 0.040374c (testable Zitterbewegung velocity)

Conceptual advance:
- Resolves Zee's "strange language full of redundancy" critique
- Aharonov-Bohm and Tonomura's experiment interpreted as evidence for
  physical phase structure (not just mathematical convenience)

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Gauge redundancy problem (Zee, Wilson, Rovelli)
  - 0-Sphere model approach; Aharonov-Bohm motivation

Section 2: Motivation and Conceptual Tension in Gauge Theory
  - Gauge transformation Eqs. [wavefunction, gauge_potential]
  - Zee quote on redundancy; Teller philosophical argument
  - Internal energy profile [Eq. internal_energy]
  - Snell's law [Eq. snell]

Section 3: Internal Structure and Dynamics of the Electron
  - Two TPE kernels: positive/negative energy solutions of Dirac
  - v_ZB = 0.040374c from SR + geodesic precession
  - Energy conservation identity [Eq. energy_conservation]
  - Photon sphere as real (not virtual) energy carrier

Section 4: Realist Gauge Geometry from First Principles
  4.1 Reinterpreting U(1) Gauge Symmetry
      - theta(x) --> theta(x) + alpha(x) as physical phase reset
  4.2 Geometric Foundation: From Snell's Law to Geodesic Motion
      - Snell: sin(theta_A)/sin(theta_B) = v_A/v_B
      - Least action: S = integral_A^B ds
      - Figure 1: f-TotalHamiltonian.png
  4.3 Discrete Bundle Structure vs. Continuous Field Theory
      - Discrete U(1) fiber per electron vs continuous field
      - Table 1: Conventional Gauge Theory vs 0-Sphere Model
  4.4 Unification without Non-Abelian Complexity
      - Multiple phase modes theta_1, theta_2,... for non-Abelian analogs
  4.5 Hierarchical Phase Periodicity as a Bridge Between Spin and Gauge
      - Energy identity [Eq. energy_conservation]
      - Thomas precession [Eq. Thomas]: Omega = (1/2c^2)[a x v]
      - sin(2*omega*t) frequency doubling --> spin-1/2

Section 5: Conclusion

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "From Clock Synchronization to Electromagnetism:
  A Realist Construction of U(1) Gauge Theory,"
  Zenodo (2025).
  https://doi.org/10.5281/zenodo.17765136

================================================================================
CONTACT INFORMATION
================================================================================

  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (June 1, 2025)
  - Initial release
  - Proposes gauge potential as clock synchronization mechanism
  - Derives U(1) gauge connection from internal phase transport
  - Hierarchical phase periodicity bridges spin (4*pi) and gauge (2*pi)

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) for assistance
in English language polishing and technical exposition. All theoretical concepts,
interpretations, and conclusions remain solely the author's responsibility.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

Document class: revtex4-1, reprint mode (APS) [NOT revtex4-2]
Font: Computer Modern (LaTeX default)

Tables:
  Table 1: Conceptual comparison: Conventional gauge theory vs 0-Sphere model
           (5 rows x 3 columns)

Figures:
  Fig. 1: f-TotalHamiltonian.png -- cos^4 / sin^4 / (1/2)sin^2 / H(phi)=1

Note on references.bib: Uploaded for completeness; bibliography is embedded
inline in main.tex and does not require separate compilation with BibTeX.

================================================================================
END OF README
================================================================================
