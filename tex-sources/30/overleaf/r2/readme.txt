================================================================================
From Curvature to Connection:
Revisiting the Geometric Origin of Conservation Laws
(Version 2 -- March 1, 2026)
================================================================================

Author: Satoshi Hanamura
Email:  hana.tensor@gmail.com
Date:   March 1, 2026

================================================================================
CONTENTS
================================================================================

This archive contains the LaTeX source file for the revised manuscript (v2):

1. main.tex
   - Main LaTeX source file (Version 2, updated from January 3, 2026 original)
   - Document class: REVTeX 4-2 (APS/PRB reprint format)
   - Compiler: pdfLaTeX
   - TeX Live version: 2025

================================================================================
WHAT IS NEW IN VERSION 2
================================================================================

Version 2 adds one new section to the original manuscript:

  Section 6: "The Einstein Equation as a Global Consistency Condition"

  This section develops the interpretation of the Einstein field equation as an
  a posteriori verification condition within the connection-based framework,
  rather than a generative dynamical law. Three subsections are included:

    6.1  From Generation to Verification
         -- The logical inversion: T_mu_nu as derived, not prescribed
         -- Bianchi identity as the primary geometric statement

    6.2  Functional Analogy with Distributed Consistency Verification
         -- Structural parallel with checksum mechanisms in distributed systems
         -- Each worldline contributes independently; Einstein equation verifies
            global coherence of the aggregate

    6.3  Microscopic Flexibility and Macroscopic Coherence
         -- Quantum fluctuations at individual worldline level
         -- Global conservation enforced without point-by-point correspondence

  The abstract has been updated to reflect the new section.
  All other sections from v1 are unchanged.

Source of the new material: The core argument was extracted from a separate
supplementary manuscript (47.tex) and integrated here as the natural locus
for this interpretation, consistent with the primary thesis of the paper.

================================================================================
COMPILATION INSTRUCTIONS
================================================================================

Requirements:
- TeX Live 2025 (or compatible distribution)
- pdfLaTeX compiler
- Required LaTeX packages (all included in standard TeX distributions):
    revtex4-2, graphicx, bm, physics, hyperref, caption, microtype,
    ragged2e, booktabs, amsthm, amsmath, amssymb

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

The Einstein field equation is conventionally interpreted as a dynamical law
equating spacetime curvature with the stress-energy tensor of matter. In this
work, we revisit an alternative perspective that has repeatedly appeared
throughout the history of theoretical physics: whether curvature or the
stress-energy tensor are truly fundamental, or whether the underlying structure
is instead encoded in connections and their associated conservation properties.

We review historical attempts by Einstein, Weyl, Cartan, Palatini, and Ashtekar
to reformulate gravity in geometric terms, identify the precise point at which
these approaches encountered conceptual or empirical limitations, and clarify
the nature of the unresolved problem. Building on recent results within the
0-Sphere model, we argue that conservation laws may be understood as consequences
of connection-based phase accumulation along thermal geodesics, with
stress-energy emerging as a derived, rather than fundamental, quantity.

A further section (added in v2) develops the interpretation of the Einstein
equation as a global consistency condition within this framework: rather than
generating curvature from matter, the equation serves as an a posteriori
verification that accumulated phase along worldlines remains globally
self-coherent.

Key topics include:
- Historical analysis of connection-based reformulations of gravity
  (Einstein, Weyl, Cartan, Palatini, Ashtekar)
- The unresolved core problem: deriving conservation laws from geometry
- Thermal geodesics and connection-based phase accumulation in the 0-Sphere model
- Open line integrals along proper-time worldlines as primary observables
- Reinterpretation of the Einstein equation as a geometric consistency condition
- Functional analogy between the Bianchi identity and distributed checksums
- Coexistence of quantum indeterminacy and macroscopic conservation

================================================================================
RELATION TO PREVIOUS WORK
================================================================================

This manuscript is a revised version (v2) of the paper originally published as:

  "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws"
  Zenodo (January 3, 2026)
  DOI: 10.5281/zenodo.18135855

Primary references cited in the text:

1. "Quantum Oscillations in the 0-Sphere Model: Bridging Zitterbewegung,
    Geodesic Paths, and Proper Time Through Radiative Energy Transfer"
   Zenodo (2024). DOI: 10.5281/zenodo.17765017

2. "Thermal Geodesics in the 0-Sphere Model: Extending General Relativity
    through Internal Thermodynamic Structure"
   Zenodo (2025). DOI: 10.5281/zenodo.17765349

3. "A Noetherian Inversion: From Einsteinian Geometry to Emergent Symmetry"
   Zenodo (2025). DOI: 10.5281/zenodo.18064535

Line Integral Trilogy (companion works):
4. "Geometric Structure of Spinorial Phase Accumulation along Thermal
    Geodesics"
   Zenodo (2025). DOI: 10.5281/zenodo.18067760

5. "Line Integrals as Fundamental Observables in Physics: A Unified Principle
    Behind the Aharonov-Bohm Effect, Berry Phase, and Wilson Loops"
   Zenodo (2026). DOI: 10.5281/zenodo.18203433

The new Section 6 consolidates and formalizes the "geometric checksum"
interpretation that was implicit in Section 5 of v1, and which appeared in
draft form in a separate supplementary manuscript (47.tex). The present paper
is the natural locus for this argument, as it is the primary work treating the
Einstein equation's role within the connection-based framework.

================================================================================
KEY RESULTS
================================================================================

What this paper establishes:
- Conservation laws emerge from connection-based phase accumulation along
  thermal geodesics, not from externally imposed stress-energy sources
- The stress-energy tensor T_mu_nu is a derived, descriptive quantity, not
  a fundamental causal agent
- The Einstein equation functions as an a posteriori consistency condition
  (geometric checksum), not a generative dynamical law
- The Bianchi identity is the primary geometric statement; energy-momentum
  conservation follows as a consistency requirement
- Open line integrals along proper-time worldlines are the primary observables

What this paper does not establish:
- A fully explicit geometric equation replacing the Einstein equation
- A complete derivation of Maxwell's equations from the connection framework
- A quantitative resolution of quantum gravity divergences
- Experimental predictions beyond those of standard general relativity

The framework preserves all empirical predictions of general relativity while
reordering the conceptual hierarchy: from curvature-based locality to
connection-based integrality.

================================================================================
DOCUMENT STRUCTURE
================================================================================

Section 1: Introduction
  - Bianchi identity as a consistency condition (not a dynamical output)
  - Overview of historical reformulation attempts
  - Objectives of the present work

Section 2: Historical Attempts to Recenter Geometry
  2.1  Einstein and the Search for a Purely Geometric Theory
  2.2  Weyl Geometry and the Primacy of the Connection
  2.3  Cartan Geometry and Torsion
  2.4  Palatini Formalism
  2.5  Ashtekar Variables and Quantum Geometry
  2.6  Summary and Perspective

Section 3: The Unresolved Core Problem
  - Common limitation: no geometric mechanism for conservation laws
  - Physical observables as history-dependent, not point-local

Section 4: Connection-Based Conservation in the 0-Sphere Model
  - Thermal geodesic equation
  - Line integral of connection one-form as primary observable
  - Energy conservation identity and phase periodicity
  - Demotion of T_mu_nu to descriptive status

Section 5: Geometric Interpretation of Phase Accumulation
  - Open worldlines as primary physical trajectories
  - Gauge dependence of local connection vs. gauge invariance of integral
  - Analogy with Berry and Aharonov-Bohm phases
  - Einstein equation as geometric checksum (first explicit statement)

Section 6: The Einstein Equation as a Global Consistency Condition  [NEW in v2]
  6.1  From Generation to Verification
  6.2  Functional Analogy with Distributed Consistency Verification
  6.3  Microscopic Flexibility and Macroscopic Coherence

Section 7: Conclusion

Non-numbered sections:
  - Acknowledgements
  - Bibliography (21 references)

Tables:
  Table 1: Comparison of Geometric Foundations in Classical and Modern
           Approaches to Gravity (6 rows: Einstein GR, Weyl, Cartan,
           Palatini, Ashtekar/LQG, 0-Sphere model)

================================================================================
LICENSE AND CITATION
================================================================================

This work is distributed under the Creative Commons Attribution 4.0
International License (CC BY 4.0).

Recommended citation format:
  Satoshi Hanamura,
  "From Curvature to Connection: Revisiting the Geometric Origin of
   Conservation Laws," v2,
  Zenodo (2026).
  DOI: 10.5281/zenodo.18135855

================================================================================
CONTACT INFORMATION
================================================================================

For questions, comments, or correspondence regarding this document:
  Email: hana.tensor@gmail.com

================================================================================
REVISION HISTORY
================================================================================

Version 1 (January 3, 2026)
  - Initial release
  - Historical analysis of connection-based reformulations
  - 0-Sphere model conservation framework
  - Geometric interpretation of phase accumulation along thermal geodesics
  - Implicit "geometric checksum" interpretation in Section 5

Version 2 (March 1, 2026)
  - Added Section 6: "The Einstein Equation as a Global Consistency Condition"
  - Developed the checksum analogy into three subsections
  - Updated abstract to reflect new section
  - Introduction roadmap updated to include Section 6
  - Japanese comments removed; English section comments added throughout

================================================================================
ACKNOWLEDGMENTS
================================================================================

The author acknowledges the use of large language models (LLMs) in the
preparation of this manuscript. LLMs were employed for language polishing,
structural refinement, and for assisting in the organization of historical
context. The scientific content, interpretations, and conclusions presented
in this document were conceived and developed by the author, who assumes
full responsibility for all claims and interpretations herein.

This research received no specific grant from funding agencies in the public,
commercial, or not-for-profit sectors.

================================================================================
TECHNICAL NOTES
================================================================================

File format: LaTeX source (.tex)
Document class: REVTeX 4-2 (reprint, APS, PRB)
Page layout: 2.5cm margins (all sides, via revtex4-2 defaults)
Line spacing: revtex4-2 default (single column reprint mode)
Font: Computer Modern (LaTeX default)

Tables:
  Table 1 (tab:historical_comparison_geometry): Comparison of geometric
    foundations across 6 theoretical approaches to gravity. Three columns:
    approach, core geometric focus, limitation encountered.

Cross-references:
  - Section labels: sec:introduction, sec:historical, sec:core_problem,
    sec:0sphere_conservation, sec:phase_interpretation, sec:consistency,
    sec:conclusion
  - Subsection labels: sec:einstein_geo, sec:weyl, sec:cartan, sec:palatini,
    sec:ashtekar, sec:historical_summary, subsec:generation_verification,
    subsec:checksum_analogy, subsec:micro_macro
  - Equation labels: eq:thermal_geodesic
  - Table label: tab:historical_comparison_geometry

Compilation:
  - First pass: resolves most content
  - Second pass: resolves all cross-references and hyperlinks

================================================================================
OVERLEAF PROJECT SETTINGS (RECOMMENDED)
================================================================================

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
