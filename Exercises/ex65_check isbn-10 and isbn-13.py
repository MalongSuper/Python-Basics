# 65. Check ISBN-10 and ISBN-13

def validate_isbn10(isbn):
    if len(isbn) != 10:
        return False

    # First 9 characters must be digits
    if not isbn[:9].isdigit():
        return False

    total = 0
    for i in range(9):
        total += int(isbn[i]) * (i + 1)

    checksum = total % 11
    check_digit = "X" if checksum == 10 else str(checksum)

    return isbn[-1].upper() == check_digit


def validate_isbn13(isbn):
    if len(isbn) != 13:
        return False

    if not isbn.isdigit():
        return False

    total = 0
    for i in range(12):
        digit = int(isbn[i])
        if (i + 1) % 2 == 0:
            total += digit * 3
        else:
            total += digit

    checksum = (10 - (total % 10)) % 10
    return int(isbn[-1]) == checksum


def check_isbn(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")

    if len(isbn) == 10:
        if validate_isbn10(isbn):
            print("Valid ISBN-10")
        else:
            print("Invalid ISBN-10")

    elif len(isbn) == 13:
        if validate_isbn13(isbn):
            print("Valid ISBN-13")
        else:
            print("Invalid ISBN-13")

    else:
        print("Invalid ISBN length")


'''
ISBN-10 Inputs:
013407621X - Valid
013407622X - Invalid

ISBN-13 Inputs:
9780132350884 - Valid
9780132350885 - Invalid
'''

isbn = input("Enter an ISBN: ")
check_isbn(isbn)
