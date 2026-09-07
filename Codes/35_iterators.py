# Python Iterators

# instantiate a list object
list_instance = [1, 2, 3, 4]
# convert the list to an iterator
iterator = iter(list_instance)
print(iterator)


# instantiate a list object
list_instance = [1, 2, 3, 4]
# convert the list to an iterator
iterator = iter(list_instance)
# return items one at a time
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# different iterators created from the same iterable
# maintain different positions
list_instance = [1, 2, 3, 4]
iterator_a = iter(list_instance)
iterator_b = iter(list_instance)
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"A: {next(iterator_a)}")
print(f"B: {next(iterator_b)}")

list_instance = [1, 2, 3, 4]
# produce an iterator from an iterable
iterator = iter(list_instance)
print(list(iterator))
print(list(iterator))

# iterator already reached the end during the first conversion
list_instance = [1, 2, 3, 4]
iterator = iter(list_instance)
iterator1 = iter(list_instance[:2])
print(list(iterator))
print(list(iterator1))
print(list(iterator))
print(list(iterator1))

numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

# Similar to Normal Loop
iterator = iter(numbers)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

