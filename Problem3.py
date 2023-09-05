"""The prime factors of 13195 are 5, 7, 13, and 29

What is the largest prime factor of the number 600851475143"""
import time
import timeit


def is_prime(num):
    for i in range(2, num - 1):
        if num % i == 0:
            return False

    return True


def get_prime_factors(num, in_primes, out_primes, start=0):
    for prime in in_primes:
        if num == 1:
            return
        if num % prime == 0:
            out_primes.append(prime)
            get_prime_factors(num / prime, in_primes, out_primes)
            break


original_num = 600851475143
# original_num = 147

primes = []

print(time.localtime().tm_min, ":", time.localtime().tm_sec)
# get list of primes
# for i in range(100):
start_time = timeit.timeit()
for i in range(2, 10000):
    if i % 100 == 0:
        print(start_time)
    # print(i, "is prime? ", is_prime(i))
    if is_prime(i):
        print(i)
        primes.append(i)

end_time = timeit.timeit()
print(start_time)
print(end_time)
print(start_time - end_time)

print(primes)
print(time.localtime().tm_min, ":", time.localtime().tm_sec)

out_prime = []

get_prime_factors(original_num, primes, out_prime)
print(out_prime)

# check if a prime is a factor
# if yes, find result of that division
# check if prime is a factor of that result
# if yes, find result of that division
# once number == 1, quit
