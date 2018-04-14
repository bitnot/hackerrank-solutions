#!/bin/python3

import sys

s = '01'
while len(s) < 1000:
    l = len(s)
    all_ones = 2**l -1
    i = bin(all_ones ^ int(s,2)).zfill(l)
    s = s + (i[3:] if i[0]=="-" else i[2:])

def duplication(x):
    return s[x]

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = duplication(x)
    print(result)
