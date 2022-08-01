# 220801 / 1753 / 최단경로
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
start = int(input())

d = [INF] * (n+1)
g = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    g[a].append([c,b])



hq = []
d[start] = 0
heapq.heappush(hq,(0,start))
while hq:
    wei, now = heapq.heappop(hq)
    if d[now] < wei: continue
    for nwei, next in g[now]:
        if d[next] > wei + nwei:
            d[next] = wei + nwei
            heapq.heappush(hq,(wei+nwei, next))

for i in range(1,n+1):
    if d[i] == INF:
        print("INF")
    else:
        print(d[i])
