# 220530 / 최단경로 / 1956 / 운동
import sys, heapq as hq
input = sys.stdin.readline
INF = sys.maxsize


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
dist = [[INF] * (V+1) for _ in range(V+1)]

heap = []
for _ in range(E):
    x, y, c = map(int, input().split())
    graph[x].append([c, y])
    dist[x][y] = c
    hq.heappush(heap, [c, x, y])


while heap:
    d, s, g = hq.heappop(heap)
    
    if s == g:
        print(d)
        break

    if dist[s][g] < d:
        continue
        

    for nd, ng in graph[g]:
        new_d = d + nd
        if new_d < dist[s][ng]:
            dist[s][ng] = new_d
            hq.heappush(heap, [new_d, s, ng])
else:
    print(-1)