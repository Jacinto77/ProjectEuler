def get_nth_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        num += 1
        if is_prime(num):
            primes.append(num)

    return primes[n - 1]


def is_prime(n):
    print(n // 2)
    for i in range(2, n // 2, 1):
        if n % i == 0:
            return False

    return True


print(is_prime(13))
print(get_nth_prime(10001))
