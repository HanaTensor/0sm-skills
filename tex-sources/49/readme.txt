================================================================================
Photon-Sphere Fragmentation as a Gravitational Mediator:
Radiation-Gradient Ejection in the pi-Cycle of the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email:  hana.tensor@gmail.com
Date:   April 4, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for a research paper in the
0-Sphere Model series proposing a microscopic gravitational-mediation mechanism:

1. main.tex
   - Main LaTeX source file (single self-contained file)
   - Document class: revtex4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (all included in standard TeX distributions):
    graphicx, bm, physics, hyperref, caption, microtype, ragged2e,
    booktabs, enumitem, amsthm, xcolor, tikz
  TikZ libraries:
    arrows.meta, calc, 3d, shadings, positioning,
    decorations.pathmorphing, decorations.markings, shapes.geometric

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references,
      equations, and hyperlinks.

Alternatively, use Overleaf with the following settings:
  - Main document:      main.tex
  - Compiler:           pdfLaTeX
  - TeX Live version:   2025
  - Compile mode:       Normal
  - Stop on first error: ON (recommended)
  - Autocompile:        ON (optional)

================================================================================
ABSTRACT
================================================================================

The 0-Sphere model identifies a photon-sphere ejection mechanism driven by
Thomas precession, understood in the kinematic sense formulated by Tomonaga:
whenever a body undergoes accelerated motion at relativistic speed, its proper
coordinate frame rotates relative to the laboratory frame even under the
condition of parallel-axis transport. The photon sphere executes simple harmonic
motion between Kernels A and B along the A-to-B thermal geodesic; at the
midpoint theta = pi/2 the kinetic energy peaks at E_0/2, exactly saturating the
geometric binding floor imposed by the Hamiltonian identity. The ground state
n = 0 is the reference case: emitting (1/2)hbar*omega would violate energy
conservation, so no fragment is released. For excited states n >= 1, each
de-excitation n -> n-1 ejects a fragment carrying hbar*omega, with n+1 ejection
opportunities per traversal corresponding to the n+1 antinodes of the
standing-wave mode. Zitterbewegung drives the cascade n -> n-1 -> ... -> 0,
providing a microscopic origin of entropic cooling; the ejected fragments mediate
phase synchronization between neighboring subsystems, identified in Paper #34 as
gravitational-like acceleration.

The geometric floor E_0/2 provides a fourth independent derivation of the
zero-point energy (1/2)hbar*omega, complementing the three routes established in
Papers #46 and #48 (uncertainty principle, AM-GM inequality, centroid geometry).
The ejection threshold coincides with this floor, and the ejected fragment
carries the pi-periodic phase structure of Omega_T proportional to
(1/2)sin(2*theta), providing the physical ejection mechanism underlying the
spin-2 candidate of Paper #48; the rank-2 tensor proof remains an open task.

A geometric ultraviolet cutoff emerges from the modal structure. Re-absorption
of an ejected fragment by the same electron constitutes the 0-Sphere counterpart
of a QED self-energy loop; the total number of such loops per cycle is bounded
by n_max + 1. Because the parabolically widening harmonic-oscillator well is
constrained by the fixed Compton-scale extent of the Kernel A-B well, n_max is
finite---in structural analogy with the finite Rydberg spectrum of hydrogen---
and the self-energy sum is naturally finite without regularization.

Key topics include:
- Thomas precession as kinematic inevitability of ZB-driven acceleration
- Geometric origin of the gravitational ejection threshold at theta = pi/2
- Photon-sphere fragment as gravitational mediator (no new degrees of freedom)
- Reinterpretation of the quantum harmonic oscillator spectrum
- Structural ultraviolet cutoff from Compton-scale mode quantization
- Closure of three open questions from Paper #34

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper is Paper #49 in the 0-Sphere Model series. It directly continues and
extends the following papers:

Primary references (cited in this work):
1. "Geometrical Confinement: Emergent Gravitational Dynamics" (#34, 2026)
   DOI: 10.5281/zenodo.18437010

2. "Geometric Origin of the One-Half Factor" (#46, 2026)
   DOI: 10.5281/zenodo.19010945

3. "Geometric Origin of g=2 in the 0-Sphere Model" (#48, 2026)
   DOI: 10.5281/zenodo.19227518

4. "A Model of an Electron Including Two Perfect Black Bodies" (#1, 2018)
   DOI: 10.5281/zenodo.16759284

5. "Spin as a Real Vector: Geometric Origin of U(1) Gauge and SU(2)" (#19, 2025)
   DOI: 10.5281/zenodo.17765238

6. "Geometrical Confinement: Rest Mass and Zitterbewegung" (#33, 2026)
   DOI: 10.5281/zenodo.18356895

7. "Redefining Electron Spin and AMM" (#10, 2023)
   DOI: 10.5281/zenodo.17764997

8. "Rotational Lorentz Contraction as Geometric Origin of AMM" (#47, 2026)
   DOI: 10.5281/zenodo.19120057

This paper provides the microscopic ejection mechanism left open in Paper #34,
and supplies the physical realization of the pi-periodic ejection structure
whose existence Paper #48 identified as a prerequisite for a full spin-2
derivation. The zero-point energy reinterpretation extends Paper #46's
AM-GM result to an ejection-threshold interpretation (fourth independent route).

================================================================================
KEY RESULTS
================================================================================

What the model establishes in this paper:
- Thomas precession naturally arises from ZB-driven acceleration (Tomonaga
  mechanism), not from geometric path curvature
- Ejection occurs at theta = pi/2 where photon-sphere KE saturates the
  geometric binding floor E_0/2 (established in Papers #46 and #48)
- n = 0 ground state emits no fragment (Hamiltonian identity forbids it)
- Each de-excitation n -> n-1 releases one quantum hbar*omega as an ejected
  photon-sphere fragment (the gravitational mediator of Paper #34)
- n-th excitation mode has n+1 ejection opportunities per A-to-B traversal
- The photon-sphere excitation number is bounded above by n_max (geometric UV
  cutoff structurally analogous to the Debye cutoff in lattice phonon theory)
- Zero-point energy (1/2)hbar*omega arises from four independent routes:
  Heisenberg uncertainty, AM-GM inequality, centroid geometry, ejection threshold

What the model cannot currently derive (open tasks):
- Quantitative derivation of Thomas-precession outward stress from first
  principles (thermal geodesic geometry and stress-to-force mapping)
- Rank-2 tensor transformation proof for the ejected fragment (spin-2 proof)
- Quantitative value of n_max and its relation to known QED scales
- Forward derivation: Thomas precession -> v_ZB -> a_e (without measured a_e)
- 1/r^2 long-range scaling from near-neighbor ejection events
- Spherical harmonic mode assignment for excitation levels n

All results are geometric-structural; empirical predictions of quantum mechanics
are reproduced exactly. This work is a geometric reinterpretation, not a
modification of quantum mechanical predictions.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Synopsis (unnumbered): Organization overview

Section 1: Introduction
  - Gravitational-mediation background and open questions from Paper #34
  - Companion paper #48 and the spin-2 candidate
  - Tennis-ball analogy and Tomonaga-Thomas precession justification
  - Zero-point energy reinterpretation
  - Structural UV cutoff

Section 2: The Hamiltonian Identity and the Geometric Zero-Point Energy
  2.1 The Three-Component Energy Identity
      (E_0 = Te_1 + Te_2 + E_ph; three-component Hamiltonian postulate)
  2.2 Algebraic Origin of the Zero-Point Floor
      (AM-GM inequality; floor cos^4 + sin^4 >= E_0/2)
  [Figure 1: QM vs 0-Sphere harmonic oscillator spectrum]
  [Table 1: Zero-point energy comparison]

Section 3: Simple Harmonic Motion and the Ejection Mechanism
  3.1 The pi-Cycle: One-Way Traversal as a Half Oscillation
  3.2 Hydrostatic Equilibrium, Electromagnetic Binding, and Ejection Threshold
    3.2.1 Hydrostatic Equilibrium Analogy and Thomas-Precession Stress
            (Tomonaga mechanism; radiation-gradient acceleration; v x a != 0)
    3.2.2 Entropy Increase as the Thermodynamic Driver
            (n=0 reference; n>=1 actual ejection; modal structure)
    [Figure 2: Standing-wave excitation modes n=0,1,2,3]
    3.2.3 Zitterbewegung as a Cooling Engine
            (cascade n->0; detailed balance; gravity as macroscopic consequence)
  3.3 Connection to the Thomas Angular Velocity and the pi Period
      (Omega_T periodicity; spin-2 candidate of Paper #48)
  [Figure 3: Kinematic profiles and ejection threshold]

Section 4: Ejected Fragment as Gravitational Mediator
  4.1 Propagation and Synchronization
  4.2 Gravitational Interaction Without an Independent Mediator
  [Table 2: Conventional graviton vs 0-Sphere photon-sphere fragment]

Section 5: Geometric Ultraviolet Cutoff from Compton-Scale Mode Quantization
  5.1 Finite Mode Spectrum: Existence of n_max
  5.2 Structural Comparison with Ultraviolet Renormalization
  5.3 Analogy with Atomic Ionization and Rydberg States
  5.4 Scope of the Compton-Scale Cutoff: Free and Bound Electrons

Section 6: Relation to Prior Work
  6.1 Successor to Paper #34: Microscopic Origin of Entropic Entrainment
  6.2 Companion to Paper #48: Physical Realization of the pi-Periodic Structure

Section 7: Open Questions and Scope
  (Ten open questions labeled i through x)

Section 8: Conclusion

Appendix A: Elements of Effective Field Theory and the Compton-Atomic Scale
            Hierarchy (scale separation, Wilsonian RG, Lamb shift, AMM,
            proton as open question)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Photon-Sphere Fragmentation as a Gravitational Mediator:
   Radiation-Gradient Ejection in the pi-Cycle of the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.[TO BE ASSIGNED]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (April 4, 2026)
  - Initial release
  - Establishes photon-sphere ejection mechanism via Tomonaga-Thomas precession
  - Closes three open questions of Paper #34
  - Provides physical ejection mechanism for Paper #48 spin-2 candidate
  - Identifies structural UV cutoff from Compton-scale mode quantization

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of a large language model (Claude Sonnet 4.6,
Anthropic) as a supplementary tool for clarifying and structuring background
descriptions of effective field theory (EFT) in the Appendix.
All physical interpretations, theoretical claims, and conclusions are the sole
responsibility of the author.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format:    LaTeX source (.tex)
Document class: revtex4-2, reprint, APS/PRB format
Figures:        Three TikZ figures (compiled inline; no external image files)

Tables:
  Table 1: Zero-point energy 1/2*hbar*omega: comparison of origins in
           conventional QM and the 0-Sphere model (6 rows)
  Table 2: Structural comparison: conventional graviton hypothesis vs
           0-Sphere photon-sphere fragment (7 rows)

TikZ figures:
  Fig. 1: Reinterpretation of the QM harmonic oscillator spectrum (side-by-side
          QM vs 0-Sphere, n=0..3, with wavefunction profiles)
  Fig. 2: Standing-wave excitation modes between Kernels A and B (soap-bubble
          schematic + potential well with n=0..3 standing waves)
  Fig. 3: Photon-sphere ejection mechanism: kinematic profiles (KE, speed,
          Omega_T) and ejection threshold condition (bottom panel)

Cross-references:
  - Section and subsection labels for internal navigation
  - Equation numbering: section-prefixed (e.g., Eq. 3.1)
  - Hyperlinked bibliography with DOI links (hyperref, colorlinks)

Compilation:
  - First pass:  resolves most content
  - Second pass: resolves all cross-references and hyperlinks

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

Compiler Settings:
  Main document:        main.tex
  Compiler:             pdfLaTeX
  TeX Live version:     2025
  Compile mode:         Normal

Error Handling:
  Stop on first error:  ON (recommended for debugging)
  Autocompile:          ON (optional, for real-time preview)

The document has been tested and compiles successfully with these settings.

================================================================================
END OF README
================================================================================
