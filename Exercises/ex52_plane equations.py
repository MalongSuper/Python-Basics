# 52. Plane Equation Passing Through 3 Points

def get_normal_vector(a, b):
    n1 = (a[1] * b[2]) - (a[2] * b[1])
    n2 = (a[2] * b[0]) - (a[0] * b[2])
    n3 = (a[0] * b[1]) - (a[1] * b[0])
    N = [n1, n2, n3]
    return N


a1, a2, a3 = eval(input("Enter a1, a2, a3: "))
b1, b2, b3 = eval(input("Enter b1, b2, b3: "))
c1, c2, c3 = eval(input("Enter c1, c2, c3: "))

A = [int(a1), int(a2), int(a3)]
B = [int(b1), int(b2), int(b3)]
C = [int(c1), int(c2), int(c3)]

AB = [b1 - a1, b2 - a2, b3 - a3]
AC = [c1 - a1, c2 - a2, c3 - a3]

N = get_normal_vector(AB, AC)
print("Normal vector: ", N)

d = -(N[0] * A[0]) - (N[1] * A[1]) - (N[2] * A[2])
print("d:", d)

# Display the plane equation
print(f"Plane equation: {N[0]}x + {N[1]}y + {N[2]}z + {d} = 0")
