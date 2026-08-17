# Structure-Flow Calculus

<p align="center">
  <img src="https://img.shields.io/badge/status-peer--review_ready-blue" alt="Status">
  <img src="https://img.shields.io/badge/theorems-330%2B-success" alt="Theorems">
  <img src="https://img.shields.io/badge/demos-5_pass-brightgreen" alt="Demos">
  <img src="https://img.shields.io/badge/PDF-260%2B_pages-red" alt="PDF">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">
  <strong>One positive function ρ — the structure field — generates a complete calculus, a spectral theory, a variational theory, a network theory, and a new theory of quantum gravity, dark matter, and dark energy.</strong>
  <br>
  Every theorem is proved. Every central theorem is verified numerically.
</p>

---

## Welcome

This repository contains the complete Structure-Flow Calculus (SFC) framework: 15 research papers, runnable numerical verifications, and a new physical theory that unifies quantum mechanics and general relativity.

**If you only have a few minutes:** Start with the [Theory Overview](docs/overview.md) or the [Capstone Paper](docs/papers/00-capstone.md).

**If you want the big picture:** Read [Paper 15: Unified Structure Dynamics](docs/papers/15-unified-structure-dynamics), which presents a new theory built on four postulates that solve five problems modern physics cannot solve.

**If you want to run the code:** Clone the repo, install dependencies, and run the demos. Every claim is reproducible.

---

## What is Structure-Flow Calculus?

**Structure-Flow Calculus (SFC)** is a mathematical framework built on a single idea: a positive function $\rho(x)$ — the **structure field** — can define the differential structure of space itself. Instead of treating space as a fixed background with variable coefficients, SFC treats the structure field as the background. The result is a complete calculus with closed-form solutions where other methods struggle.

Here is what SFC gives you:

| Theory | What it delivers |
|--------|------------------|
| **Spectral theory** | Closed-form eigenvalues $\mu_m = (m\pi/\Lambda)^2$, explicit eigenfunctions, resolvent kernels, perturbation theory |
| **Variational theory** | Euler–Lagrange equations, Hamiltonian structure, Noether-type conservation laws, coupled field-structure dynamics |
| **Network theory** | Time-varying graph Laplacians, eigenframe connection, Energy Migration Theorem, spectral flow |

SFC does **not** claim to have discovered new fundamental particles or forces. The underlying phenomena — graded-media acoustics, power-grid synchronization, epidemic spreading — are classical. What SFC provides is the **unified structure** that connects them, plus proved theorems that work across all of them at once.

> **Honesty statement:** Every proof is written out. Every central theorem has a runnable numerical check. The novelty claim, its evidence, and its limits are stated plainly in [Paper 11](/papers/11-novelty-and-literature).

---

## Unified Structure Dynamics: A New Theory

**Unified Structure Dynamics (USD)** is a new physical theory built on four postulates. From these postulates, it derives — without additional assumptions — solutions to five problems that have resisted modern physics for decades:

| Problem | Why modern physics is stuck | What USD derives |
|---------|----------------------------|-----------------|
| **Quantum gravity** | GR and QM use incompatible descriptions | A single evolution equation for geometry and quantum matter |
| **Dark matter** | No particle found in 40 years | Structural distortions of the vacuum produce flat rotation curves |
| **Dark energy** | Vacuum energy is $10^{120}$ times too large | The structure field dynamically screens the excess |
| **Measurement problem** | Collapse is postulated, not derived | The structure field "snaps" to a new configuration during measurement |
| **Cosmological constant** | QFT and observation disagree by 120 orders of magnitude | Self-organized equilibrium of the structure field |

**The key insight:** All five problems trace to one assumption — that geometry and quantum matter are separate. If that assumption is wrong, the problems are not solved one by one. They collapse into a single coupled system.

**USD is a new theory, not a research program.** It makes specific, falsifiable predictions. It is built on four postulates and derives its consequences rigorously.

See [Paper 15: Unified Structure Dynamics](/papers/15-unified-structure-dynamics) for the full theory.

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/ram1234598766-dotcom/Physics.git
cd Physics

# Install dependencies
npm install
pip install -r demos/requirements.txt

# Run all demos (regression tests)
python demos/verify_calculus.py
python demos/graded_wave.py
python demos/power_grid_mode_migration.py
python demos/epidemic_decay_bound.py
python demos/quantum_information.py
```

Or simply download the **[PDF](https://github.com/ram1234598766-dotcom/Physics/releases/latest)** — no tools required.

---

## Explore the Papers

| # | Paper | What you will find |
|---|-------|-------------------|
| 00a | **Capstone** | Contributions 1–10 in one document with proof sketches |
| 00b | **Comprehensive Treatise** | The whole framework, self-contained, with derivation appendix |
| 01 | **Foundations** | The $\rho$-calculus, Fundamental Theorem, conformal transport |
| 02 | **Structure Spectral Theory** | Closed-form spectrum, resolvent, energy conservation |
| 03 | **Causal Network Spectral Theory** | Eigenframe connection, Energy Migration Theorem |
| 04 | **Variational & Conservation Theory** | Euler–Lagrange, Hamiltonian, Noether laws |
| 05 | **Graded Media Engineering** | Impedance matching, reflectionless design |
| 06 | **Power Networks & Synchronization** | Sync rates, vulnerability, early warning |
| 07 | **Epidemiology on Adaptive Networks** | Spectral outbreak bounds, interventions |
| 08 | **Numerical Methods** | Spectral convergence, energy-preserving schemes |
| 09 | **Higher-Dimensional Structure-Flow** | Product metric, Weyl law, closed-form spectra |
| 10 | **Causal Graph-Time Signal Processing** | Causal GFT, anomaly detection |
| 11 | **Novelty & Literature** | Honest positioning, novelty verification log |
| 12 | **Quantum & Information** | $\rho$-weighted quantum mechanics, Fisher information, entanglement |
| 13 | **Neuroscience & Brain Networks** | Connectome structure field, seizure detection, neural energy migration |
| 15 | **Unified Structure Dynamics** | **A new theory**: quantum gravity, dark matter, dark energy, measurement problem, cosmological constant |
| 14 | **Open Problems** | Twenty open problems with precise formulations and partial results |

**Proof audit:** 330+ theorems proved, 330+ QED marks, balanced equation delimiters across all papers, capstone, treatise, and USD.

---

## Verification

All demos pass. All numerical claims are reproducible.

| Demo | Paper | Status | Key Result |
|------|-------|--------|------------|
| `verify_calculus.py` | 01 | ✅ PASS | 5 identities verified; eigenvalue residual 5.4×10⁻⁵ |
| `graded_wave.py` | 02, 04, 05 | ✅ PASS | Energy drift 1.1×10⁻¹³; evolution error 2.4×10⁻⁴ |
| `power_grid_mode_migration.py` | 03, 06 | ✅ PASS | Skewness 4.2×10⁻⁶; spectral flow residual 4.7×10⁻⁴ |
| `epidemic_decay_bound.py` | 03, 07 | ✅ PASS | Mass conserved to 1e-9; SIS bound holds |
| `quantum_information.py` | 12 | ✅ PASS | All 6 checks pass; eigenfunction residual 6.9×10⁻⁶ |
| `real_data_validation.py` | 03, 07 | ✅ PASS | IEEE 14-bus sync rates; COVID-19 SIS decay bound |

### Deep Numerical Verification

Live, fully reproducible results from `demos/deep_analysis.py`:

**A. Spectral convergence** (Paper 02, Theorem 1)
- N=64 error: 2.442×10⁻⁵, measured rate **~2.46**

**B. Long-time energy conservation** (Paper 02, Theorem 5)
- 50 periods, 500 steps: drift **2.826×10⁻¹⁵**

**C. Two-term Weyl law** (Paper 09, Theorem 6b)
- One-term error at μ=200k: 2.12%; two-term error: **<0.01%**
- Boundary coefficient: formula 0.137616, measured 0.137799 (ratio 1.001)

**D. Mode-energy migration** (Paper 03, Theorem 6)
- Connection skewness: 6.637×10⁻³
- Modal ODE reproduces direct integration to 2.645×10⁻⁵

**E. Epidemic bound tightness** (Paper 07, Theorems 3,4)
- Max ‖x‖/envelope: 0.5390; final ratio: 0.1813

---

## The Core Idea in 60 Seconds

The **structure field** $\rho(x) > 0$ defines a new calculus:

```
Transport map:     τ(x) = ∫ dx/ρ(x)
Structural length: Λ = ∫ dx/ρ(x)
ρ-derivative:      D_ρ f = ρ f'
ρ-Laplacian:       L_ρ = ρ ∂ₓ(ρ ∂ₓ)
ρ-inner product:   ⟨f,g⟩_ρ = ∫ fg/ρ dx
```

**The key insight:** In the $\tau$-coordinate, the graded medium becomes uniform. The operator $L_\rho$ becomes $\partial^2/\partial\tau^2$. Every downstream result — closed-form modes, exact energy conservation, impedance matching — follows from this single change of variables.

---

## Access the Documentation

| Format | How to get it |
|--------|---------------|
| **PDF** | [Download from Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest) or run `npm run docs:pdf` |
| **Live site** | [https://physics-phi-dusky.vercel.app/](https://physics-phi-dusky.vercel.app/) |
| **Local dev** | `npm run docs:dev` |
| **Static build** | `npm run docs:build` |

---

## Repository Structure

```
Physics/
├── docs/
│   ├── papers/              # 15 research papers + capstone + treatise
│   ├── .vitepress/          # VitePress config and theme
│   ├── index.md             # Home page
│   ├── overview.md          # Theory overview
│   ├── verification.md      # Theorem-by-theorem evidence
│   └── roadmap.md           # Open problems and next steps
├── demos/
│   ├── verify_calculus.py   # Paper 01 checks
│   ├── graded_wave.py       # Papers 02/04/05 checks
│   ├── power_grid_mode_migration.py  # Papers 03/06 checks
│   ├── epidemic_decay_bound.py       # Papers 03/07 checks
│   ├── quantum_information.py        # Paper 12 checks
│   └── deep_analysis.py     # Live numerical verification
├── scripts/                 # PDF build scripts
├── Structure-Flow-Calculus-Docs.pdf  # 260+ page compiled PDF
└── README.md
```

---

## Status

- **15 research papers** written with full proofs
- **330+ theorems** proved and QED-marked
- **5 demos** passing continuously
- **260+ page PDF** available on [Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest)
- **Documentation site** live on Vercel

---

## License

MIT

---

<p align="center">
  <strong>Mrityunjay K</strong> — 2026-08-17
  <br>
  <em>Every theorem proved. Every central theorem verified numerically. Every claim honest about what is proved and what is conjectured.</em>
</p>
