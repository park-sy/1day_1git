# 220703 / 동적계획법 / 효율적인 화폐 구성
import sys
INF = sys.maxsize
input = sys.stdin.readline
n,m = map(int,input().split())
mon = []
for i in range(n):
    mon.append(int(input()))

dp = [INF]*(m+1)
dp[0] = 0
for i in mon:
    for j in range(i,m+1):
        if dp[j-i] != INF:
            dp[j] = min(dp[j-i]+1, dp[j])

if dp[m] == INF:
    print(-1)
else:
    print(dp[m])