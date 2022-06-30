# 220202 / 동적계획법1 / 2565 / 전깃줄

n = int(input())
A = []
B = []
dp = [0]*n
for i in range(n):
    [a, b] = map(int, input().split())
    A.append([a,b])

B = sorted(A, key=lambda x: x[0])

for i in range(n):
    for j in range(i):
        if B[i][0] > B[j][0] and B[i][1] > B[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1


print(n-max(dp))
"""
8
1 8 -7
3 9 - 6 
2 2 0
4 1 3 
6 4 2
10 10
9 7 2
7 6 1
"""