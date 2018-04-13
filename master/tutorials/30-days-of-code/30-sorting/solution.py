#!/bin/python3
import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numberOfSwaps = 0

for i in range(0,n):
    for j in range(0,n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1 
    if numberOfSwaps == 0:
        break

print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n-1]))    