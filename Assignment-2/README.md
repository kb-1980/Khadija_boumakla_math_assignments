# Assignment 2: Numerical Interpolation (Lagrange, Newton, and Hermite)


## 📌 Introduction & Work Summary

This second assignment studies and compares three polynomial interpolation methods (**Lagrange**, **Newton**, and **Hermite**) applied to two functions with very different behaviors on the interval $[-4, 4]$:
1. The exponential function $f(x) = e^x$
2. Runge's function $f(x) = \frac{1}{1 + x^2}$

---

## 💻 Project Structure & File Links

- [`./interpolation.py`](./interpolation.py): Contains the implementation of algorithms computing the coefficients:
  - `computePL`: Lagrange formulation.
  - `compute_pN`: Newton divided differences.
  - `compute_pH`: Hermite interpolation (incorporating both function values and derivatives).
- [`./main.py`](./main.py): Main script generating the mesh grid, evaluating polynomials, and plotting the $2 \times 3$ comparative graph grid.

---

## 📊 Results Analysis & Graphical Comparison

### 1. Equivalence Between Lagrange and Newton
- **Observation:** The curves for Lagrange and Newton are perfectly identical for all values of $N$, confirming the uniqueness of the interpolating polynomial.

### 2. Behavior on the Exponential Function
- **Observation:** As the number of nodes $N$ increases ($N = 3, 5, 9, 13$), the interpolation error rapidly decreases across the entire interval $[-4, 4]$.

### 3. Runge's Phenomenon on Rational Functions
- **Observation:** Near the center of the interval ($x \approx 0$), interpolation becomes highly accurate as $N$ grows. However, **near the boundaries ($x \approx -4$ and $x \approx 4$)**, polynomials develop severe oscillations that amplify significantly for $N = 9$ and $N = 13$.

### 4. Contribution of Hermite Interpolation
- **Observation:** Hermite interpolation provides a superior approximation around the peak of the curve (at $x = 0$), even with smaller values of $N$.

