"""Structure-Flow Calculus (SFC) — core module.

This package provides the foundational objects of the Structure-Flow Calculus:
the structure field rho, the transport map tau, the rho-derivative D_rho,
the structure Laplacian L_rho, and associated spectral quantities.

All arrays are NumPy ndarrays unless otherwise noted.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.floating]


def structure_field(
    x: FloatArray,
    rho0: float = 1.0,
    kappa: float = 2.0,
    profile: str = "exponential",
) -> FloatArray:
    """Evaluate the structure field rho(x) on a grid.

    Args:
        x: Grid points in [a, b].
        rho0: Base density value.
        kappa: Gradient parameter.
        profile: One of {"exponential", "linear", "power", "grin"}.

    Returns:
        rho(x) > 0 evaluated at each grid point.
    """
    x = np.asarray(x, dtype=float)
    if profile == "exponential":
        return rho0 * np.exp(kappa * x)
    if profile == "linear":
        return rho0 * (1.0 + kappa * x)
    if profile == "power":
        return rho0 * (1.0 + kappa * x) ** 0.5
    if profile == "grin":
        return rho0 * (1.0 - (x / (x[-1] + 1e-12)) ** 2)
    raise ValueError(f"Unknown profile: {profile!r}")


def transport_map(
    x: FloatArray,
    rho: FloatArray | None = None,
    *,
    rho0: float = 1.0,
    kappa: float = 2.0,
    profile: str = "exponential",
) -> tuple[FloatArray, float]:
    """Compute the transport coordinate tau(x) and structural length Lambda.

    The transport map is tau(x) = int_a^x dt / rho(t).  It is a C^2
    diffeomorphism from [a, b] onto [0, Lambda], where
    Lambda = int_a^b dt / rho(t).

    Args:
        x: Grid points in [a, b].
        rho: Precomputed rho(x).  If None, computed from parameters.
        rho0, kappa, profile: Parameters passed to structure_field().

    Returns:
        tau: Transport coordinate at each grid point.
        Lambda: Total structural length.
    """
    x = np.asarray(x, dtype=float)
    if rho is None:
        rho = structure_field(x, rho0=rho0, kappa=kappa, profile=profile)

    dx = np.diff(x)
    rho_mid = 0.5 * (rho[:-1] + rho[1:])
    dtau = dx / rho_mid
    tau = np.concatenate([[0.0], np.cumsum(dtau)])
    Lambda = float(tau[-1])
    return tau, Lambda


def D_rho(
    f: FloatArray,
    x: FloatArray,
    rho: FloatArray,
    h: float = 1e-4,
) -> FloatArray:
    """Compute the rho-derivative D_rho f = rho * df/dx via centred differences.

    Args:
        f: Function values on the grid.
        x: Grid points (must be uniformly spaced).
        rho: Structure field values.
        h: Step size for finite differences.

    Returns:
        D_rho f evaluated at interior points.
    """
    x = np.asarray(x, dtype=float)
    f = np.asarray(f, dtype=float)
    rho = np.asarray(rho, dtype=float)
    if len(f) != len(x) or len(rho) != len(x):
        raise ValueError("f, rho, and x must have the same length.")

    dfdx = np.zeros_like(f)
    dfdx[1:-1] = (f[2:] - f[:-2]) / (2.0 * (x[2] - x[1]))
    dfdx[0] = (f[1] - f[0]) / (x[1] - x[0])
    dfdx[-1] = (f[-1] - f[-2]) / (x[-1] - x[-2])
    return rho * dfdx


def L_rho_fd(
    u: FloatArray,
    x: FloatArray,
    rho: FloatArray,
) -> FloatArray:
    """Finite-difference approximation of the structure Laplacian L_rho u.

    Uses the midpoint-flux divergence form:
        L_rho u = rho * d/dx (rho * du/dx)

    Args:
        u: Field values on the grid.
        x: Uniform grid points.
        rho: Structure field values at grid points.

    Returns:
        L_rho u evaluated at interior points (zero at boundaries).
    """
    u = np.asarray(u, dtype=float)
    x = np.asarray(x, dtype=float)
    rho = np.asarray(rho, dtype=float)

    if len(u) < 3 or len(x) < 3 or len(rho) < 3:
        raise ValueError("Need at least 3 grid points.")
    if len({len(u), len(x), len(rho)}) != 1:
        raise ValueError("u, x, and rho must have the same length.")

    h = x[1] - x[0]
    rho_face = 0.5 * (rho[:-1] + rho[1:])
    flux = rho_face * (u[1:] - u[:-1]) / h

    L = np.zeros_like(u)
    rho_node = rho[1:-1]
    L[1:-1] = rho_node * (flux[1:] - flux[:-1]) / h
    return L


def inner_rho(
    f: FloatArray,
    g: FloatArray,
    rho: FloatArray,
    x: FloatArray,
    method: str = "trapezoid",
) -> float:
    """Compute the rho-weighted inner product <f, g>_rho.

    <f, g>_rho = int_a^b f(x) g(x) / rho(x) dx.

    Args:
        f, g: Function values on the grid.
        rho: Structure field values.
        x: Grid points.
        method: Integration method {"trapezoid", "simpson"}.

    Returns:
        Inner product value.
    """
    f = np.asarray(f, dtype=float)
    g = np.asarray(g, dtype=float)
    rho = np.asarray(rho, dtype=float)
    x = np.asarray(x, dtype=float)

    integrand = f * g / rho
    if method == "trapezoid":
        return float(np.trapezoid(integrand, x))
    if method == "simpson":
        from scipy.integrate import simpson

        return float(simpson(integrand, x))
    raise ValueError(f"Unknown method: {method!r}")


def discrete_energy(
    u: FloatArray,
    v: FloatArray,
    x: FloatArray,
    rho: FloatArray,
) -> float:
    """Compute the discrete energy E = 1/2 int (v^2 + (D_rho u)^2) d(rho).

    Args:
        u: Displacement field.
        v: Velocity field (time derivative of u).
        x: Grid points.
        rho: Structure field values.

    Returns:
        Total energy.
    """
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    x = np.asarray(x, dtype=float)
    rho = np.asarray(rho, dtype=float)

    h = x[1] - x[0]
    rho_face = 0.5 * (rho[:-1] + rho[1:])
    flux = rho_face * (u[1:] - u[:-1]) / h
    kin = 0.5 * np.trapezoid(v ** 2 / rho, x)
    pot = 0.5 * np.trapezoid(flux ** 2 / rho_face, x[:-1])
    return float(kin + pot)


def modal_coefficients(
    u: FloatArray,
    phi: FloatArray,
    rho: FloatArray,
    x: FloatArray,
) -> FloatArray:
    """Project u onto the modal basis {phi_m}.

    hat u_m = <u, phi_m>_rho.

    Args:
        u: Field to project.
        phi: Modal basis functions (n_modes, n_points) or (n_points, n_modes).
        rho: Structure field values.
        x: Grid points.

    Returns:
        Modal coefficients.
    """
    u = np.asarray(u, dtype=float)
    rho = np.asarray(rho, dtype=float)
    x = np.asarray(x, dtype=float)

    phi = np.asarray(phi, dtype=float)
    if phi.ndim == 1:
        phi = phi[:, np.newaxis]

    # Ensure phi is (n_modes, n_points)
    if phi.shape[0] == len(x):
        phi = phi.T

    n_modes = phi.shape[0]
    coeffs = np.zeros(n_modes)
    for m in range(n_modes):
        coeffs[m] = inner_rho(u, phi[m], rho, x)
    return coeffs
