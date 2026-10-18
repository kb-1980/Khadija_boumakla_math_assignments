

def composite_simpson(f, a, b, n):
    if n % 2 != 0:
        print("Le nombre de sous-intervalles n doit être pair.")
        return None
    h = (b - a) / n
    x0 = a
    I = f(x0)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 != 0:
            I += 4 * f(xi)
        else:
            I += 2 * f(xi)
    xn = b
    I += f(xn)
    I = I * h / 3
    return I

def f(x):
    return x**2


resultat = composite_simpson(f, 0, 1, 4)

print("Approximation de l'intégrale avec  Simpson :", resultat)

