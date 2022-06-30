# 220307 / 최단경로 / 11404 / 플로이드
import sys
INF = sys.maxsize

v = int(input())
e = int(input())

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
floyd()
for i in range(1,v+1):
    for k in range(1,v+1):
        if d[i][k] != INF:
            print(d[i][k], end=' ')
        else: print(0, end=' ')
    print('')