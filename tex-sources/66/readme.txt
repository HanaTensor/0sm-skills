================================================================================
Subluminal Zitterbewegung and the Invariant Speed:
An Internal Refractive Index for the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: November 14, 2026
DOI: 10.5281/zenodo.23750210

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file and the numerical-verification
script for a research letter of the 0-Sphere Model series (paper #66):

1. main.tex
   - Main LaTeX source file (12 pages, 5 figures drawn in TikZ, 2 tables,
     19 references)
   - Document class: REVTeX 4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

2. verify66.py
   - Python 3 script that reproduces every number of the Letter and checks
     the identities of Appendix B:
     (1) beta_ZB, the index n = 1/beta_ZB and n^2 against sqrt(2) pi / alpha;
     (2) lambda_C, the light-speed reference nu_C, the transport frequency
     nu_ZB, the Dirac ZB frequency nu_D and their ratio 2/beta_ZB;
     (3) the three energy layers 511 keV : 20.7 keV : 419 eV, the drag
     coefficient 1 - 1/n^2 and the critical angle arcsin(1/n);
     (4) the energy identity, the radiation gradient dT_B - dT_A = sin(theta)
     and the conservation dT_A + dT_B + dK = 0;
     (5) the expansions T_A = 3/8 + (1/2)cos(theta) + (1/8)cos(2 theta),
     T_B, K, and the absence of any frequency above 2 omega;
     (6) the discrete group velocity c / (2 n(2 omega) - n(omega)).
   - Requires Python 3 and NumPy.
   - Run:  python3 verify66.py   (nine checks, each printed as PASS)

3. zenodo_23750210.pdf
   - Compiled letter (12 pages).

4. zenodo_23750210_relations.txt
   - Zenodo related-identifier list of this record (relations to earlier
     papers of the series, with reasons) and the recommended reverse
     relations.

5. primer_en.docx
   - A primer for undergraduate readers: the background needed to read the
     Letter (invariant speed, refractive index and Snell's law, phase and
     group velocity, Fizeau's experiment, the Dirac velocity operator and
     the Foldy-Wouthuysen representation), the elements of the 0-Sphere
     model that the Letter uses, a section-by-section reading of the Letter,
     a glossary, exercises with answers, and a map from the primer to the
     sections of the Letter. The primer explains the Letter; it does not
     add to or verify its claims.

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
  revtex4-2, graphicx, bm, physics, hyperref, caption, microtype, ragged2e,
  booktabs, enumitem, amsthm, listings, xcolor, tikz (libraries: arrows.meta,
  calc, 3d, shadings, positioning, decorations.pathmorphing)

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex
  pdflatex main.tex

Note: The bibliography is embedded (thebibliography); no BibTeX run is
      needed. Three passes are recommended so that cross-references and
      hyperlinks are all resolved.

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

The 0-Sphere model assigns to the electron an internal oscillation whose
speed, fixed by the anomalous magnetic moment alone, is v_ZB = 0.04047 c,
giving a Zitterbewegung frequency nu_ZB = v_ZB / lambda_C = 5.00e18 Hz in
the X-ray band. The Dirac equation attaches the speed c to the
Zitterbewegung through the eigenvalues +/-c of its velocity operator and
predicts 2 m_e c^2 / h = 2.47e20 Hz. This Letter separates two meanings of c
that the comparison conflates: the invariant speed of the Lorentz group,
which the 0-Sphere model retains without modification, and the group
velocity of the internal carrier, which it sets to c/n with
n = 1/beta_ZB = 24.71.

Fizeau's moving-water experiment shows that a medium-internal speed c/n is
compatible with special relativity; here the medium rest frame is the
electron rest frame, and the Fresnel drag coefficient is 1 - beta_ZB^2. The
Foldy-Wouthuysen representation shows that the eigenvalues +/-c belong to
one choice of position operator and do not fix the carrier speed as an
observable. The optical metric G = n^2(T) g established earlier in the
series supplies the geometric setting, and Snell's law gives a critical
angle sin(theta_c) = beta_ZB at any boundary where the index returns to
unity, independently of the shape of that boundary. The index is assigned,
not derived; its derivation from the internal temperature profile is
identified as the route by which the bridge equation becomes a derivation.

Two appendices explain why a group velocity belongs in the model. The energy
identity cos^4(theta/2) + sin^4(theta/2) + (1/2) sin^2(theta) = 1 does not
move the energy from one kernel to the other at once: the radiation gradient
is the difference of the derivatives of the two kernel energies, exactly
sin(theta), so that a transfer of constant amplitude is excluded. Resolved
into frequencies, the identity balances separately at the constant, at the
fundamental omega and at the second harmonic 2 omega; the transfer is
continuous in phase and discrete in frequency, and the group index of two
lines is the difference quotient n_g = 2 n(2 omega) - n(omega).

Key topics include:
- Two meanings of c: the invariant speed and the speed of an internal carrier
- Fizeau's experiment and the Fresnel drag coefficient 1 - beta_ZB^2
- The Dirac eigenvalues +/-c and the Foldy-Wouthuysen mean position
- The optical metric n^2(T) g and the internal index n = 1/beta_ZB = 24.71
- The critical angle 2.32 degrees, independent of the shape of the boundary
- Why a group velocity: the energy identity as a wave group
- Continuous in phase, discrete in frequency; the discrete group index
- Competing predictions: 5.00e18 Hz (20.7 keV) against 2.47e20 Hz (1.022 MeV)

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This letter builds upon:

Primary references (continued):
1. "Redefining Electron Spin and Anomalous Magnetic Moment Through Harmonic
   Oscillation and Lorentz Contraction" (Zenodo 2024)
   DOI: 10.5281/zenodo.17764997

2. "Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of
   the Spacetime Metric in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.20388056

3. "From Zero and One to the Electron: Path-Connectedness, the Double Cover,
   and the Geometric Origin of the Quartic Energy in the 0-Sphere Model"
   (Zenodo 2026)
   DOI: 10.5281/zenodo.23257458

Results used as inputs:
4. "Thermal Geodesics in the 0-Sphere Model: Extending General Relativity
   through Internal Thermodynamic Structure" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765349
5. "The Bridge Equation gamma = 1 + a from First Principles" (Zenodo 2026)
   DOI: 10.5281/zenodo.20091680
6. "Geometrical Confinement of Energy in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.18356895
7. "Geometric Origin of the One-Half Factor: Thermal Potential Energy Floor
   and Zero-Point Energy in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.19010945

Foundational framework (0-Sphere Model series):
8. "A Model of an Electron Including Two Perfect Black Bodies"
   (Zenodo 2018)
   DOI: 10.5281/zenodo.16759284

The earlier statements of the 0-Sphere ZB frequency and of its ratio to the
Dirac value in Appendix G of #33 and in #46 contain an arithmetic error and
are superseded by Eq. (I.4) of this letter, nu_ZB = beta_ZB c / lambda_C.

================================================================================
KEY RESULTS
================================================================================

What the letter establishes:
- R1. The speed c of the Dirac equation is the invariant speed of the
  Lorentz group; the 0-Sphere model retains it without modification.
- R2. The speed 0.04047 c is the group velocity of the internal carrier,
  v_ZB = c/n with n = 1/beta_ZB = 24.71.
- R3. A medium-internal speed c/n is admissible in special relativity; the
  Fresnel drag coefficient of the electron is 1 - beta_ZB^2 = 0.998362.
- R4. The Dirac eigenvalues +/-c belong to one choice of position operator
  and do not fix the carrier speed (Foldy-Wouthuysen: dX/dt = c^2 p / E).
- R5. Within the optical metric of #51, the internal index is
  n(T_int) = 1/beta_ZB; n^2 = 610.51 agrees with sqrt(2) pi / alpha to
  0.28%.
- R6. At any boundary where the index returns to unity,
  sin(theta_c) = beta_ZB, theta_c = 2.32 degrees, independently of the
  shape of the boundary.
- R7. Competing predictions: nu_ZB = 5.00e18 Hz (0-Sphere) against
  nu_D = 2.47e20 Hz (Dirac).
- R8. The amplitude of the transfer is not constant: the radiation gradient
  is sin(theta), and the kernel energies are superpositions of the
  fundamental and the second harmonic with fixed weights 1/2 and 1/8. The
  envelope is restored at every cycle and does not widen.
- R9. The transfer is continuous in phase and discrete in frequency: the
  kernel energies contain exactly the frequencies 0, omega and 2 omega; the
  identity balances separately at each frequency; the group index is
  n_g = 2 n(2 omega) - n(omega).

What the letter does not derive (open items):
- O1. The index n(T) from the internal temperature profile, which would fix
  beta_ZB independently of the anomalous moment.
- O2. The constituent responsible for n > 1, and the relation between the
  phase index and the group index, n(2 omega) = n(omega).
- O3. The factor of two between c/lambda_C and 2 m_e c^2 / h.
- O4. The shape and structure of the boundary of the internal region, and
  the leakage across it.
- O5. The coupling of the internal carrier to gravitation.
- O6. The coupling of the internal transfer to external photons. The word
  radiation in this letter denotes the internal transfer only.

Statements are marked [standard] or [0SM reading] in Appendix A, so that a
reader can accept the standard physics and still reject the model. The
decisive test is experimental: a resonant signature of the free electron in
the X-ray band near 20 keV.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section I:    Introduction (Scope)
Section II:   Two Meanings of c
Section III:  Precedent: Light in a Moving Medium
Section IV:   The Dirac Eigenvalues Do Not Fix the Carrier Speed
Section V:    The Optical Metric of the Internal Region
Section VI:   Shape-Independent Consequences
Section VII:  Limitations
Section VIII: Conclusion

Appendices:
  A. The 0-Sphere Model in Brief
     A.1 Two Kernels and the Photon Sphere
     A.2 The Internal Clock
     A.3 The Bridge Equation
     A.4 The Three-Layer Hierarchy
     A.5 Thermal Geodesics and the Optical Metric
     A.6 Two Uses of the Word Radiation
  B. Why a Group Velocity, and What It Opens
     B.1 Why a Group Velocity Belongs in This Model
     B.2 The Question That Was Open
     B.3 What the Concept Opens
     B.4 The Envelope Is Fixed by the Identity
     B.5 Continuous in Phase, Discrete in Frequency
  C. Numbers and Their Reproduction (code listing)
  D. Inputs, Results and Open Items (I1-I3, R1-R9, O1-O6)

Acknowledgments

References (19 entries, ordered by first citation)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Subluminal Zitterbewegung and the Invariant Speed: An Internal Refractive
   Index for the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.23750210

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (November 14, 2026)
  - Initial release:
  - Separation of the invariant speed from the speed of the internal carrier
  - Fizeau's experiment and the drag coefficient 1 - beta_ZB^2
  - Foldy-Wouthuysen representation and the Dirac eigenvalues +/-c
  - Internal index n = 1/beta_ZB in the optical metric of #51
  - Shape-independent critical angle
  - Why a group velocity (Appendix B): radiation gradient, wave group,
    continuous in phase and discrete in frequency, discrete group index
  - Inputs, results and open items listed for citation by later papers
  - Numerical verification script verify66.py
  - Primer for undergraduate readers (primer_en.docx)

================================================================================
ACKNOWLEDGMENTS
================================================================================

The conception of this Letter, the framing of its questions and every
decision to adopt or reject a result are the author's. The work builds on
the author's earlier papers in this series and on a sequence of working
sessions with the language model Claude Opus 5.5 (Anthropic), which drafted
the manuscript, proposed derivations and literature precedents, and carried
out numerical checks. Every derivation adopted here was checked by the
author and is reproduced by the verification script deposited with this
Letter.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: REVTeX 4-2 (APS/PRB reprint, two-column)
Page layout: REVTeX default
Line spacing: REVTeX default
Font: Computer Modern (LaTeX default)

Tables:
  - Table I:   Shape-independent quantities fixed by the internal refractive
               index n = 1/beta_ZB (Sec. II)
  - Table II:  Frequency content of the energy identity, line by line
               (App. B.5)

Figures:
  - Fig. 1: The electron of the 0-Sphere model and the two meanings of c
  - Fig. 2: The transfer from one kernel to the other is a wave group
  - Fig. 3: What the group-velocity reading changes
  - Fig. 4: The amplitude of the transfer is not constant, and its spectral
            weights are fixed
  - Fig. 5: A continuous band and a discrete set of lines
  - All drawn in TikZ inside main.tex (no external image files)

Code listings:
  - One Python code block in Appendix C (listings package); the same
    numbers, together with the identity checks of Appendix B, are produced
    by verify66.py

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref
  - Hyperlinked bibliography and DOI links

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

  - Main document: main.tex
  - Compiler: pdfLaTeX
  - TeX Live version: 2025
  - No additional files are required (figures are TikZ, bibliography is
    embedded)

================================================================================
END OF README
================================================================================
