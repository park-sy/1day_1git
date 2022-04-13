# 220413 / 동적계획법 2 / 7579 / 앱

n, m = map(int,input().split())
corr = [0] + list(map(int,input().split()))
cost = [0] + list(map(int,input().split()))
result = sum(cost)
dp = [[0]*(result+1) for _ in range(n+1)]

for i in range(n):
    b = corr[i]
    c = cost[i]
    for j in range(1,sum(cost)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(b + dp[i-1][j-c],dp[i-1][j])
        if dp[i][j] >= m:
            result = min(result,j)

print(result)