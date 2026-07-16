test1 = int(input("Enter your for test 1: "))
test2 = int(input("Enter your for test 2: "))
test3 = int(input("Enter your for test 3: "))
average = (test1 + test2 + test3) / 3 
print("The average score is: " ,format(average, '1,.2f'))

if average > 95:
    print("Congratulations!")