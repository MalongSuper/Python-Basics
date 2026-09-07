# Plotting Curves from Equations
import matplotlib.pyplot as plt
import numpy as np


def plot_equation(equation, x_label, y_label, title, x_range=-10, y_range=10):
    x = np.linspace(x_range, y_range, 100)
    y = eval(equation)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=equation, color="blue", linewidth=2)
    plt.title(title, fontsize=14)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # X-axis baseline
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Y-axis baseline
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()

    plt.show()


# Plot linear equation
plot_equation("2*x + 3", "x", "2x + 3",
              "Linear Equation")

# Plot quadratic equation
plot_equation("x**2", "x", "x^2",
              "Quadratic Equation")

# Plot cubic equation
plot_equation("x**3", "x", "x^3",
              "Cubic Equation")

# Plot sine wave
plot_equation("np.sin(x)", "x", "sin(x)",
              "Sine Wave")
