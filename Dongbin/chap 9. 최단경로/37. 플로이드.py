#220721 / sp / 플로이드
import sys
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
d = [[INF] *(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    d[a][b] = min(c,d[a][b])

for i in range(1,n+1):
    d[i][i] = 0


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]) 


for i in range(1,n+1):
    for j in range(1,n+1):
        if d[i][j] == INF:
            print(0,end = ' ')
        else: print(d[i][j], end = ' ')
    print()