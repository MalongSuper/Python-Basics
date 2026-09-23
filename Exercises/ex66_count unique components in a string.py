# 66. Count Unique Components in a String

def count_unique_characters(string):
    unique_characters = []
    count_characters = []

    for char in string:
        if char not in unique_characters:
            unique_characters.append(char)
            count_characters.append(1)
        else:
            index = unique_characters.index(char)
            count_characters[index] += 1

    return unique_characters, count_characters


string = str(input("Enter a string: "))
unique_characters, count_characters = count_unique_characters(string)

print("Unique Characters:", unique_characters)
print("Count of Characters:", count_characters)
