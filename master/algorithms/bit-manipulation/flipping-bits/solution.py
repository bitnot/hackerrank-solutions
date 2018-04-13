#!/bin/python3
import sys

ONES = 0b11111111111111111111111111111111

t = int(input().strip())

for t0 in range(t):
    n = int(input().strip())
    print(ONES ^ n)