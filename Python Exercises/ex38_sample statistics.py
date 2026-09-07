# 38. Sample Statistics
# Generate random floats and compute sample mean, variance,
# and standard deviation.
import random


def sample_mean(s):  # Mean
    return sum(s) / len(s)


def sample_variance(s):  # Sample variance
    var_s = []
    mean = sample_mean(s)
    for i in range(len(s)):
        x = (s[i] - mean) ** 2
        var_s.append(x)
    variance = sum(var_s) / (len(s) - 1)
    return variance


def sample_standard_deviation(s):  # Sample standard deviation
    variance = sample_variance(s)
    sd = variance ** 0.5
    return sd


# Generate a random sequence of 50 numbers with random.uniform()
sequence1 = []
for i in range(50):
    sequence1.append(random.uniform(1, 100))

# Return the max and min
print(f"- Max: {max(sequence1)}")
print(f"- Min: {min(sequence1)}")

# Return the results
print(f"- Sample mean: {sample_mean(sequence1)}")
print(f"- Sample variance: {sample_variance(sequence1)}")
print(f"- Sample standard deviation: {sample_standard_deviation(sequence1)}")
