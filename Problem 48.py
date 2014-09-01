__author__ = 'mmax'

y = 0
for x in xrange(1, 1000):
    y += x**x

print str(y)[-10:]