# 220727 / 네트워크
from collections import deque

def solution(n, g):
    answer = 0
    
    visit = [0] * (n)
    
    for i in range(n):
        if not visit[i]:
            bfs(i,n,g,visit)
            answer += 1
    
    
    return answer


def bfs(x,n,g,visit):
    
    visit[x] = 1
    q = deque([x])
    
    while q:
        a = q.popleft()  
        for i in range(n):
            if not visit[i] and g[a][i]:
                visit[i] = 1
                q.append(i)