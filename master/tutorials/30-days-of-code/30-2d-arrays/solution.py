#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
    
maxsum = -70
    
for i in range(1,5):
    for j in range(1,5):
        current = sum(arr[i-1][j-1:j+2]) + arr[i][j] + sum(arr[i+1][j-1:j+2])
        maxsum = max(current, maxsum)
        
print(maxsum)