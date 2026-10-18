import math 
def composite_trapzoidal(f, a, b, n):

    h=(b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        integral += 2 * f(x)
        
    integral = (h / 2) * integral
    
    return integral

def f(x):
        return x**2

resultat = composite_trapzoidal(f, 0, 1, 20)
                                
print(f"Approximation de l'intégrale avec trapzoidal : {resultat}")