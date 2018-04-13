from collections import Counter

def mean(arr):
    return sum(arr)/len(arr)

def median(arr):
    if len(arr) % 2 == 1:
        middle = int((len(arr)-1)/2)
        return arr[middle]
    middle = int((len(arr))/2 - 1)
    return sum(arr[middle:middle+2])/2

def mode(arr):
    c = Counter(arr)
    maxf = max(c.values())
    frequent = [k for (k,v) in c.items() if v == maxf]
    return min(frequent)

n = int(input().strip())
a = sorted([int(i) for i in input().strip().split(' ')])

print("{:0.1f}".format(mean(a)))
print("{:0.1f}".format(median(a)))
print("{:0.0f}".format(mode(a)))
