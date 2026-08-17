"""Network-theoretic utilities for Structure-Flow Calculus.

Provides graph Laplacian construction, eigenframe alignment,
and energy-migration diagnostics for time-varying networks.
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

FloatArray = NDArray[np.floating]


def build_laplacian(
    n: int,
    edges: list[tuple[int, int]],
    weights: FloatArray,
) -> FloatArray:
    """Build a symmetric graph Laplacian from edge list and weights.

    L = D - W, where W is the weighted adjacency matrix.

    Args:
        n: Number of nodes.
        edges: List of (i, j) edges.
        weights: Weight for each edge.

    Returns:
        Laplacian matrix (n, n).
    """
    W = np.zeros((n, n))
    for (i, j), w in zip(edges, weights):
        W[i, j] = W[j, i] = w
    D = np.diag(W.sum(axis=1))
    return D - W


def aligned_eigenframes(
    L_t: list[FloatArray],
) -> tuple[FloatArray, FloatArray]:
    """Compute eigenframes aligned continuously in time.

    Each eigenvector is defined up to sign; this function chooses the sign
    at each time step to maximise overlap with the previous frame.

    Args:
        L_t: List of Laplacian matrices at each time step.

    Returns:
        eigenvalues: (n, nt) array of eigenvalues.
        eigenvectors: (n, n, nt) array of aligned eigenvectors.
    """
    n = L_t[0].shape[0]
    nt = len(L_t)
    eigenvalues = np.zeros((n, nt))
    eigenvectors = np.zeros((n, n, nt))

    for k, L in enumerate(L_t):
        w, v = np.linalg.eigh(L)
        if k > 0:
            for j in range(n):
                if v[:, j] @ eigenvectors[:, j, k - 1] < 0:
                    v[:, j] = -v[:, j]
        eigenvalues[:, k] = w
        eigenvectors[:, :, k] = v

    return eigenvalues, eigenvectors


def eigenframe_connection(
    eigenvectors: FloatArray,
    dt: float,
) -> FloatArray:
    """Compute the skew-symmetric eigenframe connection C_{jk}.

    C_{jk} = <phi_j, d/dt phi_k> approx <phi_j(t), (phi_k(t+dt)-phi_k(t-dt))/(2dt)>.

    Args:
        eigenvectors: (n, n, nt) aligned eigenframes.
        dt: Time step.

    Returns:
        C: (nt, n, n) connection matrices.
    """
    n, _, nt = eigenvectors.shape
    C = np.zeros((nt, n, n))
    for k in range(1, nt - 1):
        d_phi = (eigenvectors[:, :, k + 1] - eigenvectors[:, :, k - 1]) / (2.0 * dt)
        C[k] = eigenvectors[:, :, k].T @ d_phi
    return C


def modal_energy_migration(
    a: FloatArray,
    C: FloatArray,
    eigenvalues: FloatArray,
    dt: float,
) -> tuple[FloatArray, FloatArray]:
    """Compute modal energy and its rate of change.

    E_j(t) = |a_j(t)|^2.
    dE_j/dt = -2 lambda_j E_j - 2 sum_k C_{jk} a_j a_k.

    Args:
        a: (nt, n) modal coefficients.
        C: (nt, n, n) connection matrices.
        eigenvalues: (n, nt) eigenvalues.
        dt: Time step.

    Returns:
        E: (nt, n) modal energies.
        dE_dt: (nt, n) energy rates.
    """
    nt, n = a.shape
    E = a ** 2
    dE_dt = np.zeros_like(E)
    for k in range(nt):
        for j in range(n):
            dE_dt[k, j] = -2.0 * eigenvalues[j, k] * E[k, j]
            dE_dt[k, j] -= 2.0 * np.sum(C[k, j, :] * a[k, :] * a[k, j])
    return E, dE_dt
