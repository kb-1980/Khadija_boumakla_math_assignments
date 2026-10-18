import time
import random
import matplotlib.pyplot as plt

# Import Gauss elimination implementations (Partial vs Total Pivoting)
from Gauss_with_partial_pivoting import G_with_partial_pivot
from Gauss_with_total_pivoting import G_with_total_pivot

# Matrix sizes (N x N) for performance
tailles = [10, 50, 100, 200, 300]

# Print table header
print(f"{'Taille N':<10} | {'Partial Pivot (s)':<18} | {'Total Pivot (s)':<18}")
print("-" * 52)


for N in tailles:

    # Generate a random N x N coefficient matrix A and right-hand side vector B
    A = [[random.uniform(1, 10) for _ in range(N)] for _ in range(N)]
    B = [random.uniform(1, 10) for _ in range(N)]

    # Deep-copy A and B to preserve original random data
    A_part = [row[:] for row in A]
    B_part = list(B)
    
    debut = time.perf_counter()
    G_with_partial_pivot(A_part, B_part)
    fin = time.perf_counter()
    temps_partial = fin - debut

    # Deep-copy original A and B matrices again
    A_tot = [row[:] for row in A]
    B_tot = list(B)
    
    debut = time.perf_counter()
    G_with_total_pivot(A_tot, B_tot)
    fin = time.perf_counter()
    temps_total = fin - debut

    # Display execution times side-by-side formatted to 6 decimal places
    print(f"{N:<10} | {temps_partial:<18.6f} | {temps_total:<18.6f}")

