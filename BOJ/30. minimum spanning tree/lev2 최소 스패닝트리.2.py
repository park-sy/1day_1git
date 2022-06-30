# 220613 / 최소신장트리 / 1197 / 최소 스패닝 트리
import sys, heapq
input = sys.stdin.readline

v,e = map(int,input().split())
g = [[] for _ in range(v+1)]
for _ in range(e):
    n1, n2, c = map(int,input().split())
    g[n1].append([c,n2])
    g[n2].append([c,n1])

visit = [0]*(v+1)
def prim(start):
    heap = []
    heapq.heappush(heap,(0,start))
    sum = 0
    cnt = 0
    while heap:
        if cnt == v: return sum
        (wei, now) = heapq.heappop(heap)
        if not visit[now]:
            visit[now] = 1
            sum += wei
            cnt += 1
            for nwei, next in g[now]:
                heapq.heappush(heap,(nwei,next))

print(prim(1))