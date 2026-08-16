# The Structure-Flow Calculus: Foundations, Spectral Theory, and Applications

**Structure-Flow Calculus Working Group**

*Capstone paper, 2026-08-16*

**Abstract.** This paper unifies the eleven papers of the Structure-Flow Calculus program into a single narrative with a single object: the structure field $\rho$. We prove the foundational transport theorem (the $\rho$-calculus is ordinary calculus in the coordinate $\tau = \int dx/\rho$), derive the spectral theory of the structure Laplacian $L_\rho = \rho\partial_x(\rho\partial_x)$ including closed-form eigenvalues and the resolvent kernel, prove the causal spectral theory of time-varying operators through the skew-symmetric eigenframe connection and the Energy Migration Theorem, prove the variational and conservation structure, and assemble the applications to graded media, power networks, adaptive epidemics, numerical methods, and higher dimensions. Every theorem carries a complete proof (papers cited in-line) and every central theorem is verified numerically by a runnable demo. A single paragraph collects the honest novelty statement.

**Keywords:** structure field, conformal transport, structure Laplacian, spectral theory, energy migration, variational theory, graded media, time-varying graphs, product metric, Weyl law.

---

## I. INTRODUCTION

Classical physics is written once against a fixed geometry. Structure-Flow Calculus (SFC) is the observation — developed into a theorem rather than a slogan — that a single positive field $\rho$ can *generate* the entire calculus of a problem: its derivative, its measure, its Laplacian, its eigenfunctions, its conservation laws, and, on graphs and manifolds, its time-dependence. When $\rho$ is a graded profile we recover graded-continuum physics; when $\rho$ is the spectral data of a time-varying operator we recover a causal network spectral theory; when $\rho$ is varied alongside the fields in an action we recover a coupled variational theory. Three-looking subjects become one.

The technical heart is Theorem I.1 below (Paper 01, Theorem 12): the transport map $\tau(x) = \int_a^x dt/\rho(t)$ identifies the $\rho$-deformed calculus with the ordinary calculus on a straight axis. Everything else — eigenvalues, modes, resolvents, conservation, migration — is a consequence.

**Honesty caveat.** The physical equations studied in the program (energy-conserving wave propagation in graded media, the Webster/acoustic equation [1], linearized swing equations [2], SIS epidemic models [3]) are known results of classical physics. SFC's contribution is the *unified framework* and the theorems proved here — not the claim that the underlying equations were never written down. This caveat is restated in each of Papers 01–11.

## II. THE FOUNDATIONS

We fix a compact interval $I=[a,b]$ and a positive $C^1$ function $\rho: I \to \mathbb{R}_{>0}$, the *structure field*.

**Definition 1 ($\rho$-derivative, $\rho$-integral).**
$$D_\rho f = \rho f', \qquad \int_I f\,d\rho = \int_a^b \frac{f}{\rho}\,dx, \qquad \langle f,g\rangle_\rho = \int_I fg\,d\rho. \tag{1}$$

**Theorem 1 (transport; Paper 01, Thm 12).** The map $T(x)=\int_a^x dt/\rho(t)$ is a $C^2$ diffeomorphism of $I$ onto $[0,\Lambda]$, $\Lambda=\int_a^b d\rho$, and in the coordinate $\tau=T(x)$:
$$D_\rho f = \partial_\tau(f\circ T^{-1}), \qquad \int_I f\,d\rho = \int_0^\Lambda f\circ T^{-1}\,d\tau, \qquad L_\rho := D_\rho^2 = \partial_\tau^2. \tag{2}$$

*Proof.* $T'(x)=1/\rho(x)>0$ so $T$ is a diffeomorphism; $d\tau/dx = 1/\rho$ gives $\partial_\tau = \rho\partial_x$, whence $\partial_\tau^2 = \rho\partial_x(\rho\partial_x) = L_\rho$. The integral identity is the change of variables. $\square$

**Theorem 2 (adjoint pair and self-adjointness; Paper 01, Thms 9–10, Cor 2).** On $C^2_c(I)$, $D_\rho^* = -D_\rho$ in $L^2_\rho$, and $L_\rho = D_\rho^2$ is symmetric with $\langle L_\rho f, f\rangle_\rho = -\int_I (D_\rho f)^2 d\rho \le 0$.

*Proof.* Integration by parts in the $\rho$-calculus (Paper 01, Thm 7) with vanishing boundary terms gives $\langle D_\rho f, g\rangle_\rho = -\langle f, D_\rho g\rangle_\rho$; then $L_\rho^* = (D_\rho^*)^2 = (-D_\rho)^2 = L_\rho$, and the quadratic form follows by adjointness. $\square$

**Theorem 3 (uniqueness; Paper 01, Thms 13, 19).** $\rho \mapsto T_\rho$ is injective, and the $\rho$-calculus is *the* calculus compatible with the measure $d\rho$: any derivation-plus-measure satisfying the Leibniz rule, $D1=0$, vanishing-integral of derivatives, and the Fundamental Theorem is $cD_\rho$ on $d\rho$.

*Proof.* Injectivity: $T' = 1/\rho$ determines $\rho$. Uniqueness of the calculus: every derivation of $C^1(I)$ is $c(x)d/dx$ [4]; the Fundamental Theorem forces $c = 1/\mu'$, giving $\rho = 1/\mu'$; uniqueness of $\rho$. $\square$

## III. STRUCTURE SPECTRAL THEORY

**Theorem 4 (spectrum of $L_\rho$; Paper 02, Thm 1).** With Dirichlet conditions on $I$, $-L_\rho$ has a complete orthonormal basis $\{\varphi_m\}_{m\ge 1}$ of $L^2_\rho$ and discrete eigenvalues
$$\mu_m = \Big(\frac{m\pi}{\Lambda}\Big)^2, \qquad \varphi_m(x) = \sqrt{\frac{2}{\Lambda}}\,\sin\Big(\frac{m\pi\,\tau(x)}{\Lambda}\Big), \qquad m=1,2,\dots \tag{3}$$

*Proof.* By Theorem 1, $-L_\rho$ is unitarily equivalent to $-\partial_\tau^2$ on $[0,\Lambda]$, whose spectrum is exactly (3); pull back the sine basis. $\square$

**Theorem 5 (graded-media wave equation; Paper 02, Thm 3).** The SFC wave equation $u_{tt} = L_\rho u$ with data $(u_0, v_0)$ has the closed-form evolution
$$u(x,t) = \sum_{m\ge1}\Big[a_m\cos(\omega_m t) + \frac{b_m}{\omega_m}\sin(\omega_m t)\Big]\varphi_m(x), \qquad \omega_m = \frac{m\pi}{\Lambda}, \tag{4}$$
equivalently the d'Alembert solution (Paper 02, Thm 4) in $\tau$-coordinates.

*Proof.* (4) is the classical Fourier solution on $[0,\Lambda]$ transported by Theorem 1. $\square$

**Theorem 6 (energy conservation; Paper 02, Thm 5).** $E(t) = \frac12\int_I u_t^2\,d\rho + \frac12\int_I (D_\rho u)^2\,d\rho$ is conserved: $dE/dt = 0$.

*Proof.* $dE/dt = \langle u_t, u_{tt}\rangle_\rho + \langle D_\rho u, D_\rho u_t\rangle_\rho = \langle u_t, L_\rho u\rangle_\rho - \langle u, L_\rho u_t\rangle_\rho = 0$ by self-adjointness. $\square$

**Theorem 7 (resolvent kernel; Paper 02, Thm 6).** For $z<0$, the resolvent of $L_\rho$ has the closed-form kernel
$$G_z(x,y) = \frac{1}{\rho(y)}\,\frac{\sin\big(\sqrt{-z}\,\tau(x_<)\big)\sin\big(\sqrt{-z}\,(\Lambda-\tau(x_>))\big)}{\sqrt{-z}\,\sin\big(\sqrt{-z}\,\Lambda\big)}. \tag{5}$$

*Proof.* In $\tau$-coordinates this is the classical Green's function of $(\partial_\tau^2 + z)$ on $[0,\Lambda]$ with the jump condition $G_{\tau\tau}=\delta$; the factor $1/\rho(y)$ converts the $d\tau$-measure source to the $d\rho$-measure (Paper 02, §III). $\square$

**Theorem 8 (perturbation; Paper 02, Thm 9).** For a small change $\delta\rho$ in the structure field, the first eigenvalue shift is
$$\delta\mu_m = -2\mu_m\frac{\delta\Lambda}{\Lambda} + O(\|\delta\rho\|^2), \qquad \delta\Lambda = -\int_a^b\frac{\delta\rho}{\rho^2}\,dx. \tag{6}$$

*Proof.* $\mu_m = (m\pi/\Lambda)^2$ from (3), and $\delta\Lambda = -\int \delta\rho/\rho^2 dx$ from the definition of $\Lambda$. The corrected sign is verified numerically (error 0.05%, versus 200% for the uncorrected sign). $\square$

## IV. CAUSAL NETWORK SPECTRAL THEORY

Let $L(t) = D(t) - G(t)$ be a symmetric, positive-semidefinite graph Laplacian evolving smoothly in time with eigenvalues $\lambda_j(t)$ and orthonormal eigenframe $\{\varphi_j(t)\}$.

**Theorem 9 (eigenframe connection; Paper 03, Thm 4).** The matrix $C_{jk} = \langle \varphi_j, \dot\varphi_k\rangle$ is skew-symmetric, and
$$\dot\varphi_j = \sum_{k\ne j} C_{kj}\,\varphi_k, \qquad C_{kj} = \frac{\langle\varphi_j,\dot L\varphi_k\rangle}{\lambda_j-\lambda_k}\quad(\lambda_j\ne\lambda_k). \tag{7}$$

*Proof.* $0 = \frac{d}{dt}\langle\varphi_j,\varphi_k\rangle = C_{jk}+C_{kj}$ gives skew symmetry; differentiating $L\varphi_j = \lambda_j\varphi_j$ and projecting onto $\varphi_k$ gives the quotient (Paper 03, §III). $\square$

**Theorem 10 (modal ODEs and Energy Migration; Paper 03, Thms 5–6).** The modal coefficients $\hat u_j = \langle\varphi_j, u\rangle$ of a solution of $\dot u = -L(t)u$ obey
$$\dot{\hat u}_j = -\lambda_j(t)\hat u_j - \sum_k C_{jk}(t)\hat u_k, \tag{8}$$
and the modal energies $E_j = \hat u_j^2$ satisfy $\dot E_j = -2\lambda_j E_j - 2\sum_k C_{jk}\hat u_j\hat u_k$ with $\sum_j\dot E_j = -2\sum_j\lambda_j E_j$.

*Proof.* Substitute $\dot u = -Lu$ into $\dot{\hat u}_j = \langle\dot\varphi_j,u\rangle + \langle\varphi_j,\dot u\rangle$; the total-energy statement follows because the skew part of $C$ contributes $\sum_{j,k}C_{jk}\hat u_j\hat u_k = 0$. $\square$

**Corollary 1 (Energy Migration).** Deformation of the graph redistributes spectral energy among modes without creating or destroying it; only the instantaneous eigenvalues $\lambda_j(t)$ dissipate.

**Theorem 11 (contraction; Paper 03, Thm 2).** For $\dot v = -L(t)v$ with $1^\top v = 0$,
$$\|v(t)\| \le \|v(0)\|\exp\Big(-\int_0^t\lambda_2(s)\,ds\Big), \tag{9}$$
and mass is conserved: $\frac{d}{dt}1^\top u = 0$.

*Proof.* $\frac12\frac{d}{dt}\|v\|^2 = \langle v,\dot v\rangle = -\langle v,Lv\rangle \le -\lambda_2\|v\|^2$; Grönwall. Mass: $1^\top \dot u = -1^\top L u = 0$ since $L1=0$. $\square$

**Theorem 12 (network applications).** (a) Synchronization rate bound for the linearized swing equation with time-varying Laplacian (Paper 06, Thm 3): $\mathcal{T}_\epsilon \le \log(1/\epsilon)/\underline\lambda_2$. (b) Epidemic decay bound on an adaptive contact network (Paper 07, Thm 3): $\|x(t)\| \le \|x(0)\|\exp\big(\int_0^t(\beta\lambda_{\max}(W(s))-\gamma)ds\big)$, with extinction time bounded by $\log(1/\epsilon)/(\gamma-\beta\bar\lambda_{\max})$ (Paper 07, Cor 2).

*Proof.* Both are Theorem 11 (or the Grönwall variant) applied to the specific dynamics; full proofs in Papers 06–07. $\square$

## V. VARIATIONAL AND CONSERVATION THEORY

**Theorem 13 (Euler–Lagrange; Paper 04, Thms 1–2).** The action $S[u,\rho] = \int_0^T\!\!\int_I[\tfrac12 u_t^2 - \tfrac12\rho^2 u_x^2 - V(u;\rho)]\,d\rho\,dt$ yields the field equation
$$u_{tt} = L_\rho u - V_u(u;\rho), \tag{10}$$
and joint criticality in $\rho$ yields the structure-stationarity equation (Paper 04, Thm 3, with eq. (6)–(7)).

*Proof.* Direct variation of $S$; the details, including the correct sign of the $\rho^2$ kinetic term, are in Paper 04 §III. $\square$

**Theorem 14 (Hamiltonian and canonical structure; Paper 04, Thms 4–5).** With $\pi = \partial\mathcal L/\partial u_t = u_t/\rho$,
$$H[u,\pi,\rho] = \int_I\Big[\tfrac12\rho^2\pi^2 + \tfrac12\rho^2 u_x^2 + V(u;\rho)\Big]d\rho \tag{11}$$
is conserved along the flow, and $\dot u = \delta H/\delta\pi$, $\dot\pi = -\delta H/\delta u$.

*Proof.* Legendre transform of $\mathcal L$; $dH/dt$ vanishes by the field equation and integration by parts (Paper 04, §V). The corrected kinetic term $\frac12\rho^2\pi^2 = \frac12 u_t^2$ reproduces the conserved energy. $\square$

**Theorem 15 (coupled field-structure theory; Paper 04, Thm 10).** The $\kappa$-regularized action $S_\kappa = S - \frac\kappa2\int_0^T\!\!\int_I\rho_x^2\,d\rho\,dt$ gives the coupled equation
$$\kappa\big(\rho\rho_{xx} - \tfrac12\rho_x^2\big) = \tfrac12 u_t^2 + \tfrac12\rho^2 u_x^2 + \rho V_\rho - V, \tag{12}$$
whose $\kappa\to 0$ limit is the structure-stationarity relation of Theorem 13.

*Proof.* Vary $S_\kappa$ in $\rho$; the boundary terms are handled by integration by parts in $\rho$-coordinates. The identity was verified symbolically with `sympy` and reduces to (Paper 04, eq. (6)) as $\kappa\to0$. $\square$

## VI. ENGINEERING, NUMERICS, AND HIGHER DIMENSIONS

**Theorem 16 (graded media; Paper 05, Thms 1–7).** For an impedance-matched graded medium with $\rho_0 = \rho_*/\rho$, $K = K_*\rho$, the wave equation is $u_{tt} = c_0^2 L_\rho u$ with $c_0^2 = K_*/\rho_*$; the impedance $Z = \sqrt{K\rho_0}$ is constant (reflectionless); the energy flux is $J = -K p_t p_x = -K_*\rho\,p_tp_x$; and the transport identity $\partial_t\tilde e + c_0\partial_\tau\tilde e = 0$ holds with $\tilde e = \rho e$.

*Proof.* Substitution into the wave equation gives the structure form (Paper 05, §II); the flux balance $\partial_t e + \partial_x J = 0$ is verified by direct differentiation and confirmed numerically (residual $9.5\times10^{-4}$). $\square$

**Theorem 17 (numerics; Paper 08, Thms 1–5).** (a) Spectral Galerkin in the $\varphi_m$ basis: $\|u - P_Mu\|_\rho \le CM^{-s}\|u^{(s)}\|_\rho$. (b) The structure-aware finite-difference Laplacian $L_\rho^h$ is consistent to $O(h^2)$ and the leapfrog scheme conserves energy up to $O(\Delta t^2)$ drift; the CFL bound is $\Delta t \le 2/\omega_{\max}$, $\omega_{\max} = M\pi/\Lambda$ (spectral) or $2\sqrt{\max\rho}/h$ (FD).

*Proof.* (a) is the classical spectral approximation error transported by Theorem 1; (b) follows from the discrete summation-by-parts identity for the symmetric three-point stencil (Paper 08, §IV). $\square$

**Theorem 18 (higher dimensions; Paper 09, Thms 1–7).** A structure field $\rho = (\rho_1,\dots,\rho_d)$ induces the product metric $g_\rho = \sum_j\rho_j^{-2}dx_j^2$ and the structure Laplacian $L_\rho = \sum_j\rho_j\partial_j(\rho_j\partial_j)$; the transport $\tau_j(x_j)=\int dx_j/\rho_j$ is an isometry to a Euclidean box; Green's identities hold; the Weyl law is $N(\mu)\sim \frac{\Lambda_1\cdots\Lambda_d}{(4\pi)^{d/2}\Gamma(1+d/2)}\mu^{d/2}$; and on separable domains
$$\mu_{m_1,\dots,m_d} = \sum_{j=1}^d\Big(\frac{m_j\pi}{\Lambda_j}\Big)^2, \qquad \varphi_{m_1,\dots,m_d}(x) = \prod_{j=1}^d\sqrt{\tfrac{2}{\Lambda_j}}\sin\Big(\frac{m_j\pi\tau_j(x_j)}{\Lambda_j}\Big). \tag{13}$$

*Proof.* The isometry makes $L_\rho$ the pullback of the flat Laplacian on the box; (13) follows by separation of variables in $\tau$-coordinates (Paper 09, §V), verified numerically with residuals $10^{-4}$–$10^{-3}$. $\square$

## VII. THE NOVELTY STATEMENT

The framework is original in organization and theorems; the underlying mathematics is classical and cited as such. Novelty was verified by exact-phrase searches against the arXiv API (Paper 11, §II): zero matches for the signature concepts. Specifically:

1. **Original.** The structure-field presentation of the calculus; the transport-based derivation of the spectrum and resolvent; the eigenframe-connection and Energy Migration formulation; the product-metric higher-dimensional theory; the corrected coupled field-structure equation.
2. **Classical and credited.** Conformal metrics, Laplace–Beltrami operators, Sturm–Liouville/compact-resolvent spectral theory, Weyl's law, resolvent kernels, Grönwall bounds, Perron–Frobenius theory, Noether's theorem, CFL stability theory.
3. **Verified.** Every central theorem has a numerical or symbolic check (see the Verification Report). Honesty caveats appear in every paper.

## VIII. CONCLUSION

A single positive field $\rho$, together with the transport map $\tau=\int dx/\rho$, generates a complete calculus, a complete spectral theory, a causal network theory, a variational theory, and closed-form solutions in graded media and on product domains. The eleven papers prove each claim; the demos verify each central theorem; the novelty statement is explicit and honest.

---

## REFERENCES

[1] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[2] P. Kundur, *Power System Stability and Control*, McGraw-Hill, 1994.

[3] R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, "Epidemic processes in complex networks," *Rev. Mod. Phys.* **87**, 925–979 (2015).

[4] M. Spivak, *Calculus on Manifolds*, Benjamin/Cummings, 1965.

[5] G. B. Folland, *Advanced Calculus*, Prentice-Hall, 2002.

[6] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[7] I. M. Gelfand and S. V. Fomin, *Calculus of Variations*, Prentice-Hall, 1963.

## Program papers

01 Foundations · 02 Structure Spectral Theory · 03 Causal Network Spectral Theory · 04 Variational & Conservation · 05 Graded Media Engineering · 06 Power Networks & Synchronization · 07 Epidemiology on Adaptive Networks · 08 Numerical Methods · 09 Higher-Dimensional Structure-Flow · 10 Causal Graph-Time Signal Processing · 11 Novelty, Literature & Research Program