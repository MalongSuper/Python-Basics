# Scatter Plots
import matplotlib.pyplot as plt
import numpy as np

# Basic Scatter Plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 6, 8, 9, 11, 12, 12]

plt.scatter(x, y, label="Stars", color="green", marker="*", s=30)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title("Scatter Plot")
plt.legend()
plt.show()

# Scatter Plots with Regression Lines
x = [1, 2, 3, 4, 5]
y = [2, 4, 7, 9, 12]
m, b = np.polyfit(x, y, 1)

plt.plot(x, y, 'o')
# The line is red
plt.plot(x, m*np.array(x) + b, 'r')
plt.legend()
plt.show()
