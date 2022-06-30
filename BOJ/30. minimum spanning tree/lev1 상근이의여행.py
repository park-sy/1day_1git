# 220328 / 최소신장트리 / 9372 / 상근이의 여행
import sys
from collections import deque
input = sys.stdin.readline

def bfs(g, start):
    cnt = 0
    queue = deque([start])
    visit = []
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            cnt += 1
            for i in g[node]:               
                queue.append(i)
                
    return cnt

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(bfs(graph,1)-1)
    
