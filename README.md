# scientific_core

A small, dependency-light collection of core numerical routines for
education and compact scientific computing workflows. The project
provides lightweight implementations of linear algebra building
blocks and basic optimization algorithms intended for learning,
experimentation, and small-scale projects.

Contents
- src/: library source modules (e.g. `linalg.py`, `optimization.py`)
- tests/: unit tests for core functionality
- notebooks/: short experiments and examples
- requirements.txt, pyproject.toml: packaging / dependencies

Quick start

1. Create a virtual environment and install requirements:

	 python -m venv .venv
	 .venv\Scripts\activate    # Windows
	 pip install -r requirements.txt

2. Run tests:

	 pytest

3. Use the library in your code or interactive session:

	 from src import linalg
	 a = [1, 2, 3]
	 b = [4, 5, 6]
	 print(linalg.vector_dot(a, b))

API (high level)

`linalg.py` - small collection of linear algebra helpers:
- `vector_dot(a, b)` — dot product of two vectors
- `norm(x, order=2)` — vector norm (L1, L2, etc.)
- `matmul(A, B)` — matrix multiplication
- `transpose(A)` — matrix transpose
- `identity(n)` — identity matrix of size `n`
- `solve_linear_system(A, b)` — simple solver (Gaussian elimination / LU)
- `inverse(A)` — matrix inverse (via solver)
- `determinant(A)` — determinant computation
- `qr_decomposition(A)` — QR decomposition (useful for least squares / PCA)
- `eigen_power_iteration(A)` — power iteration for dominant eigenpair

`optimization.py` - basic optimization utilities:
- `numerical_gradient(f, x, eps=1e-6)` — finite-difference gradient
- `gradient_descent(f, grad, x0, lr=0.01, max_iter=1000, tol=1e-6)`
	— simple gradient descent loop
- Additional helpers: batch / stochastic gradient descent, conjugate
	gradient (may be present as experimental implementations)

Development notes
- Keep implementations readable and well-tested rather than highly
	optimized — the goal is pedagogy and clarity.
- Add unit tests under `tests/` when extending the API.

Contributing
- Open an issue or submit a pull request with tests and a short
	description of the change.

License
- No license specified. Add a `LICENSE` file if you want to set one.

Contact
- For questions or contributions, open an issue on the repository.
