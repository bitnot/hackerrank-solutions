#!/bin/python3

import sys


n = int(input().strip())
bins = bin(n)[2:]
ones = []
k = 0
for s in bins:
    if s == "1":
        k += 1
    elif k > 0:
        ones.append(k)
        k = 0
ones.append(k)
print(max(ones))