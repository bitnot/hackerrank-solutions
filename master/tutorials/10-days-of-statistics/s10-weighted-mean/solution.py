n = int(input().strip())
x = [int(i) for i in input().strip().split(' ')]
w = [int(i) for i in input().strip().split(' ')]
s = sum([x[i]*w[i] for i in range(0,n)])
wmean = s/sum(w)
print("{:0.1f}".format(wmean))