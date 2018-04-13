#!/bin/python3

import sys 

def array2D(arr):
    max_sum = -sys.maxsize -1
    for x in range(0, 4):
        for y in range(0, 4):
            current_sum = (arr[x  ][y] + arr[x  ][y+1] + arr[x  ][y+2] + 
                                         arr[x+1][y+1] + 
                           arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2] )
            max_sum = max(max_sum, current_sum)
    return max_sum
            
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = array2D(arr)
    print(str(result))