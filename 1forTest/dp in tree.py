import sys
sys.setrecursionlimit(10**6)
n = int(input())

g = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

dp = [[0,0] for _ in range(n+1)]


visit = [0] * (n+1)
def dfs(now):
    visit[now] = 1
    dp[now][1] = 1
    for next in g[now]:
        if not visit[next]:
            dfs(next)
            dp[now][0] += dp[next][1]
            dp[now][1] += min(dp[next])



dfs(1)

print(min(dp[1]))


