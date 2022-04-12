# 220412 / 동적계획법 2 / 2293 / 동전 1

n,k = int(input())
dp = [0]*(k+1)
dp[0] = 1
coin = []
for _ in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(1,k+1):
        if j >= i:
            dp[j] += dp[j-i]

print(dp[k])

