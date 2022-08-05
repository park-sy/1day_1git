# 220805 / 연구소
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n,m = map(int,input().split())

g = []
virus = []
for i in range(n):
    g.append(list(map(int,input().split())))
    for j in range(m):
        if g[i][j] == 2:
            virus.append([i,j])

ans = 0
temp = [[0]*m for _ in range(n)]
def dfs(cnt):
    global ans
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = g[i][j]
        ans = max(ans,cnt_safe(temp))
        for i in range(n):
            for j in range(m):
                temp[i][j] = 0
        return

    for i in range(n):
        for j in range(m):
            if not g[i][j]:
                g[i][j] = 1
                dfs(cnt+1)
                g[i][j] = 0 



def cnt_safe(g):
    q = deque(virus)

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not g[nx][ny]:
                g[nx][ny] = 2
                q.append([nx,ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not g[i][j]:
                cnt += 1
    return cnt

dfs(0)

print(ans)