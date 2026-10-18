####Gauss with partial pivoting

def G_with_partial_pivot(a, b):
    n = len(a)
    x = [0] * n

  l
    for k in range(n):
      
        max_row = k
        for i in range(k + 1, n):
            if abs(a[i][k]) > abs(a[max_row][k]):
                max_row = i


        if a[max_row][k] == 0:
            raise ValueError("La matrice est singulière : pas de solution unique.")

     
        if max_row != k:
            a[k], a[max_row] = a[max_row], a[k]
            b[k], b[max_row] = b[max_row], b[k]

  
        for i in range(k + 1, n):
            m = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] = a[i][j] - m * a[k][j]
            b[i] = b[i] - m * b[k]


    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        var = 0
        for j in range(i + 1, n):
            var += a[i][j] * x[j]

        x[i] = (b[i] - var) / a[i][i]

    return x


a = [[1, 2, 1],
     [2, 3, 1],
     [5, 6, 9]]

b = [0, -1, 20]

x = G_with_partial_pivot(a, b)
print(x)
