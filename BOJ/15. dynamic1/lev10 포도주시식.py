# 220131 / 동적계획법 1 / 2156 / 포도주 시식

n = int(input())
arr=[0]

for i in range(n):
    arr.append(int(input()))

dp = [0]

dp.append(arr[1])
if n > 1:
    dp.append(arr[1]+arr[2])

for i in range(3,n+1):
    dp.append(max(dp[i-1],dp[i-3]+arr[i]+arr[i-1], dp[i-2]+arr[i]))

print(dp[n])
