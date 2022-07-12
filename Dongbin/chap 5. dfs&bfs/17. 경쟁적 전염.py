# 220712 / dfs bfs / 경쟁적 전염
import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
g = [[]]
data = []
for i in range(1,n+1):
    g.append([0] + list(map(int,input().split())))
    for j in range(1,n+1):
        if g[i][j]:
            data.append([g[i][j],0,i,j])
S,X,Y = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]
data.sort()
q = deque(data)

while q:
    val,now,x,y = q.popleft()
    if now == S: break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx < n+1 and 0 < ny < n+1:
            if g[nx][ny] == 0:
                g[nx][ny] = val
                q.append([val,now+1,nx,ny])


print(g[X][Y])
