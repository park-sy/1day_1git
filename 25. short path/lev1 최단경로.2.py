# 220521 / 최단경로 / 1753 / 최단경로
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    node1, node2, weight = map(int,input().split())
    graph[node1].append([node2,weight])
    graph[node2].append([node1,weight])

d = [INF]*(v+1)
d[k] = 0
heap = []

def Dijkstra(n):
    d[n] = 0
    heapq.heappush(heap,(0,n))

    while heap:
        wei, now = heapq.heappop(heap)
        if d[now] < wei:
            continue

        for w, n_node in graph[now]:
            n_wei= w + wei
            if n_wei < d[n_node]:
                d[n_node] = n_wei
                heapq.heappush(heap,(n_wei,n_node))

Dijkstra(0)

for i in d:
    print(i if i != INF else 'INF')