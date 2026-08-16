"""Closed-form vs numerical solutions of the SFC wave equation u_tt = rho (rho u_x)_x.

Closed form (Paper 2, Theorem 2.2): for profile rho(x) = rho0 e^{kappa x},
the transport coordinate is tau(x) = (1 - e^{-kappa x})/(kappa rho0),
Lambda = tau(1), and the Dirichlet modes are
    phi_m(x) = sqrt(2/Lambda) sin(m pi tau(x)/Lambda),  omega_m = m pi/Lambda.
Verifies numerically:
  (1) L_rho phi_m = -(m pi/Lambda)^2 phi_m  (mode satisfies the PDE).
  (2) Time evolution matches the closed-form standing wave.
  (3) Total energy  E = 1/2 int (u_t)^2 d(rho) + 1/2 int (D_rho u)^2 d(rho) is conserved.
"""
import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if hasattr(np, "trapezoid"):
    trapz = np.trapezoid
else:
    trapz = np.trapz

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

RHO0, KAPPA = 1.0, 2.0
A, B = 0.0, 1.0


def rho(x):
    return RHO0 * np.exp(KAPPA * x)


def tau(x):
    return (1 - np.exp(-KAPPA * (x - A))) / (KAPPA * RHO0)


def Lambda():
    return (1 - np.exp(-KAPPA * (B - A))) / (KAPPA * RHO0)


def phi(x, m, Lam):
    return np.sqrt(2 / Lam) * np.sin(m * np.pi * tau(x) / Lam)


def omega(m, Lam):
    return m * np.pi / Lam


def L_rho_fd(u, x):
    h = x[1] - x[0]
    flux = rho((x[:-1] + x[1:]) / 2) * (u[1:] - u[:-1]) / h
    L = np.zeros_like(u)
    L[1:-1] = rho(x[1:-1]) * (flux[1:] - flux[:-1]) / h
    return L


def discrete_energy(u, v, x):
    h = x[1] - x[0]
    xm = (x[:-1] + x[1:]) / 2
    flux = rho(xm) * (u[1:] - u[:-1]) / h
    kin = 0.5 * np.sum(v ** 2 / rho(x)) * h
    pot = 0.5 * np.sum(flux ** 2 / rho(xm)) * h
    return kin + pot


def main():
    Lam = Lambda()
    N_eig = 4000
    N = 400
    x_eig = np.linspace(A, B, N_eig)
    x = np.linspace(A, B, N)
    h = x[1] - x[0]

    residual = []
    for m in range(1, 5):
        mu = omega(m, Lam) ** 2
        phim = phi(x_eig, m, Lam)
        lphi = L_rho_fd(phim, x_eig)
        res = np.max(np.abs(lphi[2:-2] + mu * phim[2:-2]))
        residual.append(res)
        print(f"[PDE check] mode m={m}: max |L_rho phi - (-mu phi)| = {res:.3e}")

    modes = [1, 2]

    def u0(x):
        return sum(phi(x, m, Lam) for m in modes) / len(modes)

    def v0(x):
        return np.zeros_like(x)

    y0 = np.concatenate([u0(x), v0(x)])

    def rhs(t, y):
        u, v = y[:N], y[N:]
        u = u.copy()
        v = v.copy()
        u[0] = u[-1] = 0.0
        v[0] = v[-1] = 0.0
        return np.concatenate([v, L_rho_fd(u, x)])

    t_span = (0.0, 2.0 * np.pi / omega(modes[0], Lam))
    t_eval = np.linspace(t_span[0], t_span[1], 200)
    sol = solve_ivp(rhs, t_span, y0, t_eval=t_eval, method="RK45", rtol=1e-9, atol=1e-11)

    mid = N // 2
    u_num = sol.y[mid, :]
    u_exact = (1 / len(modes)) * sum(
        phi(x[mid], m, Lam) * np.cos(omega(m, Lam) * sol.t) for m in modes
    )
    err_evol = np.max(np.abs(u_num - u_exact))
    print(f"[Evolution] max |numeric - closed form| = {err_evol:.3e}")

    u = sol.y[:N, :]
    v = sol.y[N:, :]
    energies = [discrete_energy(u[:, k], v[:, k], x) for k in range(len(sol.t))]
    energies = np.array(energies)
    err_energy = np.max(np.abs(energies - energies[0]))
    print(f"[Energy] conserved within {err_energy:.3e}")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    for m in range(1, 4):
        axes[0].plot(x, phi(x, m, Lam), label=f"m={m}")
    axes[0].set_title("SFC mode shapes (exponential profile)")
    axes[0].legend()
    axes[1].plot(sol.t, u_num, label="numeric")
    axes[1].plot(sol.t, u_exact, "--", label="closed form")
    axes[1].set_title("Midpoint displacement u(L/2, t)")
    axes[1].legend()
    axes[2].plot(sol.t, energies)
    axes[2].set_title("Total energy")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "graded_wave.png"), dpi=120)
    plt.close(fig)

    assert max(residual) < 1e-2, "mode PDE residual too large"
    assert err_evol < 1e-2, "evolution mismatch"
    assert err_energy < 1e-3, "energy not conserved"
    print("All graded-wave checks passed.")


if __name__ == "__main__":
    main()
