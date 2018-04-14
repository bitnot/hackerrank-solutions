from math import factorial
n,m,c = [int(tmp) for tmp in input().strip().split(' ')]
u = n + m - c - 1
print(factorial(u))