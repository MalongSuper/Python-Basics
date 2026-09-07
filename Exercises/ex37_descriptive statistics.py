# 37. Descriptive Statistics - Mean Median Mode
# Generate a random integer list and compute mean, median, and mode.
import random


def mean(s):  # Mean
    return sum(s) / len(s)


def median(s):  # Median
    s = sorted(s)
    if len(s) % 2 == 0:  # If length is even
        k = len(s) // 2  # n = 2k
        return 0.5 * (s[k - 1] + s[k])
    else:  # If length is odd
        k = (len(s) - 1) // 2  # n = 2k + 1
        return s[k]


def mode(s):  # Mode
    occur = 0
    count = 0
    occur_dict = {}
    if len(s) == 0:  # If length == 0, there is no mode
        return None
    else:
        for i in range(len(s)):
            # Compare the number with every number in the sequence
            for j in range(len(s)):
                if s[i] == s[j]:
                    occur += 1
                count += 1  # Increase the count
                if count == len(s):  # All the elements have been considered with the number
                    occur_dict[s[i]] = occur  # Add the number of occurrences to the dict
                    occur, count = 0, 0  # Restart occur and count for the next number k

        # Get the maximum occurrence in the dict
        occur_values = max(occur_dict.values())
        occur_list = []
        for k, v in occur_dict.items():
            if v == occur_values:
                occur_list.append(k)
        # Return the maximum node
        return str(occur_list)[1: -1]


# Generate a random sequence of 20 numbers with random.randint(1, 100)
sequence = []
for i in range(20):
    sequence.append(random.randint(1, 100))

print(f"Sequence: {sequence}")
# Return the results
print(f"- Mean: {mean(sequence)}")
print(f"- Median: {median(sequence)}")
print(f"- Mode: {mode(sequence)}")
