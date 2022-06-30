# 220418 / 누적합 / 2559 / 수열
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
tem = [0] + list(map(int,input().split()))

dp = [0]*(n+1)
res = sys.maxsize*-1

for i in range(1,n+1):
    dp[i] = dp[i-1] + tem[i]
    if i >= k:
        res = max(res,dp[i]-dp[i-k])

print(res)