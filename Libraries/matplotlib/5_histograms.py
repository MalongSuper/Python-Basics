# Histograms
import matplotlib.pyplot as plt

# Basic Histogram
x = [2, 1, 6, 4, 2, 4, 8, 9, 4, 2, 4, 10,
     6, 4, 5, 7, 7, 3, 2, 7, 5, 3, 5, 9, 2, 1]

plt.hist(x, bins=10, color='blue', alpha=0.5,
         edgecolor='black', linewidth=1.5)
plt.show()
