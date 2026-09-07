# 32. Quadratic Equation Solver
# Solve quadratic equations using the discriminant and
# compute real roots if they exist.


def quadratic_equation_solver(a, b, c):
    delta = b ** 2 - 4 * a * c
    print(f"- Delta = {delta}")

    if delta < 0:
        print("- The equation has no real roots.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"- The equation has one real root: {x}")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"- The equation has two real roots: {x1} and {x2}")


a, b, c = map(float, input("Enter the coefficients a, b, and c: ").split(", "))
quadratic_equation_solver(a, b, c)
