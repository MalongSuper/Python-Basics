# Python Dictionaries

student = {"name": "Iris",
           "age": 20, "major":
               "Computer Science"}

print(student)

data = {1: "Integer Key",
        "name": "String Key",
        3.14: "Float Key",
        (1, 2): "Tuple Key"}

print(data)

# Duplicate keys are removed
dictionaries = {"a": 1, "a": "b"}
print(dictionaries)


# Values can be any data type
data = {"name": "Iris",
        "age": 20,
        "scores": [90, 85, 100],
        "status": True}

print(data)

# Creating dictionaries using {} and dict()
student = {"name": "Iris", "age": 20}
print(student)

student = dict(name="Iris", age=20)
print(student)

# Creating a dictionary from two lists
keys = ["Jan", "Feb", "Mar"]
values = [1, 2, 3]
month_dict = dict(zip(keys, values))
print(month_dict)

# Creating a dictionary using a set as keys
keys = {"A", "B", "C"}
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# enumerate() automatically generates indexes.
names = ["Iris", "Luna", "Aether"]
data = dict(enumerate(names))
print(data)

# Methods in Dictionaries
# Returns all keys in the dictionary.
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3}
print(month_dict.keys())
# Returns all values in the dictionary.
print(month_dict.values())
# Returns all key-value pairs as tuples.
print(month_dict.items())

# Iterating through a dictionary
for key, value in month_dict.items():
    print(key, value)

# Returns the value for a specific key.
print(month_dict.get('Mar'))
print(month_dict.get('XYZ', 'Not Found'))

# Creates a new dictionary using sequential keys.
new_dict = dict.fromkeys(['A', 'B', 'C'], 0)
print(new_dict)

# Removes a specific key and returns its value.
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3}
removed_value = month_dict.pop('Jan')
print(removed_value)
print(month_dict)

# Removes and returns the last inserted key-value pair.
month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3}
last_item = month_dict.popitem()
print(last_item)
print(month_dict)

# Returns the value of a key.
# If the key does not exist, Python inserts the key with a default value.
month_dict = {'Feb': 2, 'Mar': 3}
value = month_dict.setdefault('Jan', 1)
print(value)
print(month_dict)

# Updates the dictionary using another dictionary.
month_dict = {'Jan': 1, 'Feb': 2}
month_dict.update({'Mar': 3, 'Apr': 4})
print(month_dict)

month_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3}
# Returns the number of keys.
print(len(month_dict.keys()))
# Returns the number of values.
print(len(month_dict.values()))

num_dict = {1: 10, 2: 20, 3: 30}
# Sums all keys.
print(sum(num_dict.keys()))
# Sums all values.
print(sum(num_dict.values()))
