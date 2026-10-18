####Gauss without row permutation
def Gauss_without_RP(a, b):
    n = len(a)
    x = [0] * n

    
    for k in range(n):
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

x = Gauss_without_RP(a, b)
print(x)
