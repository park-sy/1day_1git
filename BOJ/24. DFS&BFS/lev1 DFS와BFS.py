# 220224 / DFS와BFS / 1260 / DFS와 BFS
from collections import deque

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return ' '.join(str(i) for i in visited)

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort()
                queue.extend(temp)
    
    return ' '.join(str(i) for i in visited)

graph = {}

node, edge, start = map(int,input().split())

for i in range(edge):
    n1, n2 = map(int,input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)    

print(dfs(graph, start))
print(bfs(graph, start))