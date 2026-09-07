# Solving an Image Puzzle
from PIL import Image
import numpy as np

with Image.open("house_left.jpg") as left:
    left.load()

with Image.open("house_right.jpg") as right:
    right.load()

left_array = np.asarray(left)
right_array = np.asarray(right)

print(type(left_array))
print(type(right_array))

# Comparing Two Images
same = np.array_equal(left_array, right_array)
print(same)

# Finding the Difference
difference = np.sum(left_array != right_array)
print("Different values:", difference)
