# 220502 / 동적계획법1 / 2579 / 계단오르기
import sys
input = sys.stdin.readline

n = int(input())
stair = [0]
for _ in range(n):
    stair.append(int(input()))

dp = [0]*(n+1)
dp[1] = stair[1]
if n >= 2:
    dp[2] = dp[1] + stair[2]
if n >= 3:
    for i in range(3,n+1):
        dp[i] = max(dp[i-2],dp[i-3]+stair[i-1]) + stair[i]


print(dp[n])
