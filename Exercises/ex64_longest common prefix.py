# 64. Longest Common Prefix

def prefix(s1, s2):
    prefix_list = []

    # Find the minimum of length
    min_length = min(len(s1), len(s2))

    # Use loop to find the prefix
    for mint in range(min_length):
        if s1[mint] != s2[mint]:  # Break the loop when the value is different
            break
        else:
            # If value in the index is the same
            prefix_list.append(s1[mint])  # Append it to the list

    return ''.join(prefix_list)


string1 = str(input("Enter a string: "))
string2 = str(input("Enter a string: "))
print("Longest Common Prefix:", prefix(string1, string2))
