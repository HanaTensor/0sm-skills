================================================================================
Open-Path Spinorial Transport in the 0-Sphere Model and the Status of
Torsion: Holonomy Sufficiency and the Possibility of Emergent Semigroup
Geometry (Structural Clarification Note)
================================================================================

Author: Satoshi Hanamura
Email:  hana.tensor@gmail.com
Date:   March 11, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the structural clarification
note examining torsion, open-path spinorial transport, and semigroup geometry
in the 0-Sphere Model:

1. main.tex
   - Main LaTeX source file (full manuscript with three appendices)
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
    graphicx, bm, physics, hyperref, caption, microtype, ragged2e,
    booktabs, amsthm, tikz (with arrows.meta, calc, positioning)

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

The 0-Sphere model describes the electron as a two-kernel system in which
energy is exchanged by radiation between spatially separated points, giving
rise to Zitterbewegung, anomalous magnetic moment, and gravitational redshift
of internal clocks. This note examines whether the geometric structure already
established in the model -- in particular the 4pi spinorial periodicity, the
prohibition of same-point radiation, and the ordered-path constraint
A -> B -> A' != A -> A' -> B -- is sufficient to force the appearance of
geometric torsion in the sense of Cartan.

Three distinct mechanisms are identified as candidates for generating non-zero
torsion: (i) the anti-symmetry of the connection implied by the ordered-path
physical constraint, (ii) the Thomas precession contribution to the spin
connection and its spatial gradient, and (iii) the directed nature of the
spinorial arc-length L_spin(A,B) under the 4pi periodicity of SU(2). The
analysis shows, however, that none of these mechanisms yields torsion as a
logical necessity from the currently established equations alone. The 4pi
periodicity implies non-trivial holonomy but not by itself a non-symmetric
connection; the exponential kernel remains invertible and thus admits a group
(rather than semigroup) structure; and the Thomas precession spin connection
can in principle cancel the external derivative of the vierbein in the Cartan
torsion equation.

The central unresolved question is whether the internal arc-length L_spin is
a true scalar distance or a directed quantity whose reversal is physically
inequivalent. The note formulates this question precisely, outlines what
additional structure would promote each candidate mechanism to a theorem, and
explains how the answer determines whether the model belongs to the class of
SU(2) holonomy theories or to a genuinely new class of causal torsion
geometries.

Key topics include:
- Open-path parallel transport operators and their role in the free-electron
  description
- Two-layer kernel structure: inner rest-frame kernel and outer gravitational
  layer
- Three candidate torsion mechanisms and their logical obstacles
- Distinction between curvature-holonomy framework and torsion framework
- Spacetime spin connection vs. internal gauge connection dichotomy for the
  accumulated phase Delta_varphi(A,B)
- SU(2) group structure, 4pi periodicity, and semigroup geometry
- Compatibility with general relativity and Einstein-Cartan theory

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This structural clarification note builds upon and clarifies concepts from:

Primary references (directly examined or extended):
1. "Geometrical Confinement of Energy in the 0-Sphere Model: A Topological
   Mechanism Underlying Rest Mass and Zitterbewegung" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18356895

2. "Detailed Exposition of the 0-Sphere Model Framework for
   Gravitational-Like Phenomena" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18511664

3. "Electron Interference from Internal Geometry: Two-Kernel SU(2) Structure,
   Quartic Energy Flow, and an Intrinsic Visibility Limit" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18718174

4. "On the Derivative-Order Mismatch Between Gauge Theory and Gravity:
   A Supplement on Connection, Curvature, and Line-Integral Observables"
   (Zenodo, 2026)
   DOI: 10.5281/zenodo.18736670

Line-integral trilogy (foundational for open-path transport framework):
5. "Geometric Structure of Spinorial Phase Accumulation along Thermal
   Geodesics" (Zenodo, 2025)
   DOI: 10.5281/zenodo.18067760

6. "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws" (Zenodo, 2026)
   DOI: 10.5281/zenodo.18135855

7. "Line Integrals as Fundamental Observables in Physics: A Unified Principle
   Behind the Aharonov-Bohm Effect, Berry Phase, and Wilson Loops"
   (Zenodo, 2026)
   DOI: 10.5281/zenodo.18203433

This note identifies the precise logical condition under which the SU(2)
holonomy description must be abandoned in favor of a torsion framework:
the composition U(A,B) o U(B,A) must fail to equal the identity for physical
reasons internal to the model. Whether this condition is satisfied is the
central open question.

================================================================================
KEY RESULTS
================================================================================

What this note establishes:
- The 4pi spinorial periodicity is fully consistent with a torsion-free SU(2)
  holonomy description; it does not by itself force torsion.
- The ordered-path asymmetry A -> B -> A' != A -> A' -> B is most naturally
  encoded in the curvature of the non-Abelian SU(2) connection, not in a
  non-symmetric affine connection.
- The exponential kernel K_int(A,B) = exp(i omega_0 L_int / v_ZB) remains
  group-invertible: K_int(B,A) = K_int(A,B)^{-1}, consistent with standard
  Lie group fiber bundle structure.
- Three candidate torsion mechanisms are identified and assessed; none
  constitutes a theorem from currently established equations.
- The torsion question reduces entirely to the directed arc-length conjecture:
  whether L_spin(A,B) is a proper-time scalar or a genuinely directed quantity.

What the model cannot currently derive from this note:
- A proof that torsion is present (requires establishing the directed arc-length
  conjecture).
- A proof that torsion is absent (requires ruling out the directed arc-length
  for all configurations).
- An explicit computation of the Cartan torsion two-form T^a = de^a + omega^a_b
  wedge e^b (vierbein not yet fully determined in the model).
- A distinguishing experimental prediction between the torsion and no-torsion
  versions of the model.

The open question is stated precisely: is the internal arc-length L_spin(A,B)
a proper-time scalar (symmetric in A and B after SU(2) structure) or a
directed quantity for which L_spin(A,B) + L_spin(B,A) != 0 in a sense that
cannot be accommodated within a standard Lie group fiber bundle?

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Background: 0-Sphere model and its derivations without perturbation theory
  - The torsion question: does the model already contain Cartan torsion?
  - Three analysis lines: ordered-path constraint, Thomas spin connection,
    directed arc-length
  - Relationship between curvature-holonomy and torsion frameworks

Section 2: The Two-Layer Kernel Structure and Internal Arc-Length
  - Energy identity E_0 = cos^4(theta/2) + sin^4(theta/2) + (1/2)sin^2(theta)
  - Inner kernel K_int(A,B) = exp(i omega_0 L_int / v_ZB)
  - Outer kernel: gravitational modification omega(x)
  - SU(2) round-trip relation U_{A->B} . U_{B->A} = -1
  - Directed vs. scalar arc-length: the central open question

Section 3: Open-Path Parallel Transport and the Free Electron
  - Path-ordered exponential: U(A,B) = P exp(integral_A^B omega_mu dx^mu)
  - Covariant derivative from the two-point operator
  - Non-commutativity from curvature without torsion
  - Free-electron SU(2) transport: Delta_varphi(A,B) = -Delta_varphi(B,A)

Section 4: The Ordered-Path Constraint and Its Geometric Meaning
  - Same-point radiation prohibition and its geometric translation
  - Ordered-path asymmetry as phase-matching condition (not absolute prohibition)
  - Encoding asymmetry in kernel amplitude vs. connection symmetry

Section 5: The Torsion Question: Candidate Mechanisms and Logical Obstacles
  - Mechanism 1: Antisymmetry of affine connection (ordered-path constraint)
  - Mechanism 2: Thomas spin connection gradient (spatial variation of Omega_T)
  - Mechanism 3: Directed spinorial arc-length (semigroup structure)
  - Table 1: Candidate mechanisms, physical origins, logical obstacles, status
  - Logical dependence of all three mechanisms on the directed arc-length

Section 6: Compatibility with General Relativity and the SU(2) Holonomy Option
  - Holonomy option: SU(2) principal bundle on Levi-Civita background
  - Torsion option: Einstein-Cartan gravity, T^{mu nu rho} proportional to S^{mu nu rho}
  6.1 The Spacetime vs. Internal Gauge Connection Dichotomy for Delta_varphi(A,B)
      - Mathematical home: spin connection vs. SU(2) gauge potential
      - Torsion implications of each interpretation
      - Table 2: The two interpretations and their consequences
      - Evidence from the series (#17, #32, #40) favoring internal gauge reading

Section 7: Conclusion
  - Summary: none of three mechanisms constitutes a theorem
  - The directed arc-length conjecture as the central open question
  - Logical condition for abandoning holonomy in favor of torsion

Appendices:
  - Acknowledgments
  - Bibliography (18 entries)
  - Appendix A: SU(2), Double Covers, and the Origin of the 4pi Periodicity
  - Appendix B: Connections, Curvature, and Torsion: A Geometric Primer
    (Table 3: Classification of geometric structures by curvature and torsion)
  - Appendix C: Open-Path Transport versus Wilson Loops: Why Free Electrons
    Require a Different Framework

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "Open-Path Spinorial Transport in the 0-Sphere Model and the Status of
  Torsion: Holonomy Sufficiency and the Possibility of Emergent Semigroup
  Geometry (Structural Clarification Note),"
  Zenodo (2026).
  DOI: 10.5281/zenodo.18950974

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1.0 (March 11, 2026)
  - Initial release
  - Identifies three candidate torsion mechanisms and assesses their logical
    status against the currently established equations of the model
  - Formulates the directed arc-length conjecture as the central open question
  - Clarifies the curvature-holonomy vs. torsion distinction for the 4pi
    spinorial periodicity
  - Establishes the spacetime spin connection vs. internal gauge connection
    dichotomy as the key attribution problem

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
Document class: REVTeX 4-2 (reprint, aps, prb)
Page layout: Two-column reprint format
Font: Computer Modern (LaTeX default)

Tables:
  Table 1 (tab:mechanisms): Candidate mechanisms for torsion in the 0-Sphere
           model -- three rows comparing antisymmetry, Thomas gradient, and
           directed arc-length against logical obstacles and current status
  Table 2 (tab:dichotomy):  The two interpretations of Delta_varphi(A,B) --
           spacetime spin connection vs. internal gauge connection, five
           comparison dimensions
  Table 3 (tab:geometry):   Classification of geometric structures by curvature
           and torsion -- four cases (Riemannian, flat gauge, Einstein-Cartan,
           teleparallel) with 0-Sphere relevance (Appendix B)

Cross-references:
  - Section labels for internal navigation (\label{sec:...})
  - Equation numbering per section with \label and \ref
  - Hyperlinked bibliography and DOI links

Custom macros defined in preamble:
  \iphase       internal geometric phase (theta = omega_0 t)
  \omZB         Zitterbewegung frequency (omega_ZB)
  \Lint         internal arc-length (L_int)
  \Lspin        spinorial arc-length (L_int^spin)
  \vZB          Zitterbewegung velocity (v_ZB)
  \omeff        position-dependent frequency (omega(x))
  \UAB          open-path transport operator U(A,B)
  \KAB          two-point kernel K(A,B)
  \OmT          Thomas angular velocity (Omega_T)

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
