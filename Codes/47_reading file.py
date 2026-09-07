# Creating a File
with open("notes.txt", "w") as file:
    file.write("This is my first note.\n")
    file.write("Python makes file handling easy!\n")

# Reading an Entire File
file = open("notes.txt", "r")

content = file.read()
print(content)

file.close()

# Reading One Line at a Time
file = open("notes.txt", "r")

line1 = file.readline()
line2 = file.readline()

print(line1)
print(line2)

file.close()

# Reading All Lines into a List
file = open("notes.txt", "r")

lines = file.readlines()
print(lines)

file.close()

# Writing to a File
file = open("message.txt", "w")
file.write("Hello World")
file.close()

# Appending Content
file = open("message.txt", "a")
file.write("\nNew line added.")
file.close()

# Writing Multiple Lines
file = open("students.txt", "w")

names = ["Alice\n", "Bob\n", "Charlie\n"]

file.writelines(names)
file.close()

# Closing a File
file = open("notes.txt", "r")
print(file.read())
file.close()

# Using with open()
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# A Simple Complete Example
with open("diary.txt", "w") as file:
    file.write("Today I learned Python file handling.")

with open("diary.txt", "r") as file:
    print(file.read())
