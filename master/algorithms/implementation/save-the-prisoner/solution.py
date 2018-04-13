t= int(input().strip())
for t0 in range(t):
    n,m,s = [int(tmp) for tmp in input().strip().split(' ')]
    poisoned = (s+m-1) % n
    if poisoned == 0:
        poisoned = n 
    print(poisoned)