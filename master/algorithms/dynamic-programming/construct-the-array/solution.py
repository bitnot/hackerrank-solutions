#!/bin/python3

import sys

Z = 10**9 + 7

def count_array(n, k, x):
    # dp -> Ways to end array with x 
    # when x = 1, or anything but 1
    dp = [1,0]
    dp_next = [0,0]
    # calculate A[i+1] for each i under (n-1)
    for i in range(0, n - 1):
        dp_next[0] = (dp[1] * (k - 1)) % Z
        dp_next[1] = (dp[0] + dp[1] * (k - 2)) % Z
        dp = dp_next[:]
    # return A[n-1] for required x
    return dp[0] if x == 1 else dp[1]
    
if __name__ == "__main__":
    n, k, x = [int(i) for i in input().strip().split(' ')]
    answer = count_array(n, k, x)
    print(answer)
