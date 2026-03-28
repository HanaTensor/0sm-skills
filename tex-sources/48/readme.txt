================================================================================
Geometric Origin of g = 2 in the 0-Sphere Model:
U(1) Fiber Bundle and Dual-Frame Phase Decomposition
================================================================================

Author: Satoshi Hanamura
Email: hana.tensor@gmail.com
Date: March 28, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for a structural clarification
paper in the 0-Sphere Model series:

1. main.tex
   - Main LaTeX source file (single-file, self-contained)
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
  booktabs, amsthm, listings, xcolor, tikz (with arrows.meta, calc, 3d,
  shadings, positioning, decorations.pathmorphing, shapes.geometric),
  amsmath, amssymb, revtex4-2, enumitem

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

This paper establishes the geometric phase structure of the 0-Sphere electron
model, demonstrating that its internal 2*pi periodicity naturally accommodates
two independent degrees of freedom: the center-of-mass frame and the laboratory
observation frame.

Beginning from energy conservation constraints, the paper proves that the
kinetic energy term mandates 2*pi periodicity through the single-valuedness
requirement of the state function. This periodicity induces a principal U(1)
fiber bundle structure, wherein the Berry phase gamma_intrinsic = pi emerges
as a coordinate-invariant quantity, geometrically necessitating g = 2 in the
proper-time frame. In the laboratory frame, Lorentz projection introduces a
phase distortion gamma_anomalous, yielding the decomposition
gamma_total = gamma_intrinsic + gamma_anomalous and the g-factor structure
g_lab = 2(1 + a), where a := gamma_anomalous / (2*pi).

A central result is an arc-length argument identifying the geometric mechanism
of a_e: rotational Lorentz contraction shortens the internal orbital arc
2*pi*r by the factor 1/(1+a_e), the same mechanism by which a muon's path
length L_0 is extended to gamma_L * L_0 during atmospheric transit. This
inverse calculation yields v_ZB approximately 0.04c and identifies
gamma_L = 1 + a_e as a structural consequence of special relativity applied
to the internal orbital motion. The anomalous magnetic moment and the muon
lifetime experiment are identified as two manifestations of the same
relativistic length-extension structure.

Key topics include:
- U(1) fiber bundle structure from 2*pi periodicity of the internal state
- Berry phase gamma_intrinsic = pi as topological invariant (g_CM = 2 exact)
- Dual-frame decomposition: g_lab = 2(1 + a)
- Rotational Lorentz contraction as geometric mechanism of a_e
- Structural equivalence of AMM and muon lifetime extension (ΔL = |γ_L − 1|×L₀)
- Three coexisting periodicities (pi, 2*pi, 4*pi) and gauge symmetry correspondence
- Thermodynamic spin-state classification selected by algebraic consistency
- Realist interpretation of Bloch sphere geometry

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This structural clarification paper builds directly upon and formalizes
the geometric programme of the 0-Sphere Model series:

Primary references:
1. "Spin from Geometry: Emergence of Spin via Internal Berry Phase
    in the 0-Sphere Electron Model" (Zenodo 2025)
   DOI: 10.5281/zenodo.17765409
   [Established Berry phase as origin of spin; #48 formally proves U(1)
    bundle structure and gamma_intrinsic = pi via fiber bundle framework]

2. "Geometric Phase Structure: Dual DOF within 2*pi Periodicity" (Zenodo 2026)
   DOI: 10.5281/zenodo.18718174
   [Established g_CM = 2 as topological invariant and g_lab = 2(1+a)
    decomposition; #48 provides the formal geometric proof]

3. "Detailed Exposition of the 0-Sphere Model Framework for
    Gravitational-Like Phenomena" (Zenodo 2026)
   DOI: 10.5281/zenodo.18511664
   [Provides the inverse arc-length calculation (a_e → v_ZB ≈ 0.04c)
    that is formalized in the dual-frame decomposition of this paper]

Foundational framework (0-Sphere Model):
4. "A Model of an Electron Including Two Perfect Black Bodies" (Zenodo 2018/2019)
   DOI: 10.5281/zenodo.16759284

This paper places the previously established structural results (g = 2 as
topological invariant, arc-length Lorentz contraction mechanism, muon-AMM
structural correspondence) on a formal fiber bundle foundation, and introduces
the Foucault pendulum analogy as a unifying geometric picture for the
dual-frame phase decomposition.

================================================================================
KEY RESULTS
================================================================================

What the model CAN derive:
- Berry phase gamma_intrinsic = pi as a genuine geometric invariant of the
  closed equatorial path on the Bloch sphere
- g_CM = 2 exactly, as a topological consequence of U(1) holonomy in the
  proper-time frame
- Dual-frame decomposition g_lab = 2(1 + a) from Lorentz projection
- Structural correspondence between AMM a_e and muon lifetime extension
  via ΔL = |γ_L − 1| × L_0 (inverse route: a_e^exp → v_ZB ≈ 0.04c)
- Three coexisting phase periodicities (pi, 2*pi, 4*pi) from a single
  energy conservation principle, corresponding to spin-2, spin-1, spin-1/2
- Algebraic selection of thermodynamic spin-state classification as the
  unique assignment consistent with g_CM = 2 as a topological invariant

What the model CANNOT currently derive:
- Forward chain: Thomas precession → v_ZB independent of a_e → gamma_L = 1+a_e
  as output (remains open task)
- Precise quantitative derivation of v_ZB from first principles
- Physical validation of gauge symmetry correspondence (phenomenological
  correspondence at present, not derivation)
- Quantitative radiation spectra or perturbative loop-integral calculations
  (outside scope of non-perturbative framework)

All scope limitations are stated explicitly and the framework is presented
with full methodological transparency.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Berry phase background and 0-Sphere Model overview
  - Arc-length argument summary (AMM-muon structural equivalence)
  - Dual-frame structure motivation

Section 2: Definition of the 0-Sphere Internal Structure
  2.1 Discrete Two-Point Structure
  2.2 Emergent Angular Variable

Section 3: Hamiltonian Structure and 2*pi Periodicity
  3.1 Kinetic Energy and Periodicity
      - Three phase structures (half-angle, normal-angle, double-angle)
      - Two spin-state classification schemes (thermodynamic vs. kinematic)
  3.2 Bloch Sphere Geometry and Berry Phase

Section 4: U(1) Fiber Structure and Berry Connection
  4.1 Closure in Phase Space vs. Physical Space
  4.2 Foucault Pendulum as Prototype Holonomy
      - Classical Foucault Holonomy
      - Mapping to 0-Sphere Dual-Frame Structure
      - The Bridge Equation gamma_L = 1 + a
  4.3 Emergence of U(1) Bundle
  4.4 Berry Connection
  4.5 Gauge Invariance and Holonomy
  4.6 Topological Protection

Section 5: Dual Degrees of Freedom: Center-of-Mass Frame vs. Laboratory Frame
  5.1 Proper-Time Closure in the Center-of-Mass Frame
  5.2 Lorentz Projection and Phase Distortion
      - Thomas Precession and Phase Distortion
      - Structural Correspondence of the 1/2 Factor
  5.3 g-Factor in the Laboratory Frame

Section 6: Discussion
  6.1 Geometric Framework for the g-Factor Structure
  6.2 Experimental Implications and Verification
  6.3 Reinterpretation of the Zero-Point Energy: Geometric Minimum vs.
      Quantum Fluctuation
  6.4 Realist Interpretation: Bloch Sphere as Phase Geometry
  6.5 Algebraic Consistency and the Selection of the Thermodynamic
      Classification
  6.6 Hierarchical Phase Structure and Gauge Symmetry Correspondence
  6.7 Scope and Limitations

Section 7: Conclusion

Appendices:
  A: Energy Conservation Identity (verification of cos^4 + sin^4 identity)
  B: Physical Justification of g-Factor Definition
  C: Berry Phase for Non-Single-Valued Gauge Representatives
     (large vs. small gauge transformations)
  D: Differentiability at the Turning Point and the SU(2) Covering Structure
     - The Turning Point as a Physical Rest State
     - Differentiability: Why the Kink is an Artefact
     - Front-to-Back Transition on the Bloch Sphere
     - Structural Analogy with the Dirac Equation
     - Implications for the Discreteness of Spin

Figures (TikZ, compiled inline):
  - Fig. 1: Three Phase Structures Coexisting in a Single 2*pi Cycle
  - Fig. 2: Two Interpretations of Spin-State Assignment from Omega_T
  - Fig. 3: Equatorial Trajectory on Bloch Sphere (Berry phase = pi)
  - Fig. 4: Dual-Frame Phase Decomposition (CM frame vs. Lab frame)

Tables:
  - Table 1: Comparison of Thermodynamic and Kinematic Spin-State
             Classification Schemes
  - Table 2: Berry Phase Contributions for the Real-Gauge State
  - Table 3: Structural Correspondence between the Dirac Equation
             and the 0-Sphere Model

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Geometric Origin of g = 2 in the 0-Sphere Model:
   U(1) Fiber Bundle and Dual-Frame Phase Decomposition,"
  Zenodo (2026).
  https://doi.org/10.5281/zenodo.[ID]

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (March 28, 2026)
  - Initial release
  - Establishes U(1) fiber bundle structure of the 0-Sphere internal state
  - Formal proof of Berry phase gamma_intrinsic = pi and g_CM = 2 as
    topological invariant
  - Dual-frame decomposition g_lab = 2(1+a) with Foucault pendulum analogy
  - Arc-length argument: AMM and muon lifetime as same relativistic mechanism
  - Three-periodicity gauge symmetry correspondence (phenomenological)
  - Thermodynamic spin-state classification selected by algebraic consistency

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
Document class: revtex4-2 (APS/PRB, reprint mode, two-column)
Page layout: REVTeX default
Font: Computer Modern (LaTeX default)

All figures are generated inline via TikZ macros defined in the preamble.
No external image files are required for compilation.

Tables:
  - Table 1 (tab:spin_classification): Two-column spanning table*
  - Table 2 (tab:boundary_summary): Two-column spanning table*
  - Table 3 (tab:dirac_0sphere): Two-column spanning table*

Cross-references:
  - Section labels for internal navigation
  - Equation numbering per section with \label and \ref
  - Hyperlinked bibliography and DOI links (hyperref, colorlinks=blue)

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
