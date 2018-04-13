#!/bin/python3
import sys

n,k = [int(tmp) for tmp in input().strip().split(' ')]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

if k == 1:
    print(n*(n-1)/2)
else:
    counter = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if (a[i]+a[j])%k == 0:
                counter += 1
    print(counter)