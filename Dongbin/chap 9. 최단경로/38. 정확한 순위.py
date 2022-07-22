# 220722 / 최단경로 / 정확한 순위
import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
d = [[INF] *(n+1) for _ in range(n+1)]

for _ in range(n):
    a,b = map(int,input().split())
    d[a][b] = 1

for i in range(1,n+1):
    d[i][i] = 0



for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]) 

res = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if d[i][j] != INF or d[i][j] != INF:
            cnt += 1
    if cnt == n:
        res += 1
print(res)
