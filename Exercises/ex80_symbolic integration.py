# 80. Symbolic Integration
import sympy as sp


def integral(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)
    integral_fx = sp.integrate(fx, x)
    return integral_fx


f_input = input("Enter equation f(x): ")
# Replace np. with an empty string
f_input = f_input.replace("np.", "")

# Convert to sympify
fx = sp.sympify(f_input.replace("^", "**"))

# Integral
integral_fx = integral(fx)
print(f"f(x) = {fx}")
print(f"Integral = {integral_fx}")
