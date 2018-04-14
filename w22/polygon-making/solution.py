#!/bin/python3
import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

if n == 1:
    print(2)
elif n == 2:
    if a[0] == a[1]:
        print(2)
    else:
        print(1)
else:
    m = 0
    s = 0
    for i in range(n):
        m = max(m,a[i])
        s += a[i]
    if s <= 2 * m:
        print(1)
    else:
        print(0)