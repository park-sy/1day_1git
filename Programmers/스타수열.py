# 220914 / 스타 수열
def solution(a):
    answer = -1
    n = len(a)
    if n == 1:
        return 0
    
    dp = [0] * n
    last = [-1] * n
    
    for i in range(n):
        now = a[i]
        flag = 0
        if i+1 < n and a[i+1] != now:            
            flag = 1
        if i - 1 >= 0 and a[i-1] != now and i-1 != last[now]:
            flag = 2
            
        if flag:
            if flag == 1: last[now] = i+1
            else: last[now] = i-1
            dp[now] += 1
        
    return max(dp)*2