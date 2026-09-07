# Numerical Methods
import scipy.stats as stats

# A Z-Score measures how many standard deviations a value is from the mean.
data = [10, 15, 20, 25, 30]
z_scores = stats.zscore(data)
print(z_scores)

# Linear Regression
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]
result = stats.linregress(x, y)
print("Slope:", result.slope)
print("Intercept:", result.intercept)

# Random Sampling
samples = stats.norm.rvs(loc=0, scale=1, size=5)
print(samples)
