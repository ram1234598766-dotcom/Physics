"""Numerical verification of the rho-calculus identities of Paper 1.

Checks:
  (1) Fundamental Theorem: D_rho F = f, where F(x) = int_a^x f d(rho).
  (2) Leibniz product rule.
  (3) Adjoint property: <D_rho f, g>_rho = -<f, D_rho g>_rho (vanishing BCs).
  (4) Self-adjointness of L_rho = D_rho^2.
  (5) Eigenvalue relation L_rho phi_m = -(m*pi/Lambda)^2 phi_m.
"""
import numpy as np

if hasattr(np, "trapezoid"):
    trapz = np.trapezoid
else:
    trapz = np.trapz

A, B = 0.0, 1.0
RHO0, KAPPA = 2.0, 0.3


def rho(x):
    return RHO0 + KAPPA * x


def Lambda():
    xs = np.linspace(A, B, 200001)
    return trapz(1.0 / rho(xs), xs)


def D_rho(f, x, h=1e-4):
    return rho(x) * (f(x + h) - f(x - h)) / (2 * h)


def rho_integral(f, a, b, n=60001):
    xs = np.linspace(a, b, n)
    return trapz(f(xs) / rho(xs), xs)


def inner_rho(f, g, n=200001):
    xs = np.linspace(A, B, n)
    return trapz(f(xs) * g(xs) / rho(xs), xs)


def L_rho(f, x, h=1e-4):
    p1 = rho(x - h) * (f(x) - f(x - 2 * h)) / (2 * h)
    p2 = rho(x + h) * (f(x + 2 * h) - f(x)) / (2 * h)
    return rho(x) * (p2 - p1) / (2 * h)


def tau(x):
    return (1.0 / KAPPA) * np.log(rho(x) / RHO0)


def check_fundamental_theorem():
    f = np.sin
    F = lambda x: rho_integral(f, A, x)
    xs = np.linspace(A + 2e-3, B - 2e-3, 50)
    return max(abs(D_rho(F, x) - f(x)) for x in xs)


def check_product_rule():
    f = lambda x: np.sin(2 * x)
    g = lambda x: np.cos(3 * x)
    xs = np.linspace(A + 1e-4, B - 1e-4, 100)
    return max(
        abs(D_rho(lambda x: f(x) * g(x), x) - (D_rho(f, x) * g(x) + f(x) * D_rho(g, x)))
        for x in xs
    )


def check_adjoint():
    f = lambda x: np.sin(np.pi * x)
    g = lambda x: np.cos(np.pi * x + np.pi / 2)
    lhs = inner_rho(lambda x: D_rho(f, x), g)
    rhs = inner_rho(f, lambda x: D_rho(g, x))
    return abs(lhs + rhs)


def check_laplacian_self_adjoint():
    f = lambda x: np.sin(2 * np.pi * x)
    g = lambda x: np.sin(np.pi * x)
    lhs = inner_rho(lambda x: L_rho(f, x), g)
    rhs = inner_rho(f, lambda x: L_rho(g, x))
    return abs(lhs - rhs)


def check_eigenvalue():
    Lam = Lambda()
    m = 2
    mu = (m * np.pi / Lam) ** 2
    phim = lambda x: np.sqrt(2 / Lam) * np.sin(m * np.pi * tau(x) / Lam)
    xs = np.linspace(A + 2e-3, B - 2e-3, 60)
    return max(abs(L_rho(phim, x) + mu * phim(x)) for x in xs)


def main():
    tol = 5e-3
    results = {
        "fundamental theorem": check_fundamental_theorem(),
        "product rule": check_product_rule(),
        "adjoint": check_adjoint(),
        "laplacian self-adjoint": check_laplacian_self_adjoint(),
        "eigenvalue relation": check_eigenvalue(),
    }
    for name, err in results.items():
        status = "PASS" if err < tol else "FAIL"
        print(f"[{status}] {name}: max error = {err:.3e}")
    assert all(err < tol for err in results.values()), "verification failed"
    print("All rho-calculus identities verified numerically.")


if __name__ == "__main__":
    main()
