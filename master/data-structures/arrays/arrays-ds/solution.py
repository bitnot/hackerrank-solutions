#!/bin/python3

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().strip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))