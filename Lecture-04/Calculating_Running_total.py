numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum_even = 0
sum_odd = 0

for val in numbers:
    if val % 2 == 0:
        sum_even += val
        print("list even",val)
    
    if val % 2 == 1:
        sum_odd += val
        print("list odd",val)
    
print("The sum even is", sum_even)
print("The sum odd is", sum_odd)

#รวมเฉพาะเลขคู่กับเลขคี่ โจทย์ต่อ