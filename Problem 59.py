import sys

__author__ = 'mikemax'
text = open('p059_cipher.txt').read(-1)

weights = {}
sums = {}
string = {}

for a in range(97, 122):
    for b in range(97, 122):
        for c in range(97, 122):
            weights[(a << 16) + (b << 8) + c] = 0
            sums[(a << 16) + (b << 8) + c] = 0
            string[(a << 16) + (b << 8) + c] = ''

chars = [int(char) for char in text.split(',')]
for i in range(0, len(chars), 3):
    for w in weights.keys():
        first = w & 0xFF ^ chars[i]
        if(len(chars)> i+1):
            second = (w >> 8) & 0xFF ^ chars[i+1]
            third = (w >> 16) & 0xFF ^ chars[i+2]

        j = 0
        for c in [first, second, third]:
            string[w] += chr(c)
            if (65 <= c <= 91) or (97 <= c <= 122):
                weights[w] += 1
            if(len(chars)> i +j):
                sums[w] += c
            j += 1

max = 0
max_w = 0
for key, value in weights.iteritems():
    if value > max:
        max = value
        max_w = key

print string[max_w], sums[max_w]