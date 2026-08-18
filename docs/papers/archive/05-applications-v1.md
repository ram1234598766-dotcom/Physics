# Paper 05 — Applications

**Abstract.** We apply Structure-Flow Calculus to three concrete physical problems: wave propagation in graded media with closed-form modes (acoustic impedance matching), mode energy migration in stressed power networks, and outbreak decay bounds on adaptive contact networks. Each application rests on a proven theorem of Papers 02–03 and is corroborated by a runnable numerical demo.

**Honesty caveat.** The physical models (graded-media acoustics, linearized swing equations, SIS epidemics) are standard; the contribution is the Structure-Flow theorems and their explicit use.

## 1. Graded acoustic media

Using Theorem 2.4, a graded medium with \(\rho_0 \propto 1/\rho\), \(K \propto \rho\) has wave equation \(u_{tt} = \rho(\rho u_x)_x\), whose modes are closed-form (Thm 2.1, Ex. 2.6–2.7). For an exponential profile the modes compress toward the high-speed end, enabling impedance-matched design. Energy is exactly conserved (Thm 2.5). *Verification:* `demos/graded_wave.py`.

## 2. Power networks under stress

Linearized frequency deviations on a power network follow \(\dot u = -L(t)u\) (uniform-inertia DC flow relaxation / consensus regulation). The Energy Migration Theorem (Thm 3.6) states that as a line weakens, energy is redistributed across modes without loss except through the (changing) eigenvalues \(\lambda_j(t)\). A developing outage therefore drives energy toward the modes with the smallest algebraic connectivity — the least damped, most vulnerable modes. *Verification:* `demos/power_grid_mode_migration.py` shows modal energies migrating as one edge is stressed.

## 3. Adaptive-contact epidemics

For SIS on a time-varying contact graph, Theorem 3.9 bounds the linearized outbreak by \(\|I(t)\| \le \|I(0)\| e^{\int(\beta\lambda_{\max}(W) - \gamma)ds}\). Mitigation that reduces \(\lambda_{\max}(W(s))\) (e.g. reducing effective contact mixing) tightens the bound at time \(s\). The diffusion limit obeys the algebraic-connectivity bound (Thm 3.3) and conserves mass (Thm 3.2). *Verification:* `demos/epidemic_decay_bound.py`.

## 4. Summary of verified results

| Application | Theorem | Demo | Result |
|---|---|---|---|
| Graded acoustics | 2.1, 2.3, 2.5 | graded_wave.py | modes, evolution, energy |
| Power networks | 3.3, 3.5, 3.6 | power_grid_mode_migration.py | skew, spectral flow, energy |
| Epidemics | 3.2, 3.3, 3.9 | epidemic_decay_bound.py | mass, connectivity, Grönwall |

## References
[1] D. Shuman et al., *The emerging field of signal processing on graphs*, IEEE Signal Processing Magazine, 2013.
[2] P. Kundur, *Power System Stability and Control*, 1994.
[3] R. Pastor-Satorras, C. Castellano, P. Van Mieghem, A. Vespignani, *Epidemic processes in complex networks*, Rev. Mod. Phys., 2015.
