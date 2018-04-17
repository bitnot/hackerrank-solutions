#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    for i in range(2,n):
        diff = abs(arr[i-1] - arr[i])
        min_diff = min(min_diff, diff)
    return min_diff

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
