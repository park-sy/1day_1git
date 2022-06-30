# 220315 / 동적계획법과 최단거리 역추적 / 14002 / 가장 긴 증가하는 부분 수열4

n = int(input())
a = list(map(int,input().split()))

dp = [[0,[]]for _ in range(n)]
m_num = 0
id = 0

for i in range(n):
    k = -1
    for j in range(i):
        if a[i] > a[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
            k = j
    dp[i][0]+=1
    if k != -1:
        dp[i][1]= dp[k][1] + [a[i]]
    else: dp[i][1] = [a[i]]
    if dp[i][0] > m_num:
        m_num = dp[i][0]
        id = i
print(dp[id][0])
print(*dp[id][1])
