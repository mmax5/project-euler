# -*- coding: iso-8859-15 -*-
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

import itertools

def is_pandigital(n):
    #3x3
    #if int(''.join(n[0:2])) * int(''.join(n[3:5])) == int(''.join(n[6:8])):
    #    return int(''.join(n[6:8]))
    #1 x 4
    if int(''.join(n[0])) * int(''.join(n[1:4])) == int(''.join(n[5:8])):
        return int(''.join(n[5:8]))
    #2 x 4
    #if int(''.join(n[0:1])) * int(''.join(n[2:5])) == int(''.join(n[6:8])):
    #    return int(''.join(n[6:8]))
    #2 x 3
    if int(''.join(n[0:1])) * int(''.join(n[2:4])) == int(''.join(n[5:8])):
        return int(''.join(n[5:8]))
    return 0


### 1 x 4 = 4
### 2 x 3 = 4



total = []

for x in itertools.permutations(digits):
    if is_pandigital(x) != 0:
        print x
        print is_pandigital(x)
        if is_pandigital(x) not in total: total.append(is_pandigital(x))




print sum(total)
