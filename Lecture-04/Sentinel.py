rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))

for r in range(rows):
    for c in range(columns):
        print("*", end=" ")
    print()