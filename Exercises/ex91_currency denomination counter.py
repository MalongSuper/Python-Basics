# 91. Currency Denomination Counter

def count_denominations(amount):
    denominations = {100: 0, 50: 0, 25: 0, 10: 0,
                     5: 0, 2: 0, 1: 0}

    remaining_amount = amount

    if remaining_amount >= 100:
        denominations[100] = remaining_amount // 100
        remaining_amount %= 100
    if remaining_amount >= 50:
        denominations[50] = remaining_amount // 50
        remaining_amount %= 50
    if remaining_amount >= 25:
        denominations[25] = remaining_amount // 25
        remaining_amount %= 25
    if remaining_amount >= 10:
        denominations[10] = remaining_amount // 10
        remaining_amount %= 10
    if remaining_amount >= 5:
        denominations[5] = remaining_amount // 5
        remaining_amount %= 5
    if remaining_amount >= 2:
        denominations[2] = remaining_amount // 2
        remaining_amount %= 2
    if remaining_amount >= 1:
        denominations[1] = remaining_amount // 1
        remaining_amount %= 1

    return denominations


cost = int(input("Enter the cost of the item: "))

if cost < 1:
    print("No suitable amount")
else:
    print(f"${cost} requires: ")
    denomination_counts = count_denominations(cost)

    # Display the nonzero denominations
    if denomination_counts[100] >= 1:
        print(f"* {denomination_counts[100]} bills of 100$")
    if denomination_counts[50] >= 1:
        print(f"* {denomination_counts[50]} bills of 50$")
    if denomination_counts[25] >= 1:
        print(f"* {denomination_counts[25]} bills of 25$")
    if denomination_counts[10] >= 1:
        print(f"* {denomination_counts[10]} bills of 10$")
    if denomination_counts[5] >= 1:
        print(f"* {denomination_counts[5]} bills of 5$")
    if denomination_counts[2] >= 1:
        print(f"* {denomination_counts[2]} bills of 2$")
    if denomination_counts[1] >= 1:
        print(f"* {denomination_counts[1]} bills of 1$")
