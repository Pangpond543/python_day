try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f'Result of divition: {result}')
except Exception as e:
    print(f'An error occurred: {e}')

print("End of program")