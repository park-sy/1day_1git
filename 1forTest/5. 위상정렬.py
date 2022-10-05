from collections import deque

v,e = map(int,input().split())

indegree = [0] * (v+1)

g = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    g[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(result)

        for i in g[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)

        for i in result:
            print(i)