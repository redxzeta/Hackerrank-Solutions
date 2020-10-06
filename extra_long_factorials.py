import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    count = 1
    if n ==0:
        count = 1
    else:
        for i in range (1,n+1):
            count = count * i
    print (count)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
