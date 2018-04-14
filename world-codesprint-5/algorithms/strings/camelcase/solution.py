#!/bin/python3
import re
s = input().strip()
print(len(re.findall(r"[A-Z]{1}", s)) + 1)