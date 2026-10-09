================================================================================
From Zero and One to the Electron: Path-Connectedness, the Double Cover,
and the Geometric Origin of the Quartic Energy in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: October 10, 2026
DOI: 10.5281/zenodo.23257458

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file and the numerical-verification
script for a research paper of the 0-Sphere Model series (paper #65):

1. main.tex
   - Main LaTeX source file (35 pages, 22 figures drawn in TikZ, 15 tables,
     100 references)
   - Document class: REVTeX 4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

2. verify65.py
   - Python 3 script with the seven numerical checks of Appendix A:
     (1) the two solution sets and the harmonicity criterion {0, 1, 2};
     (2) the first-order equation i d(chi)/dt = (omega/2) sigma_y chi;
     (3) the two Dirac branches and the interference identity
     n_A = 1/4 + 1/4 + (1/2)cos(omega t); (4) the quartic as a Hopf pullback;
     (5) the Wronskian Q = +/-1; (6) the mod-4 character W = chi_4(q) for
     coprime odd pairs below 40; (7) beta from a_e, the two clock
     frequencies and their ratio beta, and lambda_C = beta c T_tr.
   - Requires Python 3 and NumPy.
   - Run:  python3 verify65.py   (prints "all checks passed")

3. zenodo_23257458.pdf
   - Compiled paper (35 pages).

4. zenodo_23257458_relations.txt
   - Zenodo related-identifier list of this record (relations to earlier
     papers of the series, with reasons) and the recommended reverse
     relations.

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
  revtex4-2, graphicx, bm, physics, caption, microtype, ragged2e, booktabs,
  enumitem, amsthm, listings, xcolor, tikz (libraries: arrows.meta, calc,
  3d, shadings, positioning, decorations.pathmorphing), hyperref (loaded by
  REVTeX)

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex
  pdflatex main.tex

Note: The bibliography is embedded (thebibliography); no BibTeX run is
      needed. Three passes are recommended so that the table of contents,
      cross-references, and hyperlinks are all resolved.

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

This paper traces where the integers of a model of the electron come from.
The model is the 0-Sphere model, in which the electron is two separated
kernels exchanging a captured photon. We start from arithmetic:
the integers are fixed by 0 and 1, the numbers that do not change when
squared are exactly {0, 1}, and the invertible integers are {+1, -1}, which
is the zero-sphere S^0. The model's two energy identities share the
right-hand side 1, yet the bosonic identity n_A + n_B = 1 is solved by a
whole segment D^1, whereas the kernel part of the fermionic identity
(n_A + n_B)^2 = 1 is solved only by the two endpoints, S^0 = boundary of D^1;
the cross term is exactly the seat that lets energy travel between the two
separated points. Path-connectedness therefore enters at the foundations,
and the next topological step, a closed path that is not simply connected,
yields an integer winding number that the model identifies with electric
charge; a point vortex in fluid mechanics gives the picture, and quantized
circulation in superfluids shows that the integer and its size come from
different sources.

We retain and sharpen the earlier results of this paper: the amplitude
behind the identity obeys a first-order spinor equation unitarily equivalent
to the Dirac rest solutions, and the energy exchange between the two kernels
is exactly the interference term between the positive- and negative-energy
branches, so that zitterbewegung is read as a real internal oscillation and
the negative branch as the absorbing half of a paired emission and
absorption rather than as an antiparticle; the complex unit is the
symplectic structure of
the internal oscillator, and the quartic energies are quadratic forms on the
Bloch sphere pulled back through the Hopf double cover. We then define the
internal time as the transport cycle between the kernels, fixed by the
anomalous magnetic moment through beta = 0.04047, show that it runs exactly
beta times slower than the Dirac branch phase, and show that the kernel
separation is the transport speed times one tick, lambda_C = beta c T_tr.
Metric structure is not needed while the two kernels merely sit; it enters
with transport, together with the constitutive relation and the
fine-structure constant. We state explicitly that the model derives the
integer of charge, its existence, quantization, conservation and sign, but
not its size: the fine-structure constant is not derived here, nor is the
coupling to the electromagnetic potential or the light-cone structure. The
decisive test is experimental: the internal transport speed
beta c ~ 0.04 c, fixed with no free parameter, is unmeasured and would
confirm or exclude the internal clock.

Key topics include:
- Arithmetic of 0 and 1: idempotents {0, 1}, units {+1, -1} = S^0
- Two solution sets of one normalization: segment D^1 and its boundary S^0
- Path-connectedness and the Helmholtz decomposition in three layers
- Charge as a protected winding number (Wronskian Q = (2/omega)(a b' - b a'))
- Detuned kernels and the mod-4 Dirichlet character W = chi_4(q)
- Rest-frame Dirac equivalence and the Hopf pullback of the quartic energy
- Zitterbewegung as the interference of the two Dirac branches; a reading
  of negative energy without antiparticles
- The double cover drawn as a Riemann surface of the square root
- Internal time as the transport cycle; distance from the clock
- Pre-metric electrodynamics: where the metric and alpha enter
- Experimental test: internal transport speed beta c ~ 0.04 c

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper replaces the unpublished working draft of #65 and builds upon:

Primary references (continued):
1. "The Square Root of the Hyperspherical Laplacian: A Geometric Foundation
   for Spin Two-Valuedness on S^3" (Zenodo 2026)
   DOI: 10.5281/zenodo.20820646

2. "Redefining Electron Spin and Anomalous Magnetic Moment Through Harmonic
   Oscillation and Lorentz Contraction" (Zenodo 2024)
   DOI: 10.5281/zenodo.17764997

3. "Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of
   the Spacetime Metric in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.20388056

Results used as inputs:
4. "Geometrical Confinement of Energy in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.18356895
5. "Electron Interference from Internal Geometry: Two-Kernel SU(2)
   Structure, Quartic Energy Flow, and an Intrinsic Visibility Limit"
   (Zenodo 2026)
   DOI: 10.5281/zenodo.18718174
6. "The Bridge Equation gamma = 1 + a from First Principles" (Zenodo 2026)
   DOI: 10.5281/zenodo.20091680
7. "Emergent Conservation Laws from Internal Geometry" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765244
8. "Rotation from Scalar Oscillation" (Zenodo 2026)
   DOI: 10.5281/zenodo.19482145
9. "From Clock Synchronization to Electromagnetism: A Realist Construction
   of U(1) Gauge Theory" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765136

Foundational framework (0-Sphere Model series):
10. "A Model of an Electron Including Two Perfect Black Bodies"
    (Zenodo 2018)
    DOI: 10.5281/zenodo.16759284

The paper merges the earlier #65 results (rest-frame Dirac equivalence,
symplectic origin of i, quartic energy as a Hopf pullback) with a new
topological thread from the arithmetic of 0 and 1 to the winding number of
charge, and grounds the internal time in the transport rate of #10.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:
- The idempotents of the integers are {0, 1} and the units are
  {+1, -1} = S^0; the integers themselves are generated by 1.
- One normalization, two pictures: n_A + n_B = 1 is solved by the segment
  D^1, the kernel part of (n_A + n_B)^2 = 1 only by its boundary S^0; the
  cross term 2 n_A n_B is the transit seat (Proposition III.1).
- Charge as a winding number: the Wronskian Q = (2/omega)(a b' - b a') of
  the locked, normalized kernel pair is conserved (Abel), quantized (+/-1)
  and bounded (|Q| <= 1, Cauchy-Schwarz); its sign is the sign of charge.
- Lock and normalization go together: the gap of the amplitude curve from
  the origin is sqrt(1 - |sin delta|), so only delta in {0, pi} keeps the
  winding protected.
- Detuned pairs: W = chi_4(q), the mod-4 Dirichlet character, taking only
  the values {0} together with S^0 (checked for all coprime odd pairs up to
  301).
- The kernel rotor obeys i d(chi)/dt = (omega/2) sigma_y chi, unitarily
  equivalent to the Dirac rest solutions (Theorem VI.1); the complex unit is
  the symplectic structure of the oscillator.
- The quartic energies are quadratic Bloch forms pulled back through the
  Hopf double cover (Proposition VI.2).
- The occupation of each kernel splits into a constant part from each Dirac
  branch alone and a cross term between them, n_A = 1/4 + 1/4 +
  (1/2)cos(omega t): the energy exchange between the kernels, i.e.
  zitterbewegung, is the interference of the positive- and negative-energy
  branches. The sign of an energy eigenvalue is read as the sign of a
  frequency, registered in the kernel frame as the paired opposite rates
  dn_A/dt = -dn_B/dt (emission and absorption).
- In the degree match with the Dirac polynomial (E^2 - E_p^2)^2, the sign
  factor is structural; only the spin factor remains open.
- Internal time: transport rate beta m c^2/hbar = 5.0007e18 Hz with
  beta = 0.0404720 from a_e; exactly beta times the branch phase
  m c^2/hbar = 1.2356e20 Hz.
- Distance from the clock: lambda_C = beta c T_tr, T_tr = 1.9997e-19 s.

What the model CANNOT currently derive:
- The size of the charge: the fine-structure constant alpha is not derived.
- The coupling of the winding number to the electromagnetic potential.
- The light-cone structure (a tensor refractive index of the thermal
  geodesic would be needed).
- The spin factor of the degree match with the Dirac polynomial.
- Whether charge and spin are separate degrees of freedom or share one
  orientation of the internal rotation.

Statements are marked [standard] or [0SM reading] throughout, so that a
reader can accept the standard mathematics and still reject the model. The
decisive test is experimental: the internal transport speed beta c ~ 0.04 c.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section I: Introduction
  I.A  Integers in physics and in the model
  I.B  The model in one paragraph
  I.C  Four results of this paper
  I.D  Conventions: three layers and two kinds of statement
  I.E  What goes in and what comes out
  I.F  Organization of the paper

Section II: Zero and One: The Arithmetic Seed
  II.A The integers are fixed by 0 and 1
  II.B The numbers that do not change when squared
  II.C The invertible integers form the zero-sphere
  II.D Where the standard theory gets its integers

Section III: One Normalization, Two Pictures
  III.A The same one, read at two degrees
  III.B A worked example: one full turn, step by step
  III.C Where can the kernels alone carry the whole?
  III.D Two solution sets: a segment and its two ends
  III.E Which degree? Two independent criteria
  III.F What does not separate them

Section IV: Path-Connectedness: Joining Two Separated Points
  IV.A From two points to a connected domain
  IV.B Gradients, curls, and the first layer of the Helmholtz decomposition

Section V: Closing the Path: Winding Numbers and Charge
  V.A  From the segment to the circle
  V.B  A worked example from fluid mechanics: the point vortex
  V.C  Charge as a protected winding number
  V.D  Worked examples: winding numbers of detuned pairs
  V.E  The integer and its size come from different places

Section VI: The Quartic Energy as a Pullback of Quadratic Bloch Forms
  VI.A The kernel rotor and its first-order equation
  VI.B Unitary equivalence to the Dirac rest solutions
  VI.C Zitterbewegung as the interference of the two branches
  VI.D The complex unit is generated by the oscillator
  VI.E The fourth power is a quadratic form on the Bloch sphere
       (the double cover drawn as a Riemann surface)
  VI.F Where temperature lives
  VI.G Degree matching with the Dirac equation
  VI.H Relation to the square-root construction on S^3

Section VII: Internal Time: The Transport Cycle
  VII.A The half-angle from kinematics
  VII.B The anomalous magnetic moment fixes the rate
  VII.C Two clocks, exactly beta apart
  VII.D Proper time and background independence
  VII.E Distance from the clock
  VII.F Frequency ledger

Section VIII: Where the Metric Enters: Comparing Two Clocks
  VIII.A Two of Maxwell's equations need no metric
  VIII.B Comparing two electrons
  VIII.C From two points to a field: a research ladder
  VIII.D Distance, the constitutive relation, and alpha enter together

Section IX: What Experiment Can Decide
Section X: Distance from Standard Theory
Section XI: Conclusion

Acknowledgments

Appendices:
  A. Numerical Verification (verification map and seven code blocks)
  B. The Bloch Map and the Derivation of the Quartic
  C. Words That Split in Two
  D. Derivation: Charge as a Protected Winding Number
  E. Mathematical Terms in Plain Words (glossary)

References (100 entries, ordered by first citation)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "From Zero and One to the Electron: Path-Connectedness, the Double Cover,
   and the Geometric Origin of the Quartic Energy in the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.23257458

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (October 10, 2026)
  - Initial release. Replaces the unpublished working draft of #65
    (July 2026) with a merged paper:
  - Arithmetic of 0 and 1 and the two solution sets D^1 and S^0
  - Path-connectedness and charge as a protected winding number
    (with a full derivation in Appendix D)
  - Rest-frame Dirac equivalence and the Hopf pullback (retained)
  - Internal time as the transport cycle; distance from the clock
  - Pre-metric electrodynamics and an explicit statement of scope
    (the integer of charge is derived, alpha is not)
  - Zitterbewegung as the interference of the two Dirac branches and a
    reading of negative energy without antiparticles
  - The double cover drawn as the Riemann surface of the square root
  - Numerical verification script verify65.py

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a limited
supportive role, for organizing the presentation of the text and for checking
grammar and wording during document preparation. All physical
interpretations, methodological judgments, and philosophical commitments
remain the responsibility of the author.

The scientific content, conceptual framework, arguments, and the structure of
the paper and of its text were conceived and developed by the author, who
assumes full responsibility for all claims and interpretations herein.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: REVTeX 4-2 (APS/PRB reprint, two-column)
Page layout: REVTeX default; abstract and table of contents on the first
             pages, body from page 3
Line spacing: REVTeX default
Font: Computer Modern (LaTeX default)

Tables:
  - Table I:    Inputs and outputs of the argument (Sec. I.E)
  - Table II:   Symbols used in this paper and their layer (Sec. I.F)
  - Table III:  Four integers of established physics and their sources (II.D)
  - Table IV:   One full turn of the internal angle in steps of pi/2 (III.B)
  - Table V:    Kernel seats and transit seat (III.C)
  - Table VI:   What the model derives about charge, and what it does not (V.C)
  - Table VII:  Winding numbers of detuned kernel pairs (V.D)
  - Table VIII: The two internal clocks of the electron (VII.C)
  - Table IX:   Frequency ledger of the internal oscillation (VII.F)
  - Table X:    Maxwell's equations sorted by metric need (VIII.A)
  - Table XI:   The ladder from a single comparison to a field (VIII.C)
  - Table XII:  Three layers of the electron and what enters at each (VIII.D)
  - Table XIII: Experimental handles on the claims of this paper (Sec. IX)
  - Table XIV:  Open problems and where each enters (Sec. X)
  - Table XV:   Mathematical terms used in the paper (App. E)

Figures:
  - 22 figures, all drawn in TikZ inside main.tex (no external image files)

Code listings:
  - Seven Python code blocks in Appendix A (listings package); the same code
    is shipped as verify65.py

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
