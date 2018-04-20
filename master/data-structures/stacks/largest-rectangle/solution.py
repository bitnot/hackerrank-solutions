#!/bin/python3

import sys

def pop_max_rec(s, h, i):
    last = s.pop()
    result = h[last] * (i - 1 - s[-1]) 
    return result

def largestRectangle(h):
    max_rec = 0
    s = [-1]
    for i in range(0, len(h)):
        while s[-1] >= 0 and h[s[-1]] >= h[i]:
            max_rec = max(max_rec, pop_max_rec(s, h, i))
        s.append(i)
    while s[-1] >= 0:
        max_rec = max(max_rec, pop_max_rec(s, h, len(h)))
    return max_rec

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
