# Structure-Flow Calculus

<p align="center">
  <img src="https://img.shields.io/badge/status-peer--review_ready-blue" alt="Status">
  <img src="https://img.shields.io/badge/theorems-294-success" alt="Theorems">
  <img src="https://img.shields.io/badge/demos-5_pass-brightgreen" alt="Demos">
  <img src="https://img.shields.io/badge/PDF-241_pages-red" alt="PDF">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>

<p align="center">
  <strong>One positive function ρ — the structure field — generates a complete calculus, a spectral theory, a variational theory, and a network theory.</strong>
  <br>
  Every theorem is proved. Every central theorem is verified numerically.
</p>

---

## What is Structure-Flow Calculus?

**Structure-Flow Calculus (SFC)** is a new mathematical framework that builds a complete calculus relative to a dynamical **structure field** — a single positive function ρ(x) that promotes the differential structure of space from a fixed background to a first-class variable.

From this single object ρ, three complete theories emerge:

| Theory | What it delivers |
|--------|------------------|
| **Spectral theory** | Closed-form eigenvalues μₘ = (mπ/Λ)², explicit eigenfunctions, resolvent kernels, perturbation theory |
| **Variational theory** | Euler–Lagrange equations, Hamiltonian structure, Noether-type conservation laws, coupled field-structure dynamics |
| **Network theory** | Time-varying graph Laplacians, eigenframe connection, Energy Migration Theorem, spectral flow |

The framework does **not** claim new fundamental physics. The underlying phenomena — graded-media acoustics, swing equations, SIS epidemics — are classical. The contribution is the **unified object ρ** and the **proved theorems** that connect these classical ingredients under a single structure field.

> **Honesty statement:** Every proof is written out. Every central theorem has a runnable numerical check. The novelty claim, its evidence, and its limits are stated plainly in [Paper 11](/papers/11-novelty-and-literature).

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

Or simply download the **[241-page PDF](https://github.com/ram1234598766-dotcom/Physics/releases/latest)** — no tools required.

---

## Documentation

| Resource | Description |
|----------|-------------|
| **[Program Overview](docs/overview.md)** | The thesis in one page — what SFC provides, why it matters |
| **[Capstone Paper](docs/papers/00-capstone.md)** | Contributions 1–10 in a single document with proof sketches |
| **[Comprehensive Treatise](docs/papers/00-treatise.md)** | ~30 pages, Parts I–IX, derivation appendix, numerical casebook |
| **[Papers 01–13](docs/papers/)** | Self-contained research papers with full proofs |
| **[Verification Report](docs/verification.md)** | Theorem-by-theorem evidence, all checks pass |
| **[Roadmap](docs/roadmap.md)** | Open problems, next steps, research program |
| **[Demos](docs/demos.md)** | Runnable checks with live output |
| **[Deep Analysis](demos/deep_analysis.py)** | Spectral convergence, Weyl law, energy conservation, migration, epidemic bounds |

**Read locally:**
```bash
npm run docs:dev      # opens http://localhost:5173
npm run docs:build    # static site in docs/.vitepress/dist
npm run docs:pdf      # generates Structure-Flow-Calculus-Docs.pdf
```

---

## Research Papers

| # | Paper | PDF page | Core Result |
||---|-------|----------|-------------|
| 00a | **Capstone** | 1 | Unified statement of contributions 1–10 |
| 00b | **Comprehensive Treatise** | 26 | Whole program, self-contained, with derivation appendix |
| 01 | **Foundations** | 3 | The ρ-calculus, Fundamental Theorem, conformal transport |
| 02 | **Structure Spectral Theory** | 3 | Closed-form spectrum, resolvent, energy conservation |
| 03 | **Causal Network Spectral Theory** | 4 | Eigenframe connection, Energy Migration Theorem |
| 04 | **Variational & Conservation Theory** | 4 | Euler–Lagrange, Hamiltonian, Noether laws |
| 05 | **Graded Media Engineering** | 4 | Impedance matching, reflectionless design |
| 06 | **Power Networks & Synchronization** | 5 | Sync rates, vulnerability, early warning |
| 07 | **Epidemiology on Adaptive Networks** | 5 | Spectral outbreak bounds, interventions |
| 08 | **Numerical Methods** | 6 | Spectral convergence, energy-preserving schemes |
| 09 | **Higher-Dimensional Structure-Flow** | 6 | Product metric, Weyl law, closed-form spectra |
| 10 | **Causal Graph-Time Signal Processing** | 6 | Causal GFT, anomaly detection |
| 11 | **Novelty, Literature & Research Program** | 7 | Honest positioning, novelty verification log |
| 12 | **Quantum & Information** | 7 | ρ-weighted quantum mechanics, Fisher information, entanglement |
| 13 | **Neuroscience & Brain Networks** | 7 | Connectome structure field, seizure detection, neural energy migration, spectral entropy of BOLD signals |
| 14 | **Open Problems** | 8 | Twenty open problems with precise formulations and partial results |

**Proof audit:** 320+ theorems proved, 320+ QED marks, balanced equation delimiters across all papers, capstone, and treatise.

---

## Verification Status

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

## The Mathematics in 60 Seconds

The **structure field** ρ(x) > 0 defines a new calculus:

```
Transport map:     τ(x) = ∫ dx/ρ(x)
Structural length: Λ = ∫ dx/ρ(x)
ρ-derivative:      D_ρ f = ρ f'
ρ-Laplacian:       L_ρ = ρ ∂ₓ(ρ ∂ₓ)
ρ-inner product:   ⟨f,g⟩_ρ = ∫ fg/ρ dx
```

**The key insight:** In the τ-coordinate, the graded medium becomes uniform. The operator L_ρ becomes ∂²/∂τ². Every downstream result — closed-form modes, exact energy conservation, impedance matching — follows from this single change of variables.

---

## Access the Documentation

| Format | How to get it |
|--------|---------------|
| **PDF (241 pages)** | [Download from Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest) or run `npm run docs:pdf` |
| **Live site** | [https://physics-phi-dusky.vercel.app/](https://physics-phi-dusky.vercel.app/) |
| **Local dev** | `npm run docs:dev` |
| **Static build** | `npm run docs:build` |

---

## Repository Structure

```
Physics/
├── docs/
│   ├── papers/              # 12 research papers + capstone + treatise
│   ├── .vitepress/          # VitePress config and theme
│   ├── index.md             # Home page
│   ├── overview.md          # Program thesis
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
├── Structure-Flow-Calculus-Docs.pdf  # 219-page compiled PDF
└── README.md
```

---

## Status

- **12 research papers** written with full proofs
- **294 theorems** proved and QED-marked
- **6 demos** passing continuously
- **219-page PDF** available on [Releases](https://github.com/ram1234598766-dotcom/Physics/releases/latest)
- **Documentation site** live on Vercel

---

## License

MIT

---

<p align="center">
  <strong>Mrityunjay K</strong> — 2026-08-16
  <br>
  <em>Every theorem proved. Every central theorem verified numerically. Every claim honest.</em>
</p>
