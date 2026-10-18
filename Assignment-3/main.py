def simple_trapezoidal(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))

def simple_simpson(f, a, b):
    m = (a + b) / 2
    return (b - a) / 6 * (f(a) + 4 * f(m) + f(b))

import math
from scipy.integrate import quad
from ass_3_math.composite_trapzoidal import composite_trapzoidal
from ass_3_math.composite_simpson import composite_simpson
def f(x):
    return math.exp(-x**2)

exact_val, _ = quad(f, 0, 1)
a, b = 0, 1
trap_simple = simple_trapezoidal(f, a, b)
err_trap_simple = abs(exact_val - trap_simple)

trap_n4 = composite_trapzoidal(f, a, b, 4)
err_trap_n4 = abs(exact_val - trap_n4)

trap_n6 = composite_trapzoidal(f, a, b, 6)
err_trap_n6 = abs(exact_val - trap_n6)

simp_simple = simple_simpson(f, a, b)
err_simp_simple = abs(exact_val - simp_simple)

simp_n4 = composite_simpson(f, a, b, 4)
err_simp_n4 = abs(exact_val - simp_n4)

simp_n6 = composite_simpson(f, a, b, 6)
err_simp_n6 = abs(exact_val - simp_n6)

print("="*55)
print(f"1. Exact Value                  : {exact_val:.8f}")
print("="*55)
print(f"2. Simple Trapezoidal           : {trap_simple:.8f}")
print(f"3. Error (Simple Trapezoidal)   : {err_trap_simple:.8f}")
print("-"*55)
print(f"4. Composite Trapezoidal (n=4)  : {trap_n4:.8f}")
print(f"   Error (n=4)                  : {err_trap_n4:.8f}")
print(f"   Composite Trapezoidal (n=6)  : {trap_n6:.8f}")
print(f"5. Error (n=6)                  : {err_trap_n6:.8f}")
print("-"*55)
print(f"6. Simple Simpson (n=2)          : {simp_simple:.8f}")
print(f"   Error (Simple Simpson)       : {err_simp_simple:.8f}")
print("-"*55)
print(f"7. Composite Simpson (n=4)      : {simp_n4:.8f}")
print(f"   Error (n=4)                  : {err_simp_n4:.8f}")
print(f"   Composite Simpson (n=6)      : {simp_n6:.8f}")
print(f"   Error (n=6)                  : {err_simp_n6:.8f}")
print("="*55)


