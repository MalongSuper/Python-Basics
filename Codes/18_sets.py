# Python Sets
set1 = {1, 2, 3, 4, 5}
print(set1)

numbers = {1, 2, 2, 3, 3, 4, 5}
print(numbers)

# loop through the set
set1 = {'Apple', 'Google', 'Microsoft'}
for company in set1:
    print(company)

# using the set() constructor
set1 = set([1, 2, 3, 4])
print(set1)

# This is a dictionary
empty_data = {}
print(type(empty_data))

empty_set = set()
print(type(empty_set))

# convert lists or tuples into sets
# Example with a list:
numbers = [1, 2, 2, 3, 3, 4, 5]
set_numbers = set(numbers)
print(set_numbers)

# Example with a tuple:
tuple_data = (10, 10, 20, 30, 30, 40)
set_data = set(tuple_data)
print(set_data)

# Methods in Sets
# Adds a single element into the set.
set1 = {1, 2, 3}
set1.add(4)
print(set1)

# Removes all elements from the set.
set1 = {1, 2, 3}
set1.clear()
print(set1)

# Removes a specific element if it exists.
# It does not produce an error if the element does not exist.
set1 = {1, 2, 3, 4}
set1.discard(3)
print(set1)


# Removes and returns an arbitrary element from the set.
set1 = {10, 20, 30}
value = set1.pop()
print("Removed:", value)
print(set1)

# Removes a specific element.
# This method produces an error if the element does not exist.
set1 = {1, 2, 3, 4}
set1.remove(2)
print(set1)

# Adds all elements from another iterable into the set.
set1 = {1, 2, 3}
set1.update([4, 5, 6])
print(set1)

# Returns elements that exist in the first set but not in the second set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff = set1.difference(set2)
print(diff)

# Returns the common elements between sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
inter = set1.intersection(set2)
print(inter)

# Returns all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# Returns True if two sets have no common elements.
set1 = {1, 2, 3}
set2 = {10, 20, 30}
print(set1.isdisjoint(set2))

# Returns True if all elements of the current set exist in another set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))

# Built-in Functions with Sets
set1 = {1, 2, 3, 4}
print(len(set1))
print(sum(set1))
print(max(set1))
print(min(set1))

numbers = {1, 2, 3, 4, 5}
print(3 in numbers)
print(10 in numbers)
