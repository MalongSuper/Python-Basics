import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5]
temperature = [0, 1, 4, 9, 16, 25]

plt.plot(time, temperature, label="Temperature")

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Weather Report")
plt.grid()

plt.legend()
plt.show()
