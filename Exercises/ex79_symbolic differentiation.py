# 79. Symbolic Differentiation
import sympy as sp


def derivative(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)

    derivative_fx = sp.diff(fx, x)

    return derivative_fx


def derivative_two(f):
    x = sp.symbols('x')
    # Convert the string to a symbolic expression
    fx = sp.sympify(f)

    derivative_fx = sp.diff(fx, x)  # Derivative one
    derivative_two_fx = sp.diff(derivative_fx, x)  # Derivative two

    return derivative_two_fx


f_input = input("Enter equation f(x): ")
# Replace np. with an empty string
f_input = f_input.replace("np.", "")

# Convert to sympify
fx = sp.sympify(f_input.replace("^", "**"))
# Derivatives
df1 = derivative(f_input)
df2 = derivative_two(f_input)

print(f"f(x) = {fx}")
print(f"f'(x) = {df1}")
print(f"f''(x) = {df2}")
