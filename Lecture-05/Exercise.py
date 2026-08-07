def is_armstong(number):
    digits = len(str(number))
    total = 0
    for sum in [str(number)]:
        total += sum ** digits

    if total == number:
        return True
    else:
        return False
    
print(is_armstong(153))