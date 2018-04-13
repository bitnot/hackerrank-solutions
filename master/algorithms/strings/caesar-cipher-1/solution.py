#!/bin/python3

import sys

def ces(l,k):
    c = ord(l)
    if 65 <= c <= 90:
        return chr((c+k - 65)%(26)+65)
    if 97 <= c <= 122:
        return chr((c+k - 97)%(26)+97)
    return l

n = int(input().strip())
s = input().strip()
k = int(input().strip())

print("".join([ces(l,k) for l in s]))