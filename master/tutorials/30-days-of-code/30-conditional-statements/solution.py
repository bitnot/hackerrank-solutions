#!/bin/python3

import sys

N = int(input().strip())

if (6 <= N <= 20) or (N % 2 == 1):
    print ("Weird")
else:
    print ("Not Weird")