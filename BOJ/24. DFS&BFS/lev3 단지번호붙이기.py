# 220225 / DFS와BFS / 2667 / 단지번호붙이기
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(graph,a,b):
    n = len(graph)
    queue = deque([(a,b)])
    graph[a][b] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    cnt += 1
    return cnt

n = int(input())
edge = []
for i in range(n):
    edge.append(list(map(int,input())))

count = []
for i in range(n):
    for j in range(n):
        if edge[i][j] == 1:
            count.append(bfs(edge,i,j))

count.sort()
print(len(count))

for i in count:
    print(i)


