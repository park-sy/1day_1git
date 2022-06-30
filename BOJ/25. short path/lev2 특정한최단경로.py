# 220304 / 최단경로 / 1504 / 특정한 최단 경로
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
v,e = map(int,input().split())
g = [[]for _ in range(v+1)]
heap = []


def Dijkstra(start):
    d = [INF]*(v+1)
    d[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        wei, now = heapq.heappop(heap)

        if d[now] < wei:
            continue

        for w, n_node in g[now]:
            n_wei= w + wei
            if n_wei < d[n_node]:
                d[n_node] = n_wei
                heapq.heappush(heap,(n_wei,n_node))

    return d


for i in range(e):
    v1, v2, v3 = map(int,input().split())
    g[v1].append([v3,v2])
    g[v2].append([v3,v1])

v1, v2 = map(int,input().split())

o = Dijkstra(1)
v1_ = Dijkstra(v1)
v2_ = Dijkstra(v2)

cnt = min(o[v1]+v1_[v2]+v2_[v], o[v2]+v2_[v1]+v1_[v])
print(cnt if cnt < INF else -1)
