def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return "It's not a prime number"
    return "It's a prime number"

print(is_prime(int(input("Ener a number you want to check : "))))








