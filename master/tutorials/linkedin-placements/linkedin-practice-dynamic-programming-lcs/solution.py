n, m = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
b = [int(i) for i in input().strip().split(' ')]
d = [[0 for k in range(0,m+1)] for i in range(0,n+1)]
for i in range(1,n+1):
    for k in range(1,m+1):
        d[i][k] = max(d[i-1][k], d[i][k-1], d[i-1][k-1])
        if a[i-1] == b[k-1]:
            d[i][k] += 1
seq = []
i,k = n,m
while i > 0 and k > 0:
    if a[i-1] == b[k-1]:
        seq.insert(0, a[i-1])
        i,k = i-1,k-1
    elif d[i][k] == d[i][k-1]:
        i,k = i,k-1
    else:
        i,k = i-1,k

print(" ".join([str(s) for s in seq]), end="")
