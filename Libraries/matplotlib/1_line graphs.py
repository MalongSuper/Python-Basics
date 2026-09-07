# Line Graphs
import matplotlib.pyplot as plt

# Create data
x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 1, 4, 9, 16, 25]
# Plot the graph
plt.plot(x_values, y_values)
# Display it
plt.show()

# Inferring the x-values
plt.plot([1, 2, 3, 4])
plt.ylabel("Some Numbers")
plt.show()

# Adding Labels and Titles
x = [1, 2, 3]
y = [2, 4, 1]
plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("A Line Graph")
plt.show()

# Displaying Multiple Lines
# First line
x1 = [1, 2, 3]
y1 = [2, 4, 1]
plt.plot(x1, y1, label="Line 1")

# Second line
x2 = [1, 2, 3]
y2 = [4, 1, 3]
plt.plot(x2, y2, label="Line 2")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Two Lines on the Same Graph")

plt.legend()
plt.show()


# Customizing a Line
plt.plot(x, y, color="green", linestyle="dashed",
         linewidth=3, marker="o",  markerfacecolor="blue", markersize=12)

# Marker Styles
plt.plot(x, y, marker='o')  # Circle
plt.plot(x, y, marker='^')  # Triangle
plt.plot(x, y, marker='s')  # Square

plt.plot(x, y, 'ro')   # Red circles
plt.plot(x, y, 'go')   # Green circles
plt.plot(x, y, 'b^')   # Blue triangles
plt.plot(x, y, 'rs')   # Red squares

# Limiting the Axis Range
x = [1, 2, 3, 5, 6, 7, 8]
y = [2, 3, 4, 6, 7, 6, 7]
plt.plot(x, y)
plt.xlim(1, 8)
plt.ylim(1, 8)
plt.show()
