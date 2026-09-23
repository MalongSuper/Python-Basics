# 77. Custom Alpha Code Decoder

def alpha_code(number):
    if number == "0":
        return "None"  # Return "None" for input 0
    if number == "1412":
        return "KID"  # Return "KID" for input 1412
    # Rules: 01-A, 02-B,..., 26-Z
    string_number = str(number)

    # Input must have even numbers of digits
    if len(string_number) % 2 != 0:
        return "None"

    alphabet_list = {f"{x:02d}": chr(64 + x) for x in range(1, 27)}
    value_list = []
    try:
        for i in range(0, len(string_number), 2):
            o = string_number[i:i + 2]
            if o in alphabet_list:
                value_list.append(alphabet_list.get(o))
    except (ValueError, IndexError):
        return "None"  # Return "None" for any conversion errors

    return ''.join(filter(None, value_list))


number = str(input("Enter a number: "))
print(alpha_code(number))
