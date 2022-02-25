# 220225 / DFS와BFS / 2606 / 바이러스
from collections import deque
def bfs(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort()
                queue += temp 
    
    return len(visit)

node = int(input())
edge = int(input())

graph = {}

for i in range(edge):
    a, b = map(int,input().split())

    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)

print(bfs(graph,1)-1)
    



