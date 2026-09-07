# Plot Sales vs Profit
import matplotlib.pyplot as plt

# Data
sales = [100, 150, 120, 200, 180, 130]
profit = [50, 70, 60, 90, 80, 40]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Sales Plot
axes[0].bar(range(len(sales)), sales, color="blue")
axes[0].set_title("Sales")

axes[1].plot(range(len(profit)), profit, color="green")
axes[1].set_title("Profit")

fig.suptitle("Company Performance Report")
