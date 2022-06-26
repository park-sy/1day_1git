# 220626 / dp in tree / 1949 / 우수마을
import sys
input = sys.stdin.readline

n = int(input())
wei = list(map(int,input().split()))
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)

dp = [[0,0] for _ in range(n)]
visit = [0] * (n+1)
def dfs(start):
    visit[start] = 1
    dp[start][0] = wei[start]
    for i in g[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += max(dp[i][0],dp[i][1])

