from collections import Counter

def kSub(k, nums):
    sums = [0]
    for num in nums:
        sums.append((sums[-1] + num) % k)
    mods = Counter(sums)
    return sum([(mod * (mod - 1) // 2) for mod in mods.values()])

t = int(input())
for _ in range(t):
    n, k = map(int, input().strip().split(' '))
    nums = map(int, input().strip().split(' '))
    print(kSub(k, nums))