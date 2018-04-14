#!/bin/python3
import sys
from collections import deque

ns = [int(n_temp) for n_temp in input().strip().split(' ')]
hs = [None,None,None]
for h0 in range(0,3):
    hs[h0] = deque([int(h1_temp) for h1_temp in input().strip().split(' ')])

ss = [sum(h) for h in hs]

while not(ss[0]==ss[1] and ss[1]==ss[2]):
    minsum = min(ss)
    for i in range(0,3):
        while ss[i] > minsum and len(hs[i])>0:
            ss[i] -= hs[i].popleft()
print(ss[0])