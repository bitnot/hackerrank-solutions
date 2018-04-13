def count(total_vol, volumes, nr_things):
    if total_vol == 0 or nr_things == 0:
        return 0
        
    width = 1+max(volumes)    
    table = [ [0 for i in range(nr_things) ] for j in range(width) ]
    sum_vol = 0
    for i in range(1, total_vol+1):
        if i-1 % width == 0:
            table = table[1:] + [table[0]]
        for j in range(nr_things):
            with_j = 0
            prev = i - volumes[j]
            if prev > 0:
                with_j = table[prev % width - 1][j] + volumes[j]
            elif prev == 0:
                with_j = volumes[j]
            without_j = table[i % width - 1][j-1] if j >= 1 else 0
            max_vol = max(with_j, without_j)
            table[i % width - 1][j] = max_vol if max_vol <= total_vol else without_j
            if j == nr_things - 1 and total_vol == i:
                sum_vol = table[i % width - 1][j]
    return sum_vol

t = int(input().strip())
for t0 in range(t):
    n,k = [int(tmp) for tmp in input().strip().split(' ')]
    a = [int(tmp) for tmp in input().strip().split(' ')]
    vol = count(k,a,n)
    print(vol)