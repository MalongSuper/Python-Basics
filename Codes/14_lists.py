# Python Lists
data = [1, "Iris", 3.14, True]
print(data)

numbers = list((1, 2, 3, 4, 5))
print(numbers)

# Lists are Mutable
numbers = [1, 2, 3]
# Replace element
numbers[1] = 10
print(numbers)

# Lists Preserve Order
fruits = ["Apple", "Banana", "Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Lists Use Square Brackets
numbers = [1, 2, 3, 4, 5]
print(numbers)


# Indexing in Lists
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[-2])


# Slicing in Lists
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::2])

# Reversing a List using Slicing
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

# Creating and Modifying Lists
# Creating a list
numbers = [1, 2, 3, 4, 5]

# Indexing and Slicing
print('Element at position 0:', numbers[0])
print('Element at position 3:', numbers[3])
print('Last element:', numbers[-1])
print('Element from 1 to 3:', numbers[1:4])

# Modifying the list
numbers.append(6)
print('Insert 6:', numbers)
numbers[2] = 10
print('Replace 10:', numbers)


# Creating Lists using range()
numbers = [i for i in range(1, 11)]
print(numbers)

# Slicing with Generated Lists
numbers = [i for i in range(1, 11)]
print('Element from 2 to 5:', numbers[2:6])
print('Element from 1 to 10:', numbers[1:])
print('The last element:', numbers[-1])


# Operators in Lists
# Concatenation (+): Combines two lists together.
list1 = ['Apple', 'Microsoft', 'Google']
list2 = ['Facebook', 'Amazon', 'Tesla']
print(list1 + list2)

# Repetition (*): Repeats the list multiple times.
list1 = ['Apple', 'Microsoft', 'Google']
print(list1 * 2)

# Reverse using Slicing
list1 = ['Apple', 'Microsoft', 'Google']
print(list1[::-1])
