# 220608 / 트리 / 11725 / 트리의 부모찾기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)
parent = [0]*(n+1)

def bfs():
    q = deque([1])
    while q:
        p = q.popleft()
        for c in g[p]:
            if not parent[c]:
                q.append(c)
                parent[c] = p


bfs()
for i in range(2,n+1):
    print(parent[i])