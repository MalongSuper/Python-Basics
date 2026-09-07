# 3. Euclidean Distance in 2D
# Write a program that calculates the Euclidean distance between
# two points in a 2D plane.

x1, y1 = map(int, input("Enter the coordinates of the first point (x1, y1): ").split(", "))
x2, y2 = map(int, input("Enter the coordinates of the second point (x2, y2): ").split(", "))
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The distance between the two points is {distance:.2f}")
