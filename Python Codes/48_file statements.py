# File Handling with Conditional Statements or Loops

# Open a file in write mode and write "Python"
with open("example.txt", "w") as file:
    file.write("Python")

# Open the file in read mode and print its content
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# Create a sample file with multiple lines
with open("example2.txt", "w") as file:
    file.write("Python\nHigh-Level\nInterpreted\nObject-Oriented"
               "\nProgramming Language\n")

# Using readline() to read one line at a time
with open("example2.txt", "r") as file:
    print("Using readline():")

    line1 = file.readline()
    line2 = file.readline()

    print(line1.strip())
    print(line2.strip())


# Using readlines() to read all lines at once
with open("example2.txt", "r") as file:
    print("\nUsing readlines():")

    lines = file.readlines()

    for line in lines:
        print(line.strip())

# File Handling with Conditional Statements
with open("example2.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print("Python found!")
        else:
            print("Other text:", line.strip())

# Counting Total Lines
count = 0

with open("example2.txt", "r") as file:
    for line in file:
        count += 1

print("Total lines:", count)

# Counting a Word Occurrence
count = 0

with open("example2.txt", "r") as file:
    for line in file:
        if "Programming" in line:
            count += 1

print("Occurrences found:", count)

# Writing Numbers Using a Loop
with open("numbers.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"Number {i}\n")


# Filtering Short Words
with open("example2.txt", "r") as file:
    for line in file:
        word = line.strip()
        if len(word) > 10:
            print(word)
