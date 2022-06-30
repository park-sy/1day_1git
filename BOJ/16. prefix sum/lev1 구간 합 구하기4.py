# 220417 / 누적합 / 11659 / 구간 합 구하기4
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

nums = [0]+ list(map(int,input().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + nums[i]

for _ in range(m):
    n1,n2 = map(int,input().split())
    print(dp[n2]-dp[n1-1])
