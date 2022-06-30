# 220515 / dp2 / 11066 / 파일합치기
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    file = [0] + list(map(int,input().split()))
    pre = [0]*(n+1)
    for i in range(1,n+1):
        pre[i] = file[i] + pre[i-1]
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+2-i):
            dp[j][j+i-1] = min(dp[j][j+k]+dp[j+k+1][j+i-1] for k in range(i-1)) + (pre[j+i-1]-pre[j-1])
    print(dp[1][n])
            

