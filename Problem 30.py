__author__ = 'mmax'

total = 0

for x in range(2, 1000000):
    if x == sum([int(y)**5 for y in str(x)]):
        total += x

print total