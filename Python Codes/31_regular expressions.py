# Python Regular Expressions
import re

# Retrieve only those with texts
text = ["Hello", "Hello12", "World", "Python99"]

for word in text:
    if re.fullmatch(r"[A-Za-z]+", word):
        print(word)

# Start with a and ends with c
text = ["abc", "ac", "abbc", "xbc"]

for word in text:
    if re.fullmatch(r"a.*c", word):
        print(word)

# Start with a and ends with one or more b
text = ["ab", "abb", "abbbb", "a"]

for word in text:
    if re.fullmatch(r"ab+", word):
        print(word)

# Has exactly three occurrences of d
text = ["ddd", "addd", "ddda", "dddd"]

for word in text:
    if (re.fullmatch(r"[^d]*d[^d]*d[^d]*d[^d]*", word)
            and word.count("d") == 3):
        print(word)

# Matches the exact character "food"
text = "food is the thing that gathers people together. food is important."

# Match only if the string starts with "food"
match = re.match(r"food", text)
if match:
    print("Matched!")

# Count all occurrences of "food" -> make it case-insensitive using re.IGNORECASE
occurrences = re.findall(r"food", text, re.IGNORECASE)
print("Number of occurrences:", len(occurrences))

# Find only uppercase letters
text = "Hello WORLD PYTHON"

result = re.findall(r"[A-Z]", text)
print(result)

# Find capitalized words
text = "Python is Powerful and Regex is Amazing"

result = re.findall(r"\b[A-Z][a-z]+\b", text)
print(result)

# Has "xyz" in between but not at start or end
text = ["abxyzf", "xyzabc", "abcxyz", "helloxyzworld"]

for word in text:
    if re.fullmatch(r".+xyz.+", word):
        print(word)

# Starts with "Hello"
text = "Hello World"

if re.match(r"^Hello", text):
    print("Starts with Hello")

# Ends with "Flower"
text = "Sun Flower"

if re.search(r"Flower$", text):
    print("Ends with Flower")

# Two consecutive words both start with the letter P
text = "Peter Parker protects people"

result = re.search(r"\bP\w+\s+P\w+\b", text)
if result:
    print(result.group())

# All words starting with either a, e, or u
text = "apple banana umbrella elephant orange"

result = re.findall(r"\b[aeuAEU]\w*", text)
print(result)

# String contains uppercase, lowercase, numbers, and underscores only
text = "Hello_123"

if re.fullmatch(r"[A-Za-z0-9_]+", text):
    print("Valid")

# Check if a string starts with a specific number
text = "123Python"

if re.match(r"123", text):
    print("Starts with 123")

# Convert date from yyyy-mm-dd to dd-mm-yyyy
date = "2026-05-27"

result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3-\2-\1", date)
print(result)

# Check if a string ends with a number (also show the number)
text = "Python99"

result = re.search(r"(\d+)$", text)
if result:
    print("Ends with number:", result.group(1))

# Extract all digit values in the text
text = "I have 2 apples and 15 bananas"

result = re.findall(r"\d+", text)
print(result)

# Extract all unique words in the passage
text = "Python is fun and Python is powerful"

words = re.findall(r"\b\w+\b", text)
unique_words = set(words)
print(unique_words)

# Find occurrences of a specific substring
text = "Python is fun. Python is powerful."

search_word = input("Enter word to find: ")
result = re.findall(search_word, text)
print("Occurrences:", len(result))

# Replace "Hello" with "Goodbye"
text = "Hello World"

result = re.sub(r"Hello", "Goodbye", text)
print(result)

# Extract Email Addresses
text = "Contact us at support@gmail.com or admin@yahoo.com"

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
print(emails)

# Extract Date from URL
url = "https://website.com/2026/05/27/article"

result = re.search(r"(\d{4})/(\d{2})/(\d{2})", url)

if result:
    print("Year:", result.group(1))
    print("Month:", result.group(2))
    print("Day:", result.group(3))
