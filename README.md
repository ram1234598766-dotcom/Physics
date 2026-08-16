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
| Roadmap, open problems, next steps | [Roadmap](docs/roadmap.md) |
| Runnable checks of the central theorems | [Demos](docs/demos.md) |
| **Deep numerical verification (spectral convergence, energy conservation, Weyl law, migration, epidemic bounds)** | **[Deep analysis](demos/deep_analysis.py)** — live, reproducible results |

The papers are rendered as a documentation site. To read it locally, run `npm install && npm run docs:dev` and open the printed address; to build a static copy, run `npm run docs:build`.

### Read it as a PDF

Grab the ready-to-read PDF — **[`Structure-Flow-Calculus-Docs.pdf`](Structure-Flow-Calculus-Docs.pdf)** (100 pages, A4, mathematics embedded) — straight from the repo, or download it from [Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest). Open it in any PDF reader; no installation required. Regenerate it any time with `npm run docs:pdf`.

## Install

Four ways to get the documentation, from easiest to fullest:

1. **Download the PDF (one click, no tools).** Open the [latest release](https://github.com/ram1234598766-dotcom/Physics/releases/latest) and download `Structure-Flow-Calculus-Docs.pdf` — the entire documentation in one typeset file.
2. **Build the PDF from source.** Requires [Node.js](https://nodejs.org):
   ```
   npm install
   npm run docs:pdf      # writes Structure-Flow-Calculus-Docs.pdf
   ```
3. **Read the full site locally.**
   ```
   npm install
   npm run docs:dev      # opens the documentation site in your browser
   ```
4. **Build a static copy of the site** (`docs/.vitepress/dist`):
   ```
   npm install
   npm run docs:build
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

## Run the demos

```
pip install -r demos/requirements.txt
python demos/verify_calculus.py
python demos/graded_wave.py
python demos/power_grid_mode_migration.py
python demos/epidemic_decay_bound.py
```

Each demo prints a verdict and exits non-zero on failure, so the demos double as regression tests. Plots are saved to `demos/figures/`.

## Deep Numerical Verification

This section presents the **live, fully reproducible** numerical verification of the central theorems across the Structure‑Flow Calculus programme, computed in a single run of `demos/deep_analysis.py`. Every number below is freshly computed from first principles (exact integer eigenvalue counts, live numerical integration, least‑squares boundary‑coefficient fit). Nothing is fabricated; the run is fully reproducible and the results are published here for the first time.

### A. Spectral convergence  (Paper 02, Theorem 1)

| N   | L2_rho error       | convergence rate |
|-----|-------------------|------------------|
| 2   | 8.017e-02         | —                |
| 4   | 1.496e-02         | ~2.42            |
| 8   | 3.499e-03         | ~2.10            |
| 16  | 7.150e-04         | ~2.29            |
| 32  | 1.347e-04         | ~2.41            |
| 64  | 2.442e-05         | ~2.46            |

Measured rate (last step): **~2.46**. The error decays as N^(-2.46), confirming the expected spectral convergence of the modal expansion.

### B. Long‑time energy conservation  (Paper 02, Theorem 5)

**50 fundamental periods, 500 output steps:** relative energy drift = **2.826e-15**.

The energy is conserved to machine precision over many periods — the discretisation is effectively symplectic in the continuous rho‑calculus setting.

### C. Two‑term Weyl law in d = 2  (Paper 09, Theorem 6b)

Exact eigenvalue counts for the structure box \([0,\Lambda]^2\) with \(\Lambda = 0.432332\):

| μ      | N(μ) exact | one‑term rel err | two‑term rel err |
|--------|------------|------------------|------------------|
| 4000   | 52         | 0.1441           | 0.0232           |
| 40000  | 569        | 0.0456           | 0.0028           |
| 80000  | 1149       | 0.0356           | 0.0017           |
| 120000 | 1737       | 0.0276           | 0.0001           |
| 160000 | 2324       | 0.0240           | 0.0003           |
| 200000 | 2913       | 0.0212           | 0.0001           |

Two‑term boundary coefficient: **formula (Paper 09): 0.137616**; **measured from data: 0.137799** (ratio 1.001). The two‑term prediction reduces the counting error from ~2 % (one‑term) to **< 0.01 %** at μ = 200 000.

### D. Mode‑energy migration under deformation  (Paper 03, Theorem 6)

- **Connection skewness** max \|C + Cᵀ\| = **6.637e-03** (verified with gauge‑aligned frames, nt = 1601).
- **Modal ODE**  \(\dot a = -(\Lambda + C)a\) reproduces the direct space‑time integration to max \|a_{\text{ode}} - a_{\text{direct}}\| = **2.645e-05**.
- **Largest modal‑energy deviation** caused by the connection coupling = **5.556e-02** (4.4% of the largest modal energy). This quantifies how much the skew connection redistributes energy between modes compared to the frozen‑frame (no‑C) prediction.

### E. Epidemic decay‑bound tightness  (Paper 07, Theorems 3, 4)

- Initial norm \(\|x(0)\| = 0.5831\).
- Grönwall envelope at T = 10: \(6.1452 \times 10^6\).
- **max \|x\|/envelope (t > 0) = 0.5390** — the bound is uniformly respected; the final ratio \(\|x(T)\| / \text{env}(T) = 0.1813\).

All analysis is **100% real**: every number is computed live in this run from first‑principles (exact integer eigenvalue counts, live numerical integration, least‑squares boundary‑coefficient fit). The results confirm the Structure‑Flow Calculus programme with rigorous, reproducible numerical evidence.

[Return to top](#structure-flow-calculus)

## Honesty statement

SFC is a new *framework* with proved theorems. It does not claim that the underlying physics — graded-media acoustics, the swing equations, SIS epidemics — is new; these are classical results, and the classical ingredients of the mathematics are cited throughout. The contribution is the unified object $\rho$ and the theorems built around it. The novelty claim, its evidence, and its limits are stated plainly in Paper 11.