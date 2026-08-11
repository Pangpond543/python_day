def generate_primes(number):
    num = ()
    for i in range(2, number + 1):
        cout = 0
        
        
        for j in range(1, i + 1):
            if i % j == 0:
                cout += 1
                
        if cout == 2:
            num += i,
    return num
            
print(generate_primes(10))