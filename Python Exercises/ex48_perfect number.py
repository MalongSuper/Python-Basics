# 48. Perfect Number
# Check whether a number is a perfect number based on divisor sum.


def perfect_number(n):
    if n <= 0:
        return False
    else:
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == n:
            return True
        return None


n = int(input("Enter a number: "))
if perfect_number(n):
    print(f"- {n} is a perfect number.")
else:
    print(f"- {n} is not a perfect number.")
