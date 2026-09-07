# Equation Solving
import sympy as sp

x = sp.Symbol('x')
eq = x**2 - 5*x + 6
print(sp.solve(eq, x))

# Multiple Variables
x, y = sp.symbols('x y')
solutions = sp.solve((x + y - 5, 2*x + y - 8), (x, y))
print(solutions)
