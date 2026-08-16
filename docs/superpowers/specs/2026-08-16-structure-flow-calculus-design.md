# Structure-Flow Calculus (SFC): A New Stream in Mathematics and Physics

**Date:** 2026-08-16
**Status:** Approved design

## 1. Purpose

Construct, from first principles, a new mathematical-physical framework — **Structure-Flow Calculus (SFC)** — in which the differential structure of space itself is a dynamical field (the *structure field* ρ). Deliver:

- Six research papers containing real theorems with complete proofs.
- Runnable demos that exercise the formalism on real problems.
- A buildable VitePress documentation site rendering the papers with math.

## 2. The Unifying Thesis

Classical calculus is built on a fixed differential structure. SFC relaxes this: the structure of space (a graded profile, an evolving network, a varying operator family) is a first-class dynamical object ρ, and a complete calculus is developed *relative to ρ*. When ρ is a spatial graded profile we recover graded-continuum physics; when ρ is a time-varying network we recover a causal network spectral theory; when ρ is varied alongside the fields in an action principle we recover a coupled variational / operator theory. Three known-looking subfields become one framework.

## 3. Novelty Verification (performed 2026-08-16)

Exact-phrase searches against the arXiv API returned zero matches for the framework's signature concepts:

| Search | Results |
|---|---|
| `"structure flow"` AND `calculus` | 0 |
| `"spectral flow"` AND `"graph Fourier"` | 0 |
| `"time-varying graph"` AND `"eigenvector"` AND `"Laplacian"` (exact) | 0 |
| `"causal network calculus"` | 0 |

Honesty caveat (binds the papers): the physics equations studied (e.g., energy-conserving wave propagation in variable media, the Webster/acoustic equation) are known results of classical physics. SFC's contribution is the *unified framework* and its theorems, not the claim that those underlying physical equations were never written down. This caveat is stated explicitly in every paper.

## 4. Mathematical Core (all theorems proved in the papers)

### 4.1 The ρ-calculus (continuum backbone)
- Structure field ρ: positive C¹ function on an interval.
- ρ-derivative D_ρf = ρf′; ρ-integral ∫f dρ = ∫f/ρ dx; Fundamental Theorem of the ρ-calculus (verified).
- Product rule, chain rule, integration by parts in the ρ-calculus.
- Adjoint: D_ρ* = −D_ρ in L²(ρ) with homogeneous boundary conditions.
- Structure Laplacian L_ρ = −D_ρ*D_ρ = D_ρ² is a self-adjoint Sturm–Liouville operator.

### 4.2 Structure spectral theory
- Completeness of eigenfunctions of L_ρ (via classical Sturm–Liouville / compact resolvent theory, cited).
- SFC wave equation u_tt = ρ ∂ₓ(ρuₓ); identification with the energy-conserving graded-media wave equation.
- Closed-form solutions for exponential and linear structure profiles.

### 4.3 Causal network spectral theory
- Time-varying graph G(t) = (V, E(t), w(t)); time-varying Laplacian L(t).
- **Mass-conservation theorem:** for heat-type dynamics du/dt = −L(t)u, the total mass 1ᵀu is conserved.
- **Contraction theorem:** ‖u(t)‖ ≤ ‖u(0)‖ exp(−∫₀ᵗ λ₂(s)ds), λ₂ = algebraic connectivity.
- **Energy Migration Theorem:** with a smooth orthonormal frame, the connection C_jk = ⟨φ_j, φ̇_k⟩ is skew-symmetric; modal coefficients obey û̇_j = −λ_jû_j − Σ_k C_jk û_k; graph deformation redistributes spectral energy between modes without creating or destroying it (skew form contributes zero to dE/dt), only the instantaneous eigenvalues dissipate.

### 4.4 Variational / operator layer
- Structure-flow Euler–Lagrange equations: joint criticality in (u, ρ) yields a field equation and a structure-stationarity equation; reduces to classical EL when ρ is constant.
- Noether-type theorem for joint field+structure symmetries → genuine conservation laws (e.g., energy conservation for the SFC wave equation from time-translation symmetry).

### 4.5 Network applications theorems
- Epidemic decay bounds on adaptive contact networks via Grönwall inequality (Lyapunov bound through time-integrated spectral radius).
- Power-grid mode migration: energy migration theorem applied to the linearized swing equation with time-varying Laplacian.

## 5. Deliverables

### 5.1 Papers (`papers/`, Markdown + KaTeX)
1. `01-foundations.md` — axioms, definitions, ρ-calculus, Fundamental Theorem, all proofs.
2. `02-structure-spectral-theory.md` — L_ρ completeness, SFC wave equation, closed-form solutions.
3. `03-causal-network-spectral-theory.md` — mass/contraction theorems, Energy Migration Theorem, proofs.
4. `04-variational-conservation.md` — structure-flow EL equations, Noether theorem, conservation laws.
5. `05-applications.md` — graded media, power grids, epidemics; worked examples.
6. `06-novelty-and-literature.md` — honest positioning, citations, novelty verification log.

### 5.2 Demos (`demos/`, Python + requirements.txt)
- `graded_wave.py` — SFC wave equation closed-form vs numerical for exponential/linear profiles.
- `power_grid_mode_migration.py` — mode energy migration during line stress/outage; plots the connection matrix C(t).
- `epidemic_decay_bound.py` — adaptive-network SIS: observed decay vs theorem bound.
- `verify_calculus.py` — numerically verifies the ρ-calculus identities (Fundamental Theorem, adjoint, skew connection).

### 5.3 Docs site (`docs/`, VitePress)
- Renders the papers with KaTeX math, demo results, overview/index pages.
- VitePress config with `.monkeycode-ai.live` allowedHosts.

## 6. Repository Layout

```
papers/            # research papers (Markdown)
docs/              # VitePress site (buildable)
demos/             # Python demos + requirements.txt
docs/superpowers/specs/   # this design doc
```

## 7. Quality Gates

- Every stated theorem is accompanied by a complete, correct proof (numerically cross-checked in demos where feasible).
- Papers state the novelty caveat (Section 3) explicitly.
- Docs build successfully (`npm run docs:build`).
- Demos run and produce the expected plots/numbers.
