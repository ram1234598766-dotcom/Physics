# Structure-Flow Calculus: Compilation & Research Roadmap

**Structure-Flow Calculus Working Group** — *2026-08-16*

This document maps how the eleven papers and four demos fit together, states the open problems of the program, and lists the next steps.

## 1. How the papers fit together

```
01 Foundations ── the rho-calculus, transport tau = ∫dx/rho, adjoint pair, energy identity
   │
   ├── 02 Structure Spectral Theory ── eigenvalues (m·pi/Lambda)^2, modes, resolvent, perturbation
   │        │
   │        ├── 05 Graded Media Engineering ── impedance matching, flux, reflectionless design
   │        ├── 08 Numerical Methods ── Galerkin, finite differences, CFL bounds
   │        └── 09 Higher-Dimensional Structure-Flow ── product metric, Weyl law, product domains
   │
   ├── 03 Causal Network Spectral Theory ── eigenframe connection, Energy Migration
   │        ├── 06 Power Networks & Synchronization
   │        ├── 07 Epidemiology on Adaptive Networks
   │        └── 10 Causal Graph-Time Signal Processing
   │
   ├── 04 Variational & Conservation Theory ── EL equations, Noether laws, Hamiltonian, coupled theory
   │
   └── 11 Novelty, Literature & Research Program ── honest positioning, novelty verification log
```

### Reading order

1. **Paper 01** first: everything downstream uses the $\rho$-calculus and the transport map.
2. **Paper 02** second: the spectral theory is the workhorse for Papers 05, 08, 09.
3. **Paper 04** is self-contained variational theory (uses only 01); it can be read any time after 01.
4. **Paper 03** begins the network half; Papers 06, 07, 10 are applications of it and can be read in any order after 03.
5. **Paper 11** documents novelty and can be read last (or first, for the honest statement).
6. **Capstone** (Paper 00) collects all central theorems in one place.

## 2. What each paper contributes

| # | Paper | Central result | Verified by |
|---|---|---|---|
| 01 | Foundations | Transport theorem; uniqueness of the calculus | `verify_calculus.py` |
| 02 | Structure Spectral Theory | Closed-form spectrum & resolvent; energy conservation | `verify_calculus.py`, `graded_wave.py` |
| 03 | Causal Network Spectral Theory | Skew connection; Energy Migration; contraction | `power_grid_mode_migration.py`, `epidemic_decay_bound.py` |
| 04 | Variational & Conservation | EL equations; Hamiltonian; corrected coupled equation | `graded_wave.py`, `sympy` |
| 05 | Graded Media Engineering | Impedance matching; flux $J=-Kp_tp_x$; transport identity | `graded_wave.py`, audit check |
| 06 | Power Networks & Synchronization | Sync rates; time-to-sync; early warning | `power_grid_mode_migration.py` |
| 07 | Epidemiology on Adaptive Networks | Outbreak bounds; extinction time; interventions | `epidemic_decay_bound.py` |
| 08 | Numerical Methods | Galerkin convergence; energy-preserving FD; CFL | `graded_wave.py` |
| 09 | Higher-Dimensional Structure-Flow | Product metric; Weyl law; product-domain spectra | audit check ($d=2$ Weyl, separation) |
| 10 | Causal Graph-Time Signal Processing | Causal GFT; modal ODEs; anomaly bounds | `power_grid_mode_migration.py` |
| 11 | Novelty, Literature & Research Program | Honest positioning; verification log | arXiv/websearch |

## 3. The theorem inventory

- **Paper 01:** 19 theorems, 3 corollaries. Core: Transport (Thm 12), Uniqueness of field (Thm 13), Uniqueness of calculus (Thm 19), Energy identity (Thm 17).
- **Paper 02:** 9+ theorems. Core: Spectrum (Thm 1), Closed-form evolution (Thm 3), Energy conservation (Thm 5), Resolvent (Thm 6), Perturbation (Thm 9).
- **Paper 03:** 6+ theorems. Core: Mass conservation (Thm 1), Contraction (Thm 2), Eigenframe connection (Thm 4), Modal ODEs (Thm 5), Energy Migration (Thm 6), Sensitivity (Thm 7).
- **Paper 04:** 10 theorems. Core: EL equations (Thm 1), Structure stationarity (Thm 3), Hamiltonian (Thm 4), Momentum (Thm 6), Coupled equation (Thm 10).
- **Paper 05:** 7+ theorems. Core: Impedance matching (Thm 1), Modes (Thm 2), Flux (Thm 6), Transport identity (Thm 7), Mode count (Thm 8).
- **Paper 06:** 5+ theorems. Core: Sync rate (Thm 2), Time-to-sync (Thm 3), Energy migration (Thm 5), Early warning (Thm 6).
- **Paper 07:** 5+ theorems. Core: Decay bound (Thm 3), Extinction time (Cor 2), Sensitivity (Thm 4).
- **Paper 08:** 5+ theorems. Core: Galerkin error (Thm 1), Consistency (Thm 3), Energy drift (Thm 5), CFL (Thm 4).
- **Paper 09:** 9+ theorems. Core: Isometry (Thm 1), Green's identities (Thms 2–3), Weyl law (Thm 5), Product spectrum (Thm 6), Obstruction (Thm 8).
- **Paper 10:** 5+ theorems. Core: Causal GFT (Thm 1), Modal ODEs (Thm 2), Filter response (Thm 3), Anomaly bound (Thm 5), Truncation (Thm 6).
- **Paper 11:** novel-literature-positioning document.

Proof/QED audit across Papers 01–10: **147 proofs, 147 QED marks, balanced equation delimiters.**

## 4. Open problems

1. **Non-separable higher-dimensional domains.** Theorem 18 (obstruction, Paper 09 Thm 8) characterizes when closed forms exist; the *general* domain case needs numerical or asymptotic methods. Next step: a structure-field finite element method.
2. **Spectral flow without the simple-eigenvalue assumption.** Theorem 9 requires $\lambda_j\ne\lambda_k$; the degenerate case (eigenvalue crossings, level repulsion) is a natural extension using the connection's skew form and adiabatic theory.
3. **Nonlinear structure dynamics.** The coupled field-structure equation (Theorem 15) is the $\kappa$-regularized start; a full nonlinear theory of $\rho$-evolution (structure as a dynamical field with its own Lagrangian) is open.
4. **Stochastic structure fields.** Time-varying graphs with random edge weights make $L(t)$ a stochastic operator; Grönwall-type bounds (Theorem 11) have probabilistic analogues (large-deviation forms).
5. **Quantum analogue.** The wave operator $\partial_t^2 - L_\rho$ has a Klein–Gordon reading; a relativistic structure-field theory and its quantization are untouched.
6. **Inverse problems.** Theorem 3 guarantees identifiability of $\rho$ from transport data; reconstruction algorithms and stability estimates beyond the mean-value bounds are open.
7. **Optimal structure design.** Paper 05 gives reflectionless design; optimizing $\rho$ for a target spectrum (e.g., prescribed bandgaps) is a natural inverse-spectral-design problem.

## 5. Next steps for the program

1. **Extend Paper 09** to include the spectral-flow and energy-migration theorems on higher-dimensional time-varying structures.
2. **Add a fifth demo** exercising the coupled equation (Theorem 15) with the corrected sign, mirroring the `sympy` check.
3. **Produce figures** for the demo plots (currently saved to `demos/figures/`) and embed them in the docs.
4. **Write the open-problem paper** (paper 12) collecting items 1–7 above with precise statements and partial results.
5. **Peer-review hardening:** convert each paper to LaTeX/arXiv format with the existing proofs unchanged, keeping the honesty caveats verbatim.

## 6. Reproducibility

- Demos: `pip install -r demos/requirements.txt`, then `python demos/verify_calculus.py` etc. All four exit 0.
- Docs: `npm run docs:build` succeeds; `npm run docs:dev` serves locally.
- Verification: see the [Verification Report](/verification).