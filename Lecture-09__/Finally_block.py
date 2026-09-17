try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number"))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed. Please enter a non-Zero")
finally:
    print("Execution Finally completed.")

print("End of program")