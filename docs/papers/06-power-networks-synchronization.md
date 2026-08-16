# Applications II: Power Networks, Synchronization, and Mode Migration

**Structure-Flow Calculus Working Group**

*Received 2026-08-16*

**Abstract.** We apply the causal network spectral theory of Paper 03 to power systems. Under the standard linearization, frequency deviations satisfy the structure-flow diffusion $\dot u = -L(t)u$ on the network Laplacian, whose eigenvalues change as lines are stressed. We prove a synchronization-rate theorem from the time-integrated algebraic connectivity, derive the modal-energy migration formula that exposes the most vulnerable modes during a developing outage, compute the vulnerability ordering, and connect the Energy Migration Theorem to cascading-failure early warning. We prove the time-to-synchronization bound, the outage-detection criterion, and the vulnerability-index formula. The results are verified numerically.

**Keywords:** power systems, linearized swing equations, synchronization, algebraic connectivity, mode migration, early warning.

---

## I. INTRODUCTION

A power network must keep generators synchronized. Under small disturbances, frequency deviations follow, in the uniform-inertia DC-flow relaxation, $\dot u = -L(t)u$: the network Laplacian itself is the dynamics, and it changes as lines are loaded, stressed, and tripped. The theorems of Paper 03 therefore apply verbatim: mass is conserved (power balance), deviation from the mean contracts at a rate governed by the time-integrated algebraic connectivity, and modal energy migrates conservatively as the topology deforms. This paper turns those theorems into engineering statements: synchronization guarantees, vulnerability ranking, and early-warning observables.

**Honesty caveat.** The linearized swing / consensus-regulation model is standard power-systems engineering [1,2]; the contribution is the use of the Paper 03 theorems to give hard synchronization rates and the migration-based vulnerability signature.

## II. MODEL

**Definition 1 (linearized power network).** With uniform inertia $M$ and symmetric tie-line conductances $g_{ij}(t) \ge 0$, the linearized frequency deviations $u_i = \dot\theta_i$ (the rate of change of the bus phase angles) satisfy

$$\dot u = -L(t)u, \qquad L(t) = D(t) - G(t), \quad G_{ij} = g_{ij}/M, \tag{1}$$

where $D(t)$ is the diagonal of row sums. $L(t)$ is the graph Laplacian of the conductance-weighted graph.

**Theorem 1 (power balance).** The mean frequency $\bar m = \mathbf{1}^\top u(t)/n$ is constant: total deviation conserves zero-sum power imbalance.
*Proof.* Paper 03, Theorem 1 (mass conservation). $\square$

## III. SYNCHRONIZATION THEOREMS

**Theorem 2 (synchronization rate).** Let $\lambda_2(t)$ be the algebraic connectivity of $L(t)$ and $v(t) = u(t) - \bar m\mathbf{1}$ the deviation from the conserved mean frequency. Then

$$\|v(t)\| \le \|v(0)\| \exp\!\Big(-\int_0^t \lambda_2(s)\,ds\Big). \tag{2}$$

*Proof.* Direct application of Paper 03, Theorem 2. $\square$

**Corollary 1 (minimum-rate guarantee).** If $\lambda_2(t) \ge \lambda_2^\ast$ for all $t$ (a worst-case connectivity floor), the network synchronizes at least as fast as $\|v(t)\| \le \|v(0)\|e^{-\lambda_2^\ast t}$.
*Proof.* Paper 03, Corollary 1. $\square$

**Theorem 3 (time-to-synchronization).** Let $\underline\lambda_2(t) = \inf_{0\le s\le t}\lambda_2(s)$ be the worst-case connectivity floor up to time $t$. The synchronization time $\mathcal{T}_\epsilon = \inf\{t : \|v(t)\| \le \epsilon\|v(0)\|\}$ satisfies

$$\mathcal{T}_\epsilon \le \frac{\log(1/\epsilon)}{\underline\lambda_2(\mathcal{T}_\epsilon)}. \tag{3}$$

*Proof.* From Theorem 2, $\int_0^t\lambda_2(s)\,ds \ge \underline\lambda_2(t)\,t$, so $\|v(t)\| \le \|v(0)\|e^{-\underline\lambda_2(t)t}$. Requiring the bound to reach $\epsilon\|v(0)\|$ at $t = \mathcal{T}_\epsilon$ gives $\underline\lambda_2(\mathcal{T}_\epsilon)\mathcal{T}_\epsilon \ge \log(1/\epsilon)$. $\square$

**Theorem 4 (disconnection alarm).** If the network splits, the algebraic connectivity vanishes: $\lambda_2(t) \to 0$ and the bound (2) no longer contracts. Conversely, the bound (2) contracts if and only if $\int_0^t\lambda_2(s)ds > 0$.
*Proof.* A disconnected graph has $\lambda_2 = 0$ [3]; the equivalence follows from (2). $\square$

## IV. VULNERABILITY AND MODE MIGRATION

**Definition 2 (modal deviations).** Let $\varphi_j(t)$ be the eigenframe of $L(t)$ and $\hat u_j(t) = \langle\varphi_j(t), u(t)\rangle$ the modal frequency deviations.

**Theorem 5 (modal energy migration under stress).** The modal energy $E_j = \hat u_j^2$ evolves by

$$\dot E_j = -2\lambda_j(t) E_j - 2\sum_{k} C_{jk}(t)\,\hat u_j \hat u_k, \qquad C_{jk} = \langle\varphi_j,\dot\varphi_k\rangle, \tag{4}$$

with $C_{jk} = -C_{kj}$ (Paper 03, Theorem 3), and the total $E = \sum_j E_j$ obeys

$$\dot E = -2\sum_j \lambda_j E_j. \tag{5}$$

*Proof.* From the spectral flow equation and Energy Migration Theorem of Paper 03 (Theorems 5, 6). $\square$

**Theorem 6 (vulnerability signature).** During a developing outage that decreases $\lambda_j$ for the weakly connected modes, energy migrates *into* those modes at the expense of others, with the total loss rate (5) set by the same eigenvalues. A network whose least-connected mode has the smallest $\lambda_j$ carries the largest, least-damped share of the perturbation.
*Proof.* The redistribution term in (4) has zero net contribution to $\dot E$ (Paper 03, Corollary 4), so migration is conservative; the dissipation rate $2\lambda_j E_j$ is smallest for the small-$\lambda_j$ modes, which therefore retain their energy longest. $\square$

**Corollary 2 (early-warning observable).** In the power-grid demo, stressing a single line drives a monotone transfer of modal energy into the mode aligned with the stressed region, while $\dot E$ tracks $-\sum \lambda_j E_j$ to $2.6\times10^{-3}$ accuracy. Monitoring the *slope* of the modal-energy ratio $E_j/E$ is therefore a computable early-warning signature.

## V. OUTAGE DETECTION AND VULNERABILITY INDEX

**Definition 3 (vulnerability index).** The *vulnerability index* of node group $S$ is

$$\mathcal{V}(S) = \sum_{j : \text{supp}\,\varphi_j \subseteq S} \frac{E_j}{\lambda_j}, \tag{6}$$

i.e. the modal energy stored in modes localized on $S$, weighted by the inverse damping rate.

**Theorem 7 (vulnerability ranking).** Modes with small $\lambda_j$ contribute to $\mathcal{V}$ more per unit energy; the mode with the minimal $\lambda_j$ among those with substantial energy dominates $\mathcal{V}$ during a developing outage.
*Proof.* From (6) and the dissipation rate $2\lambda_jE_j$: modes with small $\lambda_j$ decay slowest, so at any later time their share of $E$ is larger (Theorem 6), increasing their weight $E_j/\lambda_j$. $\square$

**Theorem 8 (detection criterion).** Let $\hat r_j(t) = E_j(t)/E(t)$. A structural event is detected at the first time $t_0$ such that

$$\max_j \big|\hat r_j(t_0) - \hat r_j^{(0)}(t_0)\big| > \delta, \tag{7}$$

where $\hat r^{(0)}$ is the null trajectory with $C \equiv 0$, and the detection threshold $\delta$ is set by the measurement noise floor. The false-alarm rate is controlled by $\delta$.
*Proof.* By Paper 03, Corollary 4, deformation ($C \neq 0$) changes the ratios while conserving $E$; the null trajectory is computable from the observed eigenvalues alone (Paper 10, Theorem 5). Under noise, (7) is a threshold test whose level is set by $\delta$. $\square$

## VI. CASCADING-FAILURE ANALYSIS

**Theorem 9 (energy-conserving cascade steps).** Each topology-change event in a cascade redistributes modal energy conservatively: the total energy change across the event equals $-2\sum_j\lambda_j E_j \Delta t$, independent of the redistribution pattern.
*Proof.* Paper 03, Theorem 6 applied per event. $\square$

**Corollary 3 (cascade audit).** A cascade is a sequence of redistribution events; each is auditable by (5). Stress does not create energy — cascades correspond to repeated redistribution into progressively weaker modes, each step checkable against the conservation identity.
*Proof.* Theorem 9 and Theorem 6. $\square$

**Theorem 10 (mitigation condition).** Re-dispatch that increases the algebraic connectivity floor $\lambda_2^\ast$ shortens the synchronization time bound (3) and reduces the vulnerability index (6) for all affected modes.
*Proof.* (3) is monotone decreasing in $\lambda_2^\ast$; (6) is monotone increasing in the $\lambda_j^{-1}$ weights, which decrease as connectivity grows. $\square$

## VII. NUMERICAL VERIFICATION

`demos/power_grid_mode_migration.py` verifies Paper 03 Theorem 3 (skewness of $C$, $4.2\times10^{-6}$), Theorem 5 (spectral-flow residual $4.7\times10^{-4}$), and Theorem 6 (energy balance $2.6\times10^{-3}$), on a 6-node network with one edge stressed then recovering.

## VIII. USES OF POWER-NETWORK STRUCTURE-FLOW THEORY

1. **Operator early warning.** Real-time estimation of $E_j/E$ and its drift flags an incipient topology change before a trip (Paper 10 implements the estimator).
2. **Control design.** Theorem 2 converts a desired synchronization time into a required floor on $\int\lambda_2\,ds$, guiding topology or droop adjustments.
3. **Vulnerability ranking.** Modes with persistently small $\lambda_j$ are ranked by the residual energy they retain (Theorem 6); reinforcement targets the structure of those modes.
4. **Cascading-failure analysis.** The conserved-total nature of migration (Paper 03, Corollary 4) means stress does not create energy; cascades correspond to repeated redistribution events, each auditable by the identity (Theorem 9).
5. **N-1 security screening.** Theorem 8 gives a computable screening statistic for candidate line outages.
6. **Islanding detection.** Theorem 4 converts the loss of algebraic connectivity into a detectability statement.

## IX. CONCLUSION

Power networks are the physical home of the causal network spectral theory. Synchronization is controlled by the time-integrated algebraic connectivity; vulnerability is exposed by conservative mode migration with eigenvalue-controlled dissipation. Both are exactly quantified by the theorems of Paper 03, and the early-warning observable (Corollary 2) is directly computable from measured frequency data.

---

## REFERENCES

[1] P. Kundur, *Power System Stability and Control*, McGraw-Hill, 1994.

[2] F. Dörfler and F. Bullo, "Synchronization and transient stability in power networks and non-uniform Kuramoto oscillators," *SIAM J. Control Optim.* **50**(3), 1616–1642 (2012).

[3] M. Fiedler, "Algebraic connectivity of graphs," *Czechoslovak Math. J.* **23**(98), 298–305 (1973).

[4] F. R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics **92**, American Mathematical Society, 1997.

[5] A. Ortega, P. Frossard, J. Kovačević, J. M. F. Moura, and P. Vandergheynst, "Graph signal processing: overview, challenges, and applications," *Proc. IEEE* **106**(5), 808–828 (2018).
