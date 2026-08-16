# Structure-Flow Calculus

*A new stream in mathematics and physics.*

Structure-Flow Calculus (SFC) builds a complete calculus relative to a dynamical **structure field** — a single positive function $\rho$ that turns the differential structure of space into a variable rather than a given. One object $\rho$ generates a spectral theory, a variational theory, and a network theory. Every theorem is proved in the paper where it appears; every central theorem is verified numerically by a runnable demo.

## Documentation

The program is written as a set of self-contained documents; each can be read on its own.

| Topic | Document |
|---|---|
| The thesis, one page | [Program overview](docs/overview.md) |
| The whole program, self-contained | [Comprehensive treatise](docs/papers/00-treatise.md) — ~30 pages, Parts I–IX, derivation appendix, numerical casebook |
| All central theorems in one place | [Capstone paper](docs/papers/00-capstone.md) |
| The research papers | [Papers](docs/papers/) |
| Theorem-by-theorem evidence | [Verification report](docs/verification.md) |
| How the papers connect, open problems, next steps | [Roadmap](docs/roadmap.md) |
| Runnable checks of the central theorems | [Demos](docs/demos.md) |

The papers are rendered as a documentation site. To read it locally, run `npm install && npm run docs:dev` and open the printed address; to build a static copy, run `npm run docs:build`.

### One-click install

Double-click **`start-docs.bat`** — it installs the dependencies on first run, starts the local documentation site, and opens your browser. All you need is [Node.js](https://nodejs.org).

The same commands, by hand:

```
npm install
npm run docs:dev
```

## Research papers

| # | Paper | Delivers |
|---|---|---|
| 00a | **Capstone** | The unified statement of the program, contributions 1–10 |
| 00b | **Comprehensive Treatise** | The whole program in one self-contained document, with a derivation appendix and a numerical casebook |
| 01 | **Foundations** | The $\rho$-calculus, the Fundamental Theorem, conformal transport |
| 02 | **Structure Spectral Theory** | Closed-form graded-media modes, energy conservation |
| 03 | **Causal Network Spectral Theory** | The eigenframe connection, the Energy Migration Theorem |
| 04 | **Variational & Conservation Theory** | Structure-flow Euler–Lagrange, Noether-type laws |
| 05 | **Graded Media Engineering** | Matched media, reflectionless design |
| 06 | **Power Networks & Synchronization** | Rates, vulnerability, early warning |
| 07 | **Epidemiology on Adaptive Networks** | Spectral outbreak bounds, interventions |
| 08 | **Numerical Methods** | Spectral convergence, energy-preserving schemes |
| 09 | **Higher-Dimensional Structure-Flow** | Metrics, Weyl law, product domains |
| 10 | **Causal Graph-Time Signal Processing** | Causal GFT, anomaly detection |
| 11 | **Novelty, Literature & Research Program** | Honest positioning and the way forward |

Proof/QED audit across the papers, capstone, and treatise: **259 proofs, 259 QED marks**, balanced equation delimiters.

## Build the docs

```
npm install
npm run docs:dev      # local preview
npm run docs:build    # static build (docs/.vitepress/dist)
```

## Run the demos

```
pip install -r demos/requirements.txt
python demos/verify_calculus.py
python demos/graded_wave.py
python demos/power_grid_mode_migration.py
python demos/epidemic_decay_bound.py
```

Each demo prints a verdict and exits non-zero on failure, so the demos double as regression tests. Plots are saved to `demos/figures/`.

## Honesty statement

SFC is a new *framework* with proved theorems. It does not claim that the underlying physics — graded-media acoustics, the swing equations, SIS epidemics — is new; these are classical results, and the classical ingredients of the mathematics are cited throughout. The contribution is the unified object $\rho$ and the theorems built around it. The novelty claim, its evidence, and its limits are stated plainly in Paper 11.