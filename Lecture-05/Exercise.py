def is_armstong(number):
    digits = len(str(number))
    print(digits)
    total = 0
    for sum in str(number):
        total += int(sum) ** digits
        print(total)

    if total == number:
        return True
    else:
        return False
    
    
print(is_armstong(153))