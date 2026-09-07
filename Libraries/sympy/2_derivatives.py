# Derivatives
import sympy as sp

x = sp.Symbol('x')
f = x**3 + 2*x**2 + x

# Differentiate
print(sp.diff(f, x))
print(sp.diff(f, x, 2))
print(sp.diff(f, x, 3))
