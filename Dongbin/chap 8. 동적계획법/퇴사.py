# 220720 / dp / 퇴사
import sys
input = sys.stdin.readline

n = int(input())
dp =[[0]*(n+2) for _ in range(n+1)]

sc = [[]]
for _ in range(n):
    sc.append(list(map(int,input().split())))

res = 0
for i in range(1,n+1):
    for j in range(1,n+2):
         dp[i][j] = max(dp[i][j-1],dp[i-1][j])
         if j == i + sc[i][0]:
            dp[i][j] = max(dp[i][j],dp[i][i]+sc[i][1])

        
print(dp[-1][-1])