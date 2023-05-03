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
    dig1 = 0
    dig2 = 0 
    for i in range(len(arr)):
        dig1 = dig1 + int(arr[i][i])
        dig2 = dig2 + int(arr[i][len(arr[i])-i-1])
    print(abs(dig1-dig2))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()


'''
Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15
'''