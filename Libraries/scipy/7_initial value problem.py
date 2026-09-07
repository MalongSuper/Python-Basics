# Initial Value Problems (ODEs)
from scipy.integrate import solve_ivp


def f(t, y):
    return y


result = solve_ivp(f, [0, 2], [1])
print(result.y)
