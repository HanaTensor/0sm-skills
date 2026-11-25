================================================================================
From Thermal Rays to Matter Waves:
The Hamilton Analogy, Phase and Group Indices, and the Schrodinger Envelope
in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: [DATE-67]
DOI: [DOI-67]

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file and the numerical-verification
script for a paper of the 0-Sphere Model series (paper #67):

1. main.tex
   - Main LaTeX source file (11 pages, 1 figure drawn in TikZ, 3 tables,
     16 references)
   - Document class: REVTeX 4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025
   - Appendix A reads verify67.py with \lstinputlisting, so verify67.py
     must sit in the same folder as main.tex when compiling.

2. verify67.py
   - Python 3 script that reproduces every number of the paper:
     (1) beta_ZB, 1/beta_ZB, 2/beta_ZB, lambda_C, nu_C, nu_ZB and the line
     energies 20.68 keV and 41.36 keV;
     (2) the de Broglie wavelength at v_ZB (59.90 pm, 419.0 eV), the
     vacuum wavelength of the internal line (59.95 pm), the number of
     de Broglie wavelengths per round trip gamma*beta_ZB = 0.0405, and the
     proper-time deficit 1 - 1/gamma = 8.2e-4;
     (3) the mass m_e/(gamma*beta_ZB) = 24.7 m_e of a dispersive carrier that
     also closes on the round trip;
     (4) the imaginary diffusivity hbar/2m_e = (lambda_C/2)(c/2 pi);
     (5) the doubling time of a free Schrodinger packet of width lambda_C,
     T nu_ZB = 0.44 (a/lambda_C)^2, and the widths at which it reaches one
     half and one internal cycle;
     (6) the dipole radiation at nu_ZB for classical amplitudes lambda_C/4
     and lambda_C/2;
     (7) the Rayleigh suppression factor at 2.33 eV;
     (8) the Fourier components of cos^4(theta/2) (3/8, 1/2, 1/8) and of the
     product of two shares with unequal rates (1/4, 1/8, 1/4, 1/4, 1/8).
   - Requires Python 3 only (standard library: math, cmath).
   - Run:  python3 verify67.py

3. [PDF-67]
   - Compiled paper (11 pages).

4. [RELATIONS-67]
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
  - Main document: main.tex (upload verify67.py to the same folder)
  - Compiler: pdfLaTeX
  - TeX Live version: 2025
  - Compile mode: Normal
  - Stop on first error: ON (recommended)
  - Autocompile: ON (optional)

================================================================================
ABSTRACT
================================================================================

Hamilton's analogy places classical mechanics beside geometrical optics and
wave mechanics beside wave optics, and Schrodinger's equation was obtained by
taking the step from the first pair to the second. The 0-Sphere model has so
far stood on the first rung: internal energy transport follows thermal
geodesics of an optical metric, and the accumulated internal phase is a
Hamilton principal function of the arc between the two kernels. This paper
takes the second step.

Writing the internal wave as A exp(iS/hbar) separates, order by order in
hbar, a Hamilton-Jacobi equation for the phase from a continuity equation for
A^2 transported at the group velocity, and thereby separates two refractive
indices that the series had identified: a phase index governing stationary
phase and a group index governing energy transport. The group index
n_g = 1/beta_ZB = 24.71 does not depend on the origin of energy; the phase
index of a matter wave does, taking the value beta_ZB when the rest energy is
kept and 2/beta_ZB when it is removed.

The closure of the internal cycle on a round trip of length lambda_C fixes
the ratio of the two indices of the internal carrier, not its dispersion. A
body of mass m_e making the round trip at v_ZB holds 0.0405 of its
de Broglie wavelength and does not close, so that the internal carrier is not
the de Broglie wave of the electron's mass. If the carrier is taken
non-dispersive in its lowest mode and its phase is counted with the internal
phase theta, the dynamical phase of the series accumulates 2 pi per round
trip and the action is J = h; counted with the half angle theta/2 of the
amplitude, which carries the double cover of the spinor, the same round trip
gives J = h/2.

Factoring out the rest-energy frequency nu_C = m_e c^2 / h, which de Broglie
attached to the electron as an internal periodic phenomenon, leaves an
envelope that obeys the Schrodinger equation, a heat equation with imaginary
diffusivity hbar/2m_e = (lambda_C/2)(c/2 pi). The result is a two-tier
structure: an external envelope with a continuous spectrum, whose spreading
is real, and an internal transfer with a discrete spectrum fixed by the
energy identity, which a free Schrodinger packet of Compton size could not
sustain, since such a packet doubles its width within 0.44 of one internal
cycle. Because the internal phase advances uniformly, the quartic energy
contains only the harmonics 0, nu_ZB and 2 nu_ZB (41.36 keV); written as the
density of a product of two amplitudes, it shows that unequal rates of the
two factors would split the first line and add sum and beat lines. The
internal transfer may not oscillate the charge dipole, and an electron of
kinetic energy 419 eV carries the momentum of a 20.7 keV photon.

Key topics include:
- Hamilton's analogy: the ray layer of the series and the step to waves
- The eikonal expansion: phase at order hbar^0, intensity at order hbar^1
- Phase and group indices; the phase index depends on the origin of energy
- Closure of the internal cycle fixes n_ph / n_g, not the dispersion
- J = h (count theta) or J = h/2 (count theta/2), stated as an open choice
- The Schrodinger equation as the envelope of the rest-energy carrier
- Two tiers and the Gordon decomposition of the Dirac current
- Discrete group velocity, the correspondence principle and Heisenberg's
  multiplication rule
- The charge dipole may not oscillate; Thomson scattering and the
  two-tier structure

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper builds upon:

Primary references (continued):
1. "Helical Trajectory, Fixed-Endpoint Line Integrals, and the Emergence of
   the Spacetime Metric in the 0-Sphere Model" (version 3, Zenodo 2026)
   DOI: 10.5281/zenodo.24521440

2. "Subluminal Zitterbewegung and the Invariant Speed: An Internal
   Refractive Index for the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.23750210

Results used as inputs:
3. "From Zero and One to the Electron: Path-Connectedness, the Double Cover,
   and the Geometric Origin of the Quartic Energy in the 0-Sphere Model"
   (Zenodo 2026)
   DOI: 10.5281/zenodo.23257458
4. "Thermal Geodesics in the 0-Sphere Model: Extending General Relativity
   through Internal Thermodynamic Structure" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765349
5. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo 2025)
   DOI: 10.5281/zenodo.18067760

Foundational framework (0-Sphere Model series):
6. "A Model of an Electron Including Two Perfect Black Bodies"
   (Zenodo 2018)
   DOI: 10.5281/zenodo.16759284

The presentation of Hamilton's analogy, of the eikonal expansion and of the
correspondence principle follows H. Yukawa, Introduction to Quantum Mechanics
(Kobundo, 1954; Osaka University Press, 2021), whose equation numbers are
cited where a specific step is used.

================================================================================
KEY RESULTS
================================================================================

What the paper establishes:
- R1. The eikonal expansion separates the phase (Hamilton-Jacobi, phase
  index) from the intensity (continuity at the group velocity, group index);
  the two rows of the geodesic hierarchy of #51 are its two lowest orders.
- R2. The group index 1/beta_ZB is independent of the origin of energy; the
  phase index of a matter wave is beta_ZB with the rest energy kept and
  2/beta_ZB with it removed.
- R3. The closure of the internal cycle fixes the ratio n_ph / n_g = N of
  the indices of the internal carrier; a body of mass m_e moving at v_ZB does
  not close. For the non-dispersive lowest mode with its phase counted by
  theta, the dynamical phase accumulates 2 pi per round trip and J = h;
  counted by theta/2, J = h/2.
- R4. Factoring out nu_C leaves an envelope obeying the Schrodinger
  equation, a heat equation with imaginary diffusivity (lambda_C/2)(c/2 pi).
- R5. Two tiers: external envelope (continuous, spreading, convective
  current) and internal transfer (discrete, restored, spin current); a free
  Schrodinger packet of width lambda_C doubles in 0.44 of an internal cycle.
- R6. The uniform advance of theta places the second Fourier component of
  the energy at exactly 2 nu_ZB. Written as the density of a product of two
  amplitudes, non-identical factors would give lines at omega_A, omega_B,
  omega_A + omega_B and |omega_A - omega_B|.
- R7. The internal transfer may not oscillate the charge dipole; a free
  electron would otherwise lose its rest energy within 1e-13 s.

What the paper does not derive (open items):
- O1. The count of the internal phase (theta, giving J = h, or theta/2,
  giving J = h/2) and the non-dispersive lowest mode, on which R3 rests.
- O2. A derivation of the rest energy m_e c^2, and with it of the dispersion
  relation of the whole electron, from the internal transfer.
- O3. The physical identity of the two factors of the product in R6, and
  whether a detuning of the kernels appears as the shifted and beat lines.
- O4. The layer (bilinear or quartic) with which the Dirac frequency is to
  be compared, and the rate carried by the phase of a Dirac branch.
- O5. The bound on an internal resonance near 20.7 keV from existing
  Compton-scattering data.
- O6. The recoil closure suggested by the momentum identity, including
  whether the vacuum or the medium momentum enters it.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section I:    Introduction (Scope)
Section II:   The Ray Layer of the Series
Section III:  From Rays to Waves: Phase and Intensity
Section IV:   Phase and Group Indices
Section V:    Carrier and Envelope: the Schrodinger Equation
Section VI:   Two Tiers: External Envelope and Internal Transfer
Section VII:  Discrete Group Velocity and the Correspondence Principle
Section VIII: Consequences and Constraints
Section IX:   Limitations
Section X:    Conclusion

Appendices:
  A. Numbers and Their Reproduction (code listing of verify67.py)
  B. Inputs, Results and Open Items (I1-I3, R1-R7, O1-O6)

Acknowledgments

References (16 entries, ordered by first citation)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "From Thermal Rays to Matter Waves: The Hamilton Analogy, Phase and Group
   Indices, and the Schrodinger Envelope in the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/[DOI-67]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 ([DATE-67])
  - Initial release:
  - Hamilton's analogy carried from the ray layer of the series to the wave
    layer
  - Eikonal expansion: phase and intensity, phase and group indices
  - Closure of the internal cycle; J = h or h/2 according to the count of
    the internal phase
  - Schrodinger equation as the envelope of the rest-energy carrier
  - Two-tier structure and the Gordon decomposition
  - Discrete group velocity, correspondence principle, product density of
    the quartic energy
  - Constraints: charge dipole, Thomson scattering, momentum identity
  - Inputs, results and open items listed for citation by later papers
  - Numerical verification script verify67.py

================================================================================
ACKNOWLEDGMENTS
================================================================================

The conception of this paper, the framing of its questions and every
decision to adopt or reject a result are the author's. The author selected
and read Yukawa's Introduction to Quantum Mechanics against the series in
working sessions with the language model Claude Opus 5.5 (Anthropic), which
drafted the manuscript, proposed derivations and literature precedents,
carried out numerical checks, and, as a separate instance given only the
manuscript and its sources, reviewed the draft adversarially. Every
derivation adopted here was checked by the author and is reproduced by the
verification script deposited with this paper.

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
  - Table I:   Correspondences between the eikonal treatment of wave
               mechanics and the 0-Sphere model (Sec. III)
  - Table II:  Phase and group indices of a wave moving at the internal
               speed v_ZB = beta_ZB c (Sec. IV)
  - Table III: Derivatives and their difference quotients over discrete
               values (Sec. VII)

Figures:
  - Fig. 1: Carrier, external envelope and internal transfer
  - Drawn in TikZ inside main.tex (no external image files)

Code listings:
  - Appendix A includes verify67.py with \lstinputlisting (listings
    package)

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
  - Additional file required: verify67.py (read by Appendix A); figures are
    TikZ and the bibliography is embedded

================================================================================
END OF README
================================================================================
