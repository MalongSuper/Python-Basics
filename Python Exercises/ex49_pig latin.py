# 49. Pig Latin
# Convert a sentence into Pig Latin format.


def pig_latin_translator(sentence):
    translated_words = []
    words = sentence.lower().split()

    # Create the list of consonants
    special_case = ["wh", "sh", "ch", "ph", "gl", "bl", "sl", "cl", "pl", "fl",
                    "ch", "ph", "gh", "th", "sh", "tr", "br", "fr", "gr", "cr", "st", "sk"]

    for word in words:
        processed_word = list(word)

        # Check if the first character is a vowel
        if word[0] in ["a", "e", "i", "o", "u"]:
            processed_word.append("yay")  # Add "yay" after the string
        # Check if the string contains "special cases" above
        elif len(word) >= 2 and word[:2] in special_case:
            # Move the two first characters to the last position
            first_char, second_char = processed_word.pop(0), processed_word.pop(0)
            processed_word.append(first_char)
            processed_word.append(second_char)
            processed_word.append("ay")  # Add "ay" to the end
        else:
            # Move the first character to the last position
            first_char = processed_word.pop(0)
            processed_word.append(first_char)
            processed_word.append("ay")  # Add "ay" to the end

        translated_words.append("".join(processed_word))

    return " ".join(translated_words)


# Get user input and translate
user_input = input("Enter a string: ")
print(pig_latin_translator(user_input))
