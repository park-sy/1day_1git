# 220711 / dfs bfs / 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
n,m,k,x = map(int,input().split())
g = [[] for _ in range(n+1)]
sol = []
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)


def bfs(start,k):
    d = [INF]*(n+1)
    q = deque([start])
    d[start] = 0
    while q:
        now = q.popleft()
        for i in g[now]:
            if d[i] > d[now] + 1:
                d[i] = d[now] + 1
                q.append(i)
    
    for i in range(1,n+1):
        if d[i] == k:
            sol.append(i)


bfs(x,k)
if not sol:
    print(-1)
else:
    for i in sol:
        print(i)

