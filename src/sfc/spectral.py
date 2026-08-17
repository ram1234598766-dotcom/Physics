"""Spectral theory for the Structure-Flow Laplacian.

Provides closed-form eigenfunctions, eigenvalues, and spectral projections
for the 1D structure Laplacian on [a, b] with Dirichlet boundary conditions.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from .core import structure_field, transport_map

FloatArray = NDArray[np.floating]


def eigenfunction(
    x: FloatArray,
    m: int,
    tau: FloatArray,
    Lambda: float,
) -> FloatArray:
    """m-th Dirichlet eigenfunction of L_rho in transport coordinates.

    phi_m(x) = sqrt(2/Lambda) * sin(m * pi * tau(x) / Lambda).

    Args:
        x: Physical grid points.
        m: Mode index (1, 2, 3, ...).
        tau: Transport coordinate tau(x).
        Lambda: Structural length.

    Returns:
        Eigenfunction values at x.
    """
    return np.sqrt(2.0 / Lambda) * np.sin(m * np.pi * tau / Lambda)


def eigenvalue(m: int, Lambda: float) -> float:
    """m-th Dirichlet eigenvalue of -L_rho.

    mu_m = (m * pi / Lambda)^2.

    Args:
        m: Mode index.
        Lambda: Structural length.

    Returns:
        Eigenvalue mu_m.
    """
    return (m * np.pi / Lambda) ** 2


def spectral_projection(
    f: FloatArray,
    M: int,
    x: FloatArray,
    rho: FloatArray,
    *,
    profile: str = "exponential",
    rho0: float = 1.0,
    kappa: float = 2.0,
) -> tuple[FloatArray, FloatArray]:
    """Project f onto the first M eigenfunctions of L_rho.

    f_M(x) = sum_{m=1}^M <f, phi_m>_rho * phi_m(x).

    Args:
        f: Function values on the grid.
        M: Number of modes to keep.
        x: Physical grid points.
        rho: Structure field values.
        profile, rho0, kappa: Structure field parameters.

    Returns:
        f_M: Spectral projection.
        coeffs: Modal coefficients <f, phi_m>_rho.
    """
    x = np.asarray(x, dtype=float)
    f = np.asarray(f, dtype=float)
    rho = np.asarray(rho, dtype=float)

    tau, Lambda = transport_map(x, rho=rho, profile=profile, rho0=rho0, kappa=kappa)

    coeffs = np.zeros(M)
    for m in range(1, M + 1):
        phi_m = eigenfunction(x, m, tau, Lambda)
        # inner_rho from core
        from .core import inner_rho

        coeffs[m - 1] = inner_rho(f, phi_m, rho, x)

    f_M = np.zeros_like(f)
    for m in range(1, M + 1):
        phi_m = eigenfunction(x, m, tau, Lambda)
        f_M += coeffs[m - 1] * phi_m

    return f_M, coeffs


def weyl_count_2d(
    mu_max: float,
    L: float,
) -> int:
    """Count Dirichlet eigenvalues below mu_max for a square box [0, L]^2.

    N(mu) = #{(m1, m2) : (m1^2 + m2^2) * (pi/L)^2 <= mu}.

    Args:
        mu_max: Maximum eigenvalue.
        L: Side length of the box.

    Returns:
        Exact eigenvalue count.
    """
    m_max = int(np.floor(np.sqrt(mu_max) * L / np.pi)) + 2
    count = 0
    for m1 in range(1, m_max + 1):
        for m2 in range(1, m_max + 1):
            if (m1 * np.pi / L) ** 2 + (m2 * np.pi / L) ** 2 <= mu_max:
                count += 1
    return count
