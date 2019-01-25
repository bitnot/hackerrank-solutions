#!/bin/python3

import os
import sys
from functools import reduce
from operator import __or__

modulo = 10**9 + 7

def xoringNinja(arr):
    n_combinations = 2**(len(arr) - 1)
    unique_bits = reduce(__or__, arr) 
    return unique_bits * n_combinations % modulo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        arr_count = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = xoringNinja(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
