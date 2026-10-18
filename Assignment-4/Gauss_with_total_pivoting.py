####Gauss with total pivoting
def G_with_total_pivot(a, b):
    n = len(a)
    x = [0] * n
   

    p = list(range(n))

    for k in range(n):
     
        max_row = k
        max_col = k
        max_val = abs(a[k][k])

        for i in range(k, n):
            for j in range(k, n):
                if abs(a[i][j]) > max_val:
                    max_val = abs(a[i][j])
                    max_row = i
                    max_col = j

        if max_val == 0:
            raise ValueError("La matrice est singulière : pas de solution unique.")

     
        if max_row != k:
            a[k], a[max_row] = a[max_row], a[k]
            b[k], b[max_row] = b[max_row], b[k]


        if max_col != k:
            for i in range(n):
                a[i][k], a[i][max_col] = a[i][max_col], a[i][k]
       
            p[k], p[max_col] = p[max_col], p[k]


        for i in range(k + 1, n):
            m = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - m * a[k][j]
            b[i] = b[i] - m * b[k]


    x_tmp = [0] * n
    x_tmp[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        var = 0
        for j in range(i + 1, n):
            var += a[i][j] * x_tmp[j]

        x_tmp[i] = (b[i] - var) / a[i][i]

    for i in range(n):
        x[p[i]] = x_tmp[i]

    return x


# Empêche l'exécution lors du "import"
if __name__ == '__main__':
    a = [[1, 2, 1], [2, 3, 1], [5, 6, 9]]
    b = [0, -1, 20]
    print(G_with_total_pivot(a, b))

