# 220731 / 적록색약
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]
n = int(input())

g = []
for _ in range(n):
    g.append(list(map(str,input().rstrip())))
visit = [[0]*n for _ in range(n)]

def bfs(a,b):
    q = deque([[a,b]])
    visit[a][b] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if g[x][y] == g[nx][ny]:
                    q.append([nx,ny])
                    visit[nx][ny] = 1
                    

cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt1 += 1
            

for i in range(n):
    for j in range(n):
        visit[i][j] = 0
        if g[i][j] == 'G':
            g[i][j] = 'R'

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)




