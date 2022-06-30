# 220303 / 최단경로 / 1753 / 최단경로
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int,input().split())
k = int(input())
g = [[]for i in range(v+1)]
d = [INF]*(v+1)
heap = []

def Dijkstra(start):
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


for i in range(e):
    v1, v2, v3 = map(int,input().split())
    g[v1].append([v3,v2])


Dijkstra(k)
for i in d:
    print(i if i != INF else 'INF')