# 220901 / 매출하락 최소화
def solution(sales, links):
    answer = 0
    n = len(sales)
    team = [[] for _ in range(n+1)]
    dp = [[0,0] for _ in range(n+1)]

    for a,b in links:
        team[a].append(b)
        
    def dfs(parent):
        if not team[parent]:
            dp[parent][0],dp[parent][1] = 0, sales[parent-1]
            return
        
        sum_child = 0
        min_val = 1e9
        for child in team[parent]:
            dfs(child)
            sum_child += min(dp[child][0],dp[child][1])
            min_val = min(min_val, dp[child][1]- dp[child][0])
        if min_val < 0: min_val = 0
        
        dp[parent][0] = sum_child + min_val
        dp[parent][1] = sales[parent-1] + sum_child
        
    dfs(1)
    answer = min(dp[1][0],dp[1][1])
    return answer