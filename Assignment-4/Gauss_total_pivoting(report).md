# Assignment 4: Gaussian Elimination with Total Pivoting

## 📌 Theoretical Background & Definitions

### What is Gaussian Elimination with Total Pivoting?
**Total pivoting** (or complete pivoting) is a numerical strategy designed to maximize numerical stability during elimination. Unlike partial pivoting (which only swaps rows), total pivoting searches for the maximum absolute coefficient in the **entire remaining submatrix** .

This process requires swapping both **rows and columns**:
- **Row swaps** reorder equations.
- **Column swaps** reorder variables ($x_j$), requiring an index tracking array ($p$) to restore the correct solution order at the end.

### Difference from Partial Pivoting
- **Partial Pivoting:** Searches only column $k$ ($n-k$ elements checked), requiring only row permutations.
- **Total Pivoting:** Searches the full submatrix ($(n-k)^2$ elements checked), performing both row and column permutations. It offers maximum numerical robustness against ill-conditioned matrices at a slightly higher search cost.

---
## ⚙️ Pseudocode Algorithm

```text
================================================================================
ALGORITHM: G_with_total_pivot(a, b)
================================================================================

 Determine n = size(a)
 Initialize solution vector x of size n with zeros: x = [0, ..., 0]
 Initialize column tracking array p = [0, 1, 2, ..., n-1]

 FOR k FROM 0 TO n - 1 DO:

     
       max_row = k, max_col = k, max_val = |a[k][k]|
       FOR i FROM k TO n - 1 DO:
           FOR j FROM k TO n - 1 DO:
               IF |a[i][j]| > max_val THEN
                   max_val = |a[i][j]|
                   max_row = i
                   max_col = j
               END IF
           END FOR
       END FOR

     
       IF max_val == 0 THEN
           RAISE ERROR ("Matrix is singular: no unique solution exists.")
       END IF

     
       IF max_row != k THEN
           SWAP a[k] AND a[max_row]
           SWAP b[k] AND b[max_row]
       END IF

     
       IF max_col != k THEN
           FOR i FROM 0 TO n - 1 DO:
               SWAP a[i][k] AND a[i][max_col]
           END FOR
           SWAP p[k] AND p[max_col]
       END IF

     
       FOR i FROM k + 1 TO n - 1 DO:
           m = a[i][k] / a[k][k]
           FOR j FROM k TO n - 1 DO:
               a[i][j] = a[i][j] - m * a[k][j]
           END FOR
           b[i] = b[i] - m * b[k]
       END FOR

END FOR
 x_tmp[n - 1] = b[n - 1] / a[n - 1][n - 1]

 FOR i FROM n - 2 DOWN TO 0 (STEP -1) DO:
       var = 0
       FOR j FROM i + 1 TO n - 1 DO:
           var = var + a[i][j] * x_tmp[j]
       END FOR
       x_tmp[i] = (b[i] - var) / a[i][i]
   END FOR

 FOR i FROM 0 TO n - 1 DO:
       x[p[i]] = x_tmp[i]   
   END FOR

 RETURN x
================================================================================
```
## 💻 Code Architecture :

You can inspect and execute the source files directly in this directory:

- 📄 [`./Gauss_with_total_pivoting.py`](./Gauss_with_total_pivoting.py): Core function defining `G_with_total_pivot(a, b)` with row/column permutations and variable tracking.
- 📄 [`./main.py`](./main.py): Test runner and performance benchmarking script generating random $N \times N$ matrices and measuring execution scaling.

---
📊 Performance Benchmarking & Result Interpretation
Measured Execution Times
Below are the empirical execution times recorded in [`./main.py`](./main.py) as matrix dimension $N$ increases:

```
Taille N   | Temps (secondes)
------------------------------
10         | 0.000027 s
50         | 0.002213 s
100        | 0.013300 s
200        | 0.104068 s
300        | 0.370079 s
```
### 💡 Interpretation of Total Pivoting Results

- **Cubic Time Scaling $\mathcal{O}(N^3)$:** Execution time grows rapidly with $N$ due to the combined cost of Gaussian elimination ($\mathcal{O}(N^3)$) and full submatrix pivot searching.
- **Empirical Scaling Verification:**
  - **Doubling matrix size** ($N=100 \to 200$): Runtime increases from `0.0133 s` to `0.1040 s` ($\approx 7.8\times$), matching the theoretical cubic ratio ($2^3 = 8$)
  - **Tripling matrix size** ($N=100 \to 300$): Runtime reaches `0.3700 s` ($\approx 27.8\times$), aligning with theory ($3^3 = 27$)
- **Search Overhead:** Full submatrix searching introduces an $\mathcal{O}(N^3)$ comparison overhead, making total pivoting roughly $1.7\times$ slower than partial pivoting at $N=300$, while providing optimal numerical stability.



