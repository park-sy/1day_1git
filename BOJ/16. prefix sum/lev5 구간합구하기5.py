# 220421 / 누적합 / 11660 / 구간 합 구하기 5
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = [[]]
for _ in range(n):
    nums.append([0]+list(map(int,input().split())))

dp = [[0]*(n+1)for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i][j-1] + nums[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    sum = 0
    for i in range(x1,x2+1):
        sum += dp[i][y2] - dp[i][y1-1]
    print(sum)