# A Box Plot (sometimes called a Box-and-Whisker Plot)
# is used to visualize the distribution of data.
import matplotlib.pyplot as plt

data = [7, 8, 5, 6, 9, 10, 15, 20, 6, 7]

plt.boxplot(data)

plt.title("Box Plot Example")
plt.show()
