# Demos

Four runnable scripts turn the central theorems of the program into numbers. Each prints a verdict and exits non-zero on failure, so the demos double as regression tests.

**Requirements:** Python 3 with `pip install -r demos/requirements.txt`. Run from the repo root.

| Demo | Verifies | Run |
|---|---|---|
| `verify_calculus.py` | Paper 01: Fundamental Theorem, Leibniz rule, adjoint pair, self-adjointness, eigenvalues | `python demos/verify_calculus.py` |
| `graded_wave.py` | Papers 02/04: closed-form modes, evolution, energy conservation | `python demos/graded_wave.py` |
| `power_grid_mode_migration.py` | Paper 03: skew connection, spectral flow, energy migration | `python demos/power_grid_mode_migration.py` |
| `epidemic_decay_bound.py` | Paper 03: mass, algebraic-connectivity bound, Grönwall bound | `python demos/epidemic_decay_bound.py` |

Plots are saved to `demos/figures/`.
