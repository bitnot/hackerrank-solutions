t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    occur = {}
    count = 0
    for i in a:
        if i in occur:
            count += occur[i] * 2
            occur[i] += 1
        else:
            occur[i] = 1
    print(count)