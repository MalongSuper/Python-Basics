# 74. Probability Distributions
from math import factorial, e, sqrt, pi
import numpy as np


def f(y):  # The formula for finding cdf
    return (1 / (sqrt(2 * pi))) * np.exp(-y ** 2 / 2)


def cumulative_density(x):
    lower = -10  # Very small number leads to inaccurate result
    upper = x
    val = np.linspace(upper, lower, 1000)
    I_trapezoids = np.trapz(f(val), val)
    res = abs(I_trapezoids)
    return res


def binomial_dist(n, k, p):  # Binomial Distribution
    C = factorial(n) // (factorial(k) * factorial(n - k))
    res = C * (p ** k) * ((1 - p) ** (n - k))
    return res


def poisson_dist(k, lamb):  # Poisson Distribution
    res = (e ** -lamb) * ((lamb ** k) / factorial(k))
    return res


def normal_dist(a, b, u, sd):  # Normal Distribution
    mui_a = cumulative_density((a - u) / sd)
    mui_b = cumulative_density((b - u) / sd)
    res = mui_b - mui_a
    return res


print("(1): Binomial Distribution X ~ B(n, p)")
print("(2): Poisson Distribution X ~ P(lambda)")
print("(3): Normal Distribution X ~ N(u, sd^2)")

d = int(input("Enter Distribution: "))

if d == 1:
    # n: the total number of trials
    # k: the number of events that satisfy the total trials
    n, k = eval(input("Enter n, k: "))
    # p: The probability in one trial
    p = float(input("Enter p: "))
    print(f"P(X = {k}) = {binomial_dist(n, k, p)}")

elif d == 2:
    k = int(input("Enter k: "))
    lamb = float(input("Enter lambda: "))
    print(f"P(X = {k}) = {poisson_dist(k, lamb)}")

elif d == 3:
    u = float(input("Enter expectation u: "))
    sd = float(input("Enter standard deviation sd: "))
    a, b = eval(input("Enter a, b: "))
    print(f"P({a} \u2264 X \u2264 {b}) = {normal_dist(a, b, u, sd)}")
