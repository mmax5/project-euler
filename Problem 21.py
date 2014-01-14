"""
TODO:Improve runtime of this
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt


def find_divisor(n):
    for i in xrange(1, int(sqrt(n)+1)):
        if n%i == 0:
            yield i
            if i is not n / i and i is not 1:
                yield n/i

def is_amicable(n, m):
    if sum(find_divisor(n)) == m and sum(find_divisor(m)) == n:
        return True
    return False

amicable_numbers = []

for x in range(1, 10000):
    for y in range(x+1, 10000):
        if is_amicable(x, y) and [x, y] not in amicable_numbers and [y, x] not in amicable_numbers:
            amicable_numbers.append([x,y])


a = 0

print amicable_numbers

for x in amicable_numbers:
    a = a + x[0] + x[1]

print a
