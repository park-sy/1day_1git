# 220504 / 동적계획법1 / 12865 / 평범한 배낭
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nap = [[0,0]]
for _ in range(n):
    nap.append(list(map(int,input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        wei = nap[i][0]
        val = nap[i][1]

        if j < wei:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(val + dp[i-1][j-wei],dp[i-1][j])

print(dp[-1][-1])