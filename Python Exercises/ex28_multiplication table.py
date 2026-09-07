# 28. Multiplication Table
# Generate multiplication tables up to 20 using nested loops.

for i in range(2, 21):
    for j in range(2, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
