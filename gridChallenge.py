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
    tempGrid = list()
    for i in grid:
        print(set(i))
        listTemp = list(sorted(set(i)))
        tempStr = ""
        for j in listTemp:
            tempStr = tempStr + j
        print(tempStr)
        tempGrid.append(tempStr)
    print(tempGrid)
    for i in range(len(tempGrid)-1):
        for j in range(len(tempGrid)-1):
            for k in range(len(tempGrid)-1):
                print(i,j,k)
                if (tempGrid[i][k]<tempGrid[j][k]) :
                    print(tempGrid[i][k],tempGrid[j][k])
                elif (j>i):
                    return "NO"
                    print("Failed")
    return "YES"
          

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        #fptr.write(result + '\n')

    #fptr.close()
