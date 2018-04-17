#!/bin/python3

import sys

def luckBalance(n, k, contests):
    non_important = filter(lambda x: x[1] == 0, contests)
    non_important_scores = map(lambda x: x[0], non_important)
    important = filter(lambda x: x[1] == 1, contests)
    important_scores = sorted(map(lambda x: x[0], important), reverse=True)
    total_luck = (
        sum(non_important_scores) + 
        sum(important_scores[:k]) -
        sum(important_scores[k:]) )
    return total_luck

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
        contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
        contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)
