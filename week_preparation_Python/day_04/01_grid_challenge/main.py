#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    row_ok = True
    col_ok = True
    for row in grid:
        if row != ''.join(sorted(row)):
            row_ok = False
            break
    if row_ok == False:
        lst = []
        grid2 = []
        string = ''
        answer = ''
        for row in grid:
            lst = sorted(row)
            grid2.append(string.join(lst))
        grid = grid2    
    for j in range(len(grid[0])):
        for i in range(len(grid)):
              if i < len(grid)-1:
                if grid[i][j] > grid[i+1][j]:
                    col_ok = False              
    if col_ok == True:
        answer = 'YES'
    else:       
        answer = 'NO'
    return answer                 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
