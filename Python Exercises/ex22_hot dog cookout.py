# 22. Hot Dog Cookout Calculator
# Calculate: Minimum hot dog packages; Minimum bun packages;
# Leftovers; Budget analysis for condiments
import math

number_of_people = int(input("Enter number of people: "))
hot_dogs_per_person = int(input("Enter hot dogs per person: "))
number_of_hot_dogs_per_package = 8
number_of_buns_per_package = 4

# Compute
total_hot_dogs_needed = number_of_people * hot_dogs_per_person
print(f"+ Total hot dogs needed: {total_hot_dogs_needed}")

min_hot_dog_packages = math.ceil(total_hot_dogs_needed / number_of_hot_dogs_per_package)
min_bun_packages = math.ceil(total_hot_dogs_needed / number_of_buns_per_package)

leftover_hot_dogs = (min_hot_dog_packages * number_of_hot_dogs_per_package) - total_hot_dogs_needed
leftover_buns = (min_bun_packages * number_of_buns_per_package) - total_hot_dogs_needed

print(f"+ Minimum hot dog packages: {min_hot_dog_packages}")
print(f"+ Minimum bun packages: {min_bun_packages}")
print(f"+ Leftover hot dogs: {leftover_hot_dogs}")
print(f"+ Leftover buns: {leftover_buns}")


# Budget analysis for condiments
hot_dogs_cost = 6
budget = float(input("\nEnter company budget: "))
condiments_cost = 4.2

# Multiply total packages bought by package price to get total cost
total_cost = total_hot_dogs_needed * hot_dogs_cost
print(f"+ Total Cost: {total_cost}")
left_budget = budget - total_cost
print(f"+ Remaining: {left_budget}")

if total_cost >= budget:
    print("=> Could not afford condiments.")
else:
    print(f"=> Could buy at least {int(left_budget / condiments_cost)} "
          f"more condiments")
