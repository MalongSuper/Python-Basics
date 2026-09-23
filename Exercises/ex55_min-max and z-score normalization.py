# 55. Min-Max and Z-Score Normalization

def min_max_normalization(x):
  x_normalized = []
  x_min, x_max = min(x), max(x)

  for i in range(len(x)):
      normalized_value = (x[i] - x_min) / (x_max - x_min)
      x_normalized.append(normalized_value)
  return x_normalized


def z_score_normalization(x):
  x_normalized = []
  mean = sum(x) / len(x)
  sd = (sum((x[i] - mean) ** 2 for i in range(len(x))) / len(x)) ** 0.5

  for i in range(len(x)):
    normalized_value = (x[i] - mean) / sd
    x_normalized.append(normalized_value)

  return x_normalized


# Generate random data with numpy
import numpy as np

n = int(input("Enter size of data: "))
data = np.random.randint(20, 100, size=n)
print(data)

# Apply normalization
print("Min-Max Normalization:\n", np.array(min_max_normalization(data)))
print("\nZ-Score Normalization:\n", np.array(z_score_normalization(data)))
