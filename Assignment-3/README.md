# Assignment 3: Numerical Integration (Trapezoidal & Simpson's Rules)

## 📌 Introduction & Work Summary

This third assignment studies and compares different **numerical integration** methods to compute the integral of the Gaussian function:
$$I = \int_{0}^{1} e^{-x^2} \, dx \approx 0.74682413$$

### Main Objectives:
1. **Methods Studied:**
   - **Trapezoidal Rule:** Simple formula ($n=1$) and composite formulas ($n=4$ and $n=6$).
   - **Simpson's Rule:** Simple formula ($n=2$) and composite formulas ($n=4$ and $n=6$).
2. **Accuracy Analysis:** Comparison of approximated values and computation of absolute errors relative to the exact value (`scipy.integrate.quad`).

---

## 💻 Project Structure & File Links

- [`./composite_trapzoidal.py`](./composite_trapzoidal.py): Implementation of the composite trapezoidal rule.
- [`./composite_simpson.py`](./composite_simpson.py): Implementation of the composite Simpson's rule.
- [`./main.py`](./main.py): Main script for global evaluation and error comparison.

---

## 📊 Numerical Results Analysis

| Method | Number of Subintervals ($n$) | Approximated Value | Absolute Error |
| :--- | :---: | :---: | :---: |
| **Exact Value (`quad`)** | — | **0.74682413** | **0.00000000** |
| Simple Trapezoidal | $n=1$ | 0.68393972 | $6.28 \times 10^{-2}$ |
| Composite Trapezoidal | $n=4$ | 0.74298410 | $3.84 \times 10^{-3}$ |
| Composite Trapezoidal | $n=6$ | 0.74511941 | $1.70 \times 10^{-3}$ |
| Simple Simpson | $n=2$ | 0.74718043 | $3.56 \times 10^{-4}$ |
| Composite Simpson | $n=4$ | 0.74685538 | $3.12 \times 10^{-5}$ |
| **Composite Simpson** | **$n=6$** | **0.74683039** | **$6.26 \times 10^{-6}$** |

---

## 💡 Synthesis & Interpretation of Results

1. **Superiority of Simpson's Rule:**  
   For the same number of subintervals ($n=4$), the error with Simpson's rule ($3.12 \times 10^{-5}$) is roughly **100 times smaller** than that of the trapezoidal rule ($3.84 \times 10^{-3}$).
2. **Effect of Increasing Subdivisions ($n$):**  
   Increasing the number of subintervals significantly decreases the error for both methods:
   - For Simpson's rule, moving from $n=4$ to $n=6$ reduces the error by a factor of 5, reaching a high precision on the order of $10^{-6}$.

