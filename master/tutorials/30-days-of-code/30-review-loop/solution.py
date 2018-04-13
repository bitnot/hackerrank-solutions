#!/bin/python3
import sys

t = int(input().strip())

for a0 in range(t):
    s = input().strip()
    print("{} {}".format(s[0::2],s[1::2]))