"""Decay bounds on adaptive networks.

Part 1 (Paper 3, Theorem 3.3):  du/dt = -L(t)u with mean-centered initial data
   satisfies   ||u(t)|| <= ||u(0)|| exp(-int_0^t lambda_2(s) ds).
Part 2 (Paper 3, Thm 3.2): total mass 1^T u is conserved.
Part 3 (Paper 3, Thm 3.9): linearized SIS on a time-varying contact graph W(t)
   obeys ||I(t)|| <= ||I(0)|| exp(int_0^t (beta*lambda_max(W(s)) - gamma) ds).
"""
import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)


def main():
    rng = np.random.default_rng(7)
    n = 12

    base = rng.uniform(0.3, 1.0, size=(n, n))
    base = (base + base.T) / 2
    np.fill_diagonal(base, 0)
    base = base / base.max()

    def W(t):
        w = base * (1 + 0.3 * np.sin(0.7 * t) + 0.2 * np.sin(2.3 * t + np.pi / 4))
        np.fill_diagonal(w, 0)
        return w

    def L(t):
        w = W(t)
        return np.diag(w.sum(axis=1)) - w

    def l2(t):
        return np.linalg.eigvalsh(L(t))[1]

    T = 25.0
    ts = np.linspace(0, T, 500)
    h = ts[1] - ts[0]

    u0 = rng.normal(size=n)
    u0 -= u0.mean()

    def heat(t, y):
        return -L(t) @ y

    sol = solve_ivp(heat, (0, T), u0, t_eval=ts, rtol=1e-9, atol=1e-11)
    u = sol.y

    l2vals = np.array([l2(t) for t in ts])
    cum = np.concatenate([[0.0], np.cumsum((l2vals[1:] + l2vals[:-1]) / 2 * np.diff(ts))])
    bound = np.linalg.norm(u0) * np.exp(-cum)
    norm = np.linalg.norm(u, axis=0)
    assert np.all(norm <= bound + 1e-8), "algebraic-connectivity bound violated"
    print("[Thm 3.3] algebraic-connectivity bound holds throughout")

    masses = u.sum(axis=0)
    assert np.max(np.abs(masses - masses[0])) < 1e-9, "mass not conserved"
    print("[Thm 3.2] total mass conserved within 1e-9")

    gamma, beta = 0.5, 0.1

    def sis(t, y):
        I = y
        return beta * (1 - I) * (W(t) @ I) - gamma * I

    I0 = rng.uniform(0.005, 0.01, size=n)
    sol2 = solve_ivp(sis, (0, T), I0, t_eval=ts, rtol=1e-8, atol=1e-10)
    Inorm = np.linalg.norm(sol2.y, axis=0)

    integrand = np.array(
        [beta * np.max(np.linalg.eigvalsh(W(t))) - gamma for t in ts]
    )
    cum2 = np.concatenate([[0.0], np.cumsum((integrand[1:] + integrand[:-1]) / 2 * np.diff(ts))])
    bound2 = np.linalg.norm(I0) * np.exp(cum2)
    assert np.all(Inorm <= bound2 + 1e-8), "Grönwall bound violated"
    print("[Thm 3.9] SIS decay bound holds throughout")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].plot(ts, norm, label="||u||")
    axes[0].plot(ts, bound, "--", label="bound")
    axes[0].set_title("Diffusion decay vs lambda_2 bound")
    axes[0].legend()
    axes[1].plot(ts, masses, label="total mass")
    axes[1].set_title("Mass conservation")
    axes[1].legend()
    axes[2].plot(ts, Inorm, label="||I||")
    axes[2].plot(ts, bound2, "--", label="Grönwall bound")
    axes[2].set_title("SIS decay vs bound")
    axes[2].legend()
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "epidemic.png"), dpi=120)
    plt.close(fig)

    print("All epidemic/adaptive-network checks passed.")


if __name__ == "__main__":
    main()
