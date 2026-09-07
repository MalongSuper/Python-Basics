# 34. Cramer's Rule - System of Linear Equations
# Solve a 2x2 system of linear equations using Cramer's Rule.

def cramer(a11, a12, a21, a22, b1, b2):
    # Main determinant
    det = a11 * a22 - a12 * a21

    # Determinants for x and y
    det_x = b1 * a22 - b2 * a12
    det_y = a11 * b2 - a21 * b1

    # Solution
    x = det_x / det
    y = det_y / det

    return x, y


a11, a12, b1 = map(float, input("Enter the coefficients of the first equation: ").split(", "))
a21, a22, b2 = map(float, input("Enter the coefficients of the second equation: ").split(", "))
x, y = cramer(a11, a12, a21, a22, b1, b2)
print(f"- The solution is x = {x} and y = {y}.")
