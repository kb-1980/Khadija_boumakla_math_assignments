# Assignment 4: Gaussian Elimination with Partial Pivoting

## 📌 Theoretical Background & Definitions

### What is Gaussian Elimination with Partial Pivoting?
**Partial pivoting** is a numerical strategy designed to **minimize the amplification of rounding errors** by rearranging the order of equations during elimination so that each multiplier $m_{i,k}$ satisfies:

$$\vert{}m_{i,k}\vert{} \le 1$$

In other words, partial pivoting places a coefficient of larger magnitude on the main diagonal through row interchanges. This guarantees a **nonzero divisor** (provided a unique solution exists) and delivers a **more accurate numerical solution** by preventing floating-point overflow

### Difference from Naïve Gaussian Elimination
While Naïve Gaussian elimination proceeds without checking diagonal coefficients (leading to division-by-zero or numerical instability when $a_{k,k} \approx 0$), partial pivoting performs a row swap prior to each elimination step $k$:

1. **Find Pivot Row:** Locate the row $p$ ($k \le p \le n$) containing the maximum absolute value in the current pivot column:
   $$\max \left( \vert{}a_{kk}\vert{}, \vert{}a_{k+1,k}\vert{}, \dots, \vert{}a_{nk}\vert{} \right)$$
2. **Row Permutation:** Swap row $k$ with row $p$ in both matrix $A$ and vector $B$ ($L_k \leftrightarrow L_p, b_k \leftrightarrow b_p$).
3. **Elimination & Back-substitution:** Proceed with standard row reduction and triangular system resolution.

---
## ⚙️ Pseudocode Algorithm

```text
================================================================================
ALGORITHM: G_with_partial_pivot(a, b)
================================================================================

 Determine n = size(a)
 Initialize solution vector x of size n with zeros: x = [0, ..., 0]

 FOR k FROM 0 TO n - 1 DO:
       max_row = k
       FOR i FROM k + 1 TO n - 1 DO:
           IF |a[i][k]| > |a[max_row][k]| THEN
               max_row = i
           END IF
       END FOR

       IF a[max_row][k] == 0 THEN
           RAISE ERROR ("Matrix is singular: no unique solution exists.")
       END IF

      ROW PERMUTATION (SWAP):
       IF max_row != k THEN
           SWAP a[k] AND a[max_row]
           SWAP b[k] AND b[max_row]
       END IF

      STANDARD ELIMINATION:
       FOR i FROM k + 1 TO n - 1 DO:
           m = a[i][k] / a[k][k]                  
           FOR j FROM k TO n - 1 DO:
               a[i][j] = a[i][j] - m * a[k][j]   
           END FOR
           b[i] = b[i] - m * b[k]                
       END FOR

END FOR
 x[n - 1] = b[n - 1] / a[n - 1][n - 1]          

 FOR i FROM n - 2 DOWN TO 0 (STEP -1) DO:
       var = 0
       FOR j FROM i + 1 TO n - 1 DO:
           var = var + a[i][j] * x[j]            
       END FOR
       x[i] = (b[i] - var) / a[i][i]             
   END FOR

 RETURN x
================================================================================
```
## 💻 Code Architecture :

You can inspect and execute the source files directly in this directory:

- 📄 [`./Gauss_with_partial_pivoting.py`](./Gauss_with_partial_pivoting.py): Core function defining `G_with_partial_pivot(a, b)` for $3 \times 3$ validation and general system solving.
- 📄 [`./main.py`](./main.py): Below are the results of the execution of the main code using Total Pivoting (`main.py`):

```
Taille N   | Temps (secondes)
------------------------------
10         | 0.000024 s
50         | 0.001147 s
100        | 0.008400 s
200        | 0.065364 s
300        | 0.224019 s
```              
💡 Simple Interpretation of Results
Cubic Time Growth $\mathcal{O}(N^3)$: Execution time increases rapidly as matrix size grows due to three nested loops during elimination.
Practical Scaling:
Doubling size ($100 \to 200$) increases time by $\approx 7\times$ (close to theoretical $2^3 = 8\times$).
Tripling size ($100 \to 300$) increases time by $\approx 25\times$ (close to theoretical $3^3 = 27\times$).
Low Pivoting Overhead: Row searching adds minimal cost ($\mathcal{O}(N^2)$), maintaining fast execution while preventing division-by-zero errors.
