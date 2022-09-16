# 220916 / 순위
def solution(n, results):
    answer = 0
    g = [[0]*(n+1) for _ in range(n+1)]
    
    for i,j in results:
        g[i][j] = 1
        g[j][i] = -1
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i != j and g[i][j] == 0:
                    if g[i][k] == 1 and g[k][j] == 1:
                        g[i][j] = 1
                    elif g[i][k] == -1 and g[k][j] == -1:
                        g[i][j] = -1
    for i in range(1,n+1):
        answer += (g[i][1:].count(0) == 1)

        
    return answer