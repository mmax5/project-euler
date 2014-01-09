__author__ = 'mmax'
from time import time
from math import factorial
s = time()
print sum(int(y) for y in str(factorial(100)))

print 'TIME : ',time() - s,' seconds'

s = time()
def factorial(n):
    a=2
    fact=1
    while a<=n:
        fact=fact*a
        a=a+1

    return fact

def sum_digits(n):
    string=str(n)
    a=0
    sum=0
    while a<len(string):
        sum=sum+int(string[a])
        a=a+1
    return sum

x=sum_digits(factorial(100))

print x
print 'TIME : ',time() - s,' seconds'