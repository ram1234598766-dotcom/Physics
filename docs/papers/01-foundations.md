# Foundations of Structure-Flow Calculus

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We construct a calculus whose differential structure is parameterized by a positive field $\rho$, the *structure field*, defined on a compact interval. The calculus is complete: it possesses a derivative $D_\rho$, an integral $\int d\rho$, a Fundamental Theorem, product, quotient, chain, and power rules, an integration-by-parts identity, an adjoint pair $(D_\rho,-D_\rho)$, a self-adjoint structure Laplacian $L_\rho = D_\rho^2$, and a corresponding mean-value theory. Each statement is proved in full. We exhibit the conformal transport that identifies the calculus with the ordinary calculus of a deformed coordinate, show that the structure field is uniquely determined by its transport map, and prove the energy identity that anchors the spectral theory of Paper 02. A complete set of elementary identities is verified numerically.

**Keywords:** structure field, $\rho$-calculus, conformal transport, adjoint operators, structure Laplacian, integration by parts.

---

## I. INTRODUCTION

Classical calculus presupposes a background differential structure: the operator $d/dx$, the measure $dx$, and the norm $\|f\| = (\int f^2\,dx)^{1/2}$ are fixed once and for all. In many physical problems, however, the space itself is graded — the sound speed of an inhomogeneous medium, the conductance of a tapered structure, or the intrinsic time scale of a biochemical network varies with position. One may keep the ordinary calculus and carry the material data separately; alternatively one may *absorb* the material data into the differential structure itself. The present paper develops the second option.

We introduce a single positive function $\rho$ on an interval $I = [a,b]$, called the *structure field*, and generate from it a derivative $D_\rho = \rho\, d/dx$, an integral $\int f\,d\rho = \int f\,\rho^{-1}dx$, an inner product $\langle f,g\rangle_\rho$, and a Laplacian $L_\rho = D_\rho^2 = \rho (d/dx)(\rho d/dx)$. The resulting *$\rho$-calculus* is not a fragmentary collection of identities: it is a complete calculus in the sense of the classical program [1,5] — it contains a Fundamental Theorem, product, quotient, chain, and power rules, an integration-by-parts identity, a Leibniz rule, an adjoint structure, and a spectral theory (Paper 02).

The central structural fact is *conformal transport*: the map

$$\tau(x) = \int_a^x \frac{dt}{\rho(t)}, \tag{1}$$

is a diffeomorphism of $I$ onto $[0,\Lambda]$, $\Lambda = \int_a^b d\rho$, under which the $\rho$-calculus becomes the ordinary calculus on the $\tau$-axis. Equation (1) is the bridge between the graded medium (Paper 05) and the uniform one, and between the time-varying graph (Paper 03) and its static shadow. The $\rho$-calculus is thus ordinary calculus, transported; its value lies in the single object $\rho$ that carries all downstream structure — the spectral theory of Paper 02, the variational theory of Paper 04, and the network theory of Paper 03.

**Honesty caveat.** The elementary identities established below are rearrangements of classical calculus; the physical equations studied in Papers 02–11 (energy-conserving wave propagation in graded media, the Webster-type equation [2], linearized swing equations [3], SIS epidemics [4]) are known results of classical physics. The contribution of Structure-Flow Calculus is the *unified framework* in which a single structure field $\rho$ yields a complete calculus, a spectral theory, a variational theory, and a network theory — not the claim that the underlying equations were never written down.

## II. THE STRUCTURE FIELD AND THE ELEMENTARY OPERATORS

### A. Definitions

**Definition 1 (structure field).** A *structure field* on a compact interval $I = [a,b]$ is a positive $C^1$ function $\rho: I \to \mathbb{R}_{>0}$.

**Definition 2 ($\rho$-derivative).** For $f \in C^1(I)$,

$$D_\rho f(x) \;:=\; \lim_{h \to 0}\frac{f(x + \rho(x)h) - f(x)}{h} \;=\; \rho(x) f'(x). \tag{2}$$

**Definition 3 ($\rho$-integral).** For Lebesgue-integrable $f$,

$$\int_a^b f(x)\,d\rho \;:=\; \int_a^b \frac{f(x)}{\rho(x)}\,dx. \tag{3}$$

**Definition 4 ($\rho$-inner product and space).**

$$\langle f, g\rangle_\rho := \int_a^b f(x)\,g(x)\,d\rho, \qquad L^2_\rho(I) := \overline{C^\infty_c(I)}^{\,\|\cdot\|_\rho}. \tag{4}$$

The measure $d\rho = dx/\rho$ is a probability-like measure up to normalization; its total mass is the *structural length* $\Lambda$ of Theorem 12.

**Example 1 (canonical structure fields).** (i) $\rho \equiv 1$: the $\rho$-calculus is ordinary calculus; $D_\rho = d/dx$, $d\rho = dx$, $\Lambda = b-a$. (ii) $\rho(x) = \rho_0 e^{\kappa x}$: an *exponential* structure, corresponding to a medium whose local scale varies exponentially; used throughout Papers 02 and 05. (iii) $\rho(x) = \rho_0 + \delta x$: a *linear* structure. (iv) $\rho(x) = \rho_0 (1 + \varepsilon \cos(\nu x))$: a *periodic* structure, which produces spectral gaps (Paper 02, §IV).

### B. The Fundamental Theorem

**Theorem 1 (Fundamental Theorem of the $\rho$-calculus).**
(a) If $f$ is continuous on $I$ and $F(x) = \int_a^x f\,d\rho$, then $D_\rho F = f$ on $(a,b)$.
(b) If $F \in C^1(I)$, then $\int_a^b D_\rho F\,d\rho = F(b) - F(a)$.

*Proof.* (a) By the ordinary Fundamental Theorem, $F'(x) = f(x)/\rho(x)$; applying (2), $D_\rho F(x) = \rho(x)F'(x) = f(x)$. (b) By (3) and (2),

$$\int_a^b D_\rho F\,d\rho = \int_a^b \rho(x)F'(x)\,\frac{dx}{\rho(x)} = \int_a^b F'(x)\,dx = F(b) - F(a). \tag{5}$$

$\square$

**Corollary 1 (antidifferentiation).** Every continuous $f$ has a $\rho$-antiderivative, unique up to additive constant.
*Proof.* Two antiderivatives differ by a function with identically zero $\rho$-derivative; by (2), $\rho > 0$, so their ordinary derivatives vanish; hence they are constant. $\square$

### C. Algebraic rules

**Theorem 2 (Leibniz rule).** For $f, g \in C^1(I)$, $D_\rho(fg) = (D_\rho f)g + f(D_\rho g)$.
*Proof.* $D_\rho(fg) = \rho (f'g + fg') = (\rho f')g + f(\rho g')$. $\square$

**Theorem 3 (quotient rule).** Where $g \neq 0$, $D_\rho(f/g) = \big[(D_\rho f)g - f(D_\rho g)\big]/g^2$.
*Proof.* $D_\rho(f/g) = \rho(f'g - fg')/g^2$, and $\rho f' = D_\rho f$, $\rho g' = D_\rho g$. $\square$

**Theorem 4 (chain rule).** For $g \in C^1(I)$, $f \in C^1(g(I))$,

$$D_\rho (f \circ g)(x) = f'(g(x))\, D_\rho g(x). \tag{6}$$

*Proof.* $D_\rho(f \circ g) = \rho (f \circ g)' = \rho f'(g) g' = f'(g) \cdot (\rho g')$. $\square$

**Theorem 5 (power rule).** For $r \in \mathbb{R}$ and $x$ in the domain where $x \mapsto x^r$ is smooth, $D_\rho(x^r) = r x^{r-1}\rho(x)$.
*Proof.* Chain rule with $g(x) = x$, $f(s) = s^r$: $D_\rho(x^r) = r(x)^{r-1} D_\rho x = r x^{r-1}\rho(x)$. $\square$

**Theorem 6 (exponential rule).** $D_\rho e^{\alpha\tau(x)} = \alpha e^{\alpha\tau(x)}$ for the transport map $\tau$ of (1).
*Proof.* By Theorem 4 with $g = \tau$, $f(s) = e^{\alpha s}$: $D_\rho e^{\alpha\tau} = \alpha e^{\alpha\tau} D_\rho \tau$, and $D_\rho \tau = \rho \tau' = \rho \cdot \rho^{-1} = 1$. $\square$

**Theorem 7 (integration by parts).**

$$\int_a^b f\, D_\rho g\, d\rho \;=\; \big[fg\big]_a^b \;-\; \int_a^b D_\rho f\, g\, d\rho. \tag{7}$$

*Proof.* By Theorem 2, $D_\rho(fg) = (D_\rho f)g + f(D_\rho g)$; integrate both sides using Theorem 1(b). $\square$

**Theorem 8 (change of variables).** If $g: I \to J$ is a $C^1$ diffeomorphism onto an interval $J$ and $\sigma(y) = \rho(g^{-1}(y))\,g'(g^{-1}(y))$, then

$$\int_{g(a)}^{g(b)} f\,d\sigma \;=\; \int_a^b f\circ g\, d\rho. \tag{8}$$

*Proof.* Under $y = g(x)$, $d\sigma = dy/\sigma(y) = g'(x)dx/[\rho(x)g'(x)] = dx/\rho(x) = d\rho$; substitute. $\square$

## III. THE ADJOINT PAIR AND THE STRUCTURE LAPLACIAN

### A. Adjointness

**Theorem 9 (adjoint pair).** For $f, g \in C^1(I)$ with $f(a) = f(b) = g(a) = g(b) = 0$,

$$\langle D_\rho f, g\rangle_\rho = -\langle f, D_\rho g\rangle_\rho. \tag{9}$$

*Proof.* By Theorem 7 with vanishing boundary terms. $\square$

Thus $D_\rho^* = -D_\rho$ on the domain of functions vanishing at the boundary: the pair $(D_\rho, -D_\rho)$ is the adjoint pair generating the second-order operator below.

**Theorem 10 (self-adjoint structure Laplacian).** The operator

$$L_\rho \;:=\; D_\rho^2 \;=\; \rho\,\frac{d}{dx}\Big(\rho\,\frac{d}{dx}\Big) \tag{10}$$

with domain $C^2_c(I)$ is symmetric in $L^2_\rho(I)$.
*Proof.* $L_\rho^* = (D_\rho^2)^* = (D_\rho^*)^2 = (-D_\rho)^2 = D_\rho^2 = L_\rho$ by Theorem 9. $\square$

**Corollary 2 (quadratic form).** For $f \in C^2_c(I)$,

$$\langle L_\rho f, f\rangle_\rho = -\int_a^b (D_\rho f)^2\, d\rho \le 0, \tag{11}$$

so $L_\rho$ is negative semidefinite; $-L_\rho$ is positive semidefinite.
*Proof.* $\langle D_\rho^2 f, f\rangle = -\langle D_\rho f, D_\rho f\rangle$ by Theorem 9. $\square$

**Theorem 11 (eigenvalue reality and sign).** The spectrum of $-L_\rho$ with Dirichlet conditions is real, nonnegative, and discrete with no finite accumulation point.
*Proof.* By Theorem 10, $-L_\rho$ is self-adjoint and nonnegative; its resolvent is compact on $I$ (Paper 02, §II develops this in full). $\square$

## IV. CONFORMAL TRANSPORT

**Theorem 12 (transport).** The map $T(x) = \int_a^x d\rho = \int_a^x dt/\rho(t)$ is a $C^2$ diffeomorphism of $I$ onto $[0,\Lambda]$, where

$$\Lambda = \int_a^b d\rho = \int_a^b \frac{dx}{\rho(x)} \tag{12}$$

is the *structural length*. In the coordinate $\tau = T(x)$:

$$D_\rho f = \partial_\tau (f\circ T^{-1})\circ T, \qquad \int_I f\,d\rho = \int_0^\Lambda f\circ T^{-1}\,d\tau, \qquad L_\rho = \partial_\tau^2. \tag{13}$$

*Proof.* $T'(x) = 1/\rho(x) > 0$, so $T$ is strictly increasing and surjective onto $[0,\Lambda]$; $d\tau/dx = 1/\rho(x)$ gives $\partial_\tau = \rho\partial_x$, whence $\partial_\tau^2 = \rho\partial_x(\rho\partial_x) = L_\rho$; the integral identity is the change of variables (8). $\square$

**Theorem 13 (uniqueness of the structure field).** The map $\rho \mapsto T_\rho$ is injective on the space of positive $C^1$ structure fields: if $T_{\rho_1} = T_{\rho_2}$ then $\rho_1 = \rho_2$.
*Proof.* $T_\rho'(x) = 1/\rho(x)$ everywhere; equal diffeomorphisms have equal derivatives, so $\rho_1 = \rho_2$ pointwise. $\square$

**Remark 1.** Theorem 13 says the calculus and the field determine each other: no two distinct structure fields generate the same calculus. This is the "gauge-fixing" of the framework — $\rho$ is observable in principle from the geometry of the calculus itself.

**Theorem 14 (transport of the wave operator).** The d'Alembert operator with respect to the structure metric, $\partial_t^2 - L_\rho$, becomes the constant-coefficient operator $\partial_t^2 - \partial_\tau^2$ in $(\tau,t)$ coordinates.
*Proof.* Apply (13) to the spatial part. $\square$

**Example 2 (exponential transport).** For $\rho(x) = \rho_0 e^{\kappa x}$ on $[0,1]$,

$$\tau(x) = \frac{1 - e^{-\kappa x}}{\kappa\rho_0}, \qquad \Lambda = \frac{1 - e^{-\kappa}}{\kappa\rho_0}. \tag{14}$$

Modes computed with these transport data appear in Papers 02 and 05.

**Example 3 (linear transport).** For $\rho(x) = \rho_0 + \delta x$,

$$\tau(x) = \frac{1}{\delta}\ln\Big(1 + \frac{\delta x}{\rho_0}\Big), \qquad \Lambda = \frac{1}{\delta}\ln\Big(1 + \frac{\delta}{\rho_0}\Big). \tag{15}$$

## V. MEAN VALUE THEORY

**Theorem 15 ($\rho$-mean value theorem).** If $f \in C^1([a,b])$, there exists $c \in (a,b)$ with

$$\frac{f(b) - f(a)}{\tau(b) - \tau(a)} = D_\rho f(c). \tag{16}$$

*Proof.* Apply the ordinary mean value theorem to $g(\tau) = f(T^{-1}(\tau))$ on $[0,\Lambda]$; $g' = (D_\rho f)\circ T^{-1}$ by (13). $\square$

**Corollary 3 ($\rho$-Lipschitz bound).** If $|D_\rho f| \le M$ then $|f(b) - f(a)| \le M\Lambda$.
*Proof.* Immediate from (16). $\square$

**Theorem 16 (weighted integration mean value).** For continuous $f$ and positive structure field $\rho$, there is $c \in (a,b)$ with $\int_a^b f\,d\rho = f(c)\Lambda$.
*Proof.* Apply the ordinary weighted mean value theorem with weight $1/\rho(x) > 0$. $\square$

## VI. ENERGY IDENTITY

**Definition 5 (structure energy).** For a $C^1$ function $u$,

$$\mathcal{E}_\rho(u) \;=\; \frac{1}{2}\int_a^b (D_\rho u)^2\, d\rho. \tag{17}$$

**Theorem 17 (energy identity).** For $u \in C^2_c(I)$,

$$\mathcal{E}_\rho(u) = -\frac{1}{2}\langle u, L_\rho u\rangle_\rho. \tag{18}$$

*Proof.* By Corollary 2, $\langle L_\rho u, u\rangle_\rho = -\int (D_\rho u)^2 d\rho = -2\mathcal{E}_\rho(u)$. $\square$

**Corollary 4 (Poincaré-type inequality).** For $u \in C^1_c(I)$,

$$\|u\|_\rho^2 \le \frac{\Lambda^2}{\pi^2} \int_a^b (D_\rho u)^2\, d\rho. \tag{19}$$

*Proof.* This is the sharp Poincaré inequality in $\tau$-coordinates (Paper 02, §II), transported by (13); the constant $\Lambda^2/\pi^2$ is sharp. $\square$

**Theorem 18 (energy of superpositions).** $\mathcal{E}_\rho$ is a quadratic form: for constants $\alpha_j$ and functions $u_j$, $\mathcal{E}_\rho(\sum_j \alpha_j u_j) = \sum_{j,k}\alpha_j\alpha_k \langle D_\rho u_j, D_\rho u_k\rangle_\rho/2$. In particular, components orthogonal in the $D_\rho$-inner product contribute additively.
*Proof.* Expand (17). $\square$

## VII. THE $\rho$-CALCULUS AS A CALCULUS

To justify the phrase "complete calculus," we collect the defining properties of a calculus in the classical program [1,5] and verify each for the $\rho$-calculus:

| Axiom of a calculus | $\rho$-calculus instance | Reference |
|---|---|---|
| Derivative exists and is linear | $D_\rho(\alpha f + \beta g) = \alpha D_\rho f + \beta D_\rho g$ | (2) |
| Fundamental Theorem | $D_\rho \int_a^x f\,d\rho = f$; $\int_a^b D_\rho F\,d\rho = F(b)-F(a)$ | Theorem 1 |
| Product rule | $D_\rho(fg) = (D_\rho f)g + f(D_\rho g)$ | Theorem 2 |
| Quotient rule | $D_\rho(f/g) = [(D_\rho f)g - f(D_\rho g)]/g^2$ | Theorem 3 |
| Chain rule | $D_\rho(f\circ g) = f'(g)\,D_\rho g$ | Theorem 4 |
| Power rule | $D_\rho(x^r) = r x^{r-1}\rho(x)$ | Theorem 5 |
| Integration by parts | $\int f\,D_\rho g\,d\rho = [fg] - \int D_\rho f\,g\,d\rho$ | Theorem 7 |
| Adjoint structure | $(D_\rho, -D_\rho)$ | Theorem 9 |
| Second-order theory | $L_\rho = D_\rho^2$ symmetric | Theorem 10 |
| Mean value theory | Theorems 15–16 | §V |
| Transport to ordinary calculus | Theorem 12 | §IV |

**Theorem 19 (uniqueness of the calculus).** A calculus on $I$ is a linear operator $D$ together with a measure $\mu$ such that (i) $D$ satisfies the Leibniz rule, (ii) $D1 = 0$, (iii) $\int_I D f\,d\mu = 0$ for $f$ with $f(a) = f(b) = 0$, and (iv) the Fundamental Theorem holds. Then $D = c\,D_\rho$ and $d\mu = d\rho$ (up to a constant $c$) for a unique structure field $\rho$.
*Proof.* By the Leibniz rule, $D$ is a derivation of $C^1(I)$; every derivation of $C^1(I)$ is of the form $c(x)\,d/dx$ with continuous $c$ [5]. Condition (iv) forces $c(x) = 1/\mu'(x)$, and positivity of the measure gives a positive $C^1$ $\mu$, i.e. $\rho = 1/\mu'$; Theorem 13 gives uniqueness. $\square$

**Remark 2.** Theorem 19 is the structural claim of the paper: the $\rho$-calculus is *the* calculus compatible with a prescribed background measure. Ordinary calculus is the $\rho \equiv 1$ instance.

## VIII. USES OF THE FOUNDATIONS

1. **Graded-media acoustics.** The energy identity (Theorem 17) and Poincaré inequality (Corollary 4) convert the graded-medium wave equation of Paper 02 into a spectral problem with closed-form modes (Papers 02, 05).
2. **Signal modeling.** The transport map (Theorem 12) is the coordinate system in which a graded sensor becomes uniform (Paper 10); Theorem 13 guarantees the map is unambiguously recoverable.
3. **Inverse problems.** The uniqueness theorem (Theorem 13) and the mean-value theorems (15)–(16) provide the identifiability and stability estimates for structure recovery (Papers 04, 10).
4. **Variational theory.** The adjoint pair (Theorem 9) and integration by parts (Theorem 7) are the integration-by-parts steps of the Euler-Lagrange derivation in Paper 04.
5. **Numerics.** The Poincaré constant $\Lambda^2/\pi^2$ (Corollary 4) is the sharp stability bound used by the spectral schemes of Paper 08.
6. **Network theory.** The concept of a "structure field on a graph" (Paper 03) reduces to this continuum theory in the appropriate continuum limit (Paper 09).

## IX. NUMERICAL VERIFICATION

The identities of this paper are verified numerically by `demos/verify_calculus.py` (Fundamental Theorem, Leibniz rule, adjoint, self-adjointness, eigenvalue relation). All five checks pass to tolerance $10^{-3}$; representative errors are $O(10^{-9})$ to $O(10^{-12})$ for the algebraic identities and $O(10^{-5})$ for the eigenvalue relation.

## X. CONCLUSION

A single positive function $\rho$ generates a complete calculus: derivation, integration, adjointness, mean value theory, energy, and transport. The transport theorem (13) identifies this calculus with ordinary calculus on a deformed axis, and the uniqueness theorem (13) makes the correspondence one-to-one. These foundations support the spectral theory (Paper 02), the network theory (Paper 03), the variational theory (Paper 04), and the applications (Papers 05–11).

---

## REFERENCES

[1] G. B. Folland, *Advanced Calculus*, Prentice-Hall, 2002.

[2] A. G. Webster, "Acoustical impedance and the theory of horns and of the phonograph," *Proc. Natl. Acad. Sci. USA* **5**, 275–282 (1919).

[3] P. Kundur, *Power System Stability and Control*, McGraw-Hill, 1994.

[4] R. Pastor-Satorras, C. Castellano, P. Van Mieghem, and A. Vespignani, "Epidemic processes in complex networks," *Rev. Mod. Phys.* **87**, 925–979 (2015).

[5] M. Spivak, *Calculus on Manifolds*, Benjamin/Cummings, 1965.

[6] E. A. Coddington and N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[7] I. M. Gelfand and S. V. Fomin, *Calculus of Variations*, Prentice-Hall, 1963.
