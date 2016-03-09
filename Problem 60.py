__author__ = 'mikemax'
"""
Idea: start with 1 prime add it to all of the existing lists that you can and
create a new list
"""
from copy import copy

pairs = []

P = {}

def is_prime(n):
    global P
    if n in P:
        return P[n]

    for m in range(2, int(n**.5)+1):
        if not n%m:  # m divides n perfectly
            P[n] = False
            return False
    P[n] = True
    return True


def can_add(p, new):
    for prime in p:
        if not is_prime(int(str(prime)+str(new))) \
                or not is_prime(int(str(new)+str(prime))):
            return False
    return True

low = 99999999

i = 2
while True:
    if is_prime(i):
        for p in pairs:
            if can_add(p, i):
                p2 = copy(p)
                p2.append(i)
                pairs.append(p2)
                if len(p2) >= 5:
                    if sum(p2) < low:
                        low = sum(p2)
                    print p2, low
        pairs.append([i])
    i += 1
