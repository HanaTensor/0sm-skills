================================================================================
Spin as a Real Vector from Internal Photon-Sphere Motion:
Geometric Origin of U(1) Gauge and SU(2) Periodicity
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: June 15, 2025

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source and figure files for the above paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-1, APS format)
   - Document class: revtex4-1 (reprint, aps)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

2. f-double_frequency.png
   - Figure 1: Time evolution of internal motion components in the 0-Sphere model
   - Three panels: v=cos(omega*t), a=-sin(omega*t),
     Omega(t) = -(1/4)*sin(2*omega*t)
   - Demonstrates double-frequency mechanism for 720-degree spinor periodicity

3. f-TotalHamiltonian.png
   - Figure 2: Energy conservation in the 0-Sphere model
   - Shows cos^4(phi/2), sin^4(phi/2), (1/2)sin^2(phi), H(phi)=1

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages:
    revtex4-1, graphicx, dcolumn, bm, hyperref, braket, caption,
    threeparttable, breqn, microtype, ragged2e, booktabs

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: All three files must be in the same directory. Two passes required.

================================================================================
ABSTRACT
================================================================================

This paper proposes a geometric and deterministic model of electron spin in
which spin angular momentum arises from internal reciprocating motion of a
confined photon-sphere, rather than from an abstract pseudovector.

Key contributions:
- Corrects dimensional inconsistency in previous formulation: the scalar
  expression Omega = -(1/4c^2)*sin(2*omega*t) is replaced by the proper vector
    Omega(t) = -(1/4c^2)*sin(2*omega*t)*e_z
- Spin is a real, time-evolving vector with z-component ~ sin(2*omega*t),
  giving 4*pi periodicity naturally
- SU(2) symmetry emerges geometrically from underlying U(1) phase structure
- Challenges classification of spin as pseudovector
- Observer-independent mechanism for 720-degree spinor transformation

Central equation:
  Omega(t) = -(1/4c^2) * sin(2*omega*t) * e_z   [Thomas precession]

Energy conservation:
  E0 = E0[cos^4(omega*t/2) + sin^4(omega*t/2) + (1/2)sin^2(omega*t)]

Key topics include:
- SU(2) as geometric unfolding of U(1) phase
- Spin measurement as phase projection (no wavefunction collapse)
- Anomalous g-factor as Lorentz contraction in oscillatory motion
- Zeeman-like effects from internal magnetic field without external fields
- Parity violation reconsidered as projection artifact of symmetric geometry
- v_ZB ~ 0.04c for electron (theoretical prediction)

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon and corrects:

1. "Redefining Electron Spin and AMM" (#10)
   Cited as hanamura2309.0047
   DOI: 10.5281/zenodo.17764997
   [Corrects the dimensional inconsistency in Omega(t) from that paper]

2. "Quantum Oscillations in the 0-Sphere Model" (#11)
   Cited as hanamura2411.0117
   DOI: 10.5281/zenodo.17765017
   [Source of kernel A/B energy weight functions and photon sphere KE term]

3. "Bridging QM and GR: AMM and Geodetic Precession" (#14)
   Cited as hanamura2501.0130
   DOI: 10.5281/zenodo.17765097
   [Energy conservation identity and v_ZB ~ 0.04c]

This paper is cited in #20 (Noetherian Reinterpretation), #26 (Berry Phase /
Spin from Geometry), and #27 (Challenging the Uncertainty Principle) as the
corrected SU(2)/U(1) unification paper.

================================================================================
KEY RESULTS
================================================================================

Dimensional correction:
  Previous: Omega = -(1/4c^2)*sin(2*omega*t)  [dimensionally inconsistent]
  Corrected: Omega(t) = -(1/4c^2)*sin(2*omega*t)*e_z  [proper vector]

Physical interpretation of 720-degree periodicity:
  v(t) = cos(omega*t), a(t) = -sin(omega*t)
  Cross product a x v --> sin(2*omega*t): double frequency
  Full cycle requires 4*pi in internal time

SU(2) from U(1):
  360-degree U(1) phase <--> 720-degree SU(2) spinor double-cover
  Not two independent groups: SU(2) is geometric unfolding of U(1)

Spin as real (polar) vector:
  Collinear v and a in 1D oscillator: no classical cross product
  BUT Thomas precession at relativistic velocity generates angular momentum
  --> Spin arises from relativistic internal dynamics, not circular motion

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - ZB history: Schrodinger, Barut-Bracken, Hestenes
  - 4*pi periodicity from sinusoidal internal oscillation

Section 2: Motivation
  - Correction of dimensional inconsistency from #10
  - "What is spin?" revisited

Section 3: Notation and Physical Quantities
  - omega, t, E0, v(t), a(t), Omega(t), e_z, kernels A/B, c
  - Figure 1: f-double_frequency.png

Section 4: Discussion
  4.1 Geometric Emergence of SU(2) from U(1) Phase Evolution
  4.2 Correcting Dimensional Inconsistency in the Angular Velocity
      - Figure 2: f-TotalHamiltonian.png
  4.3 Spin as a Real Oscillating Vector: Temporal Structure and Symmetry
  4.4 Implications for Spin Measurement and Internal Structure
  4.5 Energy Distribution and Geometric Interpretation of Spin
      - Eq. total_hamiltonian; Eq. angular_velocity
  4.6 Spin as a Real Vector: Algebraic and Relativistic Basis
      - Thomas precession with collinear v, a at relativistic velocity
  4.7 Summary of Conceptual Differences
      - Table 1: Conventional QT vs 0-Sphere Model

Section 5: Conclusion

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Spin as a Real Vector from Internal Photon-Sphere Motion:
  Geometric Origin of U(1) Gauge and SU(2) Periodicity,"
  Zenodo (2025).
  https://doi.org/10.5281/zenodo.17765238

================================================================================
CONTACT INFORMATION
================================================================================

  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (June 15, 2025)
  - Initial release
  - Corrects dimensional inconsistency in Omega(t) from #10
  - Proposes SU(2) as geometric unfolding of U(1)
  - Derives 720-degree periodicity from sin(2*omega*t) double frequency

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
  Table 1: Conventional Quantum Theory vs 0-Sphere Geometric Spin Model
           (9 rows x 3 columns)

Figures:
  Fig. 1: f-double_frequency.png -- velocity, acceleration, angular velocity
  Fig. 2: f-TotalHamiltonian.png -- cos^4 / sin^4 / (1/2)sin^2 / H(phi)=1

================================================================================
END OF README
================================================================================
