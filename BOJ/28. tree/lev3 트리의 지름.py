# 220319 / 트리 / 1967 / 트리의 지름
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[]for _ in range(n+1)]

for i in range(n-1):
    n1,n2,w = map(int,input().split())
    tree[n1].append([n2,w])
    tree[n2].append([n1,w])

def bfs(start):
    queue = deque([start])
    visit = [-1]*(n+1)
    visit[start] = 0
    while queue:
        node = queue.popleft()
        for i in tree[node]:
            if visit[i[0]] == -1:
                queue.append(i[0])
                visit[i[0]] = i[1] + visit[node]
    return visit

distance1 = bfs(1)
m_num = 0
id = 0
for i in range(1,n+1):
    if m_num < distance1[i]:
        m_num = distance1[i]
        id = i

print(max(bfs(id)))
