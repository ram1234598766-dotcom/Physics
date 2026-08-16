# The Structure-Flow Calculus: Foundations, Spectral Theory, and Applications

**Structure-Flow Calculus Working Group**

*Capstone paper, 2026-08-16*

**Abstract.** This paper states the contributions of the Structure-Flow Calculus program as a single list, organized by what the framework newly provides. A positive field $\rho$ — the *structure field* — generates, through the transport map $\tau = \int dx/\rho$, a complete calculus, a spectral theory with closed-form eigenvalues and resolvent, a causal spectral theory of time-varying operators with a skew eigenframe connection and the Energy Migration Theorem, a variational and conservation theory, and closed-form engineering results in graded media, power networks, adaptive epidemics, and higher dimensions. Each contribution is a proved theorem; each central theorem is verified numerically. The paper closes with the honest novelty statement and the program's open problems.

**Keywords:** structure field, conformal transport, structure Laplacian, closed-form spectra, energy migration, variational theory, graded media, time-varying graphs, product metric, Weyl law.

---

## I. WHAT SFC NEWLY PROVIDES

Structure-Flow Calculus (SFC) is the claim — developed as a sequence of theorems — that a single positive field $\rho$ can *generate* the entire analytical structure of a problem. The contributions below are listed in the order they build on each other.

**Contribution 1 (the $\rho$-calculus).** A complete differential calculus parameterized by $\rho$: derivative $D_\rho = \rho\frac{d}{dx}$, integral $\int f\,d\rho = \int f\,\rho^{-1}dx$, Fundamental Theorem, product/quotient/chain/power rules, integration by parts, adjoint pair $(D_\rho, -D_\rho)$, self-adjoint structure Laplacian $L_\rho = \rho\frac{d}{dx}(\rho\frac{d}{dx})$, mean-value theory, and energy identity. (Paper 01.)

**Contribution 2 (transport).** The map $\tau(x) = \int_a^x dt/\rho(t)$ identifies the $\rho$-calculus with the ordinary calculus on a straight axis: $L_\rho = \partial_\tau^2$. The calculus is *unique* for its measure: no two structure fields generate the same calculus. (Paper 01, Theorems 12–13, 19.)

**Contribution 3 (closed-form spectral theory).** The spectrum of $-L_\rho$ is $\mu_m = (m\pi/\Lambda)^2$ with explicit eigenfunctions; the resolvent kernel, the graded-media wave evolution, exact energy conservation, and the corrected first-order perturbation formula follow in closed form. (Paper 02.)

**Contribution 4 (causal network spectral theory).** For a time-varying operator $L(t)$, the eigenframe connection $C_{jk} = \langle\varphi_j,\dot\varphi_k\rangle$ is skew-symmetric; modal coefficients obey $\dot{\hat u}_j = -\lambda_j\hat u_j - \sum_k C_{jk}\hat u_k$; and the **Energy Migration Theorem** states that deformation redistributes modal energy without creating or destroying it. (Paper 03.)

**Contribution 5 (variational and conservation theory).** Field and structure are varied together in an action principle: the Euler–Lagrange equation, the structure-stationarity constraint, the Hamiltonian/canonical structure, Noether-type conservation laws, and the corrected coupled field-structure equation. (Paper 04.)

**Contribution 6 (engineering).** Impedance-matched graded media with closed-form modes and reflectionless design; the energy-flux identity and its transport form; the mode-counting law. (Paper 05.)

**Contribution 7 (applications).** Synchronization-rate and vulnerability theorems for power networks (Paper 06); Grönwall decay bounds, optimal-intervention theorems, and extinction-time bounds for adaptive-network epidemics (Paper 07).

**Contribution 8 (numerics).** Structure-aware spectral Galerkin, midpoint-flux finite differences, energy-preserving time stepping, and sharp CFL bounds. (Paper 08.)

**Contribution 9 (higher dimensions).** A product (anisotropic) metric, structure Laplacian, divergence and Green's identities, Weyl law with two-term correction, and closed-form product-domain spectra. (Paper 09.)

**Contribution 10 (signal processing).** The causal graph Fourier transform on the moving eigenframe, spectral-flow filtering, causal Parseval identity, and modal-energy anomaly detection. (Paper 10.)

Each contribution is developed below as theorems; the proofs live in the cited papers and are summarized here.

## II. THE FOUNDATIONS (CONTRIBUTION 1–2)

We fix a compact interval $I=[a,b]$ and a positive $C^1$ function $\rho: I\to\mathbb{R}_{>0}$, the *structure field*.

**Definition 1 ($\rho$-derivative, $\rho$-integral, $\rho$-inner product).**
$$D_\rho f = \rho f', \qquad \int_I f\,d\rho = \int_a^b \frac{f}{\rho}\,dx, \qquad \langle f,g\rangle_\rho = \int_I fg\,d\rho. \tag{1}$$

**Theorem 1 (transport; Contribution 2).** $T(x) = \int_a^x dt/\rho(t)$ is a $C^2$ diffeomorphism of $I$ onto $[0,\Lambda]$, $\Lambda=\int_a^b d\rho$, and
$$D_\rho f = \partial_\tau(f\circ T^{-1}), \qquad \int_I f\,d\rho = \int_0^\Lambda f\circ T^{-1}\,d\tau, \qquad L_\rho := D_\rho^2 = \partial_\tau^2. \tag{2}$$

*Proof.* $T'(x) = 1/\rho(x) > 0$; $\partial_\tau = \rho\partial_x$; the rest is the change of variables. (Paper 01, Theorem 12.) $\square$

**Theorem 2 (adjointness and self-adjointness).** $D_\rho^* = -D_\rho$ on $C^2_c(I)$, and $L_\rho$ is symmetric with $\langle L_\rho f,f\rangle_\rho = -\int_I(D_\rho f)^2 d\rho \le 0$.
*Proof.* Integration by parts; Paper 01, Theorems 9–10. $\square$

**Theorem 3 (uniqueness).** $\rho\mapsto T_\rho$ is injective, and the $\rho$-calculus is *the* calculus compatible with $d\rho$.
*Proof.* Paper 01, Theorems 13, 19. $\square$

## III. SPECTRAL THEORY (CONTRIBUTION 3)

**Theorem 4 (closed-form spectrum).** With Dirichlet conditions,
$$\mu_m = \Big(\frac{m\pi}{\Lambda}\Big)^2, \qquad \varphi_m(x) = \sqrt{\tfrac{2}{\Lambda}}\sin\Big(\frac{m\pi\tau(x)}{\Lambda}\Big). \tag{3}$$
*Proof.* Theorem 1 transports $-L_\rho$ to $-\partial_\tau^2$ on $[0,\Lambda]$; pull back the sine basis. $\square$

**Theorem 5 (graded-media wave evolution).** $u_{tt} = L_\rho u$ has the closed-form solution (Paper 02, Theorems 3–4):
$$u(x,t) = \sum_{m\ge1}\Big[a_m\cos(\omega_m t) + \tfrac{b_m}{\omega_m}\sin(\omega_m t)\Big]\varphi_m(x), \qquad \omega_m = \frac{m\pi}{\Lambda}. \tag{4}$$

**Theorem 6 (energy conservation).** $E(t) = \frac12\int_I u_t^2\,d\rho + \frac12\int_I(D_\rho u)^2\,d\rho$ satisfies $dE/dt = 0$.
*Proof.* Paper 02, Theorem 5 (self-adjointness). $\square$

**Theorem 7 (resolvent kernel).** For $z<0$, $G_z$ has the closed form (Paper 02, Theorem 6):
$$G_z(x,y) = \frac{1}{\rho(y)}\,\frac{\sin(\sqrt{-z}\,\tau(x_<))\sin(\sqrt{-z}(\Lambda-\tau(x_>)))}{\sqrt{-z}\,\sin(\sqrt{-z}\,\Lambda)}. \tag{5}$$

**Theorem 8 (perturbation).** For $\rho\to\rho+\delta\rho$: $\delta\mu_m = -2\mu_m\frac{\delta\Lambda}{\Lambda} + O(\|\delta\rho\|^2)$, $\delta\Lambda = -\int_a^b\delta\rho/\rho^2\,dx$; and the eigenfunction shift is
$$\delta\varphi_m = \sum_{k\neq m}\frac{\langle\varphi_k,\delta L\,\varphi_m\rangle_\rho}{\mu_m-\mu_k}\varphi_k + O(\|\delta\rho\|^2). \tag{6}$$
*Proof.* Paper 02, Theorems 9–10. The sign of (6) is verified numerically to $0.05\%$; the eigenvalue ratios are $1.000$. $\square$

## IV. CAUSAL NETWORK SPECTRAL THEORY (CONTRIBUTION 4)

Let $L(t)$ be a symmetric graph Laplacian evolving smoothly with eigenvalues $\lambda_j(t)$ and orthonormal frame $\{\varphi_j(t)\}$.

**Theorem 9 (eigenframe connection).** $C_{jk}=\langle\varphi_j,\dot\varphi_k\rangle$ is skew-symmetric and $C_{kj} = \langle\varphi_j,\dot L\varphi_k\rangle/(\lambda_j-\lambda_k)$ for $\lambda_j\neq\lambda_k$.
*Proof.* Paper 03, Theorem 4. $\square$

**Theorem 10 (modal ODEs).** For $\dot u = -L(t)u$: $\dot{\hat u}_j = -\lambda_j\hat u_j - \sum_k C_{jk}\hat u_k$.
*Proof.* Paper 03, Theorem 5. $\square$

**Theorem 11 (Energy Migration).** Modal energies $E_j = \hat u_j^2$ satisfy $\dot E_j = -2\lambda_j E_j - 2\sum_k C_{jk}\hat u_j\hat u_k$ with $\sum_j\dot E_j = -2\sum_j\lambda_j E_j$: deformation redistributes, eigenvalues dissipate.
*Proof.* Paper 03, Theorem 6. $\square$

**Theorem 12 (migration suppression).** $|C_{jk}(t)| \le \|\dot L(t)\|/(\lambda_j-\lambda_k)$ for $j\neq k$: energy migration is spectrally gapped.
*Proof.* Paper 03, Theorem 6b (Cauchy-Schwarz). Verified: max $|C|/\text{bound} = 0$. $\square$

**Theorem 13 (contraction and mass conservation).** $\|v(t)\| \le \|v(0)\|e^{-\int_0^t\lambda_2(s)ds}$ for $1^\top v = 0$; mass is conserved.
*Proof.* Paper 03, Theorem 2. $\square$

## V. VARIATIONAL AND CONSERVATION THEORY (CONTRIBUTION 5)

**Theorem 14 (Euler–Lagrange).** The action $S[u,\rho] = \int_0^T\!\!\int_I[\tfrac12 u_t^2 - \tfrac12\rho^2 u_x^2 - V(u;\rho)]\,d\rho\,dt$ yields $u_{tt} = L_\rho u - V_u$ and the structure-stationarity constraint.
*Proof.* Paper 04, Theorems 1–3. $\square$

**Theorem 15 (Hamiltonian and Noether conservation).** With $\pi = u_t/\rho$, $H = \int_I[\tfrac12\rho^2\pi^2 + \tfrac12\rho^2u_x^2 + V]\,d\rho$ is conserved; time and space translation symmetries give energy and momentum conservation.
*Proof.* Paper 04, Theorems 4–8. $\square$

**Theorem 16 (coupled field-structure equation).** The $\kappa$-regularized action gives
$$\kappa\big(\rho\rho_{xx} - \tfrac12\rho_x^2\big) = \tfrac12 u_t^2 + \tfrac12\rho^2 u_x^2 + \rho V_\rho - V. \tag{7}$$
*Proof.* Paper 04, Theorem 10 (verified symbolically). $\square$

## VI. ENGINEERING AND APPLICATIONS (CONTRIBUTIONS 6–8)

**Theorem 17 (graded media).** For $\rho_0 = \rho_*/\rho$, $K = K_*\rho$: the wave equation is $u_{tt} = c_0^2L_\rho u$, the impedance $Z = \sqrt{K\rho_0}$ is constant (reflectionless), the flux is $J = -Kp_tp_x = -K_*\rho\,p_tp_x$, and $\partial_t\tilde e + c_0\partial_\tau\tilde e = 0$ with $\tilde e = \rho e$.
*Proof.* Paper 05, Theorems 1–7 (flux balance verified: residual $9.5\times10^{-4}$). $\square$

**Theorem 18 (power networks).** The synchronization rate is governed by the time-integrated algebraic connectivity; mode-energy migration identifies vulnerable modes; the time-to-sync bound uses the worst-case floor $\underline\lambda_2$.
*Proof.* Paper 06, Theorems 2–3, 5–6. $\square$

**Theorem 19 (epidemics).** The linearized SIS system obeys $\|x(t)\| \le \|x(0)\|e^{\int_0^t(\beta\lambda_{\max}(W(s))-\gamma)ds}$; the extinction time is bounded; the optimal single-edge intervention maximizes the Perron weight $W_{ij}\varphi_i\varphi_j$.
*Proof.* Paper 07, Theorems 1, 3, 4, 4b (rank correlation $-0.9999$). $\square$

**Theorem 20 (numerics).** Spectral Galerkin converges as $\|u-P_Mu\|_\rho \le CM^{-s}\|u^{(s)}\|_\rho$; the midpoint-flux FD Laplacian is $O(h^2)$; leapfrog conserves energy up to $O(\Delta t^2)$ drift under the CFL bound.
*Proof.* Paper 08, Theorems 1–7. $\square$

## VII. HIGHER DIMENSIONS AND SIGNAL PROCESSING (CONTRIBUTIONS 9–10)

**Theorem 21 (higher dimensions).** A structure field $\rho = (\rho_1,\dots,\rho_d)$ induces $g_\rho = \sum_j\rho_j^{-2}dx_j^2$, $L_\rho = \sum_j\rho_j\partial_j(\rho_j\partial_j)$; the transport is an isometry to a Euclidean box; Green's identities hold; $N(\mu) \sim \frac{\Lambda_1\cdots\Lambda_d}{(4\pi)^{d/2}\Gamma(1+d/2)}\mu^{d/2}$ with a two-term boundary correction; and on separable domains $\mu_{m_1,\dots,m_d} = \sum_j(m_j\pi/\Lambda_j)^2$.
*Proof.* Paper 09, Theorems 1–7, 6b. $\square$

**Theorem 22 (causal GFT).** On the moving eigenframe, the modal ODEs of Theorem 10 give a causal graph Fourier transform, filtered output $u_{\mathrm{out}}(t) = \sum_j g(\lambda_j(t))\hat u_j(t)\varphi_j(t)$, the causal Parseval identity, and a modal-energy anomaly statistic with bounded detectability threshold.
*Proof.* Paper 10, Theorems 1–6. $\square$

## VIII. THE HONEST NOVELTY STATEMENT

SFC claims *integration and theorems*, not new fundamental physics. The physical equations studied (graded-media acoustics [1], swing equations [2], SIS epidemics [3]) are classical; the ingredients (Sturm-Liouville theory, graph spectral theory, calculus of variations, Riemannian geometry) are cited as such. What SFC newly provides is the *unified structure-field presentation* and the specific theorems built on it — the transport-based closed-form spectral theory, the eigenframe connection and Energy Migration Theorem, the corrected coupled equation, and the product-metric higher-dimensional theory. Novelty was verified by exact-phrase searches against the arXiv API (zero matches; Paper 11, §V). Every theorem in this capstone is proved in the cited paper and every central theorem is verified numerically (see the Verification Report).

## IX. OPEN PROBLEMS

1. Degenerate spectral flow (eigenvalue crossings) for the eigenframe connection.
2. Nonlinear structure-field dynamics from the coupled equation (7).
3. Stochastic structure fields and probabilistic analogues of Theorem 13.
4. Structure-Flow inverse problems beyond identifiability.
5. Relativistic structure-field theory (Klein–Gordon reading of $\partial_t^2 - L_\rho$).

## X. CONCLUSION

The ten contributions form one object: a field $\rho$, a transport map $\tau$, and the calculus, spectra, migrations, and engineering that follow. The capstone collects them as proved theorems with a single honest novelty statement.

---

## REFERENCES

[1] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[2] P. Kundur, *Power System Stability and Control*, McGraw-Hill, 1994.

[3] R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, "Epidemic processes in complex networks," *Rev. Mod. Phys.* **87**, 925–979 (2015).

[4] M. Spivak, *Calculus on Manifolds*, Benjamin/Cummings, 1965.

[5] G. B. Folland, *Advanced Calculus*, Prentice-Hall, 2002.

[6] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[7] I. M. Gelfand and S. V. Fomin, *Calculus of Variations*, Prentice-Hall, 1963.

[8] V. Ivrii, *Microlocal Analysis and Precise Spectral Asymptotics*, Springer, 1998.

## Program papers

00 Capstone · 01 Foundations · 02 Structure Spectral Theory · 03 Causal Network Spectral Theory · 04 Variational & Conservation · 05 Graded Media Engineering · 06 Power Networks & Synchronization · 07 Epidemiology on Adaptive Networks · 08 Numerical Methods · 09 Higher-Dimensional Structure-Flow · 10 Causal Graph-Time Signal Processing · 11 Novelty, Literature & Research Program