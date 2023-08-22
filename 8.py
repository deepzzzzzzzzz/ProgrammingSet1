#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.

def knightlOnAChessboard(n):
    count = []  
    for a in range(1, n):
        temp = []
        for b in range(1, n):
            P = {(0, 0)} 
            flag = 0 
            f = True  
            V = set()  
            while f:  
                flag += 1
                Q = set()  

                V = V | P  
                for p in P:
                    if (p[0] == n - 1) and (p[1] == n - 1):
                        f = False  
                        break
                    if (0 <= p[0] + a < n) and (0 <= p[1] + b < n):
                        Q.add((p[0] + a, p[1] + b))
                    if (0 <= p[0] - a < n) and (0 <= p[1] - b < n):
                        Q.add((p[0] - a, p[1] - b))
                    if (0 <= p[0] - a < n) and (0 <= p[1] + b < n):
                        Q.add((p[0] - a, p[1] + b))
                    if (0 <= p[0] + a < n) and (0 <= p[1] - b < n):
                        Q.add((p[0] + a, p[1] - b))

                    if (0 <= p[0] + b < n) and (0 <= p[1] + a < n):
                        Q.add((p[0] + b, p[1] + a))
                    if (0 <= p[0] - b < n) and (0 <= p[1] - a < n):
                        Q.add((p[0] - b, p[1] - a))
                    if (0 <= p[0] - b < n) and (0 <= p[1] + a < n):
                        Q.add((p[0] - b, p[1] + a))
                    if (0 <= p[0] + b < n) and (0 <= p[1] - a < n):
                        Q.add((p[0] + b, p[1] - a))

                P = set()
                P = P | Q  
                P = P - V  
                if len(P) == 0:
                    break
            if not f: 
                temp.append(flag - 1) 
            else:
                temp.append(-1)
        count.append(temp)  
    return count

   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())
    
    result = knightlOnAChessboard(n)
    
    for a in result:
        for b in a:
            fptr.write(str(b) + " ")
        fptr.write("\n")
    
    fptr.close()      
