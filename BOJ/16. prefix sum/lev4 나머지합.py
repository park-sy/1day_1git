# 220420 / 누적합 / 10986 / 나머지 합
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = [0] + list(map(int,input().split()))
dp = [0]*(n+1)
cnt = [0]*(m)
for i in range(1,n+1):
    dp[i] = (dp[i-1] + nums[i]) % m
    cnt[dp[i]] += 1

ans = cnt[0]
for i in range(m):
    ans += (cnt[i]*(cnt[i]-1)) / 2

print(int(ans))
