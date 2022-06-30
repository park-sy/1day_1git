# 220520 / dp2 / 2293 / 동전 1
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [0]*(k+1)
dp[0] = 1
coin = []
for _ in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(1,k+1):
        if j >= i:
            dp[j] += dp[j-i]
        print(i,j,dp)
print(dp[k])
print(dp)