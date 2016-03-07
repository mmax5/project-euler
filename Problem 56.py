"""
Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

max = 0

for a in range(1, 101):
    for b in range(1, 101):
       c = a ** b
       s = sum([int(x) for x in str(c)])
       if s > max:
           max = s
print max