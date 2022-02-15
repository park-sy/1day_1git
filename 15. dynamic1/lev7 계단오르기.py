# 220129 / 동적계획법1 / 2579 / 계단 오르기

n = int(input())
stairs = []

for i in range(n):
    stairs.append(int(input()))

dp=[]

dp.append(stairs[0])
dp.append(max(stairs[0]+stairs[1],stairs[1]))
dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
for i in range(3, n):
    dp.append(max(dp[i-3]+stairs[i]+stairs[i-1], dp[i-2]+stairs[i]))
    print(dp)
print(dp[n-1])