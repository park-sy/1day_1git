# 220501 / 동적계획법 1 / 1904 / 01타일
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = (dp[i-2]+dp[i-1])%15746

print(dp[n])
