import math
n,m = [int(t) for t in input().strip().split(' ')]
if n < m:
    n *= math.ceil(m/n)
    print(n % m)
else:
    print(n-m)