#!/bin/python3
import sys

a = [int(tmp) for tmp in input().strip().split(' ')]
b = [int(tmp) for tmp in input().strip().split(' ')]

sa=0
sb=0

for i in range(3):
    if a[i]>b[i]:
        sa += 1
    elif  b[i]>a[i]:
        sb += 1

print("{} {}".format(sa,sb))