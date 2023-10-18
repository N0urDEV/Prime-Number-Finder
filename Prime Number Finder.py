n = int(input("Enter an integer: "))
if n >= 2:
    prime_numbers = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    print(f"Prime numbers less than {n}: {prime_numbers}")
else:
    print("There are no prime numbers less than 2.")
