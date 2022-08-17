# 220817 / 합승 택시 요금
import sys
INF = sys.maxsize
def solution(n, s, a, b, fares):
    answer = INF
    d = [[INF]*(n+1) for _ in range(n+1)]

    for v1,v2,w in fares:
        d[v1][v2] = min(d[v1][v2],w)
        d[v2][v1] = min(d[v2][v1],w)
    
    for i in range(1,n+1):
        d[i][i] = 0
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
                
    for i in range(1,n+1):
        temp = d[s][i] + d[i][a] + d[i][b]
        answer = min(temp,answer)
    return answer