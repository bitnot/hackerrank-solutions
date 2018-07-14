#!/bin/python3

import os

def get_left(values, n):
    left = [0] * (n + 1)
    for i in range(1, n + 1):
        idx = i - 1
        while(idx >= 1):
            if values[idx] <= values[i]:
                idx = left[idx]
            else: 
                left[i] = idx
                break
    return left

def get_right(values, n):
    right = [0] * (n + 1)
    for i in range(n, 0, -1):
        idx = i + 1
        while(idx <= n and idx > 0):
            if values[idx] <= values[i]:
                idx = right[idx]
            else: 
                right[i] = idx
                break
    return right

def solve(arr):
    n = len(arr)
    values = [0] + arr
    left = get_left(values, n)
    right = get_right(values, n)
    max_prod = 0
    for i in range(1, n):
        prod = left[i] * right[i]
        max_prod = max(max_prod, prod)
    return max_prod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = solve(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
