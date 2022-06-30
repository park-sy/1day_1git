# 220308 / 최단경로 / 10217 / KCM Travel
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    v, w, e = map(int,input().split())
    ticket = [[]for _ in range(v+1)]
    for i in range(e):
        v1, v2, c, t = map(int,input().split())
        ticket[v1].append([v2,c,t])
    

    dp = [[INF for _ in range(w+1)] for _ in range(v+1)]
    dp[1][0] = 0

    for co in range(w+1):
        for d in range(1,v+1):
            if dp[d][co] == INF:
                continue
            tm = dp[d][co]
            for dv,dc,dd in ticket[d]:
                if dc+co > w:
                    continue
                dp[dv][dc+co] = min(dp[dv][dc+co],tm+dd)


    result=min(dp[v])
 
    if result==INF:
        print('Poor KCM')
    else:
        print(result)

