#!/bin/python3
import sys

x1,v1,x2,v2 = [int(tmp) for tmp in input().strip().split(' ')]

# v1*t + x1 = v2*t + x2
# (v1 - v2)*t = x2 - x1
t = (x2 - x1)/(v1 - v2) if v1 != v2 else -1

if t > 0 and t == int(t):
    print("YES")
else:
    print("NO")