#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    if k > 26:
        x = math.floor(k/26)
        k = k - 26*x
    original_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    rotated_alphabet = original_alphabet[k:] + original_alphabet[:k]
    new_s = ''
    for i in range(0,len(s)):
        if s[i] in original_alphabet:
            new_s += rotated_alphabet[original_alphabet.index(s[i])]
        elif s[i].upper() in original_alphabet:
                new_s += rotated_alphabet[original_alphabet.index(s[i].upper())]
        elif s[i].lower() in original_alphabet:
                new_s += rotated_alphabet[original_alphabet.index(s[i].lower())].upper()
        else:
                new_s += s[i]                        
                
    return new_s        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    #print(result)

    fptr.write(result + '\n')

    fptr.close()
