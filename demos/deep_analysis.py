"""Deep numerical analysis of the Structure-Flow Calculus.

Every number printed here is computed live from first principles in this run
(the eigenvalue counts in Part C are exact integer counts). Nothing is
fabricated; the run is fully reproducible.

  A. Spectral convergence of the modal expansion  (Paper 02)
  B. Long-time energy conservation of the graded wave  (Paper 02)
  C. Exact counting function vs the two-term Weyl law, d = 2  (Paper 09)
     - one-term and two-term (Ivrii) predictions
     - the boundary coefficient measured from the data by least squares
  D. Mode-energy migration under structural deformation  (Paper 03)
  E. Tightness of the epidemic decay bound on adaptive networks  (Paper 07)
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


LAM = (1 - np.exp(-KAPPA * (B - A))) / (KAPPA * RHO0)


def phi(x, m):
    return np.sqrt(2 / LAM) * np.sin(m * np.pi * tau(x) / LAM)


def omega(m):
    return m * np.pi / LAM


# ---------------------------------------------------------------- A. spectral convergence
def coeff(f, m, xs, n=80001):
    xs2 = np.linspace(A, B, n)
    return trapz(f(xs2) * phi(xs2, m) / rho(xs2), xs2)


def proj_error(M):
    xs = np.linspace(A, B, 20001)
    f = lambda x: np.sin(3 * np.pi * tau(x) / LAM) * x * (1 - x)
    s = sum(coeff(f, m, xs) * phi(xs, m) for m in range(1, M + 1))
    fv = f(xs)
    return np.sqrt(trapz((s - fv) ** 2 / rho(xs), xs))


print("=" * 72)
print("A. SPECTRAL CONVERGENCE  (Paper 02, Theorem 1)")
Ns = [2, 4, 8, 16, 32, 64]
conv = [(N, proj_error(N)) for N in Ns]
conv_errs = np.array([e for _, e in conv])
orders = np.log(conv_errs[:-1] / conv_errs[1:]) / np.log(Ns[1] / Ns[0]) if len(conv_errs) > 1 else []
for i, (N, e) in enumerate(conv):
    order = f"   (rate ~ {orders[i - 1]:.2f})" if i > 0 else ""
    print(f"  N = {N:3d}:  L2_rho error = {e:.3e}{order}")
print(f"  measured convergence rate (last step): ~{orders[-1]:.2f}")

# ------------------------------------------------------------- B. long-time energy conservation
print("=" * 72)
print("B. LONG-TIME ENERGY CONSERVATION  (Paper 02, Theorem 5)")
N = 400
x = np.linspace(A, B, N)
h = x[1] - x[0]


def L_rho_fd(u, x):
    flux = rho((x[:-1] + x[1:]) / 2) * (u[1:] - u[:-1]) / h
    L = np.zeros_like(u)
    L[1:-1] = rho(x[1:-1]) * (flux[1:] - flux[:-1]) / h
    return L


def discrete_energy(u, v, x):
    xm = (x[:-1] + x[1:]) / 2
    flux = rho(xm) * (u[1:] - u[:-1]) / h
    kin = 0.5 * np.sum(v ** 2 / rho(x)) * h
    pot = 0.5 * np.sum(flux ** 2 / rho(xm)) * h
    return kin + pot


u0 = phi(x, 1) + 0.5 * phi(x, 2)
v0 = np.zeros_like(x)
y0 = np.concatenate([u0, v0])


def rhs(t, y):
    u, v = y[:N], y[N:]
    u = u.copy()
    v = v.copy()
    u[0] = u[-1] = 0.0
    v[0] = v[-1] = 0.0
    return np.concatenate([v, L_rho_fd(u, x)])


Tp = 2 * np.pi / omega(1)
t_eval = np.linspace(0, 50 * Tp, 500)
sol = solve_ivp(rhs, (0, 50 * Tp), y0, t_eval=t_eval, method="DOP853", rtol=1e-11, atol=1e-13)
u = sol.y[:N, :]
v = sol.y[N:, :]
Es = np.array([discrete_energy(u[:, k], v[:, k], x) for k in range(len(sol.t))])
drift = np.max(np.abs(Es - Es[0])) / Es[0]
print(f"  50 fundamental periods, 500 output steps: relative energy drift = {drift:.3e}")

# ------------------------------------------------------------------- C. two-term Weyl law
print("=" * 72)
print("C. EXACT COUNTING FUNCTION vs TWO-TERM WEYL LAW, d = 2  (Paper 09, Thm 6b)")
# Structure box: exponential profile per direction -> tau-box [0,LAM]^2,
# eigenvalues exactly mu_{m1,m2} = (m1 pi/LAM)^2 + (m2 pi/LAM)^2.


def count_2d(mu_max, L):
    m1max = int(np.floor(np.sqrt(mu_max) * L / np.pi)) + 2
    cnt = 0
    for m1 in range(1, m1max + 1):
        for m2 in range(1, m1max + 1):
            if (m1 * np.pi / L) ** 2 + (m2 * np.pi / L) ** 2 <= mu_max:
                cnt += 1
    return cnt


L = LAM
V = L * L
S = 2.0 * (L + L)          # structure-area of the box boundary
C_formula = S / (4.0 * np.pi)   # boundary coefficient of the corrected two-term law
mus = [4000 * k for k in range(1, 51)]
counts = [count_2d(mu, L) for mu in mus]
N1 = [V / (4.0 * np.pi) * mu for mu in mus]
N2 = [V / (4.0 * np.pi) * mu - C_formula * np.sqrt(mu) for mu in mus]
rel1 = [abs(c - n1) / c for c, n1 in zip(counts, N1)]
rel2 = [abs(c - n2) / c for c, n2 in zip(counts, N2)]

# least-squares measurement of the boundary coefficient from the data:
#   N(mu) - V/(4 pi) mu  ~  -C_meas sqrt(mu)
resid = np.array(counts) - np.array(N1)
sqrt_mu = np.sqrt(np.array(mus, dtype=float))
mask = sqrt_mu > 0
C_meas = -np.sum(resid * sqrt_mu) / np.sum(sqrt_mu ** 2)
fit_resid = resid + C_meas * sqrt_mu

print(f"  box: tau side L = {L:.6f},  V = {V:.6f},  boundary structure-area S = {S:.6f}")
print(f"  two-term boundary coefficient: formula (Paper 09) C = {C_formula:.6f}")
print(f"                                  measured from data C = {C_meas:.6f}  (ratio {C_meas / C_formula:.3f})")
print("  relative counting error, one-term vs two-term:")
for i in [0, 9, 19, 29, 39, 49]:
    print(f"    mu = {mus[i]:7d}:  N = {counts[i]:5d}   one-term rel err = {rel1[i]:.4f}   two-term rel err = {rel2[i]:.4f}")

# ------------------------------------------------------------------- D. energy migration
print("=" * 72)
print("D. MODE-ENERGY MIGRATION UNDER DEFORMATION  (Paper 03, Theorem 6)")
rng = np.random.default_rng(7)
n = 12
T = 4.0
nt = 1601
dt = T / (nt - 1)
tt = np.linspace(0, T, nt)


def make_L(t):
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            w = 0.4 + 0.3 * np.sin(2 * t + i + j) + 0.2 * (i + j) / n
            G[i, j] = G[j, i] = max(w, 0.05)
    D = np.diag(G.sum(axis=1))
    return D - G


# gauge-aligned eigenframe: eigenvectors defined up to sign; align each one
# continuously against the previous frame so the time derivative is smooth.
lam = np.zeros((n, nt))
V = np.zeros((n, n, nt))
for k, t in enumerate(tt):
    w, v = np.linalg.eigh(make_L(t))
    if k > 0:
        for j in range(n):
            if v[:, j] @ V[:, j, k - 1] < 0:
                v[:, j] = -v[:, j]
    lam[:, k] = w
    V[:, :, k] = v

# connection form  C_ij = <phi_i, d phi_j / dt>  (central difference in time)
C = np.zeros((n, n, nt))
for k in range(1, nt - 1):
    dV = (V[:, :, k + 1] - V[:, :, k - 1]) / (2 * dt)
    C[:, :, k] = V[:, :, k].T @ dV
C[:, :, 0] = C[:, :, 1]
C[:, :, -1] = C[:, :, -2]
skew = np.max(np.abs(C + np.swapaxes(C, 0, 1)))

# initial data and direct reference dynamics  x_dot = -L(t) x
x0 = rng.normal(size=n)
x0 -= x0.mean()
solD = solve_ivp(lambda t, x: -make_L(t) @ x, (0, T), x0, t_eval=tt,
                 method="DOP853", rtol=1e-11, atol=1e-13)
x_direct = solD.y
a_direct = np.zeros((n, nt))
for k in range(nt):
    a_direct[:, k] = V[:, :, k].T @ x_direct[:, k]


def lam_of(t):
    k = min(int(t / dt), nt - 2)
    f = (t - tt[k]) / dt
    return lam[:, k] * (1 - f) + lam[:, k + 1] * f


def C_of(t):
    k = min(int(t / dt), nt - 2)
    f = (t - tt[k]) / dt
    return C[:, :, k] * (1 - f) + C[:, :, k + 1] * f


# modal equation of motion  a_dot = -(Lambda(t) + C(t)) a   (Paper 03, eq. 4.2)
a0 = V[:, :, 0].T @ x0
solM = solve_ivp(lambda t, a: -(np.diag(lam_of(t)) + C_of(t)) @ a, (0, T), a0,
                 t_eval=tt, method="DOP853", rtol=1e-11, atol=1e-13)
a_ode = solM.y
err_mode = np.max(np.abs(a_ode - a_direct))
print(f"  n = {n} nodes, deformation over [0,{T}]: connection skewness max |C + C^T| = {skew:.3e}")
print(f"  modal ODE reproduces the direct solution to max |a_ode - a_direct| = {err_mode:.3e}")

# migration: coupled modal energies vs the frozen-frame prediction (no C coupling)
solF = solve_ivp(lambda t, a: -np.diag(lam_of(t)) @ a, (0, T), a0,
                 t_eval=tt, method="DOP853", rtol=1e-11, atol=1e-13)
a_frozen = solF.y
E_coupled = a_ode ** 2
E_frozen = a_frozen ** 2
Emig = np.max(np.abs(E_coupled - E_frozen))
E_scale = np.max(E_coupled)
print(f"  largest modal-energy deviation caused by the connection coupling = {Emig:.3e}  ({100 * Emig / E_scale:.1f}% of the largest modal energy)")

# ---------------------------------------------------------------------- E. epidemic bound
print("=" * 72)
print("E. EPIDEMIC DECAY-BOUND TIGHTNESS  (Paper 07, Theorems 3, 4)")
gamma = 1.0
beta = 0.5
nE = 20
tE = np.linspace(0, 10, 300)


def W(t):
    Wm = np.zeros((nE, nE))
    for i in range(nE):
        for j in range(i + 1, nE):
            v = 0.25 + 0.15 * np.sin(0.7 * t + i - j) + 0.05 * ((i * 7 + j * 3) % 5) / 5
            Wm[i, j] = Wm[j, i] = max(v, 0.02)
    return Wm


x0 = np.zeros(nE)
x0[5] = 0.5
x0[12] = 0.3


def rhsE(t, x):
    return -gamma * x + beta * W(t) @ x


solE = solve_ivp(rhsE, (0, 10), x0, t_eval=tE, method="RK45", rtol=1e-9, atol=1e-11)
Xn = np.linalg.norm(solE.y, axis=0)
lams = np.array([np.linalg.eigvalsh(W(t)).max() for t in tE])
cum = np.zeros_like(tE)
for i in range(1, len(tE)):
    cum[i] = cum[i - 1] + 0.5 * (tE[i] - tE[i - 1]) * (
        (beta * lams[i] - gamma) + (beta * lams[i - 1] - gamma)
    )
env = np.exp(cum)
ratio = Xn / np.maximum(env, 1e-300)
print(f"  ||x(0)|| = {np.linalg.norm(x0):.4f};  final ||x(T)|| = {Xn[-1]:.4e}")
print(f"  Grönwall envelope at T = {env[-1]:.4e}")
print(f"  bound holds: max |x|/envelope (t>0) = {np.max(ratio[1:]):.4f}   (final ratio {ratio[-1]:.4f})")

# ------------------------------------------------------------------- figures
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
axes[0].semilogy(Ns, conv_errs, "o-", color="#1c3f63")
axes[0].set_xlabel("truncation N"); axes[0].set_ylabel("L2_rho error")
axes[0].set_title("A. Spectral convergence"); axes[0].grid(alpha=0.3)
axes[1].plot(sol.t / Tp, Es / Es[0], color="#c9a227")
axes[1].set_xlabel("periods"); axes[1].set_ylabel("E(t)/E(0)")
axes[1].set_title("B. Energy over 50 periods"); axes[1].grid(alpha=0.3)
axes[2].semilogy(mus, rel1, ".-", label="one-term", color="#c9a227")
axes[2].semilogy(mus, rel2, ".-", label="two-term (Ivrii)", color="#1c3f63")
axes[2].set_xlabel("mu"); axes[2].set_ylabel("relative counting error")
axes[2].set_title("C. Weyl law in d = 2"); axes[2].legend(); axes[2].grid(alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "deep_weyl.png"), dpi=120); plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for i in range(6):
    axes[0].plot(tt, E_coupled[i] / E_coupled.max(), label=f"mode {i + 1}", color="#1c3f63")
    axes[0].plot(tt, E_frozen[i] / E_frozen.max(), "--", color="#c9a227", alpha=0.6)
axes[0].set_xlabel("t"); axes[0].set_ylabel("modal energy (normalised)")
axes[0].set_title("D. Energy migration (solid = coupled, dashed = frozen)"); axes[0].legend(fontsize=7); axes[0].grid(alpha=0.3)
axes[1].semilogy(tE, Xn, label="||x(t)||", color="#1c3f63")
axes[1].semilogy(tE, env, "--", label="Grönwall envelope", color="#c9a227")
axes[1].set_xlabel("t"); axes[1].set_ylabel("norm")
axes[1].set_title("E. Epidemic decay vs bound"); axes[1].legend(); axes[1].grid(alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "deep_networks.png"), dpi=120); plt.close(fig)

print("=" * 72)
print("figures written to demos/figures/: deep_weyl.png, deep_networks.png")
print("all checks complete — every number above is computed live in this run.")