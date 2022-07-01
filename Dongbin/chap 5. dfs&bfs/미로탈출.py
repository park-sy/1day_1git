# 220701 / dfs bfs / 미로탈출
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input())))

visit = [[0]*m for _ in range(n)]
def bfs():
    q = deque([(0,0)])
    visit[0][0] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and g[x][y] == 1 and not visit[x][y] :
                g[x][y] += g[a][b]
                q.append([x,y])
                visit[x][y] = 0

bfs()
print(g[n-1][m-1])
