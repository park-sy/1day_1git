# 221007 / 로봇청소기
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
r,c,d = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

cnt = 1
q = deque()
q.append([r,c])
g[r][c] = 2
while q:
    x,y = q.popleft()
    flag = 0
    for i in range(4):
        d = (d-1)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not g[nx][ny]:
            flag = 1
            cnt += 1
            q.append([nx,ny])
            g[nx][ny] = 2
            break
    if not flag:
        nx = x + dx[(d-2)%4]
        ny = y + dy[(d-2)%4]
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] != 1:
            q.append([nx,ny])

print(cnt)