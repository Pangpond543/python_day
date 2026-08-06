def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iter(4))