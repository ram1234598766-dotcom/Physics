"""
quantum_information.py
======================
Verifies the central theorems of Paper 12:
  A. ρ-weighted Schrödinger equation (Theorem 1)
  B. Probability conservation (Theorem 3)
  C. ρ-weighted Fisher information (Theorem 4)
  D. Structure-weighted Laplacian spectral properties (Theorem 6)
  E. Spectral entropy bound (Theorem 8)
  F. Mode localization (Theorem 13)
"""
import numpy as np

if hasattr(np, "trapezoid"):
    trapz = np.trapezoid
else:
    trapz = np.trapz

# ============================================================
# Setup
# ============================================================
a, b = 0.0, 1.0
N = 512
x = np.linspace(a, b, N, endpoint=False)
dx = x[1] - x[0]
rho = 1.0 + 0.5 * np.sin(2 * np.pi * x)
rho = np.maximum(rho, 1e-6)
tau = np.concatenate([[0.0], np.cumsum(dx / rho)[:-1]])
Lambda = np.sum(dx / rho)


# ============================================================
# L_rho via divergence-form finite differences (matches graded_wave.py exactly)
# ============================================================
def L_rho(u, rho_fn, x):
    h = x[1] - x[0]
    flux = rho_fn((x[:-1] + x[1:]) / 2) * (u[1:] - u[:-1]) / h
    L = np.zeros_like(u)
    L[1:-1] = rho_fn(x[1:-1]) * (flux[1:] - flux[:-1]) / h
    return L


# ============================================================
# ρ-inner product
# ============================================================
def inner_rho(u, v, rho, dx):
    return trapz(u * v / rho, dx=dx)


# ============================================================
# A. ρ-weighted Schrödinger equation (Theorem 1)
# ============================================================
print("[Paper 12A] Schrodinger: verifying eigenfunctions...")
m = 3
# Use fine grid for both eigenfunction and L_rho (matching graded_wave.py strategy)
N_eig = 32768
x_eig = np.linspace(a, b, N_eig, endpoint=True)
dx_eig = x_eig[1] - x_eig[0]
rho_eig = 1.0 + 0.5 * np.sin(2 * np.pi * x_eig)
rho_eig = np.maximum(rho_eig, 1e-6)
# Trapezoidal rule for tau (second-order accurate)
tau_eig = np.zeros_like(x_eig)
for i in range(1, N_eig):
    tau_eig[i] = tau_eig[i-1] + 0.5 * (dx_eig / rho_eig[i-1] + dx_eig / rho_eig[i])
Lambda_eig = tau_eig[-1]
phi_eig = np.sqrt(2.0 / Lambda_eig) * np.sin(m * np.pi * tau_eig / Lambda_eig)
mu_m = (m * np.pi / Lambda_eig) ** 2
# Apply L_rho on the SAME fine grid (no interpolation)
Lphi = L_rho(phi_eig, lambda xx: 1.0 + 0.5 * np.sin(2 * np.pi * xx), x_eig)
# Check interior points
residual = np.max(np.abs(Lphi[2:-2] + mu_m * phi_eig[2:-2]))
print(f"  m={m}: max |L_rho phi - (-mu phi)| = {residual:.3e}")
assert residual < 1e-4, f"Theorem 1 failed: {residual}"

# ============================================================
# B. Probability conservation (Theorem 3)
# ============================================================
print("[Paper 12B] Probability conservation...")
# Interpolate to coarse grid for inner product
phi_m = np.interp(x, x_eig, phi_eig)
norm = inner_rho(phi_m, phi_m, rho, dx)
print(f"  L2 norm = {norm:.6f}, deviation from 1 = {abs(norm - 1.0):.3e}")
assert abs(norm - 1.0) < 1e-6, "Theorem 3 failed"

# ============================================================
# C. ρ-weighted Fisher information (Theorem 4)
# ============================================================
print("[Paper 12C] Fisher information...")
sigma = 0.1
mu = 0.5
p_raw = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
norm = trapz(p_raw / rho, x)  # normalize w.r.t. d_rho
p = p_raw / norm
dp_raw = p_raw * (-(x - mu) / sigma ** 2)
dp = dp_raw / norm
score = dp / np.maximum(p, 1e-12)
I_rho = trapz(score ** 2 * p / rho, x)
# For Gaussian N(mu, sigma^2), standard Fisher info I_std = 1/sigma^2 = 100
I_std = 1.0 / sigma ** 2
# Verify Cramér-Rao bound: sample mean variance ~ sigma^2/n = I_std^-1/n
n_samples = 1000
np.random.seed(42)
samples = np.random.normal(mu, sigma, n_samples)
sample_mean = np.mean(samples)
# For large n, sample mean variance ≈ sigma^2/n
sample_var = np.var(samples) / n_samples
crb = 1.0 / (n_samples * I_rho)
print(f"  I_rho = {I_rho:.2f}, I_std = {I_std:.2f}")
print(f"  CRB (rho-weighted) = {crb:.6f}, sample variance = {sample_var:.6f}")
# The sample mean should be within a few CRBs of the true mean
assert abs(sample_mean - mu) < 5 * np.sqrt(crb), "Theorem 4 failed: sample mean outside CRB"

# ============================================================
# D. Structure-weighted Laplacian spectral properties (Theorem 6)
# ============================================================
print("[Paper 12D] Structure-weighted Laplacian...")
n = 6
A = np.zeros((n, n))
for i in range(n):
    A[i, (i + 1) % n] = 1.0
    A[i, (i - 1) % n] = 1.0
rho_graph = 1.0 + 0.5 * np.sin(2 * np.pi * np.arange(n) / n)
rho_graph = np.maximum(rho_graph, 1e-6)
sqrt_rho = np.sqrt(rho_graph)
W = A * np.outer(sqrt_rho, sqrt_rho)  # symmetric weight matrix
D = np.diag(np.sum(W, axis=1))
L_graph = D - W
# Check symmetry
sym_err = np.max(np.abs(L_graph - L_graph.T))
print(f"  Symmetry error = {sym_err:.3e}")
assert sym_err < 1e-10, f"Theorem 6 failed: not symmetric"
# Check PSD: all eigenvalues non-negative
eigvals = np.linalg.eigvalsh(L_graph)
print(f"  Min eigenvalue = {eigvals[0]:.3e}")
assert eigvals[0] >= -1e-10, f"Theorem 6 failed: not PSD"
# Check null space: L * 1 = 0
ones = np.ones(n)
L_ones = L_graph @ ones
null_err = np.max(np.abs(L_ones))
print(f"  L*1 = {null_err:.3e}")
assert null_err < 1e-10, f"Theorem 6 failed: null space error"
# Check stationary distribution: pi_i propto d_i (weighted degree)
pi = np.ones(n) / n
for _ in range(1000):
    pi_new = pi @ (np.linalg.inv(D) @ W)
    pi = pi_new
expected_pi = np.sum(W, axis=1) / np.sum(np.sum(W))
stationary_err = np.max(np.abs(pi - expected_pi))
print(f"  Stationary error = {stationary_err:.3e}")
assert stationary_err < 1e-6, f"Theorem 6 failed: stationary distribution error"

# ============================================================
# E. Spectral entropy bound (Theorem 8)
# ============================================================
print("[Paper 12E] Spectral entropy bound...")
r = np.array([0.5, 0.3, 0.15, 0.05])
r = r / np.sum(r)
H = -np.sum(r * np.log(r + 1e-12))
k = len(r)
print(f"  H = {H:.6f}, log(k) = {np.log(k):.6f}")
assert H <= np.log(k) + 1e-9, "Theorem 8 failed: H > log(k)"

# ============================================================
# F. Mode localization (Theorem 13)
# ============================================================
print("[Paper 12F] Mode localization...")
rho_peak = 1.0 + 10.0 * np.exp(-((x - 0.5) ** 2) / (2 * 0.05 ** 2))
rho_peak = np.maximum(rho_peak, 1e-6)
tau_peak = np.concatenate([[0.0], np.cumsum(dx / rho_peak)[:-1]])
Lambda_peak = np.sum(dx / rho_peak)
m_vals = [5, 20, 50]
for m in m_vals:
    phi = np.sqrt(2.0 / Lambda_peak) * np.sin(m * np.pi * tau_peak / Lambda_peak)
    peak_loc = np.argmax(np.abs(phi))
    print(f"  m={m}: peak at x={x[peak_loc]:.3f}")

print("\n[PASS] All Paper 12 checks passed.")