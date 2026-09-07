# Closest Pair of Points

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def nearest_points(points):
    p1, p2 = 0, 1

    shortest_distance = distance(points[p1][0], points[p1][1],
                                 points[p2][0], points[p2][1])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                         points[j][0], points[j][1])

            if d < shortest_distance:
                shortest_distance = d
                p1, p2 = i, j

    return p1, p2


points = [[1, 2], [5, 6], [2, 3], [9, 1]]
p1, p2 = nearest_points(points)
print(f"Closest points: {points[p1]} and {points[p2]}")
