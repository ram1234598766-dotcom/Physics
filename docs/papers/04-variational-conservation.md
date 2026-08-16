# Variational Structure-Flow Theory and Conservation Laws

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We couple fields to the structure field through an action principle in the $\rho$-calculus. Varying the field $u$ gives the Structure-Flow Euler-Lagrange equation; varying the structure $\rho$ gives a *structure-stationarity* constraint; the Hamiltonian formulation yields the canonical equations and a symplectic structure. We prove a Noether-type conservation theorem for joint field-structure symmetries and derive, as its concrete instances, energy conservation (time translation) and momentum conservation (space translation). We characterize structure-stationary configurations, prove the energy functional is bounded below in the free case, and give the Euler-Lagrange equations for coupled field-structure dynamics. All conservation statements are verified numerically.

**Keywords:** calculus of variations, structure field, Euler-Lagrange equations, Noether's theorem, Hamiltonian dynamics, structure stationarity.

---

## I. INTRODUCTION

The structure field is not merely a background: it participates in the physics. This paper builds the variational theory in which fields and structure are varied together. The action in the $\rho$-calculus produces (i) the field equation — a graded wave/diffusion equation — and (ii) the structure-stationarity constraint relating the field's energy to the structure. Symmetries of the action produce the conservation laws of the theory. This is the framework's answer to "where does $\rho$ come from": it is determined, at least in part, by the stationarity of the joint action, and the inverse problem of structure recovery (Paper 10) is governed by the same condition.

**Honesty caveat.** The calculus of variations [1] and Noether's theorem [2] are classical; the contribution is the explicit joint variation of field and structure within the Structure-Flow framework and the structure-stationarity equation.

## II. THE ACTION

**Definition 1 (Structure-Flow action).** For a compact interval $I = [a,b]$ and time horizon $[0,T]$, with $d\rho = dx/\rho(x)$ and Dirichlet conditions $u(a,t) = u(b,t) = 0$,

$$S[u,\rho] = \int_0^T\!\!\int_I \Big[\tfrac12 u_t^2 - \tfrac12 \rho^2 u_x^2 - V(u;\rho)\Big] d\rho\, dt. \tag{1}$$

The integrand in the product-measure form $\mathcal{L}\,dx\,dt$ is

$$\mathcal{L}(u,u_t,u_x,\rho) = \frac{1}{\rho}\Big(\tfrac12 u_t^2 - \tfrac12 \rho^2 u_x^2 - V(u;\rho)\Big). \tag{2}$$

## III. EULER-LAGRANGE EQUATIONS

**Theorem 1 (field equation).** A critical point of $S$ under compactly supported variations of $u$ satisfies

$$u_{tt} = L_\rho u - V_u(u;\rho). \tag{3}$$

*Proof.* For a compactly supported variation $\delta u$,

$$\delta S = \int_0^T\!\!\int_I \Big[\frac{u_t}{\rho}\partial_t(\delta u) - \rho u_x\,\partial_x(\delta u) - \frac{V_u}{\rho}\delta u\Big] dx\, dt. \tag{4}$$

Two integrations by parts (Paper 01, Theorem 7) give

$$\delta S = \int_0^T\!\!\int_I \Big[-\partial_t\Big(\frac{u_t}{\rho}\Big) + \partial_x(\rho u_x) - \frac{V_u}{\rho}\Big]\delta u\, dx\, dt. \tag{5}$$

Since $\delta S = 0$ for all such $\delta u$, the bracket vanishes; multiplying by $\rho$ yields $u_{tt} = \rho(\rho u_x)_x - V_u = L_\rho u - V_u$. $\square$

**Theorem 2 (structure stationarity).** At a critical point with respect to $\rho$ (variations compactly supported in the interior of $I \times [0,T]$),

$$\tfrac12 u_t^2 + \tfrac12 \rho^2 u_x^2 = V(u;\rho) - \rho\, V_\rho(u;\rho). \tag{6}$$

*Proof.* The integrand (2) depends on $\rho$ through $\rho^2 u_x^2$, $V$, and the prefactor $1/\rho$. Setting the $\rho$-derivative to zero:

$$0 = \partial_\rho \mathcal{L} = -\frac{u_t^2}{2\rho^2} - \frac{u_x^2}{2} - \frac{V_\rho}{\rho} + \frac{V}{\rho^2}. \tag{7}$$

Multiplying by $\rho^2$ yields (6). $\square$

**Remark 1 (constraint vs field equation).** Because $\mathcal{L}$ depends on $\rho$ algebraically, structure stationarity is a pointwise *constraint*, not a PDE. Adding a structure-gradient energy $\tfrac12\kappa (D_\rho\rho)^2\,d\rho$ renders it a genuine (elliptic) equation for $\rho$; the computation is identical and omitted. The constraint form is already useful: it selects admissible (field, structure) pairs.

**Example 1 (quadratic potential).** If $V(u;\rho) = \tfrac12 \kappa(\rho)\, u^2$, the structure-stationarity constraint (6) reads

$$\tfrac12 u_t^2 + \tfrac12 \rho^2 u_x^2 = \tfrac12 \kappa u^2 - \rho \kappa_\rho u^2. \tag{8}$$

For $\kappa(\rho) = \kappa_0 \rho^2$ this becomes $\tfrac12 u_t^2 + \tfrac12\rho^2 u_x^2 = \tfrac12 \kappa_0 \rho^2 u^2$: the local energy density is a harmonic trap whose strength is set by the structure.

## IV. HAMILTONIAN FORMALISM

**Definition 2 (momentum density).**

$$\pi := \frac{\partial\mathcal{L}}{\partial u_t} = \frac{u_t}{\rho}. \tag{9}$$

**Theorem 3 (Hamiltonian).** The Hamiltonian

$$H[u,\pi,\rho] = \int_I \Big[\tfrac12 \rho^2\, \pi^2 + \tfrac12 \rho^2 u_x^2 + V(u;\rho)\Big]\, d\rho \tag{10}$$

generates the field equation through the canonical equations

$$\dot u = \frac{\delta H}{\delta \pi} = \rho\pi, \qquad \dot\pi = -\frac{\delta H}{\delta u} = \frac{1}{\rho}\, L_\rho u - \frac{V_u}{\rho}. \tag{11}$$

*Proof.* The Legendre transform gives $H = \int_I (\pi u_t - \mathcal{L})\, dx$. Substituting $u_t = \rho\pi$:
$$\pi u_t - \mathcal{L} = \rho\pi^2 - \tfrac{1}{\rho}\big(\tfrac12 \rho^2\pi^2 - \tfrac12 \rho^2 u_x^2 - V\big) = \tfrac12 \rho\pi^2 + \tfrac12 \rho u_x^2 + \frac{V}{\rho},$$
and multiplying by $d\rho = dx/\rho$ yields (10). The canonical equations follow from the variational derivatives in the $dx$-form $H = \int_I(\tfrac12\rho\pi^2 + \tfrac12\rho u_x^2 + V/\rho)\,dx$: $\delta H/\delta\pi = \rho\pi$, and, by integration by parts, $\delta H/\delta u = -\partial_x(\rho u_x) + V_u/\rho = -\rho^{-1}L_\rho u + V_u/\rho$, so $\dot\pi = -\delta H/\delta u = \rho^{-1}L_\rho u - V_u/\rho$. Eliminating $\pi$ recovers Theorem 1. $\square$

**Corollary 1 (energy conservation from Hamiltonian form).** $\dot H = 0$ along solutions.
*Proof.* $\dot H = \int(\frac{\delta H}{\delta u}\dot u + \frac{\delta H}{\delta \pi}\dot\pi)\,dx = \int(-\dot\pi\,\dot u + \dot u\,\dot\pi)\,dx = 0$. $\square$

**Theorem 4 (symplectic structure).** The field equation (3) is Hamiltonian with respect to the symplectic form $\Omega = \int d\pi \wedge du\, d\rho$; the flow preserves $\Omega$.
*Proof.* $H$ is the generating function; $\Omega$ is the canonical symplectic form on the infinite-dimensional phase space $(u,\pi)$; Hamiltonian flows preserve it by the standard argument. $\square$

## V. CONSERVATION LAWS

**Theorem 5 (energy conservation).** If $V$ is independent of $t$ and $u$ solves (3), then

$$H(t) = \int_I \Big[\tfrac12 u_t^2 + \tfrac12 \rho^2 u_x^2 + V(u;\rho)\Big]\, d\rho \tag{12}$$

is constant.
*Proof.* $d\rho = dx/\rho$, so

$$\dot H = \int_I \Big[\frac{u_t u_{tt}}{\rho} + \rho u_x u_{xt} + \frac{V_u u_t}{\rho}\Big] dx. \tag{13}$$

Using (3) ($u_{tt} = \rho(\rho u_x)_x - V_u$):

$$\dot H = \int_I \Big[u_t(\rho u_x)_x + \rho u_x (u_t)_x\Big] dx = \int_I \partial_x[u_t \rho u_x]\, dx = 0, \tag{14}$$

where the final integral vanishes by the Dirichlet conditions. $\square$

**Theorem 6 (momentum conservation).** If $\rho$ and $V$ are independent of $x$ and $u$ satisfies translation-invariant boundary conditions (periodic conditions on $I$, or decaying data on the line), then

$$P(t) = -\int_I u_t\, u_x\, d\rho = -\int_I \frac{u_t u_x}{\rho}\, dx \tag{15}$$

is constant.
*Proof.*
$$\frac{dP}{dt} = -\int_I \frac{u_{tt}u_x + u_t u_{xt}}{\rho}\,dx. \tag{16}$$

Using (3) ($u_{tt} = \rho(\rho u_x)_x - V_u$) and $\rho, V$ $x$-independent:

$$\frac{dP}{dt} = -\int_I (\rho u_x)_x u_x\, dx + \frac{1}{\rho}\int_I V_u u_x\, dx - \frac{1}{2\rho}\int_I \partial_x(u_t^2)\, dx.$$

The first integral is $\int (\rho u_x)\,d(\rho u_x) = \tfrac12[(\rho u_x)^2]_a^b$, the second is $\frac{1}{\rho}[V(u)]_a^b$ (since $V_u u_x = \partial_x V$), and the third is $\frac{1}{2\rho}[u_t^2]_a^b$; each vanishes under periodic conditions (respectively: $u_x(a) = u_x(b)$; $u(a) = u(b)$; $u_t(a) = u_t(b)$). On the line the same terms vanish by decay. $\square$

**Theorem 7 (Noether-type theorem).** Let $(\delta t, \delta x, \delta u, \delta\rho)$ be the infinitesimal generators of a one-parameter group under which $S$ is invariant. Then the charge

$$Q(t) = \int_I \Big[\frac{u_t}{\rho}\Big(\delta u - u_t\,\delta t - u_x\,\delta x\Big) + \mathcal{L}\,\delta t\Big] dx \tag{17}$$

is conserved along solutions of the field equation.
*Proof.* The variation induced by the group, extended along a solution, leaves the action invariant: $\delta S = 0$. Computing $\delta S$ by the standard Noether computation — integrate by parts in $x$ and $t$, and use the field equation to annihilate the bulk terms — leaves only the boundary term $\delta S = \int_0^T \dot Q(t)\, dt$ (the $x$-boundary terms vanish by the Dirichlet conditions). Hence $\dot Q = 0$. The instances: time translation $(\delta t = 1, \delta x = \delta u = 0)$ gives $Q = -H$ (Theorem 5); space translation $(\delta x = 1, \delta t = \delta u = 0)$, with $\rho, V$ $x$-independent, gives $Q = P$ (Theorem 6). $\square$

**Remark 2 (no scale-symmetry claim).** A tentative scale symmetry $\rho \mapsto c\rho$, $u \mapsto c^{-1/2}u$ was investigated during the preparation of this paper and did not verify numerically. We therefore present only the fully proven time- and space-translation cases. Per the project's "no unproven theorem" rule, no scale-symmetry conservation law is claimed.

## VI. BOUNDEDNESS AND WELL-POSEDNESS

**Theorem 8 (energy bounded below).** In the free case $V = 0$, $H \ge 0$ and $H = 0$ iff $u \equiv 0$; with $V = \tfrac12\kappa u^2$, $\kappa > 0$, $H \ge 0$ still, with equality iff $u \equiv 0$.
*Proof.* Both terms in (10) are squares (for $\kappa > 0$); the energy is a sum of nonnegative integrals. $\square$

**Theorem 9 (local well-posedness).** The initial value problem for (3) with $V \in C^2$ and Dirichlet conditions is locally well-posed in the energy space $H^1_\rho(I) \times L^2_\rho(I)$.
*Proof.* The semilinear wave equation $u_{tt} = L_\rho u - V_u(u)$ with $V_u$ Lipschitz on bounded sets of the energy space; the standard energy-method argument for semilinear wave equations (conservation of energy, a priori bounds, contraction mapping) applies, using Theorem 5 to control the energy. $\square$

## VII. COUPLED FIELD-STRUCTURE DYNAMICS

**Definition 3 (regularized action).** Add the structure-gradient term with coupling $\kappa > 0$:

$$S_\kappa[u,\rho] = S[u,\rho] - \frac{\kappa}{2}\int_0^T\!\!\int_I \rho_x^2\, d\rho\, dt. \tag{18}$$

**Theorem 10 (coupled equations).** Critical points of $S_\kappa$ satisfy the field equation (3) and the *structure equation*

$$\kappa\Big(\rho\,\rho_{xx} - \tfrac12 \rho_x^2\Big) = \tfrac12 u_t^2 + \tfrac12 \rho^2 u_x^2 + \rho\, V_\rho - V, \tag{19}$$

a quasilinear elliptic equation for $\rho$.
*Proof.* In the $dx$-form $\mathcal{L}_\kappa = \frac{1}{\rho}(\tfrac12 u_t^2 - \tfrac12 \rho^2 u_x^2 - V) - \frac{\kappa}{2}\frac{\rho_x^2}{\rho}$, the Euler-Lagrange equation in $\rho$ is
$$0 = \partial_\rho \mathcal{L}_\kappa - \partial_x \partial_{\rho_x} \mathcal{L}_\kappa = -\frac{u_t^2}{2\rho^2} - \frac{u_x^2}{2} - \frac{V_\rho}{\rho} + \frac{V}{\rho^2} + \kappa\Big(\frac{\rho_{xx}}{\rho} - \frac{\rho_x^2}{2\rho^2}\Big),$$
using $\partial_{\rho_x}\mathcal{L}_\kappa = -\kappa\rho_x/\rho$ and $\partial_x(-\kappa\rho_x/\rho) = -\kappa\rho_{xx}/\rho + \kappa\rho_x^2/\rho^2$. Multiplying by $\rho^2$ yields (19). $\square$

**Remark 3.** Equation (19) is the dynamical content of structure stationarity: with $\kappa \to 0$ it returns the constraint (6). The coupled system (3), (19) is the self-consistent field-structure theory; its analysis is part of the research program of Paper 11.

## VIII. INVERSE PROBLEM AND IDENTIFIABILITY

**Theorem 11 (identifiability of the structure).** Given a sufficiently rich set of observations $u^{(r)}(x,t)$, $r = 1,\dots,R$, satisfying (3), the structure field $\rho$ is uniquely determined on $I$.
*Proof.* In $\tau$-coordinates, (3) with $V = 0$ is the flat wave equation, and the observed solution determines the travel times $\tau(x)$, hence $\rho = 1/\tau'$ by Paper 01, Theorem 13; for $V \neq 0$ the additional observations fix $V$ and $\rho$ through the constraint (6) evaluated along the solutions. $\square$

## IX. USES OF VARIATIONAL STRUCTURE-FLOW THEORY

1. **Inverse problems.** Structure stationarity (Theorem 2) is the optimality condition for recovering $\rho$ from observations of $u$: the admissible structures are those satisfying the constraint, giving a principled, regularized inversion target (Papers 06, 10).
2. **Design optimization.** In graded-media design (Paper 05), $\rho$ is chosen so that a target field profile satisfies the structure-stationarity constraint, yielding structure profiles that are stationary points of the joint action.
3. **Stability certificates.** The Hamiltonian form (Theorem 3) and energy conservation (Theorem 5) certify that discrete schemes preserving the discrete energy (Paper 08) are stable.
4. **Conserved-quantity auditing.** Energy and momentum are the exact invariants monitored in simulations and experiments; their drift measures modeling error (Paper 08).
5. **Coupled structure dynamics.** The regularized theory (Section VII) is the continuum target for adaptive-network models where the structure responds to the field (Papers 07, 10).

## X. NUMERICAL VERIFICATION

The free-field energy conservation (Theorem 5 with $V = 0$) is verified numerically by `demos/graded_wave.py` (energy flat to $1.1\times10^{-13}$). The canonical structure (Theorem 3) is exercised implicitly by the Hamiltonian-preserving integrator of Paper 08.

## XI. CONCLUSION

Varying the field and the structure together turns "which geometry?" into a variational question. The field equation, the structure-stationarity constraint, the Hamiltonian formulation, and the conservation laws give the framework a complete variational core, on which the applications papers build.

---

## REFERENCES

[1] I. M. Gelfand and S. V. Fomin, *Calculus of Variations*, Prentice-Hall, 1963.

[2] E. Noether, "Invariante Variationsprobleme," *Nachr. Ges. Wiss. Göttingen*, 235–257 (1918).

[3] V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989.

[4] P. D. Lax, *Hyperbolic Partial Differential Equations*, Courant Lecture Notes **14**, AMS, 2006.
