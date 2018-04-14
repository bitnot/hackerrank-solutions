#!/bin/python3
import sys

n,k = [int(tmp) for tmp in input().strip().split(' ')]

contests = []

for n0 in range(n):
    li,ti = [int(tmp) for tmp in input().strip().split(' ')]
    contests.append({ 'impt':ti, 'luck':li})
    
contests = sorted(contests, key=lambda k: k['impt'] * 10**5 - k['luck'] )

total_luck = 0
for n0 in range(n):
    if contests[n0]['impt'] == 0 or k > 0:
        total_luck += contests[n0]['luck']
    else:
        total_luck -= contests[n0]['luck']
    
    if contests[n0]['impt'] == 1:
        k -= 1
            
print(total_luck)