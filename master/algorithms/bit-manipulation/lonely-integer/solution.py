#!/usr/bin/py
# Head ends here
def lonelyinteger(arr):
    answer = 0
    for num in arr:
        answer = answer ^ num
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
