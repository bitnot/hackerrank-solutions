#!/bin/python3
import sys

n = int(input().strip())

if n % 2 == 1 or 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")