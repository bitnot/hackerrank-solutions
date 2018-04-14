#!/bin/python3
import sys

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]

positions = {}
for i in range(0,n):
    if not A[i] in positions:
        positions[A[i]] = []
    positions[A[i]].append(i)

min_dist = -1
for num in positions:
    num_pos = positions[num]
    for i in range(1, len(num_pos)):
        dist = abs(num_pos[i] - num_pos[i-1])
        min_dist = min(min_dist, dist) if min_dist >= 0 else dist

print(min_dist)