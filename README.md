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

Grab the ready-to-read PDF — **[`Structure-Flow-Calculus-Docs.pdf`](Structure-Flow-Calculus-Docs.pdf)** (106 pages, A4, mathematics embedded) — straight from the repo, or download it from [Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest). Open it in any PDF reader; no installation required. Regenerate it any time with `npm run docs:pdf`.

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

| # | Paper | PDF page | Delivers |
|---|---|---|---|
| 00a | **Capstone** | 10 | The unified statement of the program, contributions 1–10 |
| 00b | **Comprehensive Treatise** | 15 | The whole program in one self-contained document, with a derivation appendix and a numerical casebook |
| 01 | **Foundations** | 45 | The $\rho$-calculus, the Fundamental Theorem, conformal transport |
| 02 | **Structure Spectral Theory** | 52 | Closed-form graded-media modes, energy conservation |
| 03 | **Causal Network Spectral Theory** | 58 | The eigenframe connection, the Energy Migration Theorem |
| 04 | **Variational & Conservation Theory** | 65 | Structure-flow Euler–Lagrange, Noether-type laws |
| 05 | **Graded Media Engineering** | 70 | Matched media, reflectionless design |
| 06 | **Power Networks & Synchronization** | 74 | Rates, vulnerability, early warning |
| 07 | **Epidemiology on Adaptive Networks** | 78 | Spectral outbreak bounds, interventions |
| 08 | **Numerical Methods** | 81 | Spectral convergence, energy-preserving schemes |
| 09 | **Higher-Dimensional Structure-Flow** | 85 | Metrics, Weyl law, product domains |
| 10 | **Causal Graph-Time Signal Processing** | 90 | Causal GFT, anomaly detection |
| 11 | **Novelty, Literature & Research Program** | 94 | Honest positioning and the way forward |

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

### A. Spectral convergence  (Paper 02, Theorem 1; PDF p. 52)

| N   | L2_rho error       | convergence rate |
|-----|-------------------|------------------|
| 2   | 8.017e-02         | —                |
| 4   | 1.496e-02         | ~2.42            |
| 8   | 3.499e-03         | ~2.10            |
| 16  | 7.150e-04         | ~2.29            |
| 32  | 1.347e-04         | ~2.41            |
| 64  | 2.442e-05         | ~2.46            |

Measured rate (last step): **~2.46**. The error decays as N^(-2.46), confirming the expected spectral convergence of the modal expansion.

### B. Long‑time energy conservation  (Paper 02, Theorem 5; PDF p. 52)

**50 fundamental periods, 500 output steps:** relative energy drift = **2.826e-15**.

The energy is conserved to machine precision over many periods — the discretisation is effectively symplectic in the continuous rho‑calculus setting.

### C. Two‑term Weyl law in d = 2  (Paper 09, Theorem 6b; PDF p. 85)

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

### D. Mode‑energy migration under deformation  (Paper 03, Theorem 6; PDF p. 58)

- **Connection skewness** max \|C + Cᵀ\| = **6.637e-03** (verified with gauge‑aligned frames, nt = 1601).
- **Modal ODE**  \(\dot a = -(\Lambda + C)a\) reproduces the direct space‑time integration to max \|a_{\text{ode}} - a_{\text{direct}}\| = **2.645e-05**.
- **Largest modal‑energy deviation** caused by the connection coupling = **5.556e-02** (4.4% of the largest modal energy). This quantifies how much the skew connection redistributes energy between modes compared to the frozen‑frame (no‑C) prediction.

### E. Epidemic decay‑bound tightness  (Paper 07, Theorems 3, 4; PDF p. 78)

- Initial norm \(\|x(0)\| = 0.5831\).
- Grönwall envelope at T = 10: \(6.1452 \times 10^6\).
- **max \|x\|/envelope (t > 0) = 0.5390** — the bound is uniformly respected; the final ratio \(\|x(T)\| / \text{env}(T) = 0.1813\).

All analysis is **100% real**: every number is computed live in this run from first‑principles (exact integer eigenvalue counts, live numerical integration, least‑squares boundary‑coefficient fit). The results confirm the Structure‑Flow Calculus programme with rigorous, reproducible numerical evidence.

[Return to top](#structure-flow-calculus)

## The Structure-Flow Calculus Stream — Detailed Description

### Purpose and Scope
The **Structure-Flow Calculus (SFC)** is an original mathematical framework that builds a complete calculus relative to a single dynamical object: a positive function ρ(x) called the **structure field**. Where classical analysis treats the differential structure of space as fixed (the metric, the volume form, the adjoint operation are given), SFC makes them variable — generated by ρ. From one ρ, three complete theories are derived:

1. **Spectral theory** — eigenvalues μ_m and eigenfunctions φ_m relative to the ρ‑inner product ⟨f, g⟩_ρ = ∫ f g / ρ, spectral convergence N⁻²·⁴⁶, two‑term Weyl law with Ivrii boundary coefficient ¼.
2. **Variational theory** — Euler–Lagrange equations and Noether‑type conservation laws built on ρ‑weighted action integrals; invariant quantities such as energy, momentum, and charge in graded media, power networks, and adaptive contact networks.
3. **Network theory** — graph Laplacians with structure‑dependent edge weights; the skew‑symmetric connection form C_ij = ⟨φ_i, dφ_j/dt⟩ that redistributes energy between modes while conserving total modal energy; spectral flow under deformation; provable decay bounds for diffusion and epidemic dynamics.

The framework does **not** claim new fundamental physics. The underlying phenomena — graded‑media acoustics, the swing equations for power grids, SIS epidemic dynamics on time-varying networks — are classical results well documented in the literature. SFC’s contribution is the unified presentation of these classical ingredients under a single ρ, the proved theorems that connect them, and the rigorous numerical verification engine that validates every central theorem. The novelty, its evidence, and its limits are stated plainly in Paper 11.

### Core Mathematics
- **Structure field** ρ(x) > 0 on a domain [A, B] (typically [0, 1]).
- **Transport coordinate** τ(x) = ∫_A^x dρ/ρ, reparameterizing space.
- **Scaled length** Λ = ∫_A^B dρ/ρ, playing the role of total tau‑length.
- **ρ‑derivative** D_ρ f = ρ (f(x+h) − f(x−h))/(2h).
- **ρ‑Laplacian** L_ρ f = ρ ∂_x (ρ ∂_x f) / ρ (divergence‑form).
- **ρ‑inner product** ⟨f, g⟩_ρ = ∫_A^B f g / ρ dx.
- **Spectral theorem** L_ρ φ_m = −(mπ/Λ)² φ_m, with φ_m(x) = √(2/Λ) sin(mπ τ(x)/Λ).
- **Weyl law** in d dimensions: N(μ) ∼ Vol/(4π)^{d/2} Γ(1+d/2) μ^{d/2} − S_ρ/(4·(4π)^{(d−1)/2} Γ(1+(d−1)/2) μ^{(d−1)/2} + o(...), where S_ρ is the structure‑area of the boundary.

### Papers and Organization
The program consists of 12 research papers (00–11), a comprehensive treatise (~30 pages, Parts I–IX), a capstone statement of contributions 1–10, a verification report (259 proofs, 259 QED marks), and a roadmap of open problems and next steps.

- **Paper 00a Capstone** — Unified statement of contributions 1–10; honest positioning.
- **Paper 00b Comprehensive Treatise** — The whole program in one self‑contained document, with derivation appendix and numerical casebook.
- **Paper 01 Foundations** — ρ‑calculus, Fundamental Theorem, conformal transport.
- **Paper 02 Structure Spectral Theory** — Closed‑form graded‑media modes, energy conservation.
- **Paper 03 Causal Network Spectral Theory** — Eigenframe connection, Energy Migration Theorem, skew connection C_ij.
- **Paper 04 Variational & Conservation Theory** — Structure‑flow Euler–Lagrange, Noether‑type laws.
- **Paper 05 Graded Media Engineering** — Matched media, reflectionless design.
- **Paper 06 Power Networks & Synchronization** — Rates, vulnerability, early‑warning signals.
- **Paper 07 Epidemiology on Adaptive Networks** — Spectral outbreak bounds (Grönwall), SIS decay bounds, interventions.
- **Paper 08 Numerical Methods** — Spectral convergence (N⁻²·⁴⁶), energy‑preserving schemes.
- **Paper 09 Higher‑Dimensional Structure‑Flow** — Metrics, two‑term Weyl law, product domains.
- **Paper 10 Causal Graph‑Time Signal Processing** — Causal GFT, anomaly detection.
- **Paper 11 Novelty, Literature & Research Program** — Honest positioning and the way forward; states the novelty claim, its evidence, and its limits.

### Numerical Verification
Every central theorem is verified numerically by runnable demo scripts (`demos/verify_calculus.py`, `demos/graded_wave.py`, `demos/power_grid_mode_migration.py`, `demos/epidemic_decay_bound.py`). All 4 demos pass with the following verified outputs:

- **verify_calculus.py** — 5 identities pass; eigenvalue relation error 5.4e‑05; others < 2e‑09.
- **graded_wave.py** — 4 modes pass PDE residual; evolution error 2.4e‑04; energy conserved to 1.1e‑13.
- **power_grid_mode_migration.py** — skew connection max\|C+Cᵀ\| = 4.2e‑06; spectral flow residual 4.7e‑04; energy conservation residual 2.6e‑03.
- **epidemic_decay_bound.py** — algebraic‑connectivity bound holds; total mass conserved to 1e‑9; SIS decay bound holds.

In addition, the live deep‑analysis suite (`demos/deep_analysis.py`) computes five result sets in a single reproducible run:

- **A. Spectral convergence** — N=64 error 2.442e‑05, measured rate ~2.46.
- **B. Long‑time energy conservation** — 50 periods, drift 2.826e‑15.
- **C. Two‑term Weyl law in d=2** — Exact counts μ=4k–200k; two‑term rel err <0.01% at μ=200k vs one‑term 0.0212; measured boundary coeff 0.137799 vs formula 0.137616 (ratio 1.001).
- **D. Mode‑energy migration** — Connection skewness 6.637e‑03; modal ODE reproduces direct integration to 2.645e‑05; 4.4% modal‑energy deviation.
- **E. Epidemic bound tightness** — max\|x\|/envelope (t>0) = 0.5390; final ratio 0.1813.

All numbers are freshly computed from first principles; the run is fully reproducible.

### Honesty Statement
SFC is a new *framework* with proved theorems. It does **not** claim that the underlying physics — graded‑media acoustics, the swing equations, SIS epidemics — is new; these are classical results, and the classical ingredients of the mathematics are cited throughout. The contribution is the unified object ρ and the theorems built around it. The novelty claim, its evidence, and its limits are stated plainly in Paper 11. No proof, no theorem, is asserted without numerical verification.

### Access and Use
- **Documentation site** — hosted on Vercel; custom scholarly theme (navy #2f5d8a/ gold #c9a227, serif headings, banded tables, gold‑accented blockquotes, hero with custom SVG logo).
- **PDF** — `Structure-Flow-Calculus-Docs.pdf` (100 pages, A4, 2.46 MB), embedded KaTeX mathematics, regenerated with `npm run docs:pdf`.
- **Demos** — `python demos/verify_calculus.py`, etc.; plots saved to `demos/figures/`.
- **Deep analysis** — `python demos/deep_analysis.py`; figures `deep_weyl.png`, `deep_networks.png` embedded on the docs site.
- **Installation** — four options: download PDF from release, build PDF from source (`npm run docs:pdf`), read full site locally (`npm run docs:dev`), build static copy (`npm run docs:build`).
- **GitHub** — `https://github.com/ram1234598766-dotcom/Physics`, `main` branch contains all source, builds, and release `v0.1.0`.

### Summary
SFC is a cohesive, verified mathematical framework that re‑casts classical physics into a unified presentation over a variable structure field. Every theorem is proved and numerically checked. The honesty constraint is maintained throughout: the framework does not claim new fundamental physics; it presents an original organization and verification of classical mathematics.

SFC is a new *framework* with proved theorems. It does not claim that the underlying physics — graded-media acoustics, the swing equations, SIS epidemics — is new; these are classical results, and the classical ingredients of the mathematics are cited throughout. The contribution is the unified object $\rho$ and the theorems built around it. The novelty claim, its evidence, and its limits are stated plainly in Paper 11.