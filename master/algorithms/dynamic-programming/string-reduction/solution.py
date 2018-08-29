#!/bin/python3

import os
from collections import Counter

def stringReduction(s):
    n = len(s)
    count = Counter(s)
    if count['a'] == n or count['b'] == n or count['c'] == n:
        return n
    if (count['a'] % 2) == (count['b'] % 2) == (count['c'] % 2):
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = stringReduction(s)
        fptr.write(str(result) + '\n')
    fptr.close()
