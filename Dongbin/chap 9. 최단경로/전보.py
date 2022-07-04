# 220704 / 최단경로 / 전보
import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize
n,m,c = map(int,input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w = map(int,input().split())
    g[a].append((w,b))
    g[b].append((w,a))

d = [INF]*(n+1)
def dijkstra(start):
    d[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        wei, now = heapq.heappop(q)
        if d[now] < wei:
            continue

        for nwei, next in g[now]:
            
            dist = nwei + wei
            if d[next] > dist:
                d[next] = dist
                heapq.heappush(q,(nwei,next))
dijkstra(c)

res = 0
cnt = 0
for i in d:
    if i != 0 and i != INF:
        cnt += 1
        res = max(res,i)

print(cnt,res)