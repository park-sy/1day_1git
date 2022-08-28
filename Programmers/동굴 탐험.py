# 220828 / 동굴 탐험
from collections import deque

def solution(n, path, order):

    g = [[] for _ in range(n)]
    for a,b in path:
        g[a].append(b)
        g[b].append(a)
    
    visit = [0] *(n)
    pre = [0] * n
    for a,b in order:
        pre[b] = a
    q = deque([0])
    after = {}
    cnt = 0
    while q:
        now = q.popleft()
        
        if pre[now] and not visit[pre[now]]:
            after[pre[now]] = now
            continue
        visit[now] = 1
        cnt += 1
        
        for next in g[now]:
            if not visit[next]:
                q.append(next)
                
        if now in after:
            q.append(after[now])
            
    return n == cnt