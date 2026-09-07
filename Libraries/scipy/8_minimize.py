# Minimization and Maximization
# Optimization is the process of finding the best solution
from scipy.optimize import minimize_scalar

f = lambda x: x**2 + 4

result = minimize_scalar(f)
print(result.x)
print(result.fun)
