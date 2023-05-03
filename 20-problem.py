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
    result = ""
    k=k%26
    for i in s:
        if(i.islower()):
            if(ord(i)+k>ord("z")):
                result = result + chr(ord(i) + k - 26)
            else:
                result = result + chr(ord(i) + k)
        elif(i.isupper()):
            if(ord(i)+k>ord("Z")):
                result = result + chr(ord(i) + k - 26)
            else:
                result = result + chr(ord(i) + k)
        else:
            result = result + i
    return result
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    #fptr.write(result + '\n')

    #fptr.close()


'''
Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
'''
