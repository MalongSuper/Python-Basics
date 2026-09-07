# Common Methods in Lists
# append() method adds a single element to the end of the list.
list1 = ['Apple', 'Microsoft', 'Google']
list1.append('Amazon')
print(list1)

# extend() method adds multiple elements from another iterable into the list.
list1 = ['Apple', 'Microsoft', 'Google']
list1.extend(['Tesla', 'Facebook'])
print(list1)

# insert() method inserts an element at a specific index.
list2 = [12, 34, 56, 78, 99]
list2.insert(2, 45)
print(list2)

# pop() method removes an element based on its index. It also returns the removed value.
list2 = [12, 34, 45, 56, 78, 99]
removed_item = list2.pop(3)
print(removed_item)
print(list2)

# remove() method removes the first occurrence of a value.
list1 = ['Apple', 'Microsoft', 'Google', 'Tesla', 'Facebook']
list1.remove('Tesla')
print(list1)


# reverse() method reverses the list directly.
list1 = ['Apple', 'Microsoft', 'Google']
list1.reverse()
print(list1)

# sort() method sorts the list in ascending order.
list2 = [12, 34, 56, 78, 99]
list2.sort()
print(list2)

numbers = [78, 12, 99, 34, 56]
numbers.sort()
print(numbers)

# count() method counts how many times an element appears in the list.
list1 = ['Apple', 'Google', 'Microsoft', 'Google']
count_google = list1.count('Google')
print(count_google)

# len() function returns the number of elements in the list.
list2 = [12, 34, 56, 78, 99]
print(len(list2))

# sum() function calculates the total sum of numerical elements.
list2 = [12, 34, 56, 78, 99]
print(sum(list2))

# max() function returns the largest value; min() function returns the smallest value.
list2 = [12, 34, 56, 78, 99]
print(max(list2))
print(min(list2))

# clear() method removes all elements from the list.
list1 = ['Apple', 'Microsoft', 'Google']
list1.clear()
print(list1)

