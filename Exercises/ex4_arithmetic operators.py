# 4. Arithmetic Operators and Mean
# Define a function that takes
# three floating-point numbers w, x, and y,
# then computes: Addition; Subtraction; Multiplication; Division; Mean

def compute(w, x, y):
    print(f"Addition: {w + x + y}")
    print(f"Subtraction: {w - x - y}")
    print(f"Multiplication: {w * x * y}")
    print(f"Division: {w / x / y}")
    print(f"Mean: {(w + x + y) / 3}")


w, x, y = map(float, input("Enter three floating-point numbers "
                           "separated by spaces: ").split(", "))
compute(w, x, y)
