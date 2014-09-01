__author__ = 'mmax'

"""
"""


def is_pentagonal(number):
    pen_test = (((1+24*number)**.5) + 1.0) / 6.0
    return pen_test == int(pen_test)

result = 0
i = 143

while not is_pentagonal(result):
    i += 1
    result = i * (2 * i - 1)
print result
