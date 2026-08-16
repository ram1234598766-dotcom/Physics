# Structure-Flow Calculus

A new stream in mathematics and physics: a complete calculus built relative to a dynamical structure field, with proven spectral, variational, conservation, network, and signal-processing theorems, applied to graded media, power networks, adaptive contact networks, and beyond.

## Program documents

- [Program overview](docs/overview.md) — the new-stream statement
- [Comprehensive treatise](docs/papers/00-treatise.md) — the ~30-page, self-contained research paper (Parts I–IX, derivation appendix, numerical casebook)
- [Capstone paper](docs/papers/00-capstone.md) — unified statement with proofs
- [Verification report](docs/verification.md) — theorem-by-theorem evidence
- [Roadmap](docs/roadmap.md) — connections, open problems, next steps

## Papers

The research papers live in `docs/papers/` (rendered as a documentation site):

0. 00 — Capstone (unified statement of the program)
0. 00 — Comprehensive Treatise (~30 pages: the whole program, self-contained, with derivation appendix and numerical casebook)
1. 01 — Foundations ($\rho$-calculus, Fundamental Theorem, conformal transport)
2. 02 — Structure Spectral Theory (closed-form graded-media modes, energy conservation)
3. 03 — Causal Network Spectral Theory (eigenframe connection, Energy Migration Theorem)
4. 04 — Variational & Conservation Theory (structure-flow Euler-Lagrange, Noether-type laws)
5. 05 — Graded Media Engineering (matched media, reflectionless design)
6. 06 — Power Networks & Synchronization (rates, vulnerability, early warning)
7. 07 — Epidemiology on Adaptive Networks (spectral outbreak bounds, interventions)
8. 08 — Numerical Methods (spectral convergence, energy-preserving schemes)
9. 09 — Higher-Dimensional Structure-Flow (metrics, Weyl law, two-term correction, product domains)
10. 10 — Causal Graph-Time Signal Processing (causal GFT, anomaly detection)
11. 11 — Novelty, Literature & Research Program

Every theorem is proved in the paper in which it appears, and every central theorem is verified numerically by a runnable demo. Proof/QED audit across the papers, capstone, and treatise: **259 proofs, 259 QED marks**, balanced equation delimiters.

## Build the docs

```
npm install
npm run docs:dev
```

## Run the demos

```
pip install -r demos/requirements.txt
python demos/verify_calculus.py
python demos/graded_wave.py
python demos/power_grid_mode_migration.py
python demos/epidemic_decay_bound.py
```

Plots are saved to `demos/figures/`.

## Honesty statement

SFC is a new *framework* with proven theorems; it does not claim that the underlying physical equations (graded-media acoustics, swing equations, SIS epidemics) are new. See paper 11.
