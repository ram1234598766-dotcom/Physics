"""Structure-Flow Calculus (SFC) — professional package.

This package provides the core mathematical objects and numerical routines
for the Structure-Flow Calculus framework:

- ``core``: structure field, transport map, rho-derivative, Laplacian
- ``spectral``: closed-form eigenfunctions, eigenvalues, Weyl counting
- ``network``: graph Laplacians, eigenframe alignment, energy migration
- ``utils``: grid utilities, integration helpers
"""

from __future__ import annotations

from .core import (
    D_rho,
    FloatArray,
    L_rho_fd,
    discrete_energy,
    inner_rho,
    modal_coefficients,
    structure_field,
    transport_map,
)
from .network import (
    aligned_eigenframes,
    build_laplacian,
    eigenframe_connection,
    modal_energy_migration,
)
from .spectral import eigenfunction, eigenvalue, spectral_projection, weyl_count_2d
from .utils import ensure_uniform_grid, trapz

__all__ = [
    "FloatArray",
    "structure_field",
    "transport_map",
    "D_rho",
    "L_rho_fd",
    "inner_rho",
    "discrete_energy",
    "modal_coefficients",
    "eigenfunction",
    "eigenvalue",
    "spectral_projection",
    "weyl_count_2d",
    "build_laplacian",
    "aligned_eigenframes",
    "eigenframe_connection",
    "modal_energy_migration",
    "ensure_uniform_grid",
    "trapz",
]

__version__ = "0.1.0"
