"""Energy Migration Theorem on a small time-varying power network.

Dynamics: du/dt = -L(t) u on a 6-node grid whose Laplacian L(t) is stressed
along one edge (simulating a line under stress, e.g. a developing outage).

Verifies (Paper 3, Theorems 3.4-3.6):
  (1) The connection C_jk = <phi_j, phi_k'> is skew-symmetric.
  (2) Spectral flow equation: uhat_j' = -lambda_j uhat_j - sum_k C_jk uhat_k.
  (3) Energy balance: dE/dt = -2 sum_j lambda_j uhat_j^2
      (deformation redistributes energy between modes, never creates/destroys it).
"""
import os
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)


def build_laplacian(n, edges, w):
    L = np.zeros((n, n))
    for (i, j), wij in zip(edges, w):
        L[i, i] += wij
        L[j, j] += wij
        L[i, j] -= wij
        L[j, i] -= wij
    return L


def main():
    n = 6
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 2), (1, 3), (2, 4)]
    w0 = np.ones(len(edges)) * 2.0
    stress_idx = edges.index((1, 3))

    def edge_weights(t):
        w = w0.copy()
        s = 0.5 + 0.5 * np.tanh((t - 3.0) / 0.8)
        w[stress_idx] = w0[stress_idx] * (1.0 - 0.9 * s)
        return w

    def L(t):
        return build_laplacian(n, edges, edge_weights(t))

    T, steps = 8.0, 2000
    t = np.linspace(0, T, steps + 1)
    h = t[1] - t[0]

    x0 = np.sin(np.linspace(0, 3, n) + 1.0)
    u0 = x0 - x0.mean()

    def rhs(t, y):
        return -L(t) @ y

    sol = solve_ivp(rhs, (0, T), u0, t_eval=t, rtol=1e-10, atol=1e-12)
    u = sol.y.T
    for k in range(steps + 1):
        u[k] -= u[k].mean()

    phis = np.zeros((steps + 1, n, n))
    lams = np.zeros((steps + 1, n))
    for k in range(steps + 1):
        evals, evecs = np.linalg.eigh(L(t[k]))
        order = np.argsort(evals)
        evals, evecs = evals[order], evecs[:, order]
        if k > 0:
            for j in range(n):
                if phis[k - 1, :, j] @ evecs[:, j] < 0:
                    evecs[:, j] *= -1
        phis[k] = evecs
        lams[k] = evals

    C = np.zeros((steps + 1, n, n))
    for k in range(1, steps):
        dPhi = (phis[k + 1] - phis[k - 1]) / (2 * h)
        C[k] = phis[k].T @ dPhi

    skew_err = max(np.max(np.abs(C[k] + C[k].T)) for k in range(1, steps))
    print(f"[Skew] max |C + C^T| = {skew_err:.3e}")

    uhat = np.einsum("kji,kj->ki", phis, u)
    duhat = np.zeros_like(uhat)
    for k in range(1, steps):
        duhat[k] = (uhat[k + 1] - uhat[k - 1]) / (2 * h)
    pred = -lams * uhat - np.einsum("kij,kj->ki", C, uhat)
    rel = np.max(
        np.abs(duhat[1:steps] - pred[1:steps]) / (np.max(np.abs(uhat)) + 1e-12)
    )
    print(f"[Spectral flow] max relative residual = {rel:.3e}")

    E = np.sum(uhat**2, axis=1)
    dE = np.gradient(E, h)
    diss = -2 * np.sum(lams * uhat**2, axis=1)
    en_res = np.max(np.abs(dE[1:steps] - diss[1:steps]))
    print(f"[Energy] max |dE/dt + 2 sum lambda_j uhat_j^2| = {en_res:.3e}")

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    for j in range(1, n):
        axes[0].plot(t, lams[:, j], label=f"lambda_{j}")
    axes[0].set_title("Eigenvalues (edge stressed then recovers)")
    axes[0].legend(fontsize=7)
    for j in range(n):
        axes[1].plot(t, uhat[:, j] ** 2, label=f"|uhat_{j}|^2")
    axes[1].set_title("Modal energies (energy migration)")
    axes[1].legend(fontsize=7)
    axes[2].plot(t, E)
    axes[2].set_title("Total energy (dissipates via lambdas)")
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "power_grid.png"), dpi=120)
    plt.close(fig)

    assert skew_err < 1e-2, "connection not skew-symmetric"
    assert rel < 1e-2, "spectral flow equation violated"
    assert en_res < 1e-2, "energy balance violated"
    print("All power-grid spectral-flow checks passed.")


if __name__ == "__main__":
    main()
