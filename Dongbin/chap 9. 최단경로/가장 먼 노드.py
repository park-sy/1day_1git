# 220727 / 가장먼노드
import sys, heapq
INF = sys.maxsize
def solution(n, edge):
    g = [[] for _ in range(n+1)]
    for v1,v2 in edge:
        g[v1].append(v2)
        g[v2].append(v1)
        
    d = [INF] *(n+1)
    d[1] = 0
    q = []
    heapq.heappush(q,(0,1))
    while q:
        w, now = heapq.heappop(q)
        if d[now] < w: continue
        
        for next in g[now]:
            if d[next] > w + 1:
                d[next] = w + 1
                heapq.heappush(q,(w+1, next))
                
    answer = 0
    maxn = d[1]
    for i in d:
        if maxn == i:
            answer += 1
        elif i != INF and i > maxn:
            answer = 1
            maxn = i
        
            
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))