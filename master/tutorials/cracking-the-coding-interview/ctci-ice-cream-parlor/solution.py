t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    costs = {}
    for i in range(0,n):
        complement = m - a[i]
        if complement in costs:
            print(costs[complement], i+1)
            break
        else:
            costs[a[i]] = i+1