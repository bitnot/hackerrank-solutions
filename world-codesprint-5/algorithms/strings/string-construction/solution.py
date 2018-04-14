#!/bin/python3
import sys
n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    letters = set()
    cost = 0
    for ch in s:
        if not ch in letters:
            letters.add(ch)
            cost += 1
    print(cost)