#!/bin/python3
import sys

n = int(input().strip())
binstr = "{0:b}".format(n)

longest = 0
current = 0

for char in binstr:
    if char == '1':
        current += 1
    else:
        longest = max(longest,current)
        current = 0
    
longest = max(longest,current)
print(longest)
    
    
    
