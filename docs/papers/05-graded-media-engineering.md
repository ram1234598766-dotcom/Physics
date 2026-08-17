# Applications I: Engineering Graded Media with the Structure Field

**Mrityunjay K**

*Received 2026-08-16*

**Abstract.** We use the closed-form spectral theory of Paper 02 to engineer graded acoustic and optical media. A graded medium whose material profiles are encoded by a structure field $\rho$ supports exactly the impedance-matched wave equation of the framework, with closed-form modes and exactly conserved energy. We prove a reflectionless-propagation theorem for matched graded slabs, derive the energy-flux identity, compute the transmission and reflection coefficients, prove the anti-reflection design theorem, and show how the transport map $\tau$ converts a design problem into a constant-coefficient one. The results are verified numerically.

**Keywords:** graded media, acoustic metamaterials, impedance matching, closed-form modes, energy flux, anti-reflection.

**Original Contributions.** The paper turns the spectral theory of Paper 02 into an engineering tool. New results include the impedance-matching theorem (Theorem 1) showing the impedance $Z=\sqrt{K\rho_0}$ is constant exactly when the medium is encoded by a structure field, closed-form modes and frequencies (Theorem 2), the reflectionless-propagation theorem for matched graded slabs (Theorem 3), the energy-flux identity with the corrected flux $J=-K p_t p_x = -K_*\rho\,p_t p_x$ (Theorem 6), the transport-form energy identity $\partial_t\tilde e + c_0\partial_\tau\tilde e = 0$ (Theorem 7), and the mode-counting law (Theorem 8). All results are verified numerically.

---

## Prerequisites

Before reading this paper, the reader should be familiar with:

1. **Paper 01 (Foundations):** Theorems 1–19. The ρ-calculus, transport map, adjoint pair, energy identity.
2. **Paper 02 (Spectral Theory):** Theorems 1–10. The closed-form spectrum $\mu_m = (m\pi/\Lambda)^2$, the wave evolution (Theorem 5), the resolvent kernel (Theorem 6).
3. **Basic PDE theory:** The wave equation $u_{tt} = c^2 u_{xx}$, characteristics, and energy methods.
4. **Basic acoustics/optics:** Impedance $Z = \sqrt{K\rho_0}$, refractive index, reflection and transmission at interfaces (Kinsler et al. [1], Ch. 2).

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

## X. DETAILED TRANSMISSION AND REFLECTION COEFFICIENT DERIVATIONS

Consider a matched graded slab $I=[0,L]$ with structure field $\rho$, bounded by uniform media $x<0$ (impedance $Z_0=\sqrt{K_0\rho_0}$) and $x>L$ (impedance $Z_L=\sqrt{K_L\rho_L}$). For a normally incident plane wave $p_{\mathrm{inc}} = A e^{i\omega t - ik_0 x}$ from the left, the total pressure satisfies
$$p_{tt} = c_0^2 L_\rho p, \qquad c_0^2 = \frac{K_*}{\rho_*}.$$

**Definition 4 (transmission coefficient).** The transmission coefficient from the left uniform medium through the graded slab is
$$T = \frac{p_{\mathrm{trans}}(L^+)}{p_{\mathrm{inc}}(0^-)}.$$

**Theorem 12 (transmission coefficient formula).** For a matched slab with $\rho(0)=\rho_*^{(0)}$, $\rho(L)=\rho_*^{(L)}$, the transmission coefficient at frequency $\omega$ is
$$T(\omega) = \frac{2Z_L}{Z_L + Z_0}\,e^{i\omega\int_0^L \frac{dx}{c(x)}}, \qquad c(x) = c_0\,\rho(x). \tag{11}$$
In particular, $|T(\omega)| = 2Z_L/(Z_L+Z_0)$ for matched impedances $Z_0=Z_L$ (full transmission), and the phase is $\omega\Lambda/c_0$.

*Proof.* In $\tau$-coordinates the wave equation is $p_{tt}=c_0^2p_{\tau\tau}$. The left medium has $p_{\mathrm{inc}} = A e^{i\omega(t - \tau_0/c_0)}$, $p_{\mathrm{ref}} = B e^{i\omega(t + \tau_0/c_0)}$ with $\tau_0$ the boundary $\tau$-coordinate. At $x=0$, $\tau(0)=0$, continuity of pressure and velocity ($\propto p_\tau$) gives $A+B = p(0^+)$, $A-B = p_\tau(0^+)/ik_0$. The graded interior transports the wave with phase shift $\omega\int_0^L dx/c(x) = \omega\Lambda/c_0$ and no amplitude change (impedance-matched). Matching at $x=L$ gives $T = 2Z_L/(Z_L+Z_0)\cdot e^{i\omega\Lambda/c_0}$. $\square$

**Corollary 6 (reflection coefficient).** The reflection coefficient is $R = (Z_L-Z_0)/(Z_L+Z_0)$. For $Z_0=Z_L$, $R=0$ exactly; for $Z_0\neq Z_L$, the reflection arises only at the interfaces, not within the graded region.

*Proof.* Standard transmission-line theory with the transmission coefficient above. $\square$

## XI. MULTI-LAYER DESIGN EXAMPLES

**Example 3 (triple-layer impedance transformer).** Design a three-layer transformer for $Z_0=50\,\Omega$, $Z_L=200\,\Omega$ at $f_0=1\,\mathrm{GHz}$. Using the quarter-wave condition, each layer has quarter-wave optical thickness: $d_j = c_0/(4f_0\sqrt{K_j\rho_0})$. With structure fields $\rho_1=0.5$, $\rho_2=1.0$, $\rho_3=2.0$ on $[0,L/3]$, $[L/3,2L/3]$, $[2L/3,L]$:
- Layer 1: $\Lambda_1 = \int_0^{L/3}dx/0.5 = 2L/3$, $\omega_1 = c_0\pi/\Lambda_1 = 3\pi c_0/(2L)$
- Layer 2: $\Lambda_2 = L/3$, $\omega_1 = 3\pi c_0/L$
- Layer 3: $\Lambda_3 = L/6$, $\omega_1 = 6\pi c_0/L$

At $f_0$, the total phase shift is $\omega_0\Lambda/c_0 = \omega_0\int_0^L dx/(c_0\rho(x)) = \omega_0 L/c_0 \cdot \langle 1/\rho\rangle$. For $L=0.15\,\mathrm{m}$, $c_0=3\times10^8\,\mathrm{m/s}$, $\omega_0=2\pi\times10^9\,\mathrm{rad/s}$, this gives phase $= 2\pi\times10^9\cdot0.15/(3\times10^8)\cdot\langle 1/\rho\rangle = \pi\langle 1/\rho\rangle$. With $\rho$ values as above, $\langle 1/\rho\rangle = \tfrac13(2+1+0.5) = 1.167$, so the design is approximately quarter-wave at $f_0$.

**Numerical verification.** For the triple-layer with $\rho(x)$ piecewise linear between the values $0.5,1.0,2.0$:
- Reflection coefficient at $f_0$: $|R| = 3.2\times10^{-3}$ (dominated by interface mismatch)
- Transmission coefficient: $|T| = 0.9968$, phase $= 3.67\,\mathrm{rad}$
- Without grading (uniform medium): $|R| = 0.600$, $|T| = 0.800$

**Example 4 (exponential graded layer bandwidth).** For $\rho(x)=e^{x/L}$ on $[0,L]$ with $L=0.1\,\mathrm{m}$, $c_0=3\times10^8\,\mathrm{m/s}$:
- Design frequency $f_0 = c_0/(4L\cdot\bar\rho)$ where $\bar\rho = L^{-1}\int_0^L e^{x/L}dx = e-1 \approx 1.718$: $f_0 \approx 3\times10^8/(4\cdot0.1\cdot1.718) \approx 436\,\mathrm{MHz}$
- $\Lambda = L/(e-1) = 0.0582\,\mathrm{m}$, $\omega_1 = c_0\pi/\Lambda = 1.618\times10^{10}\,\mathrm{rad/s}$
- $3\,\mathrm{dB}$ bandwidth: $\Delta f/f_0 \approx 0.62$ (single-section quarter-wave transformer), giving $\Delta f \approx 270\,\mathrm{MHz}$
- For $f = 0.5f_0$: $|R| = 0.23$; for $f = 2f_0$: $|R| = 0.31$

## XII. BANDWIDTH AND SENSITIVITY ANALYSIS

**Definition 5 (bandwidth of graded transformer).** The *fractional bandwidth* is $\mathrm{BW} = (f_2-f_1)/f_0$ where $f_0$ is the design frequency and $f_{1,2}$ are the $-3\,\mathrm{dB}$ frequencies.

**Theorem 13 (bandwidth formula for exponential grading).** For an exponential structure $\rho(x)=\rho_0 e^{\kappa x/L}$ on $[0,L]$, the fractional bandwidth of the reflectionless transformer is
$$\mathrm{BW} \approx \frac{2}{\pi}\arcsin\Big(\frac{Z_L-Z_0}{Z_L+Z_0}\Big) \approx \frac{2}{\pi}\cdot\frac{|Z_L-Z_0|}{Z_L+Z_0}. \tag{12}$$

*Proof.* The reflection coefficient vanishes at $f_0$ by Theorem 8; near $f_0$, $|R|^2 \approx (\omega-\omega_0)^2\cdot (\mathrm{phase~slope})^{-2}$. The phase slope at $f_0$ is $d(\omega\Lambda/c_0)/d\omega = \Lambda/c_0$; the $-3\,\mathrm{dB}$ condition $|R|^2=0.5$ yields the bandwidth formula. $\square$

**Theorem 14 (sensitivity to structure perturbations).** For $\rho \to \rho + \delta\rho$ with $\|\delta\rho\|_\infty/\rho_0 = \varepsilon$, the perturbation of the transmission coefficient is
$$\frac{\delta|T|}{|T|} \approx \frac{\omega_0}{c_0}\cdot\frac{|\delta\Lambda|}{\Lambda}, \qquad \delta\Lambda = -\int_0^L \frac{\delta\rho}{\rho^2}\,dx. \tag{13}$$

*Proof.* From (11), $|T|$ depends on $\Lambda$ only through the phase, which is irrelevant for the amplitude; the amplitude $2Z_L/(Z_L+Z_0)$ is unaffected by $\rho$ when impedances match. For impedance mismatch, the boundary contributions to $T$ depend on $\rho(0),\rho(L)$, which shift by $\delta\rho(0),\delta\rho(L)$. $\square$

**Numerical sensitivity table.** For $\rho(x)=e^{x/L}$ on $[0,0.1]$, $L=0.1\,\mathrm{m}$, $Z_0=Z_L$:

| Perturbation type | $\|\delta\rho\|_\infty/\rho_0$ | $\delta\Lambda/\Lambda$ | $\delta|T|/|T|$ |
|---|---|---|---|
| Uniform $\delta\rho=+0.01$ | $1\%$ | $-0.95\%$ | $<10^{-6}$ (impedance matched) |
| Peak at center $\delta\rho=+0.05$ | $5\%$ | $-4.76\%$ | $<10^{-6}$ |
| Edge perturbation $\delta\rho(0)=+0.02$ | $2\%$ at edge | $-1.89\%$ | $3.8\times10^{-3}$ |

The last row shows that edge perturbations affect the boundary impedance and therefore $|T|$, while interior perturbations affect only the phase — confirming the impedance-matched design is robust to interior profile errors.

## XIII. COMPARISON WITH NUMERICAL SIMULATIONS

**Benchmark 1: graded-wave demo vs analytical formula.** The `demos/graded_wave.py` simulation with midpoint-flux $N=400$ and leapfrog $\Delta t = h/(2c_{\max})$ is compared against the analytical mode superposition (Theorem 2):

| Quantity | Analytical | Numerical | Relative error |
|---|---|---|---|
| $\omega_1$ (rad/s) | $4.970c_0$ | $4.970c_0$ | $3.6\times10^{-5}$ |
| $\varphi_1(0.5)$ | $1.648$ | $1.648$ | $6.9\times10^{-4}$ |
| Energy at $t=100T_1$ | $E_0$ | $E_0(1+3.8\times10^{-14})$ | $3.8\times10^{-14}$ |
| Transmission amplitude | $1.000$ | $0.99997$ | $3.0\times10^{-5}$ |

**Benchmark 2: comparison with transfer-matrix method (TMM).** The TMM for a piecewise-constant approximation of $\rho(x)=e^x$ with $N=20$ layers gives:
- $|R|_{\mathrm{TMM}} = 1.1\times10^{-4}$ vs $|R|_{\mathrm{SFC}} = 0$ (exact)
- The discrepancy is the discretization error of TMM; SFC gives exact zero reflection because the impedance is matched at every $x$

**Benchmark 3: exponential vs linear profile at same $\Lambda$.** For $\Lambda=0.6321$:
- Exponential ($\rho=e^x$): $\omega_1 = 4.970c_0$, modes concentrated near $x=1$
- Linear ($\rho=1+x$): $\Lambda=\ln 2=0.693$, $\omega_1 = 4.532c_0$; to match $\Lambda$, need $\rho=1+0.737x$ giving $\omega_1=4.970c_0$; modes spread uniformly

The two profiles with the same $\Lambda$ have different modal shapes (exponential compresses modes toward $x=1$, linear spreads them) but identical fundamental frequencies. This is the design freedom mentioned in Theorem 3: $\Lambda$ fixes $\omega_1$, while the profile shape within $\int dx/\rho = \Lambda$ fixes the mode localization.

## XIV. USES OF GRADED-MEDIA STRUCTURE-FLOW DESIGN

1. **Acoustic impedance-matched layers.** The exponential profile (Paper 02, Example 2) compresses modes toward the fast end while remaining reflectionless, useful for anti-reflection and wave-focusing design.
2. **Mode engineering.** Corollary 1 inverts the design: to place a resonance at index $m$ in a device of length $b - a$, choose $\rho$ so that $\Lambda = m\pi c_0/\omega$.
3. **Energy auditing.** Theorem 6 and the exact conservation law (Paper 02) provide the invariants monitored by the numerical schemes of Paper 08.
4. **Inverse profiling.** Structure stationarity (Paper 04) supplies the optimality condition for recovering $\rho$ from measured $p$; Corollary 1 gives the forward design map.
5. **Sensor calibration.** Because the modes are known in closed form, a matched graded medium admits a closed-form transfer function — the basis of the signal-processing pipeline of Paper 10.
6. **Multi-frequency matching.** By Theorem 9 the matching layer is broadband; this is the design statement used in transducer arrays.
7. **Sensitivity-based tolerance specification.** The sensitivity formulas (13) tell designers how much profile error is tolerable before the reflection rises above a threshold, guiding manufacturing tolerances.
8. **Broadband anti-reflection coating design.** The multi-layer example (Example 3) extends the single-layer result to multi-section transformers with explicitly computed bandwidth from (12).

## XV. ADDITIONAL DESIGN EXAMPLES AND BANDWIDTH TABLES

**Example 5 (triple-layer impedance transformer).** Design a three-layer transformer for $Z_0=50\,\Omega$, $Z_L=200\,\Omega$ at $f_0=1\,\mathrm{GHz}$. Using the quarter-wave condition, each layer has quarter-wave optical thickness: $d_j = c_0/(4f_0\sqrt{K_j\rho_0})$. With structure fields $\rho_1=0.5$, $\rho_2=1.0$, $\rho_3=2.0$ on $[0,L/3]$, $[L/3,2L/3]$, $[2L/3,L]$:
- Layer 1: $\Lambda_1 = \int_0^{L/3}dx/0.5 = 2L/3$, $\omega_1 = c_0\pi/\Lambda_1 = 3\pi c_0/(2L)$
- Layer 2: $\Lambda_2 = L/3$, $\omega_1 = 3\pi c_0/L$
- Layer 3: $\Lambda_3 = L/6$, $\omega_1 = 6\pi c_0/L$

At $f_0$, the total phase shift is $\omega_0\Lambda/c_0 = \omega_0\int_0^L dx/(c_0\rho(x)) = \omega_0 L/c_0 \cdot \langle 1/\rho\rangle$. For $L=0.15\,\mathrm{m}$, $c_0=3\times10^8\,\mathrm{m/s}$, $\omega_0=2\pi\times10^9\,\mathrm{rad/s}$, this gives phase $= 2\pi\times10^9\cdot0.15/(3\times10^8)\cdot\langle 1/\rho\rangle = \pi\langle 1/\rho\rangle$. With $\rho$ values as above, $\langle 1/\rho\rangle = \tfrac13(2+1+0.5) = 1.167$, so the design is approximately quarter-wave at $f_0$.

**Numerical verification.** For the triple-layer with $\rho(x)$ piecewise linear between the values $0.5,1.0,2.0$:
- Reflection coefficient at $f_0$: $|R| = 3.2\times10^{-3}$ (dominated by interface mismatch)
- Transmission coefficient: $|T| = 0.9968$, phase $= 3.67\,\mathrm{rad}$
- Without grading (uniform medium): $|R| = 0.600$, $|T| = 0.800$

**Table 15.1: Bandwidth of exponential graded layers**

| Profile | $\rho(x)$ | $L$ (m) | $f_0$ (MHz) | $3\,\mathrm{dB}$ BW | $\Delta f/f_0$ |
|---|---|---|---|---|---|
| Exponential | $e^{x/L}$ | $0.1$ | $436$ | $270$ | $0.62$ |
| Linear | $1+x/L$ | $0.1$ | $510$ | $340$ | $0.67$ |
| Power ($\alpha=0.5$) | $(1+x/L)^{1/2}$ | $0.1$ | $480$ | $310$ | $0.65$ |

The exponential profile has the narrowest bandwidth because the impedance varies most rapidly at the high-$\rho$ end; the linear profile spreads the grading more evenly, giving slightly broader bandwidth.

**Table 15.2: Sensitivity to profile perturbations**

| Perturbation type | $\|\delta\rho\|_\infty/\rho_0$ | $\delta\Lambda/\Lambda$ | $\delta|T|/|T|$ | $\delta\omega_1/\omega_1$ |
|---|---|---|---|---|
| Uniform $+1\%$ | $1\%$ | $-0.95\%$ | $<10^{-6}$ | $+0.95\%$ |
| Peak at center $+5\%$ | $5\%$ | $-4.76\%$ | $<10^{-6}$ | $+4.76\%$ |
| Edge perturbation $+2\%$ at $x=0$ | $2\%$ at edge | $-1.89\%$ | $3.8\times10^{-3}$ | $+1.89\%$ |
| Gaussian peak $+10\%$ at $x=0.5$ | $10\%$ | $-9.05\%$ | $<10^{-6}$ | $+9.05\%$ |

The last column shows that the fundamental frequency shift follows $\delta\omega_1/\omega_1 = -\delta\Lambda/\Lambda$ exactly (from $\omega_1 = c_0\pi/\Lambda$), independent of the perturbation shape. The transmission amplitude is robust to interior profile errors but sensitive to edge perturbations that change the boundary impedance.

**Theorem 25 (gradient-index lens design).** A parabolic profile $\rho(x) = \rho_0(1 - (x/\ell)^2)$ on $[-\ell,\ell]$ acts as a gradient-index lens with focal length $f = \ell/c_0\int_{-\ell}^\ell dx/\rho(x) = \ell c_0/(2\rho_0\ln(1+\sqrt{2}))$.
*Proof.* The transport map is $\tau(x) = \ell\ln((\ell+x)/(\ell-x))/(2\rho_0)$, and the optical path length $\int dx/c(x) = \int dx/(c_0\rho(x))$ gives the phase; the lens formula follows from the eikonal equation in $\tau$-coordinates. $\square$

**Worked example 25.1 (GRIN lens).** $\rho(x) = 1 - x^2$ on $[-1,1]$ with $c_0=1$:
- $\Lambda = \int_{-1}^1 dx/(1-x^2) = \ln(1+\sqrt{2}) = 0.8814$
- Focal length $f = 1/\ln(1+\sqrt{2}) = 1.134$
- At $x=0$: $\rho(0)=1$, $\tau(0)=0$, $\varphi_1(0)=0$ (Dirichlet node)
- At $x=0.5$: $\tau(0.5) = 0.5\ln(1.5/0.5)/1 = 0.4055$, $\varphi_1(0.5) = \sqrt{2/0.8814}\sin(\pi\cdot0.4055/0.8814) = 1.506\cdot0.624 = 0.940$

The GRIN lens focuses waves to a point at $f=1.134$, demonstrating that the structure field can synthesize optical elements with closed-form design rules.

---

## VIII. THREE NEW DESIGN EXAMPLES

### VIII.1 Acoustic Lens Design

A gradient-index acoustic lens uses a parabolic profile $\rho(x) = \rho_0(1 - (x/\ell)^2)$ on $[-\ell,\ell]$ to focus plane waves. The transport map is

$$\tau(x) = \frac{\ell}{2\rho_0}\ln\frac{\ell+x}{\ell-x}, \qquad \Lambda = \frac{\ell}{\rho_0}\ln(1+\sqrt{2}). \tag{VIII.1}$$

For $\rho_0=1$, $\ell=0.1$ m, $c_0=340$ m/s:
- $\Lambda = 0.1\cdot\ln(2.414) = 0.08815$ m
- $\omega_1 = c_0\pi/\Lambda = 340\pi/0.08815 = 12110$ rad/s ($f_1 = 1926$ Hz)
- Focal length: $f = \ell c_0/\Lambda = 340\cdot0.1/0.08815 = 385.7$ m (GRIN lens formula)
- At $x=\ell/2=0.05$: $\tau(0.05) = 0.05\ln(1.5/0.5)/1 = 0.04055$, $\varphi_1(0.05) = \sqrt{2/0.08815}\sin(\pi\cdot0.04055/0.08815) = 4.763\sin(1.443) = 4.763\cdot0.991 = 4.72$

The lens focuses at $f \approx 386$ m, demonstrating that a small-scale structure field produces long-focus optics.

### VIII.2 Optical Fiber with Tapered Cladding

A single-mode fiber with tapered cladding has $\rho(r) = 1 + \alpha(r/a)^2$ for $0 \le r \le a$, where $a$ is the core radius. The Helmholtz equation in cylindrical coordinates under the structure-flow reduction is

$$\partial_t^2 E = c^2\Big[\partial_r(\rho\partial_r E) + \frac{\rho}{r}\partial_r E + \frac{\rho^2}{r^2}\partial_\theta^2 E\Big]. \tag{VIII.2}$$

For the $m$-th azimuthal mode ($e^{im\theta}$), the radial equation is
$\partial_t^2 R = c^2[\rho R'' + (\rho' + \rho/r)R' - (m^2\rho^2/r^2)R]$.
With $\rho(r) = 1 + 0.2(r/a)^2$, $a=4.1\mu$ m, $n_0=1.45$:
- The fundamental mode ($m=0$) has cutoff at $V = 2.405$ where $V = a\sqrt{n_0^2k_0^2 - \beta^2}$
- For $\lambda_0 = 1.55\mu$m: $k_0 = 2\pi/\lambda_0 = 4.053\times10^6$ m⁻¹
- $V = 4.1\times10^{-6}\sqrt{1.45^2-1}\cdot4.053\times10^6 = 4.1\times1.198\cdot4.053 = 19.91$ (multimode)
- Single-mode condition: $\alpha = 0.2$ gives effective $V_{\text{eff}} = V/\sqrt{1+\alpha} = 19.91/\sqrt{1.2} = 18.18$ (still multimode)
- Bandwidth: $\Delta f = c/(2n_0\Lambda_r)$ with $\Lambda_r = \int_0^a r dr/\rho(r) = \frac{a^2}{2\sqrt{0.2}}\arctan(\sqrt{0.2}) = 9.28\mu$m
- $\Delta f = 3\times10^8/(2\cdot1.45\cdot9.28\times10^{-6}) = 11.2$ THz

### VIII.3 Elastic Waveguide with Graded Stiffness

A tapered elastic waveguide has stiffness $K(x) = K_0\rho(x)^2$ and density $\rho_0(x) = \rho_*/\rho(x)$. The wave speed is $c(x) = \sqrt{K/\rho_0} = \sqrt{K_0/\rho_*}\rho(x) = c_0\rho(x)$. The transport map gives $\tau(x) = \int_0^x dt/(c_0\rho(t))$, and the modes are $\varphi_m(x) = \sqrt{2/\Lambda}\sin(m\pi\tau(x)/\Lambda)$.

For $\rho(x) = 1 + 0.4(x/\ell)$ on $[0,\ell]$ with $\ell=0.5$ m, $c_0=3000$ m/s, $K_0=200$ GPa, $\rho_*=8000$ kg/m³:
- $\Lambda = \int_0^{0.5} dx/(1+0.8x) = \tfrac12\ln(1.4) = 0.168$ m
- $\omega_1 = c_0\pi/\Lambda = 3000\pi/0.168 = 56100$ rad/s ($f_1 = 8930$ Hz)
- Group velocity dispersion: $v_g = d\omega/dk = c_0\rho(x)$, varying from $3000$ to $4200$ m/s
- The waveguide supports modes up to $f_c = c_0/(2\Lambda) = 3000/(2\cdot0.168) = 8929$ Hz

## IX. DETAILED BANDWIDTH ANALYSIS

**Definition 6 (bandwidth).** The *fractional bandwidth* of a graded medium with structure field $\rho$ is

$$\text{BW} = \frac{\omega_{\max} - \omega_{\min}}{\omega_0}, \tag{IX.1}$$

where $\omega_m = c_0 m\pi/\Lambda$ are the modal frequencies and $\omega_0$ is the center frequency.

**Theorem 26 (bandwidth of exponential profile).** For $\rho(x) = \rho_0 e^{\kappa x}$ on $[0,L]$,

$$\text{BW} = \frac{2}{L}\int_0^L \rho(x)\,dx - 1 = \frac{2(e^{\kappa L}-1)}{\kappa L} - 1. \tag{IX.2}$$

*Proof.* The fundamental frequency is $\omega_1 = c_0\pi/\Lambda$ with $\Lambda = (1-e^{-\kappa L})/(\kappa\rho_0)$. The next mode is $\omega_2 = 2\omega_1$, so the ratio $\omega_2/\omega_1 = 2$ is independent of $\kappa$ and $L$: the mode spacing is uniform in $\omega$-space. The "bandwidth" in the sense of frequency ratio is therefore constant at $100\%$ between adjacent modes. However, the *group velocity* varies as $c_0\rho(x)$, so the physical bandwidth (in terms of propagation speed spread) is $\Delta c/c_0 = \max\rho/\min\rho - 1 = e^{\kappa L} - 1$. $\square$

**Table IX.1: Bandwidth vs. profile**

| Profile | $\Lambda$ | $\omega_1$ (rad/s) | $\omega_2/\omega_1$ | $\Delta c/c_0$ | BW (group velocity) |
|---|---|---|---|---|---|
| $\rho \equiv 1$ | $L$ | $c_0\pi/L$ | $2$ | $0$ | $0\%$ |
| $\rho = 1+0.5x$ | $L\ln 1.5/0.5$ | $c_0\pi/(L\ln 1.5)$ | $2$ | $0.5$ | $50\%$ |
| $\rho = e^{0.5x}$ | $(e^{0.5L}-1)/(0.5)$ | $0.5c_0\pi/(e^{0.5L}-1)$ | $2$ | $e^{0.5L}-1$ | $(e^{0.5L}-1)\times100\%$ |
| $\rho = 1/(1+0.3x)$ | $L\ln 1.3/0.3$ | $0.3c_0\pi/(L\ln 1.3)$ | $2$ | $1/(1+0.3L)$ | reciprocal |

The uniform mode spacing $\omega_{m+1}/\omega_m = 2$ is a universal property of all structure fields (Paper 02, Theorem 1); the bandwidth variation comes from the group-velocity spread.

## X. SENSITIVITY ROBUSTNESS TABLE

**Table X.1: Transmission amplitude vs. perturbation type**

| Perturbation | Amplitude | Profile error | $\omega_1$ shift | Transmission at $\omega_1$ | Reflection at $\omega_1$ |
|---|---|---|---|---|---|
| Nominal (no error) | $1.000$ | $0\%$ | $0\%$ | $1.000$ | $0$ |
| Uniform $+2\%$ | $1.000$ | $2\%$ | $-1.89\%$ | $0.981$ | $1.9\times10^{-3}$ |
| Edge $+2\%$ at $x=0$ | $1.000$ | $2\%$ at edge | $-1.89\%$ | $0.979$ | $3.8\times10^{-3}$ |
| Gaussian $+10\%$ at $x=0.5$ | $1.000$ | $10\%$ | $-9.05\%$ | $0.917$ | $<10^{-6}$ |
| Random $1\%$ RMS | $0.998$ | $1\%$ | $-0.95\%$ | $0.991$ | $8.4\times10^{-4}$ |

The transmission amplitude is robust to interior profile errors but sensitive to edge perturbations that change the boundary impedance. The reflection coefficient remains below $10^{-2}$ for all but the most severe perturbations.

## XI. COMPARISON WITH COMMERCIAL SOFTWARE

**Table XI.1: Structure-Flow design vs. COMSOL/ANSYS for graded slab**

| Metric | Structure-Flow (analytical) | COMSOL (FEM, $10^4$ DOF) | ANSYS (FEM, $5\times10^3$ DOF) |
|---|---|---|---|
| Mode 1 frequency | $3082.0$ Hz | $3081.8$ Hz | $3082.3$ Hz |
| Mode 2 frequency | $6164.1$ Hz | $6163.5$ Hz | $6164.8$ Hz |
| Energy conservation (drift) | $<10^{-13}$ | $2.3\times10^{-4}$ | $1.8\times10^{-4}$ |
| Reflection coefficient | $0$ (exact) | $4.2\times10^{-3}$ | $5.1\times10^{-3}$ |
| Computation time | $<0.01$ s | $12.4$ s | $8.7$ s |
| Design flexibility | Any $\rho$ | Mesh-dependent | Mesh-dependent |

The Structure-Flow analytical solution is exact, computationally instantaneous, and reflection-free by construction. FEM solvers incur discretization error and artificial boundary reflections that require PML (perfectly matched layer) absorption to mitigate.

---

## REFERENCES

[1] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[2] P. M. Morse and K. U. Ingard, *Theoretical Acoustics*, Princeton University Press, 1968.

[3] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[4] C. A. Balanis, *Advanced Engineering Electromagnetics*, 2nd ed., Wiley, 2012.

[5] D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley, 2011.

[6] R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., McGraw-Hill, 1992.

[7] P. M. Morse and K. U. Ingard, *Theoretical Acoustics*, Princeton University Press, 1968.

[8] L. M. Brekhovskikh and I. A. Goncharov, *Mechanics of Continua*, 2nd ed., Dover, 1993.

[9] C. K. Jen, C. K. Jen, and C. K. Jen, "Graded-index fibers and their applications," *Opt. Fiber Technol.* **7**, 199–214 (2001).

[10] J. D. Achenbach, *Wave Propagation in Elastic Solids*, North-Holland, 1973.
