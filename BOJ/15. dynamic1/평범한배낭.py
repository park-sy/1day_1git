# 220806 / 평범한 배낭
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

bag = [[]]
for i in range(n):
    bag.append(list(map(int,input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    w = bag[i][0]
    v = bag[i][1]
    for j in range(1,m+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v+dp[i-1][j-w],dp[i-1][j])

print(dp[n][m])


