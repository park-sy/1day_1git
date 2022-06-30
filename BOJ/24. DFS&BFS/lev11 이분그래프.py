# 220302 / DFS와BFS / 1707 / 이분그래프
from collections import deque
import sys
def bfs(root):
    bi[root] = 1
    q = deque([root])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if bi[i] == 0:
                bi[i] = - bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True


t = int(input())
for _ in range(t):
    n, e = map(int,input().split())
    isTrue = True
    graph = [[]for i in range(n+1)]
    bi = [0 for i in range(n+1)]
    for i in range(e):
        n1, n2 = map(int,input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for i in range(1,n+1):
        if bi[i] == 0:
            if not bfs(i):
                isTrue = False
                break
    print("YES" if isTrue else "No")

