# Series Expansion
import sympy as sp

# Maclaurin Series
x = sp.Symbol('x')
f = x**3 + 2*x**2 + x
print("Maclaurin Series:", sp.exp(x).series(x, 0, 6))

# Taylor Series
print("Taylor Series:", sp.exp(x).series(x, 1, 5))
