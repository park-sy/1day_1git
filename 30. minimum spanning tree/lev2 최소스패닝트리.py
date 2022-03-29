# 220329 / 최소신장트리 / 1197 / 최소 스패닝 트리
import sys,heapq
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[]for _ in range(n+1)]
visit = [False]*(n+1)
heap = [[0,1]]
for i in range(e):
    n1,n2,w = map(int,input().split())
    graph[n1].append([w,n2])
    graph[n2].append([w,n1])

sum = 0
cnt = 0
while heap:
    if cnt == n:
        break
    w, node = heapq.heappop(heap)
    if not visit[node]:
        visit[node] = True
        sum += w
        cnt += 1
        for i in graph[node]:
            heapq.heappush(heap,i)

print(sum)