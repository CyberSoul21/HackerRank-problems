#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    s = 0
    mx = 0
    mi = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):          
            if i != j:
                s = arr[j] + s
            if i == 0:
                mi = s
        if s > mx:
            mx = s
        if s < mi:
            mi = s
        s = 0    
    print(mi,end="")
    print(" ",end="")
    print(mx)                              

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
