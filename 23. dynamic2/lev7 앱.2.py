# 220522 / dp2 / 7579 / 앱
import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
byte = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
result = sum(cost)

dp = [[0]*(sum(cost)+1) for _ in range(n+1)]

for i in range(1,n+1):
    b = byte[i]
    c = cost[i]

    for j in range(1,sum(cost)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(b + dp[i-1][j-c],dp[i-1][j])
        if dp[i][j] >= m:
            result = min(result,j)

print(result)