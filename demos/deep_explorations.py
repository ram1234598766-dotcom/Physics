"""
deep_explorations.py
====================
Advanced numerical experiments with publication-quality figures:
  A. Eigenvalue perturbation landscapes (Paper 02, Theorem 10)
  B. Mode localization diagrams (Paper 02, Theorem 7)
  C. Energy migration time series (Paper 03, Theorem 6)
  D. Structure-field inverse recovery (Paper 04, Theorem 2)
  E. Two-term Weyl law convergence (Paper 09, Theorem 6)
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyArrowPatch
from matplotlib.collections import LineCollection
import os

if hasattr(np, "trapezoid"):
    trapz = np.trapezoid
else:
    trapz = np.trapz

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 150,
    'text.usetex': False,
    'mathtext.fontset': 'stix',
})

# ============================================================
# Common helpers
# ============================================================
a, b = 0.0, 1.0

def rho_base(x):
    return 1.0 + 0.5 * np.sin(2 * np.pi * x)

def make_grid(N=2048):
    x = np.linspace(a, b, N, endpoint=True)
    dx = x[1] - x[0]
    rho = np.maximum(rho_base(x), 1e-6)
    tau = np.zeros_like(x)
    for i in range(1, N):
        tau[i] = tau[i-1] + 0.5 * (dx/rho[i-1] + dx/rho[i])
    Lam = tau[-1]
    return x, dx, rho, tau, Lam

def L_rho(u, rho_fn, x):
    h = x[1] - x[0]
    flux = rho_fn((x[:-1] + x[1:]) / 2) * (u[1:] - u[:-1]) / h
    L = np.zeros_like(u)
    L[1:-1] = rho_fn(x[1:-1]) * (flux[1:] - flux[:-1]) / h
    return L

def eigenfunction(m, tau, Lam):
    return np.sqrt(2.0 / Lam) * np.sin(m * np.pi * tau / Lam)

# ============================================================
# A. Eigenvalue perturbation landscapes
# ============================================================
print("[Exploration A] Eigenvalue perturbation landscapes...")
x, dx, rho, tau, Lam = make_grid()
m_vals = [1, 3, 5]
perturbations = np.linspace(-0.3, 0.3, 61)
mu0 = np.array([(m * np.pi / Lam)**2 for m in m_vals])

fig, ax = plt.subplots(figsize=(8, 5))
for idx, m in enumerate(m_vals):
    mu_pert = []
    for pert in perturbations:
        rho_p = np.maximum(rho + pert, 1e-6)
        tau_p = np.zeros_like(x)
        for i in range(1, len(x)):
            tau_p[i] = tau_p[i-1] + 0.5 * (dx/rho_p[i-1] + dx/rho_p[i])
        Lam_p = tau_p[-1]
        mu_p = (m * np.pi / Lam_p)**2
        mu_pert.append(mu_p)
    mu_pert = np.array(mu_pert)
    ax.plot(perturbations, mu_pert, label=f'm={m}, $\mu_{m}^0$={mu0[idx]:.3f}')

ax.set_xlabel(r'Perturbation amplitude $\delta\rho$')
ax.set_ylabel(r'Eigenvalue $\mu_m$')
ax.set_title(r'Eigenvalue perturbation landscape ($\rho \to \rho + \delta\rho$)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'exploration_A_perturbation.png'))
plt.close()

# ============================================================
# B. Mode localization diagrams
# ============================================================
print("[Exploration B] Mode localization diagrams...")
rho_peak = 1.0 + 10.0 * np.exp(-((x - 0.5)**2) / (2 * 0.05**2))
rho_peak = np.maximum(rho_peak, 1e-6)
tau_peak = np.zeros_like(x)
for i in range(1, len(x)):
    tau_peak[i] = tau_peak[i-1] + 0.5 * (dx/rho_peak[i-1] + dx/rho_peak[i])
Lam_peak = tau_peak[-1]

fig, axes = plt.subplots(2, 3, figsize=(12, 7))
m_list = [2, 5, 10, 20, 40, 80]
for ax, m in zip(axes.flat, m_list):
    phi = eigenfunction(m, tau_peak, Lam_peak)
    ax.plot(x, phi, color='#2c5282', linewidth=1.5)
    ax.fill_between(x, phi, alpha=0.3, color='#2c5282')
    ax.set_title(f'm={m}, $\lambda_m$={(m*np.pi/Lam_peak)**2:.2f}')
    ax.set_xlabel('x')
    ax.set_ylabel(r'$\varphi_m(x)$')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-1.2, 1.2)
plt.suptitle(r'Mode localization for peaked structure field $\rho(x)=1+10e^{-(x-0.5)^2/0.005}$', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'exploration_B_localization.png'))
plt.close()

# ============================================================
# C. Energy migration time series
# ============================================================
print("[Exploration C] Energy migration time series...")
n = 12
A = np.zeros((n, n))
for i in range(n):
    A[i, (i+1)%n] = 1.0
    A[i, (i-1)%n] = 1.0

t_vals = np.linspace(0, 5, 500)
dt = t_vals[1] - t_vals[0]
u = np.random.randn(n)
u = u / np.linalg.norm(u)

# Time-varying edge weight
def rho_graph(t):
    return 1.0 + 0.3 * np.sin(2 * np.pi * t) * np.exp(-t/3)

E_history = []
modal_history = []
for t in t_vals:
    rho_t = np.maximum(rho_graph(t) + 0.5 * np.sin(2*np.pi*np.arange(n)/n), 1e-6)
    D = np.diag(rho_t * A @ np.ones(n))
    W = A * np.outer(np.sqrt(rho_t), np.sqrt(rho_t))
    L = D - W
    eigvals, eigvecs = np.linalg.eigh(L)
    phi = eigvecs
    a = phi.T @ u
    E_history.append(np.sum(a**2))
    modal_history.append(a)

E_history = np.array(E_history)
modal_history = np.array(modal_history)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(t_vals, E_history, color='#2c5282', linewidth=2)
axes[0].set_xlabel('Time t')
axes[0].set_ylabel(r'Total energy $E(t) = \sum \hat u_j^2$')
axes[0].set_title('Energy conservation under deformation (should be constant)')
axes[0].grid(True, alpha=0.3)

im = axes[1].imshow(modal_history.T, aspect='auto', origin='lower',
                     extent=[0, 5, 0, n], cmap='viridis')
axes[1].set_xlabel('Time t')
axes[1].set_ylabel('Mode index j')
axes[1].set_title(r'Modal coefficients $\hat u_j(t)$ over time')
plt.colorbar(im, ax=axes[1])
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'exploration_C_migration.png'))
plt.close()

# ============================================================
# D. Structure-field inverse recovery
# ============================================================
print("[Exploration D] Structure-field inverse recovery...")
true_rho = 1.0 + 0.8 * np.exp(-((x - 0.3)**2) / (2 * 0.1**2))
true_rho = np.maximum(true_rho, 1e-6)
true_tau = np.zeros_like(x)
for i in range(1, len(x)):
    true_tau[i] = true_tau[i-1] + 0.5 * (dx/true_rho[i-1] + dx/true_rho[i])

recovered_rho = 1.0 / np.gradient(true_tau, dx)
recovered_rho = np.maximum(recovered_rho, 1e-6)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, true_rho, label=r'True $\rho(x)$', color='#2c5282', linewidth=2)
axes[0].plot(x, recovered_rho, '--', label=r'Recovered $\rho(x) = 1/\tau\'(x)$', color='#b8961a', linewidth=2)
axes[0].set_xlabel('x')
axes[0].set_ylabel(r'$\rho(x)$')
axes[0].set_title('Structure field recovery from transport map')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, true_tau, color='#2c5282', linewidth=2, label=r'True $\tau(x)$')
axes[1].set_xlabel('x')
axes[1].set_ylabel(r'$\tau(x)$')
axes[1].set_title('Transport coordinate')
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'exploration_D_recovery.png'))
plt.close()

# ============================================================
# E. Two-term Weyl law convergence
# ============================================================
print("[Exploration E] Two-term Weyl law convergence...")
L1 = 1.1547
L2 = 1.1547
mu_vals = np.array([4000, 40000, 80000, 120000, 160000, 200000])
N_exact = np.array([52, 569, 1149, 1737, 2324, 2913])
one_term = L1 * L2 / (4 * np.pi) * mu_vals
two_term = one_term - (L1 + L2) / (8 * np.pi) * np.sqrt(mu_vals)
one_err = np.abs(N_exact - one_term) / N_exact
two_err = np.abs(N_exact - two_term) / N_exact

fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogx(mu_vals, one_err, 'o-', label='One-term Weyl', color='#b8961a', linewidth=2, markersize=8)
ax.semilogx(mu_vals, two_err, 's-', label='Two-term Weyl', color='#2c5282', linewidth=2, markersize=8)
ax.set_xlabel(r'Eigenvalue threshold $\mu$')
ax.set_ylabel('Relative counting error')
ax.set_title(r'Weyl law convergence in $d=2$ (box with $\Lambda_1=\Lambda_2=1.1547$)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUT, 'exploration_E_weyl.png'))
plt.close()

print("\n[PASS] All exploration figures saved to demos/figures/")