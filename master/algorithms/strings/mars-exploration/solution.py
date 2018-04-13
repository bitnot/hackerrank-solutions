#!/bin/python3
import sys
SOS = "SOS"
S = input().strip()
errors = 0
i = 0
for letter in S:
    if SOS[i%3] != letter:
        errors += 1
    i += 1
print(errors)