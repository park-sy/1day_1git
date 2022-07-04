# 220704 / 최단경로 / 미래 도시
import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())

d = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    d[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    d[a][b] = 1
    d[b][a] = 1

x,k = map(int,input().split())



for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]

res = d[1][k]+d[k][x]
if res >= INF:
    print(-1)
else:
    print(res)

