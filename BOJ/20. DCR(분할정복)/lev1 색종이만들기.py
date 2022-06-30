# 220214 / 분할정복 / 2630 / 색종이만들기
import sys
input = sys.stdin.readline
n = int(input())

sqr = []
for i in range(n):
    sqr.append(list(map(int,input().split())))
w = [0]
b = [0]
def div(arr):
    print(arr)
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
            w[0] += 1
            return 
        elif i == l-1 and r == 1:
            b[0] += 1
            return
                

    arr1 = [[arr[i][j] for j in range(l//2) ] for i in range(l//2)]
    arr2 = [[arr[i][j] for j in range(l//2, l) ] for i in range(l//2)]
    arr3 = [[arr[i][j] for j in range(l//2) ] for i in range(l//2, l)]
    arr4 = [[arr[i][j] for j in range(l//2,l) ] for i in range(l//2,l)]
    div(arr1)
    div(arr2)
    div(arr3)
    div(arr4)

div(sqr)
print(w[0])
print(b[0])
