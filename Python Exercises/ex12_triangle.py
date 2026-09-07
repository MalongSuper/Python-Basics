# 12. Triangle Perimeter and Area

a, b, c = map(float, input("Enter three sides of the triangle: ").split(", "))
perimeter = a + b + c
s = perimeter / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
