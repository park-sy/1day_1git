# 220507 / 분할정복 / 10830 / 행렬제곱
import sys
input = sys.stdin.readline
def matpower(a,b):
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k]*b[k][j]
    return c

def power(a,b):
    if b == 1:
        return a
    temp = power(a,b//2)
    if b % 2 == 0:
        return matpower(temp,temp)
    else:
        return matpower(matpower(temp,temp),mrx)
    
n,m = map(int,input().split())
mrx = []
for _ in range(n):
    mrx.append(list(map(int,input().split())))

k = power(mrx,m)
for i in range(n):
    for j in range(n):
        print(k[i]%1000,end =' ')
    print('')
