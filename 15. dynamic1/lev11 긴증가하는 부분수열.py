#220201 / 동적계획법1 / 11053 / 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n


for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i]+=1

print(max(dp))

