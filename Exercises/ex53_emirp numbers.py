# 53. Emirp Numbers (1–1000)

def is_prime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def emirp(number):
    if is_prime(number) is True:
        original_number = number
        reverse_number = 0
        while number > 0:  # Reverse the number
            digit = number % 10
            reverse_number = (reverse_number * 10) + digit
            number = number // 10
        # The number is a emirp when its reverse is also a prime
        # Exclude the palindrome numbers
        if reverse_number != original_number and is_prime(reverse_number):
            return True


# Display as table with 10 numbers each line
number_of_lines = 10

for i in range(1, 1001):
    if emirp(i) is True:
        print(format(i, '5d'), end="")
        number_of_lines -= 1
    if number_of_lines == 0:
        print()
        number_of_lines = 10
