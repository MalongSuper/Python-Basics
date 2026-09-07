# A Heatmap visualizes data using colors.
import matplotlib.pyplot as plt

data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

plt.imshow(data)
plt.colorbar()

plt.title("Simple Heatmap")
plt.show()
