#220201 / 동적계획법1 / 11053 / 가장 긴 증가하는 부분 수열

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*n
print(arr[:3])

dp[0] = 1
for i in range(1, n):
    j = arr[i]
    while True:
        j -= 1
        if j in arr[:i]:
            b = arr[:i]
            a = b[::-1].index(j)
            dp[i] = dp[i-a] + 1
            break
        
        if j <= min(arr):
            dp[i] = 1
            break

print(max(dp))
print(dp)

"""
2 7
7-2+1
0 2 7
7-2
1 1
2 2번째 이전 값 비교
"""