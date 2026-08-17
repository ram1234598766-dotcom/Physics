"""Utility functions for Structure-Flow Calculus."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.floating]


def ensure_uniform_grid(
    x: FloatArray,
    tol: float = 1e-12,
) -> tuple[FloatArray, float]:
    """Verify that x is a uniform grid and return (x, h).

    Args:
        x: Grid points.
        tol: Tolerance for uniformity check.

    Returns:
        x: The input grid.
        h: Uniform spacing.

    Raises:
        ValueError: If the grid is not uniform.
    """
    x = np.asarray(x, dtype=float)
    h = np.diff(x)
    if np.max(np.abs(h - h[0])) > tol:
        raise ValueError("Grid is not uniform.")
    return x, float(h[0])


def trapz(y: FloatArray, x: FloatArray | None = None) -> float:
    """Trapezoidal integration, compatible with old and new NumPy.

    Args:
        y: Function values.
        x: Grid points.  If None, uses unit spacing.

    Returns:
        Integral value.
    """
    y = np.asarray(y, dtype=float)
    if x is None:
        return float(np.trapezoid(y) if hasattr(np, "trapezoid") else np.trapz(y))
    x = np.asarray(x, dtype=float)
    return float(np.trapezoid(y, x) if hasattr(np, "trapezoid") else np.trapz(y, x))
