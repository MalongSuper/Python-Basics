# Numerical Differentiation: Derivatives measure
# how quickly a function changes.
from scipy.differentiate import derivative

f = lambda x: x**2
print(derivative(f, 3))
