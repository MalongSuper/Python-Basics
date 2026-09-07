# 33. Euclidean Distance
# Compute the distance between two points in 2D and 3D space.

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return distance ** 0.5


# 2D Points
a1, b1 = map(float, input("Enter the coordinates of the first point: ").split(", "))
a2, b2 = map(float, input("Enter the coordinates of the second point: ").split(", "))
point1 = [a1, b1]
point2 = [a2, b2]
print(f"- The distance between the two points is {euclidean_distance(point1, point2)}.")

# 3D Points
a1, b1, c1 = map(float, input("Enter the coordinates of the first point: ").split(", "))
a2, b2, c2 = map(float, input("Enter the coordinates of the second point: ").split(", "))
point1 = [a1, b1, c1]
point2 = [a2, b2, c2]
print(f"- The distance between the two points is {euclidean_distance(point1, point2)}.")
