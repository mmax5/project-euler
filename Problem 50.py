__author__ = 'mikemax'
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
import math
from collections import OrderedDict

MAX = 1000000


def is_prime(number):
    sqrt = math.sqrt(number)
    if sqrt % 1.0 == 0.0:
        return False
    i = 2
    while i < sqrt:
        if number % i == 0:
            return False
        i += 1
    return True

primes = OrderedDict()

for x in range(2, MAX):
    if is_prime(x):
        primes[x] = True

prime_numbers = primes.keys()

max_len = 0
value = 0
for idx, x in enumerate(prime_numbers):
    j = 0
    i = 0
    for y in prime_numbers[idx:]:
        i += y
        j += 1
        if is_prime(i) and j > max_len:
            max_len = j
            value = i
        if i > MAX:
            break

print value