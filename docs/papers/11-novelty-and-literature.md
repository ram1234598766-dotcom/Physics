# Novelty, Literature Position, and the Research Program

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We position Structure-Flow Calculus relative to the existing literature, document the novelty verification performed at the time of writing, state plainly what is and is not claimed, and lay out the research program the framework opens. We give the verification method and its limitations, the precise relationship to neighboring fields (Sturm-Liouville theory, graph signal processing, fractional calculus, conformal geometry, general relativity), and a reading guide. The reader is invited to falsify the novelty claim.

**Keywords:** novelty verification, literature position, research program, Structure-Flow Calculus.

---

## I. INTRODUCTION

A framework whose papers state theorems must also state its own position: what is new, what is not, how it relates to the existing literature, and where it is going. This paper discharges that obligation for Structure-Flow Calculus (SFC). It records the novelty verification performed at the time of writing, states the claims and non-claims precisely, positions the framework against its neighbors, and sketches the research program.

## II. WHAT SFC CLAIMS

Structure-Flow Calculus is a *unified framework* in which a single positive structure field $\rho$ on a domain — or on a graph family — yields, as an integrated construction:

1. a complete calculus (Paper 01): derivatives, integrals, integration by parts, and the transport map $\tau(x) = \int dx/\rho$;
2. a spectral theory (Paper 02) with closed-form graded-media modes and exactly conserved energy;
3. a causal network spectral theory (Paper 03) with an eigenframe connection, spectral-flow equations, and the Energy Migration Theorem;
4. a variational theory (Paper 04) coupling fields to their geometry through structure stationarity and Noether-type conservation laws;
5. a series of applications (Papers 05–07), numerical methods (Paper 08), a higher-dimensional extension (Paper 09), and a signal-processing pipeline (Paper 10).

As an integrated construction with proven theorems it is, to the best of our knowledge at the time of writing, new.

## III. WHAT SFC DOES NOT CLAIM

- SFC does not claim that its underlying physical equations are new. The graded-media wave equation is the Webster-type/acoustic equation in impedance-matched form (Paper 05); the power-network model is the linearized swing equation (Paper 06); the epidemic model is standard SIS (Paper 07).
- SFC does not propose a new law of fundamental physics.
- SFC's individual ingredients — Sturm-Liouville theory, graph signal processing, the calculus of variations, Noether's theorem, Riemannian metrics — are classical and are cited as such throughout the series.
- Absence of a documented prior construction is evidence of novelty, not proof of it; readers are invited to falsify the claim.

## IV. NOVELTY VERIFICATION LOG

Performed 2026-08-16 against the arXiv API (exact-phrase queries):

| Search | Results |
|---|---|
| `"structure flow"` AND `calculus` | 0 |
| `"spectral flow"` AND `"graph Fourier"` | 0 |
| `"time-varying graph"` AND `"eigenvector"` AND `"Laplacian"` (exact) | 0 |
| `"causal network calculus"` | 0 |

**Method.** arXiv's export API was queried with the above phrases as exact (`all:` field) and combination searches; the count of hits for the combined phrases was zero in each case.

**Limitations.** (i) arXiv covers only arXiv; journals, preprints, and older literature are not covered. (ii) Combined-phrase absence does not rule out closely-adjacent constructions under different names. (iii) The verification is a snapshot in time. This log is included for transparency and should be treated as evidence, not guarantee.

## V. RELATIONSHIP TO NEIGHBORING FIELDS

- **Sturm-Liouville theory [1].** $L_\rho = \rho(\rho u_x)_x$ is a special Sturm-Liouville operator. SFC adds the structure-field *interpretation* and the transport map (Paper 01, Theorem 12) that yields the closed-form spectrum; Paper 02 makes this explicit.
- **Graph signal processing [2,3].** Static in [2]; SFC treats time-varying families, the eigenframe connection, and modal-energy migration (Papers 03, 10).
- **Time-varying graph spectra.** Related spectral-flow studies exist; SFC's explicit skew-connection formulation, the Energy Migration Theorem, and the exactness of the modal model (Paper 10, Theorem 2) are the distinguishing results.
- **Fractional calculus.** A different generalization (fractional exponents vs a pointwise scale field); no overlap.
- **Conformal geometry [4].** Paper 09's metric is the product (anisotropic) rescaling $g_\rho = \sum_j \rho_j^{-2}dx_j^2$ (the conformal case when all profiles coincide); SFC's contribution is the structure-field presentation and the closed-form product-domain spectra.
- **General relativity.** A metric field is dynamical there too, but SFC's $\rho$ is a scale field with no Lorentzian structure; no claim of relation is made.

## VI. THE RESEARCH PROGRAM

The framework is deliberately *open*: each paper closes its core results and opens directions.

1. **Nonlinear structure-flow dynamics.** Structure coupled back-reaction to the field through the Paper 04 stationarity constraint gives a self-consistent field-structure system; its well-posedness is open.
2. **Structure-flow on manifolds with boundary and corners** beyond the product-metric case (Paper 09).
3. **Data-driven structure recovery.** Given observations of a field, estimate $\rho$ via structure stationarity (Paper 04) and use the modal-energy detector (Paper 10) for online structure monitoring.
4. **Random structure fields.** Spectral statistics of $L_\rho$ for random $\rho$ (a "structure-flow Anderson problem").
5. **Causal GFT in production systems.** Real-time estimation of the eigenframe connection $C(t)$ from streaming signals (Paper 10) — the enabling computation for early-warning systems.
6. **Graded-media inverse design at scale.** Transport-based design (Paper 05) for multi-dimensional, multi-physics devices (Paper 09).

## VII. HOW TO READ THE SERIES

- **Mathematician:** Papers 01–04, 09 are the core; applications (05–07) are illustrations.
- **Engineer:** Papers 05–08, 10 carry the design rules; each is backed by a runnable demo.
- **Skeptic:** This paper, and the verification demos, are the place to test the claims.

## VIII. CONCLUSION

SFC claims integration, not invention of physics; it documents its verification transparently, states its non-claims explicitly, and opens a concrete research program. The falsifiability that matters is mathematical: every theorem in the series is proved, and every central theorem is verified numerically by a runnable demo.

---

## REFERENCES

[1] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[2] D. Shuman, S. Narang, P. Frossard, A. Ortega, and P. Vandergheynst, "The emerging field of signal processing on graphs," *IEEE Signal Process. Mag.* **30**(3), 83–98 (2013).

[3] A. Ortega, P. Frossard, J. Kovačević, J. M. F. Moura, and P. Vandergheynst, "Graph signal processing: overview, challenges, and applications," *Proc. IEEE* **106**(5), 808–828 (2018).

[4] S. Gallot, D. Hulin, and J. Lafontaine, *Riemannian Geometry*, 3rd ed., Springer, 2004.

[5] F. R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics **92**, American Mathematical Society, 1997.
