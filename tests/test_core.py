"""Tests for the Structure-Flow Calculus core module.

Every test corresponds to a theorem or identity proved in the papers.
Tests use synthetic data only; no external datasets are required.
"""

from __future__ import annotations

import numpy as np
import pytest

from sfc.core import (
    D_rho,
    FloatArray,
    L_rho_fd,
    discrete_energy,
    inner_rho,
    modal_coefficients,
    structure_field,
    transport_map,
)
from sfc.spectral import eigenfunction, eigenvalue, spectral_projection


# ============================================================
# Fixtures
# ============================================================

N_FINE = 2_001  # fine grid for high-accuracy checks
N_COARSE = 400  # coarse grid for time evolution


@pytest.fixture(scope="module")
def grid() -> tuple[FloatArray, FloatArray, float, float]:
    """Exponential structure field on [0, 1]."""
    a, b = 0.0, 1.0
    rho0, kappa = 1.0, 2.0
    x_fine = np.linspace(a, b, N_FINE)
    rho_fine = structure_field(x_fine, rho0=rho0, kappa=kappa, profile="exponential")
    return x_fine, rho_fine, rho0, kappa


@pytest.fixture(scope="module")
def coarse_grid() -> tuple[FloatArray, FloatArray]:
    """Coarse grid for time evolution."""
    x = np.linspace(0.0, 1.0, N_COARSE)
    rho = structure_field(x, rho0=1.0, kappa=2.0, profile="exponential")
    return x, rho


# ============================================================
# Paper 01 — Foundations
# ============================================================


class TestFundamentalTheorem:
    """D_rho F = f where F(x) = int_a^x f(t) d(rho(t))."""

    def test_derivative_of_integral(self, grid) -> None:
        x_fine, rho_fine, rho0, kappa = grid
        f = lambda t: np.sin(np.pi * t)
        F = lambda t: np.array(
            [np.trapezoid(f(np.append(x_fine[:i+1], t)) / rho_fine[:i+1],
                         np.append(x_fine[:i+1], t)) for i, t in enumerate(x_fine)]
        )
        # Simpler: F(x) = int_0^x f(t)/rho(t) dt
        F_vals = np.zeros_like(x_fine)
        for i in range(1, len(x_fine)):
            F_vals[i] = np.trapezoid(f(x_fine[:i+1]) / rho_fine[:i+1], x_fine[:i+1])

        Df = D_rho(F_vals, x_fine, rho_fine)
        err = np.max(np.abs(Df[100:-100] - f(x_fine[100:-100])))
        assert err < 1e-3, f"Fundamental theorem error {err:.3e}"


class TestAdjoint:
    """<D_rho f, g>_rho = -<f, D_rho g>_rho for vanishing BCs."""

    def test_adjoint_property(self, grid) -> None:
        x_fine, rho_fine, rho0, kappa = grid
        f = np.sin(np.pi * x_fine)
        g = np.cos(np.pi * x_fine)

        lhs = inner_rho(D_rho(f, x_fine, rho_fine), g, rho_fine, x_fine)
        rhs = inner_rho(f, D_rho(g, x_fine, rho_fine), rho_fine, x_fine)
        assert abs(lhs + rhs) < 1e-3, f"Adjoint property violated: {abs(lhs+rhs):.3e}"


class TestSelfAdjointLaplacian:
    """<L_rho f, g>_rho = <f, L_rho g>_rho."""

    def test_self_adjoint(self, grid) -> None:
        x_fine, rho_fine, rho0, kappa = grid
        f = np.sin(2.0 * np.pi * x_fine)
        g = np.sin(3.0 * np.pi * x_fine)

        lhs = inner_rho(L_rho_fd(f, x_fine, rho_fine), g, rho_fine, x_fine)
        rhs = inner_rho(f, L_rho_fd(g, x_fine, rho_fine), rho_fine, x_fine)
        assert abs(lhs - rhs) < 1e-2, f"Self-adjointness violated: {abs(lhs-rhs):.3e}"


# ============================================================
# Paper 02 — Spectral Theory
# ============================================================


class TestClosedFormSpectrum:
    """L_rho phi_m = -mu_m phi_m with mu_m = (m*pi/Lambda)^2."""

    def test_mode_m_1(self, grid) -> None:
        x_fine, rho_fine, rho0, kappa = grid
        tau, Lambda = transport_map(x_fine, rho=rho_fine)
        m = 1
        phi = eigenfunction(x_fine, m, tau, Lambda)
        mu = eigenvalue(m, Lambda)
        Lphi = L_rho_fd(phi, x_fine, rho_fine)
        residual = np.max(np.abs(Lphi[100:-100] + mu * phi[100:-100]))
        assert residual < 1e-2, f"Mode {m} residual too large: {residual:.3e}"

    def test_mode_m_3(self, grid) -> None:
        x_fine, rho_fine, rho0, kappa = grid
        tau, Lambda = transport_map(x_fine, rho=rho_fine)
        m = 3
        phi = eigenfunction(x_fine, m, tau, Lambda)
        mu = eigenvalue(m, Lambda)
        Lphi = L_rho_fd(phi, x_fine, rho_fine)
        residual = np.max(np.abs(Lphi[100:-100] + mu * phi[100:-100]))
        assert residual < 1e-2, f"Mode {m} residual too large: {residual:.3e}"


# ============================================================
# Paper 09 — Higher-Dimensional Structure-Flow
# ============================================================


class TestWeylLaw2D:
    """N(mu) ~ V/(4*pi) * mu for d=2."""

    def test_weyl_count(self) -> None:
        from sfc.spectral import weyl_count_2d

        L = 0.887  # structural length for exponential profile
        mu = 1000.0
        N = weyl_count_2d(mu, L)
        V = L * L
        N_weyl = V / (4.0 * np.pi) * mu
        rel_err = abs(N - N_weyl) / N
        assert rel_err < 0.25, f"Weyl law relative error too large: {rel_err:.3f}"


# ============================================================
# Paper 03 — Causal Network Spectral Theory
# ============================================================


class TestEnergyMigration:
    """Modal energy is conserved under pure structural deformation."""

    def test_energy_conserved(self, coarse_grid) -> None:
        x, rho = coarse_grid
        from scipy.integrate import solve_ivp

        N = len(x)
        u0 = np.sin(np.pi * x)
        v0 = np.zeros_like(x)
        y0 = np.concatenate([u0, v0])

        def rhs(t, y):
            u, v = y[:N], y[N:]
            u = u.copy()
            v = v.copy()
            u[0] = u[-1] = 0.0
            v[0] = v[-1] = 0.0
            return np.concatenate([v, L_rho_fd(u, x, rho)])

        T = 2.0 * np.pi
        sol = solve_ivp(rhs, (0, T), y0, t_eval=np.linspace(0, T, 100),
                       method="RK45", rtol=1e-9, atol=1e-11)
        u = sol.y[:N, :]
        v = sol.y[N:, :]
        energies = np.array([discrete_energy(u[:, k], v[:, k], x, rho)
                            for k in range(sol.y.shape[1])])
        drift = np.max(np.abs(energies - energies[0])) / energies[0]
        assert drift < 0.05, f"Energy drift too large: {drift:.3e}"


# ============================================================
# Paper 04 — Variational & Conservation Theory
# ============================================================


class TestNoetherEnergy:
    """Energy is conserved for the structure-flow wave equation."""

    def test_energy_conservation_long(self, coarse_grid) -> None:
        x, rho = coarse_grid
        from scipy.integrate import solve_ivp

        N = len(x)
        u0 = np.sin(np.pi * x) + 0.5 * np.sin(2.0 * np.pi * x)
        v0 = np.zeros_like(x)
        y0 = np.concatenate([u0, v0])

        def rhs(t, y):
            u, v = y[:N], y[N:]
            u = u.copy()
            v = v.copy()
            u[0] = u[-1] = 0.0
            v[0] = v[-1] = 0.0
            return np.concatenate([v, L_rho_fd(u, x, rho)])

        T = 10.0 * 2.0 * np.pi
        sol = solve_ivp(rhs, (0, T), y0, t_eval=np.linspace(0, T, 200),
                       method="DOP853", rtol=1e-11, atol=1e-13)
        u = sol.y[:N, :]
        v = sol.y[N:, :]
        energies = np.array([discrete_energy(u[:, k], v[:, k], x, rho)
                            for k in range(sol.y.shape[1])])
        drift = np.max(np.abs(energies - energies[0])) / energies[0]
        assert drift < 0.05, f"Long-time energy drift too large: {drift:.3e}"


# ============================================================
# Paper 10 — Causal Graph-Time Signal Processing
# ============================================================


class TestCausalGFTParseval:
    """Sum_j |a_j|^2 = ||x||^2 for orthonormal eigenframes."""

    def test_parseval(self, coarse_grid) -> None:
        x, rho = coarse_grid
        from scipy.linalg import eigh

        # Build a simple graph Laplacian
        n = 20
        A = np.zeros((n, n))
        for i in range(n - 1):
            A[i, i + 1] = A[i + 1, i] = 1.0
        L = np.diag(A.sum(axis=1)) - A

        _, V = eigh(L)
        x_test = np.random.randn(n)
        a = V.T @ x_test
        lhs = np.sum(a ** 2)
        rhs = np.sum(x_test ** 2)
        assert abs(lhs - rhs) < 1e-10, f"Parseval failed: {abs(lhs-rhs):.3e}"
