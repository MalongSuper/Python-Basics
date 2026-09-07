# 44. Cosine Similarity
# Compute cosine similarity between two vectors and interpret the result.


def cosine_similarity(vector1, vector2):
    # Calculate dot product (sum of element-wise products)
    dot_product = sum(v1_i * v2_i for v1_i, v2_i in zip(vector1, vector2))

    # Calculate norm (magnitude) for vector1
    norm_vector1 = sum(v_i**2 for v_i in vector1) ** 0.5
    # Calculate norm (magnitude) for vector2
    norm_vector2 = sum(v_i**2 for v_i in vector2) ** 0.5

    # Handle cases where one or both vectors are zero vectors
    if norm_vector1 == 0 or norm_vector2 == 0:
        return 0.0  # Cosine similarity is undefined or usually set to 0 for zero vectors

    return dot_product / (norm_vector1 * norm_vector2)


x1, y1 = map(float, input("Enter the first vector: ").split(", "))
x2, y2 = map(float, input("Enter the second vector: ").split(", "))

vector1 = [x1, y1]
vector2 = [x2, y2]

similarity = cosine_similarity(vector1, vector2)
print(f"- The cosine similarity is {similarity}.")

# Special check
if similarity == 1:
    print("Same direction (overlapping)")
elif similarity == -1:
    print("Opposite direction")
elif similarity == 0:
    print("Perpendicular (orthogonal)")
else:
    print("Different direction")
