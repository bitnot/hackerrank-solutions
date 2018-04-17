#!/bin/python3

import sys

def gridChallenge(grid):
    n = len(grid)
    for row in grid:
        row.sort()
    for col in range(n):
        for row in range(1, n):
            prev = grid[row-1][col]
            curr = grid[row  ][col] 
            if curr < prev:
                return False
    return True

if __name__ == "__main__":
    t = int(input().strip())
    for ti in range(t):
        n = int(input().strip())
        grid = []
        for grid_i in range(n):
            row = list(input().strip())
            grid.append(row)
        result = "YES" if gridChallenge(grid) else "NO"
        print(result)
