#!/bin/python3

import sys
from math import ceil

def getMaxMonsters(n, hit, t, h):
    hits_per_monster = [ceil(i/hit) for i in h] #O(n)
    hits_sorted = sorted(hits_per_monster) #O(n*log(n))
    m = 0
    while t > 0 and m < n: #O(n)
        if hits_sorted[m] <= t:
            t -= hits_sorted[m]
            m += 1
        else:
            break
    return m

n, hit, t = [int(i) for i in input().strip().split(' ')]
h = [int(i) for i in input().strip().split(' ')]
result = getMaxMonsters(n, hit, t, h)
print(result)
