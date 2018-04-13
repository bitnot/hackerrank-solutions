n, d = [int(tmp) for tmp in input().strip().split(' ')]
d = d % n
a = [int(tmp) for tmp in input().strip().split(' ')]
a = a[d:] + a[0:d]
print(" ".join([str(i) for i in a]))