def generate_primes(number):
    for i in range(1,number):
        if i % number == 0:
            print(i)

generate_primes(10)