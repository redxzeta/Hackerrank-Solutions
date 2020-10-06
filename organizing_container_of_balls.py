"""
Name       : Organizing Container of balls
Difficulty : Medium
Category   : Implementation
Language   : Python3
Link       : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
"""

def row_sum(mat, n):
    row=[]
    for i in range(n): row.append(sum(mat[i]))
    row.sort()
    return row

def col_sum(mat, n):
    col=[]
    for i in range(n): col.append(sum(row[i] for row in mat))
    col.sort()
    return col

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat =[]
        for i in range(n):
            mylist = list(map(int, input().split()))
            mat.append(mylist)
        
        row = row_sum(mat, n)
        col = col_sum(mat, n)
        if(row == col): print("Possible")
        else: print("Impossible")

if __name__ == "__main__":
    main()
