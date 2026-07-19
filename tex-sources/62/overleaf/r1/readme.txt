================================================================================
The Bridge Equation gamma = 1 + a from First Principles:
Representation Duality of the Anomalous Moment and the Geometric
Origin of the Root-Mean-Square Factor in the 0-Sphere Model
================================================================================

Author: Satoshi Hanamura
Email : hana.tensor@gmail.com
Date  : June 13, 2026
DOI   : 10.5281/zenodo.20091680

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source for a First-Principles Foundation
paper that grounds both ends of the 0-Sphere Model's bridge equation:
the meaning of the input a (the anomalous magnetic moment) and the origin
of the 1/sqrt(2) factor in its velocity-determining form.

1. main.tex
   - Main LaTeX source file (single-file manuscript)
   - Document class: REVTeX 4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-2, amsmath, amssymb, graphicx, bm, physics, hyperref,
    caption, microtype, ragged2e, booktabs, enumitem, amsthm, tikz

Compilation commands:
  pdflatex main.tex
  pdflatex main.tex

Note: Two compilation passes are required for proper cross-references,
      equations, and hyperlinks.

Alternatively, use Overleaf with the following settings:
  - Main document : main.tex
  - Compiler      : pdfLaTeX
  - TeX Live      : 2025
  - Compile mode  : Normal
  - Stop on first error : ON (recommended)
  - Autocompile   : ON (optional)

================================================================================
ABSTRACT
================================================================================

The 0-Sphere model relates the anomalous magnetic moment a of a
spin-1/2 particle to the Lorentz factor of an internal Zitterbewegung
oscillation through the bridge equation gamma = 1 + |a|, with a
velocity-determining variant gamma_v = 1 + |a|/sqrt(2) carrying an
explicit factor of 1/sqrt(2). This work supplies a first-principles
foundation for both ends of that equation: the meaning of the input a
and the origin of the 1/sqrt(2) factor in the transformation.

For the input, the anomalous moment is argued to be a single
frame-independent invariant with two representations: externally, in a
Penning trap, a_e = T_c / T_a is a per-revolution phase slip
accumulated over many cyclotron turns; internally, in the 0-Sphere
model, a_e = (L_0 - L) / L_0 is the rotational Lorentz contraction of
the internal orbital arc. The factor gamma_L = 1 + a_e acts as a
representation translator between a time ratio and a length ratio, in
the same way a single Lorentz boost joins time dilation and length
contraction. The claim boundary is stated with discipline: the
field-independence of a_e is CONSISTENT with an internal-geometric
representation but does not force it, since standard quantum
electrodynamics is equally field-free.

For the transformation, the 1/sqrt(2) factor is shown to be not
imported from an alternating-voltage analogy but contained in the
energy-conservation identity
cos^4(theta/2) + sin^4(theta/2) + (1/2) sin^2(theta) = 1.
The momentum-carrying term gamma*_KE = (1/2) sin^2(theta) has a
time-averaged-to-peak ratio whose square root is exactly 1/sqrt(2);
because the velocity is the square root of this term, identified
through the relativistic decomposition (mc^2/E)^2 + (pc/E)^2 = 1, its
cycle representative is necessarily the root-mean-square (RMS), not
the peak.

The geometric carrier is identified as a pulsating-radius helix with
R(theta) = (1/sqrt(2)) |sin(theta)|, whose squared radius equals
gamma*_KE exactly, vanishes on the kernels, and reaches maximum
amplitude 1/sqrt(2) at the midpoint. The internal winding number is
fixed to unity through an SU(2) (720 degrees) amplitude versus U(1)
(360 degrees) energy phase duality.

The result places the mass-determining peak factor and the
velocity-determining RMS factor on a common footing as two readings of
the same sin^2(theta) partition. The placement of the factor is stated
with the same discipline applied to the input: the ratio derived here
is a velocity-level ratio, whereas the canonical form
gamma_v = 1 + |a|/sqrt(2) places the factor at the level of a; because
the bridge relation is nonlinear, the two placements differ by a
residual factor of 2^(1/4) at the velocity level, and their exact
reconciliation is recorded as an open task rather than asserted.

Key topics include:
- Representation duality of the anomalous moment: external time ratio
  (T_c / T_a, Penning trap) versus internal length ratio
  ((L_0 - L) / L_0, rotational Lorentz contraction)
- Geometric origin of the modulus in gamma = 1 + |a|: the contraction
  deficit depends on v_ZB^2 only and is rotation-sense independent
- Derivation of 1/sqrt(2) as the square root of the average-to-peak
  ratio of the momentum term, replacing the AC-voltage analogy of
  Paper #10
- The pulsating-radius helix R(theta) = (1/sqrt(2)) |sin(theta)| with
  R^2 = gamma*_KE, recovering the kernel stationary points
- Winding number fixed to unity by the SU(2)/U(1) phase duality
  (Paper #19); three routes to 1/sqrt(2) from one sin^2(theta) term
- The a-level versus velocity-level placement of the factor recorded
  as an open correspondence (residual 2^(1/4))
- Line-integral genealogy and the inverse-direction use of geometry
  across the model (appendix)

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper forms a pair with the immediately preceding Paper #61:

  #61 -- APPLICATION: gamma-equation applied to the proton
                      (parameter-free hadronic mass scale)
                      DOI 10.5281/zenodo.19934138
  #62 -- FOUNDATION : first-principles grounding of the bridge
                      equation itself (this paper)
                      DOI 10.5281/zenodo.20091680

Primary references (continues + requires):

1. "Redefining Electron Spin and Anomalous Magnetic Moment Through
    Harmonic Oscillation and Lorentz Contraction" (Zenodo 2023)
   DOI: 10.5281/zenodo.17764997
   -- Source of the bridge equation and of the RMS heuristic. The
      present paper replaces its alternating-voltage analogy with a
      first-principles derivation of the 1/sqrt(2) factor.

2. "Rotational Lorentz Contraction as the Geometric Origin of the
    Anomalous Magnetic Moment in the 0-Sphere Model" (Zenodo 2026)
   DOI: 10.5281/zenodo.19120057
   -- Establishes the internal length-ratio representation
      a_e = (L_0 - L) / L_0. The present paper elevates it into the
      representation duality and derives the modulus as its geometric
      consequence.

3. "Helical Trajectory, Fixed-Endpoint Line Integrals, and the
    Emergence of the Spacetime Metric in the 0-Sphere Model"
    (Zenodo 2026)
   DOI: 10.5281/zenodo.20388056
   -- Supplies the constant-radius helical description of the photon
      sphere, refined here into the pulsating-radius helix.

4. "Application of the gamma-Equation to the Proton: A Parameter-Free
    Hadronic Mass Scale" (Zenodo 2026)
   DOI: 10.5281/zenodo.19934138
   -- Canonical use of the mass-determining (peak) and
      velocity-determining (RMS) forms; the present paper places the
      two on a common footing.

Foundational framework:

5. "A Model of an Electron Including Two Perfect Black Bodies"
   (Zenodo 2018) -- DOI: 10.5281/zenodo.16759284
   -- Foundational paper. Supplies the conservation identity
      cos^4(theta/2) + sin^4(theta/2) + (1/2) sin^2(theta) = 1, the
      two-kernel architecture, and the thermal gradient
      E_0 sin(theta) used to motivate the pulsating radius.

6. "Coexistence of Positive and Negative-Energy States in the Dirac
    Equation with One Electron" (Zenodo 2020)
   DOI: 10.5281/zenodo.17760132
   -- Supplies the relativistic reading of the identity as a
      mass/momentum partition of E^2 = (mc^2)^2 + (pc)^2 and the
      stationary points where the photon-sphere momentum vanishes.

7. "Spin as a Real Vector from Internal Photon-Sphere Motion:
    Geometric Origin of U(1) Gauge and SU(2) Periodicity"
    (Zenodo 2025) -- DOI: 10.5281/zenodo.17765238
   -- Supplies the SU(2) (720 degrees) amplitude versus U(1)
      (360 degrees) energy phase duality that fixes the winding
      number to unity.

Line-integral genealogy (recorded in Appendix B):
Papers #29 (10.5281/zenodo.18067760), #30 (10.5281/zenodo.18819682),
#31 (10.5281/zenodo.18203433), #54 (10.5281/zenodo.19701297), and
#55 (10.5281/zenodo.19800797) establish the reading of internal phase
as a line integral and of observable closed loops as compositions of
open-path residuals, supporting the apparent-loop reading of the
Penning-trap integral.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:

- Representation duality of the input: the anomalous moment as one
  frame-independent invariant carried as an external time ratio
  a_e = T_c / T_a and an internal length ratio a_e = (L_0 - L) / L_0,
  joined by the translator gamma_L = 1 + a_e (Section II).
- Geometric origin of the modulus in gamma = 1 + |a|: the internal
  arc-contraction deficit depends only on v_ZB^2 and is independent
  of the sense of circulation; the length-ratio representation is
  intrinsically non-negative (Section II, Fig. 1).
- Three-scale separation: T_c ~ 10^-12 s, T_a ~ 10^-9 s,
  T_ZB ~ 10^-19 s, with a_e the unique B-independent invariant at the
  intersection of the field-dependent external layer and the
  field-independent internal layer (Section II).
- The identity-intrinsic RMS ratio: the momentum term
  gamma*_KE = (1/2) sin^2(theta) has time average 1/4 and peak 1/2,
  and the square root of their ratio is exactly 1/sqrt(2)
  (Section III, Eq. III.6). Simple-average (2/pi) and naive (1/2)
  alternatives are excluded.
- The pulsating-radius helix R(theta) = (1/sqrt(2)) |sin(theta)| with
  R^2 = gamma*_KE exactly; vanishing on the kernels (recovering the
  stationary points) and maximal (1/sqrt(2)) at the midpoint
  (Section IV).
- Winding number unity for the velocity description, fixed by the
  SU(2)/U(1) phase duality; the unit-winding helical projection
  reproduces 1/sqrt(2) exactly (Section V, Eq. V.3).
- Structural reading of the mass-peak / velocity-RMS asymmetry: peak
  for mass and RMS for velocity are two faces of the same
  sin^2(theta) partition (Section VI).

What the model CANNOT currently derive:

- The a-level placement of the factor: what the identity yields is a
  velocity-level ratio (cycle-representative to peak velocity); the
  canonical form gamma_v = 1 + |a|/sqrt(2) places the factor on a.
  Because the bridge relation is nonlinear, the two placements differ
  by a residual factor of 2^(1/4) at the velocity level
  (0.0405c vs 0.0340c). Their exact reconciliation is recorded as an
  open task, with a candidate route (contraction deficit proportional
  to the transverse helix amplitude) noted without commitment
  (Section III).
- A selection between the internal-geometric and the standard QED
  account of a_e: field-independence is a property of both, and the
  paper claims consistency only, not privilege (Section II).
- Observable connections for two internal ratios: the 3:1
  time-averaged mass-to-momentum partition and the c/2 longitudinal
  cycle representative are recorded and deliberately set aside
  (Appendix C).
- The paper advances a reinterpretation within the special-relativistic
  scope of the Dirac equation, not a new testable prediction; the
  gravitational extension of the framework lies outside its scope
  (Appendix A).

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section I  : Introduction
              - The bridge equation and its two open questions
                (input and transformation)
              - The 2023 AC-analogy placement of 1/sqrt(2) as an
                interpretive placeholder
              - Organization of the paper

Section II : The Anomalous Moment as a Frame-Independent Invariant
              - External representation: per-revolution phase slip
              - Internal representation: rotational length contraction
              - One invariant, two projections (gamma_L translator)
              - Origin of the modulus (rotation-sense independence;
                Fig. 1)
              - Three-scale separation
              - The claim boundary, stated with discipline
              - The apparent loop

Section III: The Momentum Term and the Origin of 1/sqrt(2)
              - Mass/momentum partition of the conservation identity
              - Time average versus peak; the RMS ratio (Eq. III.6)
              - The placement of the factor: an open correspondence
                (residual 2^(1/4))
              - Why the square root forces the RMS

Section IV : The Pulsating-Radius Helix
              - R^2 = gamma*_KE exactly
              - Why the radius must vary (sin(theta) thermal gradient)
              - Recovery of the stationary points
              - Coincidence of the maximum amplitude with the RMS
                factor

Section V  : SU(2) Amplitude and U(1) Energy: Fixing the Winding
              - Two phase scales in one identity (720/360 degrees)
              - The velocity description as a U(1) energy-level
                quantity
              - The unit-winding helix reproduces the factor (Eq. V.3)
              - Three routes, one origin

Section VI : Discussion
              - Mass-peak and velocity-RMS on a common footing
              - Relation to the velocity scales of the helical model
              - Scope

Appendix A : Theoretical Scope of the Bridge Equation
              - Reinterpretation within the scope of the Dirac
                equation; no new testable prediction; gravitational
                extension out of scope

Appendix B : Line-Integral Genealogy and the Inverse-Direction Use
              of Geometry
              - Six-paper genealogy of the line-integral reading
              - Three pillars of the inverse-direction pattern
                (Noether inversion, Synge inverse-use, Maxwell
                two-stage construction)

Appendix C : Internal Ratios Considered and Set Aside
              - The 3:1 partition and the c/2 representative

Other:
  - Figure 1: Rotation-sense independence of the internal arc
    contraction (TikZ, two-panel)
  - Bibliography (24 entries: 15 Hanamura papers, 9 external)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "The Bridge Equation gamma = 1 + a from First Principles:
   Representation Duality of the Anomalous Moment and the Geometric
   Origin of the Root-Mean-Square Factor in the 0-Sphere Model,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.20091680

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (June 13, 2026)
  - Initial release of the First-Principles Foundation paper for the
    bridge equation.
  - Representation duality of the anomalous moment established
    (external time ratio / internal length ratio, joined by
    gamma_L = 1 + a_e).
  - Modulus in gamma = 1 + |a| derived as a geometric consequence of
    rotation-sense independence of the arc-contraction deficit.
  - The 1/sqrt(2) factor derived from the conservation identity as
    the square root of the average-to-peak ratio of the momentum
    term, replacing the AC-voltage analogy of Paper #10.
  - Pulsating-radius helix identified as the geometric carrier
    (R^2 = gamma*_KE); winding number fixed to unity via the
    SU(2)/U(1) phase duality.
  - The a-level versus velocity-level placement of the factor
    (residual 2^(1/4)) registered as an open task.
  - Two internal ratios (3:1 partition; c/2 representative) examined
    and set aside (Appendix C).

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in a
limited supportive role for textual organization during document
preparation. All physical interpretations, methodological judgments, and
philosophical commitments remain the responsibility of the author.

The scientific content, conceptual framework, and theoretical
interpretations presented in this document were conceived and developed
by the author, who assumes full responsibility for all claims and
interpretations herein.

This research received no specific grant from funding agencies in the
public, commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format   : LaTeX source (.tex)
Document class: REVTeX 4-2 (APS/PRB reprint format)
Page layout   : REVTeX default (two-column reprint)
Font          : Computer Modern (LaTeX default)

Figures:
  - Figure 1 : Rotation-sense independence of the internal arc
               contraction (TikZ two-panel figure; full-width
               figure* environment, Section II)

Cross-references:
  - Section labels for internal navigation
  - Equation numbering with \label and \ref (section-prefixed)
  - Hyperlinked bibliography and DOI links

Compilation:
  - First pass : resolves most content
  - Second pass: resolves all cross-references and hyperlinks

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

If uploading to Overleaf, use these project settings:

Compiler settings:
  Main document       : main.tex
  Compiler            : pdfLaTeX
  TeX Live            : 2025
  Compile mode        : Normal
  Stop on first error : ON
  Autocompile         : ON (optional)

Project structure (single file):
  /main.tex            -- the entire manuscript

================================================================================
END OF README
================================================================================
