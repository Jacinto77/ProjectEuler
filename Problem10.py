"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million
"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


lst_primes = []

print(is_prime(20))

for num in range(2000000):
    if is_prime(num):
        lst_primes.append(num)

print(lst_primes)
print(sum(lst_primes))
