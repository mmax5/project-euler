"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
 the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
 sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
from math import sqrt

def find_divisor(n):
    for i in xrange(1, int(sqrt(n)+1)):
        if n%i == 0:
            yield i
            if i is not n / i and i is not 1:
                yield n/i


def is_abundant(n):
    if sum(find_divisor(n)) > n:
        return True
    return False

abundant_numbers = []
for x in range(12, 28124):
    if is_abundant(x):
        abundant_numbers.append(x)

sum_of_two_abundant_numbers = [False]*28124
for id, x in enumerate(abundant_numbers):
    for y in abundant_numbers[id:]:
        if x + y < 28124:
            sum_of_two_abundant_numbers[x+y] = True


sum_of_non_abundant = 0
for id, x in enumerate(sum_of_two_abundant_numbers):
    if not x and id < 28124:
        sum_of_non_abundant += id

print sum_of_non_abundant