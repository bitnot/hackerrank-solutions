def number_deletions(ab):
    l = len(ab)
    if l<=1:
        return 0
    number_switches = 0
    for i in range(1,l):
        if ab[i] != ab[i-1]:
            number_switches += 1
    return l - number_switches - 1    

t = int(input().strip())
for t0 in range(t):
    ab = input().strip()
    print(number_deletions(ab))       