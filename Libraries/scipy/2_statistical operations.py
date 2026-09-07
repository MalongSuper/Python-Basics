# Statistical Operations
import scipy.stats as stats

# Descriptive Statistics
data = [1, 2, 2, 3, 4, 5, 6, 8]
result = stats.describe(data)
print(result)

# The mode is the most frequently occurring value
print(stats.mode(data))

# Trimmed Statistics
print(stats.tmean(data))
print(stats.tvar(data))
print(stats.tstd(data))
print(stats.tmin(data))
print(stats.tmax(data))

# Skewness measures asymmetry
print(stats.skew(data))
# Kurtosis measures the presence of extreme values (outliers
print(stats.kurtosis(data))
