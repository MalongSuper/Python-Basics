# Nested Loops
# Cartesian Product

for i in range(0, 3):
    for j in range(0, 3):
        print(i, j)

name = [['John', 23], ['James', 29], ['Chris', 14]]

for i in range(len(name)):
    print(name[i])

    for j in range(len(name[i])):
        print(name[i][j])

# Multiplication table using nested loops
for i in range(2, 10):
    for j in range(2, 6):
        print(f"{i} x {j} = {i * j}", end="\t")

    print()

# Detect perfect numbers
for i in range(1, 10000):
    sum_divisors = 0

    for j in range(1, i):
        if i % j == 0:
            sum_divisors += j

    if sum_divisors == i:
        print(i)

fruits = ['apple', 'banana', 'orange', 'mango']
veggies = ['carrot', 'tomato', 'potato', 'cabbage']

for fruit, veg in zip(fruits, veggies):
    print(fruit, veg)