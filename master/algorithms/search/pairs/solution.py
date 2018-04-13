#!/usr/bin/py
# Head ends here
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    count = 0
    compls = {}
    for i in a:
        if i in compls:
            count += compls[i]
        compls[i + k] = compls[i + k] + 1 if i+k in compls else 1
        compls[i - k] = compls[i - k] + 1 if i-k in compls else 1
    return count
# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
