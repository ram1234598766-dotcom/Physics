# Paper 06 — Novelty and Literature Position

**Abstract.** We position Structure-Flow Calculus relative to the existing literature, document the novelty verification performed at the time of writing, and state plainly what is and is not claimed.

## 1. What SFC claims

Structure-Flow Calculus is a *unified framework* in which a single structure field $\rho$ yields (a) a complete calculus, (b) a spectral theory with closed-form graded-media modes, (c) a causal network spectral theory with an Energy Migration Theorem, and (d) a variational theory coupling fields to their geometry. As an integrated construction with proven theorems it is, to the best of our knowledge at the time of writing, new.

## 2. What SFC does not claim

- SFC does not claim that its underlying physical equations are new. The graded-media wave equation is the Webster-type/acoustic equation in impedance-matched form; the power-network model is the linearized swing equation; the epidemic model is standard SIS.
- SFC does not propose a new law of fundamental physics.
- SFC's individual ingredients (Sturm-Liouville theory, graph signal processing, the calculus of variations, Noether's theorem) are classical.

## 3. Novelty verification log

Performed 2026-08-16 against the arXiv API (exact-phrase `all:` fields):

| Search | Results |
|---|---|
| `"structure flow"` AND `calculus` | 0 |
| `"spectral flow"` AND `"graph Fourier"` | 0 |
| `"time-varying graph"` AND `"eigenvector"` AND `"Laplacian"` (exact) | 0 |
| `"causal network calculus"` | 0 |

This is evidence, not a guarantee: absence from arXiv is not absence from the literature. Readers are invited to falsify novelty.

## 4. Relationship to neighboring fields

- **Sturm-Liouville theory** [1]: SFC's $L_\rho$ is a special Sturm-Liouville operator; SFC adds the structure-field interpretation and the transport (Thm 1.11).
- **Graph signal processing** [2]: static in [2]; SFC treats time-varying families and the eigenframe connection.
- **Fractional calculus**: a different generalization (fractional exponents vs a pointwise scale field).
- **General relativity**: a metric field is dynamical there too, but SFC's $\rho$ is a *scale* field with no Lorentzian structure; no claim of relation is made.

## References
[1] E. Coddington, N. Levinson, *Theory of Ordinary Differential Equations*, 1955.
[2] D. Shuman et al., *The emerging field of signal processing on graphs*, IEEE Signal Processing Magazine, 2013.
[3] F. Chung, *Spectral Graph Theory*, AMS, 1997.
