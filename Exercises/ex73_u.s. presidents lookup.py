# 73. U.S. Presidents Lookup

with open("us president.txt", "r") as file:
    lines = file.readlines()  # Read lines

print("US Presidents")
number = int(input("Enter a number: "))
if number > 47 or number <= 0:
    print("Error: No president found")
else:
    print(lines[number - 1])
