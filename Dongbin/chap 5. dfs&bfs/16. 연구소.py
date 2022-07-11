# 220711 / dfs bfs / 연구소
import sys
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().split())
g = []
temp = [[0]*(m) for _ in range(n)]
for _ in range(n):
    g.append(list(map(int,input().split())))

res = 0
def virus(a,b):
    q = deque([[a,b]])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                    g[nx][ny] = 2
                    q.append([nx,ny])
def cnt_safe():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(cnt):
    global res
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = g[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        res = max(res, cnt_safe)
        return
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                g[i][j] = 1
                cnt += 1
                dfs(cnt)
                g[i][j] = 0
                cnt -= 1

dfs(0)
print(res)
