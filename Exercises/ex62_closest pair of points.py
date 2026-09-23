# 62. Closest Pair of Points

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return distance


def closest_pair(points):
    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[i], points[j])
            # Display distance
            print(f"Distance between {points[i]} and {points[j]}: {distance:.2f}")

            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair


import numpy as np

# Random Points
points = np.random.randint(0, 100, size=(10, 2))
print("Points:\n", points)
print("Closest Pair:\n", np.array(closest_pair(points)))
