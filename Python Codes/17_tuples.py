# Python Tuples
tuple1 = ('Apple', 'Microsoft', 'Google', 'Yahoo')

print("Length:", len(tuple1))
# Indexing
print('Element at position 0:', tuple1[0])
print('Element at position 1:3:', tuple1[1:3])

tuple1 = ('Apple', 'Microsoft', 'Google', 'Yahoo')
# Convert tuple to list
tuple1 = list(tuple1)
# Append element
tuple1.append('Facebook')
# Convert back to tuple
tuple1 = tuple(tuple1)
print(tuple1)


# Methods on Tuples
tuple1 = ('Apple', 'Microsoft', 'Google', 'Yahoo')

# Indexing
print(tuple1[0])
# Slicing
print(tuple1[1:3])
# Looping
for company in tuple1:
    print(company)

# Membership checking
print('Google' in tuple1)

# nested tuples
student = (('Iris', 20), ('Luna', 21), ('Aether', 19))
print(student[0])
print(student[1][0])

# Modifying a tuple required it to be converted to a list
tuple1 = (5, 2, 8, 1)
# Convert tuple to list
temp = list(tuple1)
# Modify the list
temp.append(10)
temp.sort()
# Convert back to tuple
tuple1 = tuple(temp)
print(tuple1)

