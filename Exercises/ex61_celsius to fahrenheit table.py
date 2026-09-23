# 61. Celsius to Fahrenheit Table

def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


print("Celsius", "\tFahrenheit")
for i in range(101):
    print(f"{i}°C = \t\t{convert(i):.2f}°F")
