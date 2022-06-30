# 220406 / 트리에서 동적 계획법 / 1949 / 우수 마을
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
w = [0]+list(map(int,input().split()))
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dp = [[0,0]for _ in range(n+1)]
visit = [False]*(n+1)

def dfs(node):
    visit[node] = True
    dp[node][0] = w[node]
    for i in graph[node]:
        if not visit[i]:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += max(dp[i][0],dp[i][1])

dfs(1)
print(max(dp[1]))