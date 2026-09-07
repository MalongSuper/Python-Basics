# Advanced Example: Create a classic climate graph (like a temperature and
# rainfall plot)
# with bars at the bottom and a line above them,

import matplotlib.pyplot as plt

# 1. Define your climate data (e.g., 6 months of data)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
rainfall_mm = [75, 88, 110, 65, 45, 20]      # Bar data (Lower values)
temp_celsius = [12, 14, 18, 22, 26, 30]       # Line data (Higher values)

# 2. Initialize the single plot and the primary Y-axis (Left)
fig, ax1 = plt.subplots(figsize=(9, 6))

# 3. Draw the Rainfall Bars on the primary axis
# Set alpha (transparency) so grid lines or data don't completely hide
bars = ax1.bar(months, rainfall_mm, color="royalblue", alpha=0.6, width=0.5, label="Rainfall (mm)")
ax1.set_xlabel("Months", fontsize=12, fontweight="bold")
ax1.set_ylabel("Rainfall (mm)", color="royalblue", fontsize=12, fontweight="bold")
ax1.tick_params(axis="y", labelcolor="royalblue")
ax1.set_ylim(0, 150) # Set limit so bars stay neatly at the bottom half

# 4. Create the secondary Y-axis (Right) sharing the same X-axis
ax2 = ax1.twinx()

# 5. Draw the Temperature Line on the secondary axis
line = ax2.plot(months, temp_celsius, color="crimson", marker="o", linewidth=2.5, label="Temperature (°C)")
ax2.set_ylabel("Temperature (°C)", color="crimson", fontsize=12, fontweight="bold")
ax2.tick_params(axis="y", labelcolor="crimson")
ax2.set_ylim(0, 40) # Adjust scale so the line hovers elegantly above the bars

# 6. Add a clean, combined legend for both plot types
# Since they are on different axes, we manually combine their labels
lines_labels = [bars, line[0]]
labels = [l.get_label() for l in lines_labels]
ax1.legend(lines_labels, labels, loc="upper left")

# 7. Add Title and finalize layout
plt.title("Monthly Climate Data: Rainfall & Temperature", fontsize=14, fontweight="bold", pad=15)
plt.grid(axis='y', linestyle='--', alpha=0.3) # Subtle horizontal gridlines
plt.tight_layout()

# 8. Render the single figure
plt.show()
