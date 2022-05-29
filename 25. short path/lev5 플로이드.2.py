# 220529 / 최단 경로 / 11404 / 플로이드
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
d = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if d[a][b] > c:
        d[a][b] = c


for i in range(1,n+1):
    d[i][i] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            d[j][k] = min(d[j][k], d[j][i] + d[i][k])



for i in range(1,n+1):
    for j in range(1,n+1):
        print(d[i][j], end=' ')
    print()