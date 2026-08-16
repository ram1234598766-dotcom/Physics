# Demos

All demos require Python 3 with `pip install -r demos/requirements.txt`. Run from the repo root.

| Demo | Verifies | Run |
|---|---|---|
| `verify_calculus.py` | Paper 1: Fundamental Theorem, Leibniz, adjoint, self-adjointness, eigenvalues | `python demos/verify_calculus.py` |
| `graded_wave.py` | Papers 2/4: closed-form modes, evolution, energy | `python demos/graded_wave.py` |
| `power_grid_mode_migration.py` | Paper 3: skew connection, spectral flow, energy migration | `python demos/power_grid_mode_migration.py` |
| `epidemic_decay_bound.py` | Paper 3: mass, connectivity bound, Grönwall bound | `python demos/epidemic_decay_bound.py` |

Plots are saved to `demos/figures/`. Each demo exits non-zero on failure, so they double as tests.
