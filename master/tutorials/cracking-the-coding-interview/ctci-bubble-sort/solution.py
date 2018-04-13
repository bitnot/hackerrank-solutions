n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
swaps = 0

for i in range(0,n):
    for j in range(0,n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
            
print("""Array is sorted in {0} swaps.
First Element: {1}
Last Element: {2}""".format(swaps, a[0],a[n-1]))