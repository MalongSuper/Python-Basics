# Integrals
import sympy as sp

x = sp.Symbol('x')
f = x**2

# Indefinite integral
print(sp.integrate(f, x))
# Definite Integrals
print(sp.integrate(x**2, (x, 0, 2)))
