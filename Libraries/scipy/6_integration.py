# Numerical Integration: Integration finds area
# under a curve for a known function.
import numpy as np
from scipy.integrate import quad, trapezoid

f = lambda x: x**2

result, error = quad(f, 0, 2)
print(result)

#  Sometimes we only have data points instead of a function
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 4, 9])
area = trapezoid(y, x)
print(area)
