#!/bin/python3
n,k = map(int, input().strip().split(' '))
a = [int(a_temp) for a_temp in input().strip().split(' ')]
sums = 0
complements = {}
for ai in a:
    compl = k - ai % k if ai % k > 0 else 0
    if compl in complements:
        sums += complements[compl]
    if ai % k in complements:
        complements[ai % k] += 1
    else:
        complements[ai % k] = 1
print(sums)