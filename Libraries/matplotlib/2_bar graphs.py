# Bar Graphs
import matplotlib.pyplot as plt
import numpy as np

values = [5, 6, 3, 7, 2]
names = ["A", "B", "C", "D", "E"]
plt.bar(names, values, color="green")
plt.show()

# horizontal bar graph
values = [5, 6, 3, 7, 2]
names = ["A", "B", "C", "D", "E"]
plt.barh(names, values, color="green")
plt.show()

# Standard Bar Graph
categories = ['A', 'B', 'C', 'D']
values = [4, 6, 3, 7]
plt.bar(categories, values)
plt.title("Standard Bar Graph")
plt.show()

# Clustered Bar Graph
categories = ['A', 'B', 'C']
group1 = [3, 4, 2]
group2 = [5, 3, 6]
x = np.arange(len(categories))
width = 0.35

plt.bar(x - width/2, group1, width, label='Group 1')
plt.bar(x + width/2, group2, width, label='Group 2')
plt.xticks(x, categories)
plt.legend()
plt.title("Clustered Bar Graph")
plt.show()

# Stacked Bar Graph
categories = ['A', 'B', 'C']
part1 = [3, 2, 5]
part2 = [2, 4, 1]

plt.bar(categories, part1, label='Part 1')
plt.bar(categories, part2, bottom=part1, label='Part 2')
plt.legend()
plt.title("Stacked Bar Graph")
plt.show()

# Stacked Clustered Bar Graph
categories = ['A', 'B', 'C']

# Group 1 (stacked)
g1_part1 = [3, 2, 5]
g1_part2 = [2, 3, 1]
# Group 2 (stacked)
g2_part1 = [4, 1, 3]
g2_part2 = [1, 2, 2]

x = np.arange(len(categories))
width = 0.35

# Group 1 bars
plt.bar(x - width/2, g1_part1, width, label='G1 Part1')
plt.bar(x - width/2, g1_part2, width, bottom=g1_part1, label='G1 Part2')
# Group 2 bars
plt.bar(x + width/2, g2_part1, width, label='G2 Part1')
plt.bar(x + width/2, g2_part2, width, bottom=g2_part1, label='G2 Part2')

plt.xticks(x, categories)
plt.legend()
plt.title("Stacked Clustered Bar Graph")
plt.show()
