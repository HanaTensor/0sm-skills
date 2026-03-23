================================================================================
Rotational Lorentz Contraction as the Geometric Origin of the Anomalous
Magnetic Moment: A Structural Correspondence with the Muon Lifetime Problem
(Structural Clarification Note)
================================================================================

Author: Satoshi Hanamura
Email:  hana.tensor@gmail.com
Date:   March 20, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the research paper:

1. main.tex
   - Main LaTeX source file (REVTeX 4-2, APS/PRB format)
   - Document class: revtex4-2, reprint, aps, prb
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (included in standard TeX distributions):
    revtex4-2, graphicx, bm, physics, hyperref, caption,
    microtype, ragged2e, booktabs, enumitem, amsthm,
    xcolor, tikz (with arrows.meta, calc, positioning,
    shapes.geometric libraries)

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

We demonstrate that the anomalous magnetic moment of the electron a_e and
the muon atmospheric lifetime extension are two manifestations of the same
relativistic length-extension mechanism.
In the 0-Sphere electron model, Thomas precession applied to sinusoidal
internal oscillation yields the double-angle angular velocity Omega ~
sin(2*omega*t), geometrically necessitating g = 2.
The deviation from g = 2 is identified with the rotational Lorentz
contraction of the internal orbital arc 2*pi*r in [L]: the arc is
shortened by the factor 1/(1+a_e) in the laboratory frame, in structural
analogy to the extension of the muon's proper path length L_0 in [L] to
gamma_L * L_0.
An inverse calculation from a_e^exp yields the Zitterbewegung velocity
v_ZB ~ 0.04c and the Lorentz factor gamma_L = 1 + a_e.
In both cases, a length [L] is modified by the Lorentz factor of the
relevant velocity; the structural mechanism is identical.
The forward derivation---determining v_ZB independently of a_e from
Thomas precession alone---remains the open task whose completion would
elevate this correspondence to a confirmed physical equivalence.

Key topics include:
- Relativistic length-extension identity Delta[L] = |gamma_L - 1| * L_0
  as the unifying equation for both phenomena
- Thomas precession with sinusoidal oscillation deriving the double-angle
  angular velocity Omega ~ sin(2*omega*t) and the geometric basis for g = 2
- Rotational Lorentz contraction of the internal orbital arc 2*pi*r as
  the geometric source of the anomalous magnetic moment a_e
- Inverse calculation: a_e^exp -> v_ZB ~ 0.04c, confirming gamma_L = 1 + a_e
- Structural comparison of the muon lifetime experiment (v ~ c, gamma_L >> 1)
  and the electron anomalous moment (v_ZB ~ 0.04c, gamma_L - 1 ~ 10^-3)
- RMS correction factor 1/sqrt(2) for peak vs. average Lorentz contraction
  in a harmonic oscillator
- Open forward chain: Thomas precession -> v_ZB -> a_e (future derivation)

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This paper makes explicit and self-contained a structural correspondence
first identified through an inverse calculation in:

Primary reference:
1. "Redefining Electron Spin and Anomalous Magnetic Moment Through
   Harmonic Oscillation and Lorentz Contraction" (#10)
   (Zenodo, 2023)
   DOI: 10.5281/zenodo.17764997

Foundational framework (0-Sphere Model):
2. "A Model of an Electron Including Two Perfect Black Bodies" (#1)
   (Zenodo, 2018)
   DOI: 10.5281/zenodo.16759284

The structural analogy between the muon lifetime problem and the electron
anomalous moment was identified in #10 through the inverse calculation
from a_e to v_ZB. The present paper (Structural Clarification Note) makes
this analogy fully explicit by introducing the unifying equation
Delta[L] = |gamma_L - 1| * L_0 and placing both phenomena side by side
in a unified figure and table.

================================================================================
KEY RESULTS
================================================================================

Main structural result:
- The anomalous magnetic moment a_e and the muon atmospheric lifetime
  extension are governed by the same identity:
    Delta[L] = |gamma_L - 1| * L_0
  where [L] is a length in the rest frame and gamma_L is the Lorentz
  factor of the relevant velocity.

Muon case:
- v ~ 0.9994c, gamma_L ~ 29, L_0 ~ 660 m, L_lab ~ 19 km

Electron case (0-Sphere Model):
- v_ZB ~ 0.04047c, gamma_L - 1 = a_e ~ 1.16e-3
- Thomas precession with sinusoidal oscillation gives Omega ~ sin(2*omega*t),
  establishing g = 2 as the geometric baseline
- Rotational Lorentz contraction of arc 2*pi*r gives a_e as fractional
  arc shortening: L/L_0 = 1/gamma_L ~ 1/(1 + a_e)
- Inverse calculation via RMS correction:
    sqrt(1 - v_ZB^2/c^2) = 1 / (1 + a_e^exp / sqrt(2))
    => v_ZB ~ 0.04047c, gamma_L ~ 1 + a_e

What the model CAN demonstrate:
- Structural correspondence between the two phenomena at the level
  of the length-extension identity
- Geometric basis for g = 2 via double-angle Thomas precession
- Identification of gamma_L = 1 + a_e as a consequence of SR applied
  to the internal orbital arc
- Numerical value v_ZB ~ 0.04c inferred from a_e^exp

What the model CANNOT currently derive:
- v_ZB from first principles (Thomas precession alone), independently
  of the measured a_e value
- The forward chain: Thomas precession -> v_ZB -> a_e

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Anomalous magnetic moment a_e and atmospheric muon surplus as
    two phenomena sharing a structural mechanism
  - Identification of the correspondence; organization of the paper

Section 2: Relativistic Length Extension: General Structure
  - Lorentz factor gamma_L = 1/sqrt(1 - v^2/c^2)
  - Length extension/contraction: L_lab = gamma_L * L_0 and L_0/gamma_L
  - Unifying identity: Delta[L] = |gamma_L - 1| * L_0
  - Figure 1: Structural comparison diagram (TikZ, two-panel)

Section 3: Muon Lifetime: The Textbook Case
  - Muons at v ~ 0.9994c, gamma_L ~ 29
  - L_lab = gamma_L * L_0 ~ 19 km; surplus path ~ 18 km
  - Paradigmatic SR length-extension event

Section 4: Electron Internal Orbit: The 0-Sphere Model
  4.1 Thomas Precession with Sinusoidal Oscillation
      - Sinusoidal internal photon motion: v_gamma* = cos(omega*t)
      - Thomas angular velocity: Omega = -sin(2*omega*t) / (4c^2)
      - Double-angle structure as geometric origin of g = 2
      - Three occurrences of 1/2 in the 0-Sphere Model (noted, future work)
  4.2 Rotational Lorentz Contraction and the Anomalous Moment
      - Ehrenfest paradox / Einstein (1912) rotational contraction
      - Arc shortening: L/L_0 = 1/gamma_L ~ 1/(1 + a_e)
      - a_e as fractional shortening of the internal orbital arc
  4.3 Inverse Calculation: a_e -> v_ZB
      - RMS correction: sqrt(1 - v_ZB^2/c^2) = 1/(1 + a_e^exp/sqrt(2))
      - Result: v_ZB^2/c^2 = 0.001638, v_ZB ~ 0.04047c
      - gamma_L = 1/sqrt(1 - v_ZB^2/c^2) ~ 1 + a_e confirmed
      - Status: inverse route (a_e -> v_ZB), not forward derivation

Section 5: Structural Comparison
  - Three-point shared structure: L_0, gamma_L, Delta[L]
  - Table 1: Side-by-side comparison of muon and electron cases
  - Muon: dramatic (gamma_L - 1 ~ 28); Electron: tiny but structurally
    identical (gamma_L - 1 = a_e ~ 10^-3)

Section 6: Open Direction: The Forward Chain
  - Inverse route established in #10; forward chain still open
  - Forward chain: Thomas precession -> v_ZB (open) -> gamma_L -> a_e
  - Berry-phase / fiber-bundle treatment of gamma_L = 1 + a_e (future)

Section 7: Conclusion
  - Summary: a_e and muon lifetime as two instances of Delta[L] identity
  - Physical mechanism identical; velocity scale differs

Figures:
  Fig. 1 (fig:comparison): Structural correspondence diagram — two-panel
    TikZ figure showing muon lifetime (blue, left) and electron anomalous
    moment (orange, right) with unifying equation in bottom strip.

Tables:
  Table 1 (tab:comparison): Structural comparison of muon lifetime
    extension and electron anomalous magnetic moment — 7 rows covering
    length modified, relevant velocity, Lorentz factor, observable
    surplus/deficit, observed quantity, calculation direction,
    and open forward direction.

Appendices:
  None.

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Rotational Lorentz Contraction as the Geometric Origin of the
  Anomalous Magnetic Moment: A Structural Correspondence with the
  Muon Lifetime Problem (Structural Clarification Note),"
  Zenodo (2026).

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (March 20, 2026)
  - Initial release
  - Establishes structural correspondence between the electron anomalous
    magnetic moment and the muon atmospheric lifetime extension via the
    relativistic length-extension identity Delta[L] = |gamma_L - 1| * L_0
  - Introduces unified two-panel TikZ figure and comparison table
  - States the open forward chain: Thomas precession -> v_ZB -> a_e

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author thanks the open-access infrastructure of Zenodo for enabling
incremental publication of this research series.

The physical concepts, theoretical framework, and all original ideas
presented in this work---including the identification of the anomalous
magnetic moment with rotational Lorentz contraction of the internal orbital
arc, a central claim of the 0-Sphere model developed continuously since
2018---are solely the author's own. A large language model (LLM) was used
exclusively for linguistic polishing and paragraph composition; it
contributed no conceptual content.

This research received no specific grant from funding agencies in the
public, commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: revtex4-2 (APS/PRB, reprint mode)
Compiler: pdfLaTeX

Tables:
  Table 1 (tab:comparison): Structural comparison of muon lifetime
    extension and electron anomalous magnetic moment. 7 data rows.
    Appears in Section 5 (Structural Comparison).

Figures:
  Fig. 1 (fig:comparison): Two-panel TikZ diagram showing structural
    correspondence between muon lifetime (blue panel) and electron
    anomalous moment (orange panel) with unifying equation strip.
    Placed as figure* (full-width) in Section 2.

Cross-references:
  - Section labels: sec:intro, sec:sr, sec:muon, sec:0sphere,
    sec:thomas, sec:lorentz_contraction, sec:inverse,
    sec:comparison, sec:forward, sec:conclusion
  - Equation labels: eq:gamma_def, eq:length_extension,
    eq:length_contraction, eq:delta_L, eq:muon_path,
    eq:v_sin, eq:a_sin, eq:thomas_general, eq:omega_double,
    eq:lorentz_arc, eq:inverse_rms, eq:beta_sq,
    eq:v_ZB_result, eq:gamma_result, eq:forward_chain
  - Table label: tab:comparison
  - Figure label: fig:comparison
  - Hyperlinked bibliography and DOI links via hyperref

Compilation:
  - First pass:  resolves most content
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
