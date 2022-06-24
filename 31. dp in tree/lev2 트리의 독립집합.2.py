# 220624 / dp in tree / 2213 / 트리의 독립집합
import sys
input = sys.stdin.readline

n = int(input())
wei = [0] + list(map(int,input().split()))
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)


dp = [[0] * 2 for i in range(n + 1)]
visit = [0 for i in range(n+1)]
num = [[[], []] for i in range(n + 1)]
def dfs(start):
    visit[start] = 1
    dp[start][0] = wei[start]
    num[start][0].append(start)
    for i in g[start]:
        if not visit[i]:
            dfs(i)
            dp[start][0] += dp[start][1]
        for j in num[i][1]:
            num[start][0].append(j)
        if max(dp[i][1], dp[i][0]) == dp[i][1]:
            dp[start][1] += dp[i][1]
            for k in num[i][1]:
                num[start][1].append(k)
        else:
            dp[start][1] += dp[i][0]
            for k in num[i][0]:
                num[start][1].append(k)

dfs(1)
if max(dp[1][0], dp[1][1]) == dp[1][0]:
    print(dp[1][0])
    a = num[1][0]
    a.sort()
    print(*a)
else:
    print(dp[1][1])
    a = num[1][1]
    a.sort()
    print(*a)