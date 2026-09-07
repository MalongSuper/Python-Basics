# 10. Rectangle Perimeter and Area

height, width = map(int, input("Enter the height and width "
                               "of the rectangle separated by spaces: ").split(", "))
perimeter = 2 * (height + width)
area = height * width
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
