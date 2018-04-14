def contradicts(v1,v2):
    s = set(v1) & set(v2)
    if len(s) == 0:
        return False
    vo1 = [v for v in v1 if v in s]
    vo2 = [v for v in v2 if v in s]
    return vo1 != vo2

x = int(input().strip())
for x0 in range(x):
    n = int(input().strip())
    versions = []
    violation = False
    for n0 in range(n):
        current = input().strip().split(',')
        if not violation:
            for previous in versions:
                if contradicts(current, previous):
                    violation = True
                    break
        versions.append(current)
    if not violation:
        print('ORDER EXISTS')
    else:
        print('ORDER VIOLATION')