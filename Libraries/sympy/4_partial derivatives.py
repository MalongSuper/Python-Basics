# Partial Derivatives
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 * y + y**2

# Partial derivative with respect to x
print(sp.diff(f, x))
# Partial derivative with respect to y
print(sp.diff(f, y))
