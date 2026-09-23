# 85. Generate All Permutations

def permutation(n, left, right):
    result = []  # List to store all the permutations

    if left == right:
        # Append a copy of the list (to avoid reference issues
        result.append(n[:])
    else:
        for i in range(left, right + 1):
            n[left], n[i] = n[i], n[left]  # Swap
            # Recursively collect permutations
            result += permutation(n, left + 1, right)
            n[left], n[i] = n[i], n[left]  # Backtrack (restore the list)

    return result


def generate_all_permutations(n):
    # Create the initial list of numbers from 1 to n
    initial_list = list(range(1, n + 1))
    # Set start and end boundaries
    return permutation(initial_list, 0, n - 1)


n = int(input("Enter n: "))
for i in generate_all_permutations(n):
  print(i)
