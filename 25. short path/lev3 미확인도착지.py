# 220305 / 최단경로 / 9370 / 미확인 도착지
import sys,heapq
INF = sys.maxsize
input = sys.stdin.readline
def Dijkstra(start):
    heap = []
    d = [INF]*(n+1)
    d[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        wei, now = heapq.heappop(heap)

        if d[now] < wei:
            continue

        for w, n_node in graph[now]:
            n_wei= w + wei
            if n_wei < d[n_node]:
                d[n_node] = n_wei
                heapq.heappush(heap,(n_wei,n_node))

    return d

T = int(input())

for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [[]for _ in range(n+1)]
    for i in range(m):
        n1,n2,w = map(int,input().split())
        graph[n1].append([w,n2])
        graph[n2].append([w,n1])

    candi = []
    one,gd,hd = Dijkstra(s), Dijkstra(g), Dijkstra(h)
    for i in range(t):
        k = int(input())
        if one[g] + gd[h] + hd[k] == one[k] or one[h] + hd[g] + gd[k] == one[k]:
            candi.append(k)
    candi.sort()
    print(*candi)