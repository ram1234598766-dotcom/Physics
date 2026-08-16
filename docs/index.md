---
layout: home

hero:
  name: Structure-Flow Calculus
  text: A new stream in mathematics and physics
  tagline: One positive function ρ — the structure field — generates a complete calculus, a spectral theory, a variational theory, and a network theory. Every theorem is proved; every central theorem is verified numerically.
  image:
    src: /sf-mark.svg
    alt: Structure-Flow mark
  actions:
    - theme: brand
      text: Read the program statement
      link: /overview
    - theme: alt
      text: Comprehensive treatise
      link: /papers/00-treatise
    - theme: alt
      text: Download the PDF
      link: https://github.com/ram1234598766-dotcom/Physics/releases/latest

features:
  - title: Graded media
    details: Closed-form modes for wave propagation in impedance-matched graded media, and reflectionless design (Papers 02, 05).
  - title: Power networks
    details: Mode-energy migration as a grid is stressed — a proven redistribution law that exposes the vulnerable modes (Papers 03, 06).
  - title: Adaptive contact networks
    details: Provable decay bounds for diffusion and epidemic dynamics on time-varying networks (Papers 03, 07).
  - title: Verified end to end
    details: 259 proofs, 259 QED marks, and every central theorem checked numerically by a runnable demo.

---
# Introduction

The **Structure-Flow Calculus (SFC)** is a new mathematical framework that builds a complete calculus relative to a dynamical **structure field** — a single positive function ρ(x) that treats the differential structure of space as a variable rather than a given. From this single object ρ, three complete theories emerge: a spectral theory (eigenvalues and eigenfunctions relative to ρ), a variational theory (Euler–Lagrange equations and Noether‑type conservation laws relative to ρ), and a network theory (graph Laplacians with structure‑dependent edge weights and a skew‑symmetric connection form that enables energy migration while conserving total modal energy).

The framework does **not** claim new fundamental physics; the underlying phenomena (graded‑media acoustics, swing equations, SIS epidemics) are classical. The contribution is the unified object ρ and the theorems built around it, all of which are numerically verified through runnable demos and the deep analysis suite (`demos/deep_analysis.py`). The novelty, its evidence, and its limits are stated plainly in Paper 11.

Every theorem is proved in the paper in which it appears. Every central theorem is verified numerically. The complete program consists of 12 research papers (00–11), a comprehensive treatise (~30 pages, Parts I–IX), a capstone statement of contributions 1–10, a verification report (259 proofs, 259 QED marks), and a roadmap of open problems and next steps.

---
## Research papers

- [00 — Capstone](/papers/00-capstone): unified statement of the program
- [00 — Comprehensive Treatise](/papers/00-treatise): ~30 pages, the whole program self-contained, with derivation appendix and numerical casebook
- [01 — Foundations](/papers/01-foundations): $\rho$-calculus, Fundamental Theorem, conformal transport
- [02 — Structure Spectral Theory](/papers/02-structure-spectral-theory): closed-form graded-media modes, energy conservation
- [03 — Causal Network Spectral Theory](/papers/03-causal-network-spectral-theory): eigenframe connection, Energy Migration Theorem
- [04 — Variational & Conservation Theory](/papers/04-variational-conservation): structure-flow Euler–Lagrange, Noether-type laws
- [05 — Graded Media Engineering](/papers/05-graded-media-engineering): matched media, reflectionless design
- [06 — Power Networks & Synchronization](/papers/06-power-networks-synchronization): rates, vulnerability, early warning
- [07 — Epidemiology on Adaptive Networks](/papers/07-epidemiology-adaptive-networks): spectral outbreak bounds, interventions
- [08 — Numerical Methods](/papers/08-numerical-methods): spectral convergence, energy-preserving schemes
- [09 — Higher-Dimensional Structure-Flow](/papers/09-higher-dimensional-structure-flow): metrics, Weyl law, product domains
- [10 — Causal Graph-Time Signal Processing](/papers/10-causal-graph-time-signal-processing): causal GFT, anomaly detection
- [11 — Novelty, Literature & Research Program](/papers/11-novelty-and-literature)

Every theorem is proved in the paper in which it appears. Every central theorem is verified numerically by a runnable demo (see the [Verification Report](/verification)).

## Demos

Four runnable scripts turn the central theorems into numbers and double as regression tests. See the [demos page](/demos).