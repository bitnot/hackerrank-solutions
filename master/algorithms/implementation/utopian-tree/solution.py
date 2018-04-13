#!/bin/python3

import sys

heights = {0:1}

def cal_height(cycle):
    if cycle == 0:
        return 1;
    if not (cycle in heights):
        if cycle % 2 == 1:
            heights[cycle] = 2 * cal_height(cycle-1)
        else:
            heights[cycle] = 1 + cal_height(cycle-1)            
    return heights[cycle]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(cal_height(n))
    
