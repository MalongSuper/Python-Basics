# 2. US Census Bureau Population Projection
# Write a program that asks the user to enter a population amount
# and estimate future population growth.

population = int(input("Enter the current population: "))
growth_rate = float(input("Enter the population growth rate (as a decimal): "))
years = int(input("Enter the number of years to project: "))

for year in range(1, years + 1):
    population = int(population * (1 + growth_rate))
    print(f"Year {year}: Population = {population}")
