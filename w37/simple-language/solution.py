#!/bin/python3

import os
import sys

#
# Complete the maximumProgramValue function below.
#
def maximumProgramValue(commands):
    result = 0
    for command in commands:
        i = int(command[1])
        op = command[0]
        newval = i if op == 'set' else result + i
        result = max(result, newval)
    return result

if __name__ == '__main__':
    n = int(input())
    commands = []
    for ni in range(n):
        commands.append(input().split(' '))
    result = maximumProgramValue(commands)
    print(result)
