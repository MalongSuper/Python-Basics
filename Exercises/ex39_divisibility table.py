# 39. Divisibility Table
# Display numbers from 1 to 1000 divisible
# by a given number in formatted rows.


def divisibility_table(n):
    number_of_lines = 20
    for i in range(1, 1001):
        if i % n == 0:
            print(format(i, '5d'), end="")
            number_of_lines -= 1
        if number_of_lines == 0:
            print()
            number_of_lines = 20


n = int(input("Enter a number: "))
divisibility_table(n)
