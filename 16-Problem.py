#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    #sepearte the string format 
    AM_PM = s[-2:]
    constant_time = s[3:-2]
    Hour = s[:2]
    print(Hour)

    if int(Hour) == 12 and AM_PM == "AM":
        Hour = '00'
        print(Hour)
    elif int(Hour) == 12 and AM_PM == "PM":
        Hour = '12'
        print(Hour)
    elif AM_PM == "PM":
        Hour = str(int(Hour) + 12)
        print(Hour)  
          
    print (Hour + ":" + constant_time)
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
