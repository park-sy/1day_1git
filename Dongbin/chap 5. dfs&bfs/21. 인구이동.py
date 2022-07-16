#220716 / dfs  bfs / 인구이동
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,l,r = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))
visit = [[0]*(n) for _ in range(n)]

def bfs(a,b):
    q = deque([[a,b]])
    temp = [[a,b]]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                diff = abs(g[nx][ny] - g[x][y])
                if l <= diff <= r:
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
                
    return temp

cnt = 0
while 1:
    visit = [[0] * n for i in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                visit[i][j] = 1
                temp = bfs(i,j)
                if len(temp) > 1:
                    flag = 1
                    num = sum(g[x][y] for x,y in temp) // len(temp)
                    for x,y in temp:
                        g[x][y] = num
    if not flag:
        break
    cnt += 1

print(cnt)
