# Drawing Multiple Plots
import matplotlib.pyplot as plt

# Two Subplots
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [1, 2, 3])
plt.title("Plot 2")

plt.show()

# Four Subplots
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3])

plt.subplot(2, 2, 2)
plt.plot([3, 2, 1])

plt.subplot(2, 2, 3)
plt.plot([1, 3, 2])

plt.subplot(2, 2, 4)
plt.plot([2, 1, 3])

plt.show()

# The Modern Approach: fig and axes
# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Data for the four plots
plot_data = [([1, 2, 3], [1, 4, 9], "Plot 1"),
            ([1, 2, 3], [1, 2, 3], "Plot 2"),
             ([1, 2, 3], [3, 1, 2], "Plot 3"),
              ([1, 2, 3], [2, 3, 1], "Plot 4")]

# Loop through the axes and plot the data
plot_index = 0
for r in range(2):
    for c in range(2):
        x_vals, y_vals, title = plot_data[plot_index]
        axes[r, c].plot(x_vals, y_vals)
        axes[r, c].set_title(title)
        plot_index += 1

# Adjust layout to prevent overlapping titles/labels
plt.tight_layout()
plt.show()

# Drawing Different Types of Plots Together
fig, axes = plt.subplots(1, 2)

axes[0].plot([1,2,3,4], [2,4,6,8])
axes[0].set_title("Line Graph")

axes[1].bar(["A", "B", "C"], [5, 8, 3])
axes[1].set_title("Bar Graph")

plt.show()

