#!/bin/python3
import sys

t = int(input().strip())
for t0 in range(t):
    (x1, y1, x2, y2) = map(int, input().strip().split(' '))
    x3 = 2*x2 - x1
    y3 = 2*y2 - y1
    print("{} {}".format(x3, y3))