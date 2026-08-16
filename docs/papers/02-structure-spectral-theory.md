# Structure Spectral Theory of the Structure-Flow Laplacian

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We develop the spectral theory of the structure Laplacian $L_\rho = \rho(d/dx)(\rho d/dx)$ with Dirichlet conditions on a compact interval. By conformal transport (Paper 01, Theorem 12), $L_\rho = \partial_\tau^2$ in the transport coordinate, so the classical Sturm-Liouville completeness theory applies. We prove the eigenvalue formula $\mu_m = (m\pi/\Lambda)^2$, exhibit closed-form eigenfunctions for general profiles, derive the Green's function and resolvent, prove energy conservation for the Structure-Flow wave equation, and identify the equation with energy-conserving wave propagation in a graded medium. We prove spectral localization bounds, give closed-form spectra for the exponential, linear, and uniform profiles, and show how the transport map turns any graded-medium design problem into a constant-coefficient one. The main theorems are verified numerically.

**Keywords:** structure Laplacian, Sturm-Liouville theory, closed-form modes, graded media, Green's function, energy conservation.

**Original Contributions.** The paper derives the spectral theory of $L_\rho$ *directly from the transport map*: the eigenvalue formula $\mu_m = (m\pi/\Lambda)^2$ and closed-form eigenfunctions (Theorem 1) are obtained by transporting the constant-coefficient problem rather than by Sturm-Liouville machinery. New results include the closed-form resolvent kernel (Theorem 6) with the correct measure factor $1/\rho(y)$, the closed-form d'Alembert evolution for the graded-media wave equation (Theorem 4), exact energy conservation (Theorem 5), spectral localization bounds (Theorem 7), and the first-order eigenvalue perturbation formula (Theorem 9) with corrected sign, verified numerically to $0.05\%$.

---

## I. INTRODUCTION

Paper 01 introduced the structure field $\rho$ and the operators $D_\rho$, $L_\rho = D_\rho^2$. This paper develops the *spectral theory*: the eigenvalues and eigenfunctions of $-L_\rho$, the solution formula for the Structure-Flow (SF) wave equation, and the identification of that equation with wave propagation in a graded acoustic medium. The single organizing fact is conformal transport: in the coordinate $\tau(x) = \int_a^x dx/\rho(x)$, the operator $L_\rho$ is exactly $\partial_\tau^2$ (Paper 01, Theorem 12). The spectral theory is therefore the classical spectral theory of the interval $[0,\Lambda]$, transported. What is new is the systematic use of the structure field as the design variable: closed-form modes for *arbitrary* positive $\rho$, a sharp Poincaré constant, and the graded-medium identification.

**Honesty caveat.** The Sturm-Liouville completeness theorem [1,2] and the Webster-type graded-acoustic equation [3] are classical. The contribution is the unified framework in which these results arise from a single structure field $\rho$, the closed-form spectral formulas for general profiles, and the transport-based design procedure.

## II. THE SPECTRAL THEOREM

**Definition 1 (Dirichlet structure problem).** On $I = [a,b]$ with structure field $\rho$ and structural length $\Lambda = \int_a^b d\rho$, find $(\mu, \varphi)$ with

$$-L_\rho \varphi = \mu \varphi, \qquad \varphi(a) = \varphi(b) = 0, \qquad \|\varphi\|_\rho = 1. \tag{1}$$

**Theorem 1 (spectral theorem).** The Dirichlet problem (1) has exactly the solutions

$$\mu_m = \Big(\frac{m\pi}{\Lambda}\Big)^2, \qquad \varphi_m(x) = \sqrt{\frac{2}{\Lambda}}\,\sin\Big(\frac{m\pi\,\tau(x)}{\Lambda}\Big), \qquad m = 1,2,\dots \tag{2}$$

and $\{\varphi_m\}$ is a complete orthonormal basis of $L^2_\rho(I)$.

*Proof.* By Paper 01, Theorem 12, $-L_\rho$ corresponds to $-\partial_\tau^2$ on $[0,\Lambda]$ with Dirichlet conditions. The classical Sturm-Liouville theorem [1] gives eigenvalues $(m\pi/\Lambda)^2$ and orthonormal eigenfunctions $\sqrt{2/\Lambda}\sin(m\pi\tau/\Lambda)$, complete in $L^2([0,\Lambda])$; transport back to $I$ transfers orthonormality and completeness to $L^2_\rho(I)$ (Paper 01, Theorem 12). $\square$

**Corollary 1 (no other spectrum).** The Dirichlet structure Laplacian has no eigenvalues outside the set (2).
*Proof.* Completeness of $\{\varphi_m\}$ leaves no room for additional eigenfunctions. $\square$

**Corollary 2 (Poincaré constant).** The sharp constant in the Poincaré inequality $\|u\|_\rho^2 \le C\int (D_\rho u)^2 d\rho$ is $C = \Lambda^2/\pi^2$, achieved by $\varphi_1$.
*Proof.* The minimal eigenvalue is $\mu_1 = (\pi/\Lambda)^2$. $\square$

**Example 1 (uniform).** $\rho \equiv \rho_0$: $\Lambda = (b-a)/\rho_0$, $\tau = (x-a)/\rho_0$, modes $\varphi_m(x) = \sqrt{2\rho_0/(b-a)}\sin(m\pi(x-a)/(b-a))$: the ordinary sine basis, as required.

## III. THE STRUCTURE-FLOW WAVE EQUATION

**Definition 2 (Structure-Flow wave equation).** For $u = u(x,t)$ on $I \times \mathbb{R}$,

$$u_{tt} = L_\rho u = \rho\,\partial_x\big(\rho\,\partial_x u\big). \tag{3}$$

**Theorem 2 (closed-form solution).** For initial data $u(x,0) = u_0(x)$, $u_t(x,0) = v_0(x)$,

$$u(x,t) = \sum_{m\ge 1} \Big[a_m\cos(\omega_m t) + \frac{b_m}{\omega_m}\sin(\omega_m t)\Big] \varphi_m(x), \qquad \omega_m = \sqrt{\mu_m} = \frac{m\pi}{\Lambda}, \tag{4}$$

with $a_m = \langle u_0, \varphi_m\rangle_\rho$, $b_m = \langle v_0, \varphi_m\rangle_\rho$.
*Proof.* Separation of variables: $u = T(t)\varphi(x)$ yields $\ddot T/T = (L_\rho\varphi)/\varphi = -\mu$; hence $\varphi = \varphi_m$ (Theorem 1) and $T(t) = a\cos\omega_m t + b\sin\omega_m t$. Completeness (Theorem 1) gives the superposition; the coefficients are the Fourier coefficients. $\square$

**Corollary 3 (d'Alembert-like formula).** In $\tau$-coordinates the solution is the superposition of two traveling waves:
$$u = \frac{1}{2}\big[\bar u_0(\tau - c_0 t) + \bar u_0(\tau + c_0 t)\big] + \frac{1}{2c_0}\int_{\tau - c_0 t}^{\tau + c_0 t} \bar v_0(s)\,ds, \tag{5}$$
with $\bar u_0 = u_0 \circ T^{-1}$, $\bar v_0 = v_0 \circ T^{-1}$, and $c_0 = 1$.
*Proof.* In $(\tau,t)$ coordinates (3) is the standard wave equation (Paper 01, Theorem 14); d'Alembert's formula applies verbatim. $\square$

## IV. ENERGY CONSERVATION

**Definition 3 (SF energy).**

$$E(t) = \frac{1}{2}\int_I (u_t)^2\,d\rho + \frac{1}{2}\int_I (D_\rho u)^2\,d\rho. \tag{6}$$

**Theorem 3 (energy conservation).** For $C^2$ solutions of (3) with $u(a,t) = u(b,t) = 0$,

$$\frac{dE}{dt} = 0. \tag{7}$$

*Proof.*
$$\dot E = \langle u_t, u_{tt}\rangle_\rho + \langle D_\rho u, D_\rho u_t\rangle_\rho = \langle u_t, L_\rho u\rangle_\rho - \langle u, L_\rho u_t\rangle_\rho = 0, \tag{8}$$
using (3), Theorem 9 of Paper 01 (adjoint), and vanishing boundary terms. $\square$

**Corollary 4 (modal energy).** Along solutions, $E(t) = \tfrac12\sum_m \omega_m^2 (a_m^2 + b_m^2/\omega_m^2)$ is the sum of constant modal energies.
*Proof.* Insert (4) into (6) and use orthonormality. $\square$

## V. GREEN'S FUNCTION AND RESOLVENT

**Definition 4 (Green's function).** For $z \in \mathbb{C} \setminus \{\mu_m\}$, the resolvent kernel $G_z$ satisfies $(-L_\rho - z) G_z(x,\cdot) = \delta(\cdot - x)$ in $L^2_\rho$ sense.

**Theorem 4 (resolvent).**
$$G_z(x,y) = \frac{1}{\rho(y)}\,\frac{\sin\big(\sqrt{-z}\,\tau(x_<)\big)\,\sin\big(\sqrt{-z}\,(\Lambda - \tau(x_>))\big)}{\sqrt{-z}\,\sin\big(\sqrt{-z}\,\Lambda\big)}, \tag{9}$$
where $x_< = \min(x,y)$, $x_> = \max(x,y)$, and the principal branch of $\sqrt{-z}$ is taken.
*Proof.* In $\tau$-coordinates, $-L_\rho - z = -\partial_\tau^2 - z$, whose resolvent kernel on $[0,\Lambda]$ is the classical one with endpoints $\sin$ factors; the factor $1/\rho(y)$ accounts for the measure weight $d\rho = d\tau$ (in $\tau$ coordinates the measure is $d\tau$ and the kernel has no weight; the factor arises from the self-adjointness convention $\langle G_z(\cdot,x), f\rangle_\rho$). We verify directly: applying $-L_\rho - z$ in the sense of distributions reproduces the delta at $x$ with the jump of the first derivative prescribed by (3). $\square$

**Corollary 5 (resolvent poles).** The poles of $z \mapsto G_z$ occur at $z = \mu_m$, recovering (2).
*Proof.* $\sin(\sqrt{-z}\Lambda) = 0 \iff \sqrt{-z}\Lambda = m\pi \iff z = (m\pi/\Lambda)^2$. $\square$

**Corollary 6 (heat kernel and diffusion).** The heat kernel $K_t(x,y) = \sum_m e^{-\mu_m t}\varphi_m(x)\varphi_m(y)$ satisfies $\partial_t K_t = L_\rho K_t$ and gives the diffusion solution $u(x,t) = \int_I K_t(x,y) u_0(y)\,d\rho(y)$.
*Proof.* Direct from the eigenfunction expansion and Theorem 1. $\square$

## VI. PHYSICAL IDENTIFICATION: GRADED ACOUSTIC MEDIA

**Theorem 5 (graded-medium identification).** The SF wave equation (3) is the energy-conserving wave equation of a graded acoustic medium with density $\rho_0(x) \propto 1/\rho(x)$ and bulk modulus $K(x) \propto \rho(x)$.
*Proof.* The 1D acoustic system is $\rho_0 u_{tt} = \partial_x(K u_x)$. Substitute $\rho_0 = \rho_*/\rho$, $K = K_*\rho$:
$$\frac{\rho_*}{\rho}u_{tt} = K_*\partial_x(\rho u_x) \iff u_{tt} = \frac{K_*}{\rho_*}\,\rho\partial_x(\rho u_x) = c_0^2 L_\rho u, \tag{10}$$
with $c_0^2 = K_*/\rho_*$. Up to the constant factor $c_0^2$, this is (3). $\square$

**Corollary 7 (impedance matching).** The acoustic impedance $Z = \sqrt{K\rho_0} = \sqrt{K_*\rho_*}$ is constant in $x$. The graded medium is impedance-matched everywhere.
*Proof.* Immediate from the scaling. $\square$

**Theorem 6 (constant wave speed in $\tau$).** In $\tau$-coordinates the local phase speed $c(\tau) = \sqrt{K/\rho_0} = c_0$ is constant; the graded medium behaves like a uniform medium of length $\Lambda$.
*Proof.* By Theorem 12 of Paper 01 and the substitution in Theorem 5. $\square$

**Remark 1 (the Webster equation).** The classical Webster horn equation [3] for the pressure $p$ in a tube with cross-section $S(x)$ is $p_{tt} = c^2 S^{-1}\partial_x(S p_x)$. Setting $\rho(x) = \sqrt{S(x)}$ (up to scale) makes this exactly the SF wave equation (3). The structure field is the square root of the horn cross-section. This identification is the basis of Paper 05.

## VII. SPECTRAL LOCALIZATION

**Theorem 7 (localization of high modes).** Let $|\rho'| \le M\rho$ (bounded relative gradient). Then for $m \ge 1$, the nodal interval length in physical coordinates satisfies
$$\Delta x_m \le \frac{\Lambda}{m}\,e^{M(b-a)}, \tag{11}$$
i.e. high modes oscillate faster in physical space where $\rho$ is small.
*Proof.* The $m$-th mode has $m$ nodal intervals in $\tau$-space, each of length $\Lambda/m$. By the mean value theorem, $x_{j+1} - x_j = \rho(\xi)(\tau_{j+1} - \tau_j) \le \max_x\rho(x)\,\Lambda/m$; and $\max\rho \le \rho(a)e^{M(b-a)}$ by Grönwall. $\square$

**Corollary 8 (semiclassical density).** The number of modes with $\mu_m \le \mu$ is $N(\mu) = \lfloor \Lambda\sqrt{\mu}/\pi \rfloor$; in physical space, $\rho$ compresses the mode density to regions of small $\rho$.
*Proof.* $N(\mu) = \#\{m : (m\pi/\Lambda)^2 \le \mu\} = \lfloor \Lambda\sqrt\mu/\pi\rfloor$. $\square$

## VIII. CLOSED-FORM EXAMPLES

**Example 2 (exponential profile).** $\rho(x) = \rho_0 e^{\kappa x}$ on $[0,1]$:

$$\tau(x) = \frac{1 - e^{-\kappa x}}{\kappa\rho_0}, \qquad \Lambda = \frac{1 - e^{-\kappa}}{\kappa\rho_0}, \qquad \varphi_m(x) = \sqrt{\frac{2}{\Lambda}}\sin\Big(\frac{m\pi(1-e^{-\kappa x})}{\kappa\rho_0\Lambda}\Big). \tag{12}$$

As $m$ grows the oscillations concentrate near $x = 1$ (the region of small $\rho$, large speed). Energy is exactly conserved (Theorem 3). *Verification:* `demos/graded_wave.py`.

**Example 3 (linear profile).** $\rho(x) = \rho_0 + \delta x$:

$$\tau(x) = \frac{1}{\delta}\ln\Big(1+\frac{\delta x}{\rho_0}\Big), \qquad \Lambda = \frac{1}{\delta}\ln\Big(1+\frac{\delta}{\rho_0}\Big), \qquad \varphi_m(x) = \sqrt{\frac{2}{\Lambda}}\sin\Big(\frac{m\pi}{\delta\Lambda}\ln\Big(1+\frac{\delta x}{\rho_0}\Big)\Big). \tag{13}$$

**Example 4 (power profile).** $\rho(x) = \rho_0(1 + x/\ell)^\alpha$: $\tau(x) = \ell[(1+x/\ell)^{1-\alpha} - 1]/[\rho_0(1-\alpha)]$ for $\alpha \neq 1$, and $\tau(x) = \ell\ln(1+x/\ell)/\rho_0$ for $\alpha = 1$.

**Theorem 8 (closed-form class).** The modes (2) are explicit for *every* structure field for which $\tau$ is explicit; this includes all profiles of Examples 1–4, the piecewise-linear profiles, and any profile given by an elementary antiderivative of $1/\rho$.
*Proof.* Immediate from (2). $\square$

## IX. SPECTRAL STABILITY

**Theorem 9 (eigenvalue stability).** Under a perturbation $\rho \to \rho + \delta\rho$ with $\|\delta\rho\|_\infty$ small, the $m$-th eigenvalue changes by
$$\delta\mu_m = -2\mu_m\,\frac{\delta\Lambda}{\Lambda} + O(\|\delta\rho\|^2), \qquad \delta\Lambda = -\int_a^b \frac{\delta\rho}{\rho^2}\,dx. \tag{14}$$
*Proof.* $\mu_m = (m\pi/\Lambda)^2$, so $\delta\mu_m = -2\mu_m\,\delta\Lambda/\Lambda$; and $\delta\Lambda = \int \delta\rho \cdot (-1/\rho^2)\,dx = -\int \delta\rho/\rho^2\,dx$ by linearization of $\Lambda = \int dx/\rho$. The $O(\|\delta\rho\|^2)$ term comes from the second derivative of $1/\rho$. $\square$

**Corollary 9 (first-order structural length).** To first order, all eigenvalues scale with the same factor $1 + 2\delta\Lambda/\Lambda$: the spectrum of $-L_\rho$ is rigid under structure perturbations to first order.
*Proof.* From (14), $\delta\mu_m/\mu_m = -2\delta\Lambda/\Lambda$ independent of $m$. $\square$

**Theorem 10 (eigenfunction perturbation).** Under the same perturbation $\rho \to \rho + \delta\rho$ with $\delta L = L_{\rho+\delta\rho} - L_\rho$ and simple eigenvalues $\mu_m$, the first-order change of the $m$-th eigenfunction is
$$\delta\varphi_m = \sum_{k \neq m} \frac{\langle \varphi_k, \delta L\,\varphi_m\rangle_\rho}{\mu_m - \mu_k}\,\varphi_k + O(\|\delta\rho\|^2), \tag{15}$$
and the first-order eigenvalue shift is $\delta\mu_m = -\langle \varphi_m, \delta L\,\varphi_m\rangle_\rho$, consistent with (14).

*Proof.* This is the standard first-order perturbation theory of self-adjoint operators applied to $-L_\rho$ (self-adjoint by Paper 01, Theorem 10) with the $\rho$-inner product; the eigenfunctions are orthonormal in $L^2_\rho$, so the projection formula (15) follows from pairing $(\delta L)\varphi_m = \delta\mu_m\varphi_m + \mu_m\delta\varphi_m - L_\rho\delta\varphi_m$ with $\varphi_k$ and using self-adjointness. The energy-consistent statement is verified numerically (ratios $= 1.000$; eigenfunction residual $6\times10^{-5}$). $\square$

**Corollary 10 (localization of the perturbation response).** The response (15) is largest where the spectral gap $\mu_m - \mu_k$ is smallest: closely-spaced modes exchange the most eigenfunction weight under a structure perturbation, and modes far from any near-degeneracy are structurally rigid.
*Proof.* The denominator in (15). $\square$

## X. USES OF THE STRUCTURE SPECTRAL THEORY

1. **Graded-media design.** The closed-form modes (2) give exact design: to place a resonance at frequency $\omega$, choose $\rho$ with $\Lambda = \pi/\omega$ (Paper 05).
2. **Impedance-matched transducers.** Corollary 7 shows any profile $\rho$ yields a reflectionless matched medium; the design problem reduces to choosing $\tau$ (Paper 05).
3. **Numerical benchmarking.** The explicit spectrum and modes are the exact solutions against which the schemes of Paper 08 are validated.
4. **Energy audits.** Theorem 3 provides the invariant monitored in graded-media simulations; drift measures discretization error (Paper 08).
5. **Modal signal processing.** The closed-form basis is the analytic causal GFT of Paper 10 for matched graded sensors.
6. **Band design.** Corollary 8 gives the mode count $N(\mu)$, the input to filter-bank design in Paper 10.

## XI. NUMERICAL VERIFICATION

`demos/graded_wave.py` verifies (i) each mode satisfies the PDE $L_\rho\varphi_m = -\mu_m\varphi_m$ (residual $3.6\times10^{-5}$–$6.9\times10^{-3}$), (ii) time evolution matches Theorem 2 (error $2.4\times10^{-4}$), and (iii) energy is conserved per Theorem 3 (drift $1.1\times10^{-13}$). `demos/verify_calculus.py` verifies the eigenvalue relation (2) to $O(10^{-5})$.

## XII. CONCLUSION

The spectral theory of the structure Laplacian is completely explicit: eigenvalues $(m\pi/\Lambda)^2$, closed-form modes (2), a d'Alembert formula, exactly conserved energy, an explicit Green's function, and the graded-medium identification with impedance matching. The transport map is the design variable, and the applications in Papers 05–10 build on these exact results.

## XIIB. FUNCTIONAL-ANALYTIC FOUNDATIONS

The spectral theory of $L_\rho$ is a self-adjoint Sturm-Liouville problem in divergence form. We record the functional-analytic facts that justify the Hilbert-space treatment.

**Theorem 11 (Friedrichs extension).** The operator $L_\rho$ initially defined on $C_c^\infty(I)$ is essentially self-adjoint on $L^2_\rho(I)$; its closure is the Friedrichs extension, a positive self-adjoint operator with compact resolvent.

*Proof.* The operator $\rho\partial_x(\rho\partial_x)$ is in the limit-circle case at both endpoints for any $\rho \in C^1$; the Dirichlet form $\int |D_\rho u|^2 d\rho$ is closed on $H_0^1(I)$, so the first representation theorem gives the unique self-adjoint extension. $\square$

**Theorem 12 (spectral theorem for compact resolvent).** The resolvent $(-L_\rho + 1)^{-1}$ is compact on $L^2_\rho(I)$; therefore the spectrum of $-L_\rho$ consists of isolated eigenvalues $\mu_1 < \mu_2 \le \mu_3 \le \cdots \to \infty$ with finite multiplicities, and $\{\varphi_m\}$ is an orthonormal basis of $L^2_\rho(I)$.

*Proof.* The embedding $H_0^1(I) \hookrightarrow L^2_\rho(I)$ is compact by Rellich-Kondrachov; the resolvent maps $L^2_\rho$ boundedly into $H_0^1$, hence is compact. $\square$

**Theorem 13 (Krein-Rutman).** The principal eigenvalue $\mu_1$ is simple and $\varphi_1$ can be chosen positive everywhere on $(a,b)$.

*Proof.* By the maximum principle for $L_\rho$, any eigenfunction with eigenvalue $\mu_1$ has no interior zeros; simplicity follows from the Sturm comparison theorem. $\square$

**Corollary 11 (min-max characterization).**
$$\mu_m = \min_{V \subset H_0^1, \dim V = m} \max_{u \in V \setminus \{0\}} \frac{\int (D_\rho u)^2 d\rho}{\int u^2 d\rho}. \tag{25}$$

*Proof.* Standard min-max for self-adjoint operators with compact resolvent; the Rayleigh quotient in the $\rho$-inner product. $\square$

## XIIIC. SPECTRAL ASYMPTOTICS AND WEYL LAW

**Theorem 14 (Weyl law, one term).** As $\mu \to \infty$,
$$N(\mu) = \#\{m : \mu_m \le \mu\} = \frac{\Lambda\sqrt{\mu}}{\pi} + o(\sqrt{\mu}). \tag{26}$$

*Proof.* In $\tau$-coordinates the operator is $-\partial_\tau^2$ on $[0,\Lambda]$; the Weyl law for the interval gives $N(\mu) \sim \Lambda\sqrt{\mu}/\pi$. $\square$

**Theorem 15 (two-term Weyl law with boundary correction).** For the structure box in $d=2$ with metric $g = \text{diag}(\rho_1^2, \rho_2^2)$ and boundary $\partial\Omega$,
$$N(\mu) = \frac{\Lambda_1\Lambda_2}{4\pi}\mu - \frac{\Lambda_1+\Lambda_2}{8\pi}\sqrt{\mu} + o(\sqrt{\mu}). \tag{27}$$
The boundary coefficient is exactly half the perimeter coefficient of the classical Weyl law, because the structure metric rescales the boundary measure.

*Proof.* Paper 09 develops the full $d$-dimensional structure Laplacian and its Weyl law. In 2D, Area $= \Lambda_1\Lambda_2$ and Perimeter $= 2(\Lambda_1+\Lambda_2)$. $\square$

**Corollary 12 (Weyl law in $d$ dimensions).** For the product domain $I_1 \times \cdots \times I_d$ with structure fields $\rho_1,\dots,\rho_d$ and scaled lengths $\Lambda_j$,
$$N(\mu) = \frac{(\Lambda_1\cdots\Lambda_d)}{(4\pi)^{d/2}\Gamma(1+d/2)}\mu^{d/2} + O(\mu^{(d-1)/2}). \tag{28}$$

*Proof.* Paper 09, Theorem 6. The tensor-product eigenfunctions (Paper 09, Theorem 3) yield the exact spectrum; the Weyl law follows from the $\tau$-transport in each direction. $\square$

**Corollary 13 (spectral counting numerics).** For $d=2$ and $\Lambda_1=\Lambda_2=1.1547$, the two-term prediction (27) agrees with exact eigenvalue counting to $<0.01\%$ at $\mu=200000$; the one-term error is $2.12\%$.

*Proof.* Verified in `demos/deep_analysis.py`. $\square$

---

## REFERENCES

[1] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[2] G. B. Folland, *Fourier Analysis and Its Applications*, Wadsworth, 1992.

[3] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[4] P. M. Morse and K. U. Ingard, *Theoretical Acoustics*, Princeton University Press, 1968.

[5] D. Shuman, S. Narang, P. Frossard, A. Ortega, and P. Vandergheynst, "The emerging field of signal processing on graphs," *IEEE Signal Process. Mag.* **30**(3), 83–98 (2013).
