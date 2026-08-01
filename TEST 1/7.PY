def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input("Enter a number: "))
print(f"{n} is a prime number: {is_prime(n)}")