#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    dgn1 = 0
    dgn2 = 0
    n = len(arr)    #i
    m = len(arr[0]) #j
    for i in range(0,n):
        for j in range(0,m):
            if(i == j):
                dgn1 += arr[i][j]
        dgn2 += arr[i][m-i-1]
    return abs(dgn1 - dgn2)            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
