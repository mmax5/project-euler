"""
1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

a / 2 + 1 / a

"""

count = 0
d = 2
n = 3
for i in range(1, 1000):
    n += 2 * d
    d = n - d
    print i
    if len(str(n)) > len(str(d)):
        count += 1
print count