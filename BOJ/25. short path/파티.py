# 221005 / 파티
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

n,m,x = map(int,input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    g[a].append([c,b])

def dijkstra(start,dest):
    q = []
    q.append([0,start])
    d = [INF] * (n+1)
    d[start] = 0
    while q:
        w, now = heapq.heappop(q)
        if d[now] < w: continue
        if now == dest : break
        for nw, next in g[now]:
            nwei = nw + w
            if d[next] > nwei:
                heapq.heappush(q,[nwei,next])
                d[next] = nwei

    return d[dest]
ans = 0

for i in range(1,n+1):
    temp = dijkstra(i,x) + dijkstra(x,i)
    ans = max(ans,temp)

print(ans)