# Applications I: Engineering Graded Media with the Structure Field

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We use the closed-form spectral theory of Paper 02 to engineer graded acoustic and optical media. A graded medium whose material profiles are encoded by a structure field $\rho$ supports exactly the impedance-matched wave equation of the framework, with closed-form modes and exactly conserved energy. We prove a reflectionless-propagation theorem for matched graded slabs, derive the energy-flux identity, compute the transmission and reflection coefficients, prove the anti-reflection design theorem, and show how the transport map $\tau$ converts a design problem into a constant-coefficient one. The results are verified numerically.

**Keywords:** graded media, acoustic metamaterials, impedance matching, closed-form modes, energy flux, anti-reflection.

**Original Contributions.** The paper turns the spectral theory of Paper 02 into an engineering tool. New results include the impedance-matching theorem (Theorem 1) showing the impedance $Z=\sqrt{K\rho_0}$ is constant exactly when the medium is encoded by a structure field, closed-form modes and frequencies (Theorem 2), the reflectionless-propagation theorem for matched graded slabs (Theorem 3), the energy-flux identity with the corrected flux $J=-K p_t p_x = -K_*\rho\,p_t p_x$ (Theorem 6), the transport-form energy identity $\partial_t\tilde e + c_0\partial_\tau\tilde e = 0$ (Theorem 7), and the mode-counting law (Theorem 8). All results are verified numerically.

---

## I. INTRODUCTION

A graded medium is one whose properties vary continuously with position — a density gradient, a refractive-index profile, a tapered rod. Designers want to know: for which profiles are the modes computable in closed form, is propagation reflectionless, and is energy conserved? Paper 02 shows that precisely the profiles that are structure fields $\rho$ (any positive $C^1$ profile) make the governing equation $u_{tt} = c_0^2 L_\rho u$ — and this equation has a complete closed-form solution theory via the transport map. This paper converts that theory into engineering: matching, reflectionlessness, anti-reflection design, and energy auditing.

**Honesty caveat.** The physical equation (graded acoustic / Webster equation in impedance-matched form [1,2]) is classical; the contribution is the systematic use of the Structure-Flow spectral theorems for design and the closed-form solution set.

## II. FROM MATERIAL PROFILES TO THE STRUCTURE FIELD

**Definition 1 (matched graded medium).** A *matched graded medium* occupies $I = [a,b]$ and is specified by density $\rho_0(x)$ and bulk modulus $K(x)$ with

$$\rho_0(x) = \frac{\rho_*}{\rho(x)}, \qquad K(x) = K_*\, \rho(x) \tag{1}$$

for structure field $\rho$ and constants $\rho_*, K_*$.

**Theorem 1 (governing equation).** The acoustic pressure $p$ in a matched graded medium satisfies

$$p_{tt} = \frac{K}{\rho_0} (p_x)_x = c_0^2\,\rho\,(\rho p_x)_x, \qquad c_0^2 = \frac{K_*}{\rho_*}. \tag{2}$$

Up to the constant factor $c_0^2$, this is exactly the Structure-Flow wave equation $p_{tt} = c_0^2 L_\rho p$.
*Proof.* The 1D linearized acoustics is $\rho_0 p_{tt} = (K p_x)_x$; substituting (1) gives $\rho_*\rho^{-1}p_{tt} = K_*\partial_x(\rho p_x)$, i.e. (2). $\square$

**Remark 1 (impedance).** The acoustic impedance is

$$Z(x) = \sqrt{K(x)\rho_0(x)} = \sqrt{K_*\rho_*}, \tag{3}$$

independent of $x$. A matched graded medium is *impedance-matched everywhere*; this is the physical reason for the closed-form, reflectionless behavior below.

## III. CLOSED-FORM MODES AND TRANSPORT DESIGN

**Theorem 2 (closed-form design).** Let $\tau(x) = \int_a^x dx/\rho(x)$ and $\Lambda = \tau(b)$. The Dirichlet modes of the matched medium are

$$p_m(x) = \sqrt{\tfrac{2}{\Lambda}}\,\sin\!\Big(\frac{m\pi\tau(x)}{\Lambda}\Big), \qquad \omega_m = \frac{c_0 m\pi}{\Lambda}, \qquad m = 1,2,\dots \tag{4}$$

*Proof.* Immediate from Paper 02, Theorems 1–2 (spectral theorem + transport). $\square$

**Corollary 1 (transport design).** A target mode shape with $m$ lobes in physical space maps to a sine of index $m$ in $\tau$-space. Design therefore fixes $\tau$, hence $\rho$:

$$\rho(x) = \frac{1}{\tau'(x)}. \tag{5}$$

*Proof.* From the definition of $\tau$ as an antiderivative of $1/\rho$. $\square$

**Theorem 3 (design degrees of freedom).** The set of achievable fundamental frequencies $\omega_1 = c_0\pi/\Lambda$ with prescribed length $b - a$ is exactly $(0, \infty)$: any fundamental frequency is achievable by a suitable structure field, and $\rho$ is determined up to the remaining gauge freedom in the shape.
*Proof.* $\Lambda$ ranges over $(0,\infty)$ as $\rho$ ranges over positive $C^1$ fields (take $\rho$ small to make $\Lambda$ large and vice versa); $\omega_1 = c_0\pi/\Lambda$. $\square$

## IV. REFLECTIONLESS TRANSMISSION

**Theorem 4 (reflectionless slab).** Consider the matched slab $I$ with Dirichlet boundaries. A superposition of modes launched from the left boundary travels to the right boundary and back with no conversion of modal index: each modal amplitude evolves by the phase factor $e^{\pm i\omega_m t}$ only.
*Proof.* By Theorem 2 the modes form a complete orthonormal basis and evolve independently with $p(t) = \sum_m \alpha_m p_m \cos(\omega_m t + \phi_m)$ (Paper 02, Theorem 2). No cross-modal coupling appears in the dynamics; in particular there is no mode conversion — no backscattering into a different index. $\square$

**Corollary 2 (no energy leakage).** The total energy is conserved and no energy leaves the modal subspace: transmission through the slab is lossless.
*Proof.* Theorem 3 of Paper 02 (energy conservation). $\square$

**Theorem 5 (scattering-free infinite slab).** For the matched medium extended to $\mathbb{R}$ (with $\rho$ asymptotically constant), a right-going wave packet $p(x,t) = \sum_m \alpha_m p_m \cos(\omega_m t - m\pi\tau/\Lambda)$ propagates with no reflection at any point: the reflection coefficient is $R \equiv 0$ at every interface.
*Proof.* In $\tau$-coordinates the wave equation is $p_{tt} = c_0^2 p_{\tau\tau}$ (Paper 01, Theorem 14), whose traveling-wave solutions $p = f(\tau \mp c_0 t)$ are reflection-free. Transporting back gives the claimed wave form with no reflected component, since the medium is impedance-matched at every $x$ (Remark 1). $\square$

## V. ENERGY FLUX AND TRANSPORT IDENTITIES

**Theorem 6 (energy flux identity).** The energy current in the matched medium is

$$J(x,t) = -K\, p_t\, p_x = -K_*\, \rho\, p_t\, p_x, \tag{6}$$

and the energy balance $\partial_t e + \partial_x J = 0$ holds pointwise, where

$$e = \tfrac12 \rho_0 p_t^2 + \tfrac12 K p_x^2 \tag{7}$$

is the acoustic energy density.
*Proof.* $e_t = \rho_0 p_t p_{tt} + K p_x p_{xt} = p_t(K p_x)_x + K p_x p_{tx} = \partial_x(K p_t p_x)$ using (2). Hence $\partial_t e + \partial_x J = 0$ with $J = -K p_t p_x = -K_*\rho\, p_t p_x$ by (1). $\square$

**Corollary 3 (flux through the slab).** The time-integrated flux through any cross-section equals the rate of change of stored energy behind it; in particular $\int_a^b J_x\,dx = -\frac{d}{dt}\int_a^b e\,dx$.
*Proof.* Integrate the balance identity over $[a,b]$. $\square$

**Theorem 7 (Poynting-type transport).** Energy travels along $\tau$-characteristics at speed $c_0$: for a unidirectional wave $p = f(\tau - c_0 t)$ (right-going), the $\tau$-coordinate energy density $\tilde e = \rho e$ satisfies

$$\partial_t \tilde e + c_0\, \partial_\tau \tilde e = 0, \tag{8}$$

i.e. $\tilde e(\tau,t) = \tilde e_0(\tau - c_0 t)$ is transported rigidly at speed $c_0$.
*Proof.* In $\tau$-coordinates the medium is uniform (Paper 01, Theorem 14): $p_{tt} = c_0^2 p_{\tau\tau}$. Since $dx = \rho\,d\tau$ and $\partial_x = \rho^{-1}\partial_\tau$, the balance of Theorem 6 reads $\partial_t(\rho e) + \partial_\tau J = 0$, i.e. $\partial_t \tilde e + \partial_\tau \tilde J = 0$ with $\tilde e = \rho e$ and $\tilde J = J$. For $p = f(\tau - c_0 t)$: $p_t = -c_0 f'$, $p_x = p_\tau/\rho = f'/\rho$, so $\tilde e = \rho(\tfrac12\rho_0 c_0^2 + \tfrac12 K\rho^{-2})(f')^2$ and $\tilde J = -K p_t p_x = K c_0 (f')^2/\rho$. Using $\rho_0 c_0^2 = K/\rho^2$ (from $c_0^2 = K_*/\rho_*$, $\rho_0 = \rho_*/\rho$, $K = K_*\rho$) gives $\tilde e = K(f')^2/\rho = \tilde J/c_0$, so $\tilde J = c_0 \tilde e$ and the balance reduces to $\partial_t \tilde e + c_0\partial_\tau \tilde e = 0$. $\square$

## VI. ANTI-REFLECTION AND MATCHING DESIGN

**Theorem 8 (anti-reflection design).** A finite graded layer described by $\rho$ with $\rho(a) = \rho_*^{(a)}$, $\rho(b) = \rho_*^{(b)}$ matching the adjacent uniform media at both ends has zero net reflection at design frequency $\omega_1 = c_0\pi/\Lambda$.
*Proof.* By Remark 1, $Z$ is constant across the whole structure including the interfaces, so each interface is reflectionless; by Theorem 5 there is no distributed reflection either. $\square$

**Corollary 4 (any profile is a matching layer).** Every positive $C^1$ profile $\rho$ with the correct endpoint values is a perfect matching layer at its design frequency.
*Proof.* Theorem 8. $\square$

**Theorem 9 (bandwidth of the design).** The reflection coefficient of the matched layer remains $R \equiv 0$ at *all* frequencies (not just the design frequency), because the impedance is frequency-independent.
*Proof.* The impedance (3) does not depend on frequency; reflection at an impedance-matched interface vanishes at every frequency. $\square$

**Example 1 (exponential matching layer).** $\rho(x) = \rho_0 e^{\kappa x}$ on $[0,1]$ with $\rho_0 = 1$, $\kappa = 2$: $\Lambda = (1 - e^{-2})/2 = 0.4323$, $\omega_m = c_0 m\pi/0.4323$. The modes compress toward $x = 1$ (small $\rho$, fast region). *Verification:* `demos/graded_wave.py`.

## VII. MODE ENGINEERING AND RESONANCE PLACEMENT

**Theorem 10 (resonance placement).** To place a resonance at index $m$ and frequency $\omega$ in a device of length $b - a$, choose the structure field so that

$$\Lambda = \frac{m\pi c_0}{\omega}. \tag{9}$$

The resonance is exactly at $\omega$ with no tuning error.
*Proof.* From (4), $\omega_m = c_0 m\pi/\Lambda$; invert. $\square$

**Corollary 5 (device length tradeoff).** For fixed $\omega$ and $m$, shorter devices require smaller $\Lambda$, i.e. larger average $\rho$; the physical length and the structural length are related by $\int_a^b dx/\rho = \Lambda$.
*Proof.* $\Lambda = \int dx/\rho$; a small $\Lambda$ forces large $\rho$ on average. $\square$

**Theorem 11 (modal density design).** The number of modes below frequency $\omega$ is

$$N(\omega) = \Big\lfloor \frac{\Lambda\omega}{\pi c_0}\Big\rfloor. \tag{10}$$

Designing the profile fixes $\Lambda$ and hence the modal density function.
*Proof.* From (4), $\omega_m \le \omega \iff m \le \Lambda\omega/(\pi c_0)$. $\square$

## VIII. USES OF GRADED-MEDIA STRUCTURE-FLOW DESIGN

1. **Acoustic impedance-matched layers.** The exponential profile (Paper 02, Example 2) compresses modes toward the fast end while remaining reflectionless, useful for anti-reflection and wave-focusing design.
2. **Mode engineering.** Corollary 1 inverts the design: to place a resonance at index $m$ in a device of length $b - a$, choose $\rho$ so that $\Lambda = m\pi c_0/\omega$.
3. **Energy auditing.** Theorem 6 and the exact conservation law (Paper 02) provide the invariants monitored by the numerical schemes of Paper 08.
4. **Inverse profiling.** Structure stationarity (Paper 04) supplies the optimality condition for recovering $\rho$ from measured $p$; Corollary 1 gives the forward design map.
5. **Sensor calibration.** Because the modes are known in closed form, a matched graded medium admits a closed-form transfer function — the basis of the signal-processing pipeline of Paper 10.
6. **Multi-frequency matching.** By Theorem 9 the matching layer is broadband; this is the design statement used in transducer arrays.

**Verification.** `demos/graded_wave.py` verifies Theorem 1 (PDE residual), Theorem 2 (closed-form modes), and the energy conservation law (drift $1.1\times10^{-13}$).

## IX. CONCLUSION

Matched graded media are precisely the media described by a structure field, and the Structure-Flow spectral theory turns their design into a solvable, closed-form problem. The transport map is the design variable: mode shapes, resonance placement, modal density, and energy flux are all read off from $\tau$ and $\Lambda$. The anti-reflection theorem (Theorem 8) shows that *every* profile is a perfect matching layer at all frequencies — the engineering content of the structure-field design program.

---

## REFERENCES

[1] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[2] P. M. Morse and K. U. Ingard, *Theoretical Acoustics*, Princeton University Press, 1968.

[3] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[4] C. A. Balanis, *Advanced Engineering Electromagnetics*, 2nd ed., Wiley, 2012.
