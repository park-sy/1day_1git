# 220701 / dfs bfs / 음료수 얼려먹기
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input())))

def bfs(a,b):
    q = deque([(a,b)])
    g[a][b] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and g[nx][ny] == 0:

                q.append([nx,ny])
                g[nx][ny] = 1

cnt = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            bfs(i,j)
            cnt+=1
print(cnt)