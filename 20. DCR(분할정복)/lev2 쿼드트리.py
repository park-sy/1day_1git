# 220214 / 분할정복 / 1992 / 쿼드트리
import sys
input = sys.stdin.readline
n = int(input())

sqr = []
for i in range(n):
    sqr.append(list(map(int,list(str(input().strip())))))
w = []
def div(arr):
    
    l = len(arr[0])
    r = arr[0][0]
    for i in range(l):
        t = True
        for j in range(l):
            if arr[i][j] != r:
                t = False
                break
        if t == False:
            break
        
        if i == l-1 and r == 0:
            w.append(r)
            return 
        elif i == l-1 and r == 1:
            w.append(r)
            return
                

    arr1 = [[arr[i][j] for j in range(l//2) ] for i in range(l//2)]
    arr2 = [[arr[i][j] for j in range(l//2, l) ] for i in range(l//2)]
    arr3 = [[arr[i][j] for j in range(l//2) ] for i in range(l//2, l)]
    arr4 = [[arr[i][j] for j in range(l//2,l) ] for i in range(l//2,l)]
    w.append('(')
    div(arr1)
    div(arr2)
    div(arr3)
    div(arr4)
    w.append(')')

div(sqr)
for i in w:
    print(i,end='')

