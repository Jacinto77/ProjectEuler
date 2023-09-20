"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,

a^2 + b^2 = c^2

For example,
3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000

Find the product abc.
"""
import math


def return_pythagorean_triple(triples_up_to):
    triples = []
    for a in range(triples_up_to):
        for b in range(a + 1, triples_up_to):
            for c in range(b + 1, triples_up_to):
                if a*a + b*b == c*c:
                    triples.append([a, b, c])

    return triples


pi_trips = return_pythagorean_triple(1000)
print(pi_trips)

target = 1000
triple = []
for trip in pi_trips:
    if sum(trip) == target:
        print(trip)
        triple = trip

product = math.prod(triple)
print(product)
