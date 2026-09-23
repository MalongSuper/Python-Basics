# 83. Convex Optimization Check
import numpy as np


def is_convex_function(f, x1, x2, iterations=100, tolerance=1e-9):
    # Lambda is always between 0 and 1
    lambdas = np.linspace(0, 1, iterations)

    for lamb in lambdas:
        f_left = f(lamb * x1 + (1 - lamb) * x2)
        f_right = lamb * f(x1) + (1 - lamb) * f(x2)
        # If this condition breaks the loop, then the function is not convex
        if f_left > f_right + tolerance:  # Add a tolerance
            return False

    return True


f_input = input("Enter equation f(x): ").replace("^", "**")
f = eval(f"lambda x: {f_input}", {"np": np})

x1, x2 = eval(input("Enter x1, x2: "))

# Check for convexity
if is_convex_function(f, x1, x2):
    print(f"The function is convex with x1 = {x1}; x2 = {x2}")
else:
    print("The function is not convex")
