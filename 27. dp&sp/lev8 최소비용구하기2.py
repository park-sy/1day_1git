# 220606 / DB&SP / 11779 / 최소비용구하기2
import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[]for _ in range(n+1)]
for _ in range(8):
    n1, n2, c = map(int,input().split())
    g[n1].append([c,n2])

s,e = map(int,input().split())
d = [INF]*(n+1)

heap = []
near = [s]*(n+1)

def Dijkstra(n):
    d[n] = 0
    heapq.heappush(heap,(0,n))

    while heap:
        wei, now = heapq.heappop(heap)
        if d[now] < wei:
            continue

        for w, n_node in g[now]:
            n_wei= w + wei
            if n_wei < d[n_node]:
                d[n_node] = n_wei
                near[n_node] = now
                heapq.heappush(heap,(n_wei,n_node))
Dijkstra(s)
ans = []
tmp = e
while tmp != s:
    ans.append(tmp)
    tmp = near[tmp]
ans.append(s)
ans.reverse()
print(d[e])
print(len(ans))
print(*ans)