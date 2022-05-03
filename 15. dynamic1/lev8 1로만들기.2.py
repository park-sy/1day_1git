# 220503 / 동적계획법1 / 1463 / 1로만들기
import sys
n = int(input())
dp = [0]*(n+1)

for i in range(2,n+1):
    a = sys.maxsize
    b = sys.maxsize
    c = dp[i-1] + 1
    if i % 3 == 0:
        a = dp[i//3] + 1
    if i % 2 == 0:
        b = dp[i//2] + 1
    dp[i] = min(a,b,c)

print(dp[n]) 