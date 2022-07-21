# 220721 / dp / 병사 배치하기
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if p[i] < p[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n - max(dp))