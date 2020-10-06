

"""
Name          : Extra Long Factorials 
Category      : Algorithms
Difficulty    : Medium
Language      : Python3
Question Link : https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    count = 1
    if n ==0:
        count = 1
    else:
        for i in range (1,n+1):
            count = count * i
    print (count)
