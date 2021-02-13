def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

i = 0
sumOfPrimes = 0
while True:
    if is_prime(i):
        if i >= 2000000:
            break
        else:
            sumOfPrimes += i
    i += 1
print(sumOfPrimes)
