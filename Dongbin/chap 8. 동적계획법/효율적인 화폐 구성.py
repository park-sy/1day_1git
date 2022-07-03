# 220703 / 동적계획법 / 효율적인 화폐 구성
import sys
INF = sys.maxsize
input = sys.stdin.readline
n,m = map(int,input().split())
mon = []
for i in range(n):
    mon.append(int(input()))

dp = [INF]*(10001)
for coin in mon:
    dp[coin] = 1

for i in range(1,m+1):
    for coin in mon:
        if i - coin > 0:
            dp[i] = min(dp[i],dp[i-coin]+1)
print(dp)
if dp[m] == INF:
    print(-1)
else:
    print(dp[m])