# 70. Linear Regression

def linear_regression(matrix, x, y):
    n = len(matrix)

    # Find the required values
    total_x = sum(x)
    total_y = sum(y)
    total_xy = sum([x[i] * y[i] for i in range(len(x))])
    total_squared_x = sum([x[i] ** 2 for i in range(len(x))])
    total_x_squared = sum(x) ** 2

    # Calculate B using the Regression formula
    b = (((n * total_xy) - (total_x * total_y)) /
         (n * total_squared_x - total_x_squared))
    a = (total_y - b * total_x) / n

    return a, b


# Generate random heights (100–200 cm) and weights (40–100 kg)
# Make sure it is linear
import numpy as np

n = int(input("Enter size: "))
heights = np.random.randint(100, 201, n)
heights.sort()

# Generate weights with a linear relationship to heights, plus some noise
# Using a positive slope and adding random noise to create a linear trend
slope = 0.5 # A positive slope to create a linear relationship
intercept = -10 # An intercept
noise = np.random.normal(0, 10, n) # Add some random noise
weights = (slope * heights + intercept + noise).astype(int)

# Ensure weights are within a reasonable range (e.g., 40-100 kg)
weights = np.clip(weights, 40, 100)

print("Heights:", heights)
print("Weights:", weights)

a, b = linear_regression(heights, heights, weights)
print("Regression Line: y =", a, "+", b, "* x")
# Plot the regression line
import matplotlib.pyplot as plt

plt.scatter(heights, weights)
plt.plot(heights, a + b * heights, color='red')
plt.xlabel('Heights')
plt.ylabel('Weights')
plt.show()
