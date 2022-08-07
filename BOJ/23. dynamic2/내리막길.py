# 220807 / 1520 / 내리막길
import sys
from collections import deque
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [-1,1,0,0]
n,m = map(int,input().split())

g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

d = [[-1]*(m) for _ in range(n)]

def dfs(a,b):
    if a == n- 1 and b == m-1:
        return 1

    if d[a][b] != -1:
        return d[a][b]
    d[a][b] = 0
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if g[nx][ny] < g[a][b]:
                d[a][b] += dfs(nx,ny) 
    
    return d[a][b]
    


print(dfs(0,0))
print(d)  