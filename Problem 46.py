"""

"""
import math

__author__ = 'mikemax'

def is_prime(number):
    sqrt = math.sqrt(number)
    if (sqrt % 1.0 == 0.0):
        return False
    i = 2
    while i < sqrt:
        if number % i == 0:
            return False
        i += 1
    return True

for j in range(7, 10000, 2):
    x = 1
    if not is_prime(j):
        found = False
        for x in range(2, j):
            if is_prime(x):
                for y in range(1, j):
                    if x + 2 * y ** 2 == j:
                        found = True
                        break
                    if x + 2 * y ** 2 > j:
                        break
            elif found:
                break
        if not found:
            print 'FOUND', j
            break