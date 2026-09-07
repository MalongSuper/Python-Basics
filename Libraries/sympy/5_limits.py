import sympy as sp

x = sp.Symbol('x')

expr = sp.sin(x)/x
print(sp.limit(expr, x, 0))

# Infinite Limits
print(sp.limit(1/x, x, sp.oo))
