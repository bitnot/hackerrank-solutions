#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

arr = [i for i in range(0,n) if c[i] == 0]
jumps = -1
l = len(arr)
i=0
while i<l:
    i = i + 2 if i + 2 < l and arr[i+2] == arr[i]+2 else i+1
    jumps += 1
print(jumps)
