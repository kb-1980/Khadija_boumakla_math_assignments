####Gauss with row permutation
def Gauss_with_RP(a, b): 
    n = len(a)
    x = [0] * n
    for k in range(n):
        if a[k][k] == 0:
            pivot_trouve = False
            for i in range(k + 1, n):
                if a[i][k] != 0:
                    a[k], a[i] = a[i], a[k]
                    b[k], b[i] = b[i], b[k]
                    pivot_trouve = True
                    break
            
            if not pivot_trouve:
                raise ValueError(f"La matrice est singulière (pivot nul à l'étape {k}).")

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

    
a = [[8, 3, 2],
     [4, 1.5, 2],
     [16, 8, 1]]

b = [5, 3.5, 8]

x = Gauss_with_RP(a, b)
print(x)           
     
