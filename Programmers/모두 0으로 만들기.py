# 220914 / 모두 0으로 만들기
import sys
sys.setrecursionlimit(300000)
def solution(a, edges):
    global answer 
    answer = 0
    if sum(a) != 0:
        return -1
    g = [[] for _ in range(len(a))]
    for i,j in edges:
        g[i].append(j)
        g[j].append(i)
    
    visit = [0]*len(a)
    def dfs(now):
        global answer
        visit[now] = 1
        v = a[now]
        for child in g[now]:
            if not visit[child]:
                v += dfs(child)

        answer += abs(v)
        return v
    
    dfs(0)
    return answer