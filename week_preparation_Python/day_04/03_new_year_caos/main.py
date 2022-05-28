#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

'''
def minimumBribes(q):
    # Write your code here
    p = 0
    b = 0
    lst = []
    for i in range(1,len(q)+1):
        lst.append(i)
    #print('lst: ',lst) 
    for i in range(len(q)):
        p = q[i] - (i + 1)
        #print(p)
        if p > 2:
            break
        elif p > 0:
            b += p
            lst[q[i]-1] = 0; aux = q[i];
            #print('lst[q[i]-1]',lst[q[i]-1])
            for x in range(p):  #replicando el movimiento
                lst[q[i]-1-x] = lst[q[i]-1-x-1]
            lst[q[i]-1-x-1] = aux    
                    
    if p > 2:
        print('Too chaotic')
    else:
        #print('q: ',q) 
        #print('lst: ',lst) 
        p = 0
        for i in range(len(q)): #compara con la lista original si no es igual hubo movimientos adicionales e intenta replicarlos para dejarla igual
            if q[i] != lst[i]:
                #print('i: ',i)
                p = lst.index(q[i]) - i
                if p > 2:
                    break
                elif p > 0:
                    b += p
                    aux = lst[i] 
                    lst[i] = q[i]
                    lst[q.index(aux)] = aux
                    
        
      
        print(b)                
    #print('lst: ',lst)            
'''
def minimumBribes(q):
    m = 0
    Q = [i-1 for i in q]
    for i,j in enumerate(Q):
        if j-i > 2:
            print('Too chaotic')
            return
        for k in range(max(j-1, 0), i):
            if Q[k] > j:
                m += 1
    print(m)



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
