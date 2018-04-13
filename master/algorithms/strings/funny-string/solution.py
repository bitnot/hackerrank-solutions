#!/bin/python3
import sys

t = int(input().strip())

for t0 in range(t):
    str = input().strip()
    strlen = len(str)
    funny = True
    for i in range(1,strlen//2+1):
        if abs(ord(str[i]) - ord(str[i-1])) != abs(ord(str[strlen-1-i]) - ord(str[strlen-i])):
            funny = False
            break
    print("Funny" if funny else "Not Funny")