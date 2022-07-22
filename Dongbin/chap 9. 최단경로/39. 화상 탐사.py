# 220722 / sp / 화성 탐사
import sys,heapq
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n = int(input())
g = []

for i in range(n):
    g.append(list(map(int,input().split())))

d = [[INF]*(n) for _ in range(n)]

def bfs():
    q = []
    heapq.heappush(q,(g[0][0],0,0))
    d[0][0] = g[0][0]
    while q:
        dist, x,y = heapq.heappop(q)
        if dist[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist+g[nx][ny]
                if cost < d[nx][ny]:
                    d[nx][ny] = cost
                    q.append(q, (cost,nx,ny))

bfs()
print(d[n-1][n-1])

"""
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
"""