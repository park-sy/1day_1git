# 220204 / 동적계획법 1 / 12865 / 평범한 배낭

n, k = map(int, input().split())

s = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    s.append(list(map(int, input().split())))
    

for i in range(1,n+1):
    for j in range(1,k+1):
        weight = s[i][0]
        value = s[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight],dp[i-1][j])

print(dp[-1][-1])

"""
k - s[0][0]
s[0] : dp[0] > 점수 기록 w[0] > 무게 기록
s[1] : w[0] + w[1] < k 라면 점수기록 무게 기록

"""
