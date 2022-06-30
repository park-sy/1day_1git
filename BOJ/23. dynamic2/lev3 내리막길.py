# 220409 / 동적계획법2 / 1520 / 내리막길 / 시간초과
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

n,m = map(int,input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dp = [[-1 for _ in range(m)]for _ in range(n)]

def dfs(a,b):
    if a == n-1 and b == m-1:
        return 1
    
    if dp[a][b] != -1:
        return dp[a][b]
    dp[a][b] = 0
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m:
            if maps[x][y] < maps[a][b]:
                dp[a][b] += dfs(x,y)
    return dp[a][b]

print(dfs(0,0))