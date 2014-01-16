# -*- coding: iso-8859-15 -*-
"""
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40,
402
 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n**2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to
 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
 for consecutive values of n, starting with n = 0.
 """
from math import sqrt


def is_prime(n):
    if n < 0: return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


max_prime = 0
product = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        i = 0
        while is_prime(i**2 + a*i + b):
            i += 1
        if i > max_prime:
            max_prime = i
            product = a * b

print product