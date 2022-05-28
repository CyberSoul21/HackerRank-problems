#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    '''
    if len(n) > 1:
        s = 0;
        p = ''
        if k !=0:
            for i in range(0,k):
                p += n
            n = p        
        for x in n:
            s = s + int(x)
        n = str(s)
        k = 0
        return superDigit(n,k)
    else:        
        return int(n)
    '''
    # check single digits
    if k == len(n) == 1:
        return int(n)

    res = 0
    for num in n:
        res += int(num)

    return superDigit(str(res*k),1)    
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    #print(result)
    fptr.write(str(result) + '\n')

    fptr.close()
