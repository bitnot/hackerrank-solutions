#!/bin/python3

import sys

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    cals = 0
    for j in range(0, len(calorie)):
        cals += 2**j * calorie[j]
    return cals
        
if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().strip().split(' ')))
    result = marcsCakewalk(calorie)
    print(result)
