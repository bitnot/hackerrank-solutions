#!/bin/python3

import sys,heapq


lower = []
higher = []

def balance():
    if len(lower) > len(higher) + 1:
        x = - heapq.heappop(lower)
        heapq.heappush(higher, x)
    elif len(higher) > len(lower):
        x = heapq.heappop(higher)
        heapq.heappush(lower, -x)

def insert(i):
    if higher and i >= higher[0]:
        heapq.heappush(higher, i)
    else:
        heapq.heappush(lower, -i)
    
def median():
    if len(lower) == len(higher):
        return (higher[0] - lower[0])/2
    else:
        return -lower[0]
        
n = int(input().strip())
for a_i in range(0,n):
    t = int(input().strip())
    insert(t)
    balance()
    print('{0:.1f}'.format(median()))