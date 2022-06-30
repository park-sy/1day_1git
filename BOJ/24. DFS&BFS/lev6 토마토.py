# 220228 / DFS와BFS / 7576 / 토마토
from collections import deque
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
box = []
queue = deque([])
for i in range(n):
    box.append(list(map(int,input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i,j])
cnt = 0
while queue:
    (a, b) = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
            queue.append([x, y])
            box[x][y] = box[a][b] + 1

zero = False
for i in range(n):
    if 0 in box[i]:
        zero = True
        break
if zero == True:
    print(-1)
else:
    print(box[a][b]-1)