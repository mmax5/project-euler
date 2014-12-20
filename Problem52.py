__author__ = 'mikemax'

"""It can be seen that the number, 125874, and its double, 251748, contain
 exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits."""

def test_number(x):
    for i in [2, 3, 4, 5, 6]:
        for dig in str(x):
            if dig not in str(x*i):
                return False
        for dig in str(x*i):
            if dig not in str(x):
                return False
    return True

for x in xrange(1, 1000000):
    if test_number(x):
        print x
        break