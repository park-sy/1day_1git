# 220214 / 분할정복 / 1780 / 종이의 개수
import sys
input = sys.stdin.readline
n = int(input())

sqr = []
for i in range(n):
    sqr.append(list(map(int,input().split())))
w = [0,0,0]
def div(arr):
    
    l = len(arr[0])
    r = arr[0][0]
    for i in range(l):
        t = True
        for j in range(l):
            if arr[i][j] != r :
                t = False
                break
        if t == False:
            break
        
        if i == l-1 and r == -1:
            w[0] += 1
            return 
        elif i == l-1 and r == 0:
            w[1] += 1
            return
        elif i == l-1 and r == 1:
            w[2] += 1
            return
                
    v = l//3
    arr1 = [[arr[i][j] for j in range(v) ] for i in range(v)]
    arr2 = [[arr[i][j] for j in range(v) ] for i in range(v,l-v)]
    arr3 = [[arr[i][j] for j in range(v) ] for i in range(l-v,l)]
    arr4 = [[arr[i][j] for j in range(v,l-v) ] for i in range(v)]
    arr5 = [[arr[i][j] for j in range(v,l-v) ] for i in range(v,l-v)]
    arr6 = [[arr[i][j] for j in range(v,l-v) ] for i in range(l-v,l)]
    arr7 = [[arr[i][j] for j in range(l-v,l) ] for i in range(v)]
    arr8 = [[arr[i][j] for j in range(l-v,l) ] for i in range(v,l-v)]
    arr9 = [[arr[i][j] for j in range(l-v,l) ] for i in range(l-v,l)]

    div(arr1)
    div(arr2)
    div(arr3)
    div(arr4)
    div(arr5)
    div(arr6)
    div(arr7)
    div(arr8)
    div(arr9)    


div(sqr)
for i in w:
    print(i)

