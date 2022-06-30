# 220309 / 최단경로 / 1956 / 운동
import sys,heapq
INF = sys.maxsize
input = sys.stdin.readline

v,e = map(int,input().split())

def floyd():
    for m in range(1,v+1):
        for f in range(1,v+1):
            for b in range(1,v+1):
                if d[f][b] > d[f][m] + d[m][b]:
                    d[f][b] = d[f][m] + d[m][b]


d = [[INF for _ in range(v+1)] for _ in range(v+1)]
for i in range(1,v+1):
    d[i][i] = 0

for i in range(e):
    e1, e2, w = map(int,input().split())
    if d[e1][e2] > w:
        d[e1][e2] = w
result = INF
floyd()

for i in range(v):
    result = min(result, d[i][i])
if result == INF:
    print(-1)
else:
    print(result)


