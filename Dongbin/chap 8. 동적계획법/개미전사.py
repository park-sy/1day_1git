# 220703 / 동적계획법 / 개미전사
import sys
n = int(input())
wh = [0] + list(map(int,input().split()))

dp = [0]*(n+1)
dp[1] = wh[1]
dp[2] = max(wh[2], dp[1])
for i in range(2,n+1):
    dp[i] = max(dp[i-1],dp[i-2] + wh[i])

print(max(dp))
