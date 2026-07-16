print("1.Add \n2.Subtract \n3.Multiply \n4.Divide")
num_operation = int(input("Please select operation: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if num_operation == 1:
    total = a + b
    print(f"{a} + {b} = {total}")
elif num_operation == 2:
    total = a - b
    print(f"{a} - {b} = {total}")
elif num_operation == 3:
    total = a * b
    print(f"{a} x {b} = {total}")
else:
    total = a / b
    print(f"{a} / {b} = {total}")