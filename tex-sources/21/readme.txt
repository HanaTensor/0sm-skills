================================================================================
Anomalous Magnetic Moments Without Fields:
A Geometric and Observer-Dependent Interpretation
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: June 29, 2025

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
- Required LaTeX packages:
    revtex4-1, graphicx, dcolumn, bm, hyperref, braket, caption,
    threeparttable, breqn, microtype, ragged2e, booktabs

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references.

================================================================================
ABSTRACT
================================================================================

Building upon the 0-Sphere electron model with its internal structure of two
thermal kernels and a photon sphere exhibiting Zitterbewegung oscillations, this
paper presents a new observer-dependent interpretation that fundamentally
reframes the origin of anomalous magnetic moments in quantum electrodynamics.

While conventional QED requires external magnetic field interactions for any
observable anomaly, this work demonstrates that anomalous magnetic moments can
arise as purely geometric effects in free electrons (B = 0) through relativistic
observer transformations.

The crucial insight: the same internal ZB motion at v ~ 0.04c yields different
measurements depending on the observer's reference frame:
- Co-moving observer: measures g-factor = 2 exactly (Dirac prediction)
- Laboratory observer: perceives Lorentz contraction --> anomalous magnetic moment

Central relation:
  gamma = 1 + a_e    (Lorentz factor = 1 + anomalous magnetic moment)

Key topics include:
- L/L0 = 1/(1 + a_e) as Lorentz contraction ratio [Eq. length_contraction]
- gamma = 1 + a_e [Eq. gamma_anomaly_relation]
- Thomas precession: Omega = (1/2c^2)[a x v] [Eq. Thomas1]
- v(t) = v0*cos(omega*t) --> double-frequency angular momentum sin(2*omega*t)
- Two conditions for ZB velocity = 0:
    (1) Co-moving frame (SR): universal, all leptons
    (2) Critical radius (GR): decay threshold, muon and tau only
- Prediction: internal velocity v ~ 0.04c, frequency ~ 10^18 Hz
- Observer-dependent interpretation: anomaly as relational quantity

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon:

1. "A Model of an Electron Including Two Perfect Black Bodies" (#1)
   Cited as hanamura2018
   DOI: 10.5281/zenodo.16759284

2. "Redefining Electron Spin and AMM" (#10)
   Cited as hanamura2309.0047
   DOI: 10.5281/zenodo.17764997
   [Source of gamma = 1 + a_e and v ~ 0.04c prediction]

3. "Bridging QM and GR: AMM and Geodetic Precession" (#14)
   Cited as hanamura2501.0130
   DOI: 10.5281/zenodo.17765097
   [Critical radii and GR extension]

This paper is cited in #26 (Spin from Geometry) as the observer-dependent
geometric interpretation used in the Foucault pendulum analogy (g=2 in
co-moving frame vs g=2+a in lab frame). It is also thematically related to
#36 (Non-Perturbative Nature and Fine-Structure Constant) which elaborates
the scope of the non-perturbative approach.

================================================================================
KEY RESULTS
================================================================================

What the model establishes:
- Anomalous magnetic moments are observer-dependent geometric effects, not
  interaction-based corrections (no external B field required)
- gamma = 1 + a_e: direct bridge between QM anomaly and SR geometry
- Double-frequency Thomas precession from single-frequency ZB oscillation
  explains spin-1/2 magnetic efficiency (g vs orbital g)
- Free electrons exhibit anomaly through internal structure observable from
  laboratory frame

Comparison with other ZB-based models (Table 1):
- Hestenes (2010): helical light-speed motion; derives g=2 only; no observer dependence
- Kozlov & Nemchenko (2012): semi-classical circular orbit; reproduces Schwinger term;
  no frame analysis
- 0-Sphere (2018-2025): subluminal v~0.04c; exact gamma=1+a_e; observer
  dependence as central principle; field-free prediction

Experimental limitation noted:
- Direct measurement of free-electron anomaly remains challenging without B field
- Alternative: measure ZB velocity directly (~0.04c) via high-frequency
  Compton scattering or ultrafast temporal interference

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Conventional QED interpretation and its assumptions
  - Observer-dependent alternative via 0-Sphere model
  - Implications for geometric reinterpretation of QM

Section 2: Motivation
  2.1 Fundamental Departure from QED: Observer-Dependent Anomaly in Free Electrons
      - H_total = H_0 + H_1; anomaly only with B != 0 (conventional)
      - gamma = 1 + a_e [Eq. gamma_anomaly_relation]
      - L/L0 = 1/(1+a_e) [Eq. length_contraction]
  2.2 Comparison with Other Zitterbewegung-Based Models
      - Table 1: Hestenes / Kozlov-Nemchenko / 0-Sphere comparison

Section 3: Observer-Dependent Anomalous Magnetic Moment
  3.1 Internal ZB Dynamics and the Geometric Origin of Spin Anomaly
      - Thomas precession [Eq. Thomas1]
      - v(t) = v0*cos(omega*t); a(t) = -v0*omega*sin(omega*t)
      - Cross product --> sin(2*omega*t): double-frequency mechanism
  3.2 Implications for QM and Relativistic Consistency
      - Running of alpha: geometric interpretation
      - Critical radii for muon/tau decay
  3.3 Conditions for Zero Zitterbewegung Velocity
      - Condition 1: co-moving frame (SR, universal)
      - Condition 2: critical radius (GR, muon/tau decay threshold)

Section 4: Conclusion

Appendices: (none)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Anomalous Magnetic Moments Without Fields:
  A Geometric and Observer-Dependent Interpretation,"
  Zenodo (2025).
  https://doi.org/10.5281/zenodo.16980206

================================================================================
CONTACT INFORMATION
================================================================================

  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (June 29, 2025)
  - Initial release
  - Proposes observer-dependent geometric interpretation of AMM
  - gamma = 1 + a_e as central relation
  - Compares systematically with Hestenes and Kozlov-Nemchenko models
  - Two conditions for zero ZB velocity (SR and GR)

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
  Table 1: Comparison of ZB-Based Models for Anomalous Magnetic Moment
           (9 rows x 4 columns: Hestenes / Kozlov-Nemchenko / 0-Sphere)

Figures: (none)

Key equations:
  L/L0 = 1/(1 + a_e)                     [Eq. length_contraction]
  gamma = 1 + a_e                          [Eq. gamma_anomaly_relation]
  Omega = (1/2c^2)[a x v]                 [Eq. Thomas1]

================================================================================
END OF README
================================================================================
