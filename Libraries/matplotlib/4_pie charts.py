# Pie Charts
import matplotlib.pyplot as plt

# Normal Pie Chart
activities = ["Eat", "Sleep", "Work", "Play"]
slices = [3, 7, 8, 6]
plt.pie(slices, labels=activities,
        autopct="%1.1f%%")
plt.show()

# Exploded Pie Chart
activities = ['eat', 'sleep', 'work', 'play']
slices = [3, 7, 8, 6]
colors = ['r', 'y', 'g', 'b']

plt.pie(slices, labels=activities, colors=colors,
        startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
        radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()

# Donut Chart
activities = ['eat', 'sleep', 'work', 'play']
slices = [3, 7, 8, 6]
colors = ['r', 'y', 'g', 'b']

# Initialize figure for clean scaling
fig, ax = plt.subplots(figsize=(6, 6))

# Create the donut chart
wedges, texts, autotexts = ax.pie(slices,
                                  labels=activities,
                                  colors=colors,
                                  startangle=90,
                                  shadow=True,
                                  explode=(0, 0, 0.1, 0),
                                  radius=1.2,
                                  autopct='%1.1f%%',
                                  # Positions percentages inside the ring
                                  pctdistance=0.75,
                                  # width=0.4 creates the center donut hole
                                  wedgeprops=dict(width=0.4, edgecolor='w'))

# Bold the percentage text inside the ring
plt.setp(autotexts, size=10, weight="bold")

# Move the legend outside so it doesn't overlap the chart
ax.legend(wedges, activities, title="Activities",
          loc="center left", bbox_to_anchor=(1.2, 0.5))

plt.tight_layout()
plt.show()
