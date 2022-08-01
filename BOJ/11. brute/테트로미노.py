# 220801 / 14500 / 테트로미노
import sys

input = sys.stdin.readline
dx = [0,0,-1,1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
g = []
max_val = 0
for i in range(n):
    g.append(list(map(int,input().split())))
    max_val = max(max_val, max(g[i]))
visit = [[0]*m for _ in range(n)]
ans = 0

def dfs(a,b,cnt,total):
    global ans
    if ans >= total + max_val*(3-cnt):
        return
    if cnt == 3:
        ans = max(ans,total)
        return

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if cnt == 1:
                visit[nx][ny] = 1
                dfs(a,n,cnt +1, total + g[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx,ny,cnt +1, total + g[nx][ny])
            visit[nx][ny] = 0
     
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i,j,0,g[i][j])
        visit[i][j] = 0


print(ans)
