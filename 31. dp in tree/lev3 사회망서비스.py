# 220405 / 트리에서 동적할당 / 2533 / 사회망서비스(SNS)
import sys
input = sys.stdin.readline

n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visit = [False]*(n+1)
dp =[[0,0]for _ in range(n+1)]

def dfs(start):
    visit[start] = True
    dp[start][0] = 1
    for i in graph[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += min(dp[i][0],dp[i][1])
            dp[start][1] += dp[i][0]

dfs(1)
print(min(dp[1][0],dp[1][1]))