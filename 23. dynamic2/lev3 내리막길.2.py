# 220517 / dp2 / 1520 / 내리막길
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
mp = []
for _ in range(n):
    mp.append(list(map(int,input().split())))

dp = [[0]*(m) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(a,b):
    if a == n-1 and b == m-1:
        return 1

    if dp[a][b]:
        return dp[a][b]

    dp[a][b] = 0
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0<=x<n and 0<=y<m:
            if mp[a][b] > mp[x][y]:
                dp[a][b] += dfs(x,y)
    return dp[a][b]

print(dfs(0,0))
