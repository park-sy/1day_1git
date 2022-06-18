# 220618 / 최단경로 / 11657 / 타임머신
import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
g = []
dist = [INF]*(n+1)

def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            n1,n2, c = g[j]
            if dist[n1] != INF and dist[n2] > dist[n1] + c:
                dist[n2] = dist[n1] + c
                if i == n-1:
                    return True
    return False

for _ in range(m):
    n1,n2,c = map(int,input().split())
    g.append([n1,n2,c])

if bellman_ford(1):
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])

