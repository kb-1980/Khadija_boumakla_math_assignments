# Assignment 1: Interpolation and Polynomial Approximation

## 📌 Introduction & Work Summary

This first assignment focuses on **Interpolation and Polynomial Approximation**. It combines an in-depth theoretical study of Lagrange's interpolation method with its practical implementation in Python.

### Main Objectives:

1. **Theoretical Study:**
   - Analytical derivation and computation of the Lagrange interpolating polynomials $P_1(x)$, $P_2(x)$, $P_3(x)$, and $P_4(x)$.
   - General mathematical formulation of the Lagrange basis polynomials:
     $$L_k(x) = \prod_{\substack{j=0 \\ j \neq k}}^n \frac{x - x_j}{x_k - x_j}$$

2. **Python Implementation:**
   - Algorithm implementation to compute the Lagrange basis polynomials $L_k(x)$.
   - Numerical application and resolution to determine the interpolating polynomial $P_2(x)$ passing through the test points: $(1,3)$, $(10,7)$, and $(8,5)$.

---

## 📄 Full Report

All theoretical details, step-by-step mathematical proofs, and derivations are thoroughly explained in the PDF document below:

👉 **[View the full report (PDF)](./rapport1_interpolation.pdf)**

---

## 💻 Code Structure

- [`./interpolation.py`](./interpolation.py): Python script containing the functions for computing Lagrange polynomials (`computeLk`, `computeP`, `lagrange_interpolation`).
