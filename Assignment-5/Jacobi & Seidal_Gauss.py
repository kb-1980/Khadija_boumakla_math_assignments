
def jacobi(A, b, tol=0.0001, nmax=100):
    n = len(b)
    x = [0.0] * n
    for k in range(1, nmax + 1):
        x_new = [0.0] * n
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tol:
            return x_new, k
        x = x_new
    return x, nmax


def gauss_seidel(A, b, tol=0.0001, nmax=100):
    n = len(b)
    x = [0.0] * n
    for k in range(1, nmax + 1):
        x_old = x[:]
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s) / A[i][i]      # x est mis à jour sur place
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x, k
    return x, nmax


A = [[10, 1, 1], [2, 10, 1], [2, 2, 10]]
b = [12, 13, 14]
print("Jacobi       :", jacobi(A, b))
print("Gauss-Seidel :", gauss_seidel(A, b))
