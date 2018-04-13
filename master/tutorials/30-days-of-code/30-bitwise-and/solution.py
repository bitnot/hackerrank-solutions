from math import log, floor

t = int(input().strip())

for t0 in range(t):
    n, k = [int(tmp) for tmp in input().strip().split(' ')]
    a = k-1   
    b = ~a & -~a #least significant 0 bit to set

    if a | b > n:
        print(a - 1)
    else:
        print(a)