# 220202 / 동적계획법1 / 11054 / 가장 긴 바이토닉 부분 수열

n = int(input())
arr = list(map(int, input().split()))
arr2 = arr[::-1]
dp1 = [0]*n
dp2 = [0]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp1[i] < dp1[j]:
            dp1[i] = dp1[j]
        
        if arr2[i] > arr2[j] and dp2[i] < dp2[j]:
            dp2[i] = dp2[j]
    dp1[i]+=1
    dp2[i]+=1
dp = [x+y for x,y in zip(dp1,dp2[::-1])]

print(max(dp)-1)
