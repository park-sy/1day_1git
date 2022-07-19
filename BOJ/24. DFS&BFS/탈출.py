# 220718 / bfs / 3055 / 탈출
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
g = []
for i in range(n):
    g.append(list(input().rstrip()))
    for j in range(m):
        if g[i][j] == "D":
            bx,by = i,j

d = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque([[]])

def bfs(bx,by):
    flag = 0
    if g[bx][by] == "S":
        return d[bx][by]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if g[nx][ny] == '.' or g[nx][ny] == 'D' and g[x][y] =='S':
                    g[nx][ny] = 'S'
                    d[nx][ny] = d[x][y] + 1
                    q.append([nx,ny])
                if g[nx][ny] == '.' or g[nx][ny] == 'S' and g[x][y] =='*':
                    g[nx][ny] = '*'
                    q.append([nx,ny])                     
    return "KAKTUS"

for i in range(n):
    for j in range(m):
        if g[i][j] == "S":
            q.append([i,j])
    
for i in range(n):
    for j in range(m):
        if g[i][j] == "*":
            q.append([i,j])

print(bfs(bx,by))