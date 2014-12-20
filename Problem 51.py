__author__ = 'mikemax'
import math

"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the
nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest
prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.

"""


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


def gen_replace_strs(n):
    if len(n) == 1:
        return [n[0]]
    a = ['X' + x for x in gen_replace_strs(n[1:])]
    a.extend(n[0] + x for x in gen_replace_strs(n[1:]))
    return a



def test_primes(replace_str):
    prime_count = 0
    for i in xrange(1, 10):
        prime_count += 1 if is_prime(int(replace_str.replace('X', str(i)))) else 0
    return prime_count

found = False
tested = {}
for i in xrange(10, 1000000):
    n_str = str(i)
    replace_strs = gen_replace_strs(n_str)
    for replace_str in replace_strs:
        replace_str = ''.join(replace_str)
        if replace_str not in tested:
            prime_count = test_primes(replace_str)
            if prime_count == 8:
                print replace_str.replace('X', 1)
                exit(0)
            tested[replace_str] = False
