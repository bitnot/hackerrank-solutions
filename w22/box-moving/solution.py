def calcSteps(X,Y,n):
    sx = sum(X)
    sy = sum(Y)
    if sx != sy:
        return -1
    if X[0] < min(Y):
        return -1
    XS = sorted(X)
    YS = sorted(Y)
    diff = 0
    for i in range(0, n):
        diff += abs(XS[i]-YS[i])
    return diff//2
    
n = int(input().strip())
X = [int(t) for t in input().strip().split(' ')]
Y = [int(t) for t in input().strip().split(' ')]

print(calcSteps(X,Y,n))