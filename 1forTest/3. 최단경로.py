import heapq,sys
INF = sys.maxsize

g = []
def dikjstra(n, start):

    q = [[0,start]]
    d = [INF] * n
    d[start] = 0

    while q:
        w,now = heapq.heappop(q)
        if d[now] < w: continue

        for next,nwei in g[now]:
            if d[next] > w + nwei:
                d[next] = w + nwei
                heapq.heappush([w+nwei,next])


def f_w(n):

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                g[i][j] = min(g[i][j],g[i][k]+g[k][i])



from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    answer = [-1,1e9]
    q = []
    g = [[] for _ in range(n+1)]
    for i,j,w in paths:
        g[i].append([w,j])
        g[j].append([w,i])
    
    visit = [1e9] * (n+1)
    for i in gates:
        heapq.heappush(q,(0,i))
        visit[i] = 0 
        
    while q:
        w,now = heapq.heappop(q)
        if now in summits or visit[now] < w:
            continue
            
        for nwei,next in g[now]:
            new_int = max(w,nwei)
            if visit[next] > new_int:
                visit[next] = new_int
                heapq.heappush(q,(new_int,next))
    
    summits.sort()
    for i in summits:
        if answer[1] > visit[i]:
            answer = [i,visit[i]]
            
    return answer