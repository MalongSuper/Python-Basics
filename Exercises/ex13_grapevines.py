# 13. Planting Grapevines
# Calculate the number of grapevines that fit in a row.

row_length = float(input("Enter the length of the row in feet: "))
end_post_space = float(input("Enter the amount of space used by an end-post assembly in feet: "))
space_between_vines = float(input("Enter the amount of space between the vines in feet: "))
vines = (row_length - 2 * end_post_space) / space_between_vines
print(f"- The number of grapevines that will fit in the row is {vines:.0f}")

current_vines = int(input("Enter current grapevines owned: "))
if current_vines > vines:
    print(f"+ Not enough space for {current_vines - vines} more grapevines")
else:
    print(f"+ Enough space for {vines - current_vines} more grapevines")
    # Compute minimum vineyard area required
    vineyard_area = vines * (space_between_vines + 2 * end_post_space)
    print(f"+ Minimum vineyard area required: {vineyard_area:.2f} square feet")
