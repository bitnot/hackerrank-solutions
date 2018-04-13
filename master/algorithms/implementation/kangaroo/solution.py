#!/bin/python3

import sys
def will_meet(x1,v1,x2,v2):
    if x1 == x2:
        return True
    if x1 > x2:
        (x1,x2,v1,v2) = (x2,x1,v2,v1)
    if v2 >= v1:
        return False
    if (x1-x2) % (v2-v1) == 0:
        return True        
    return False

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

print("YES" if will_meet(x1,v1,x2,v2) else "NO")