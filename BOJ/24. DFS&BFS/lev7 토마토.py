# 220228 / DFS와BFS / 7569 / 토마토
from collections import deque
import sys
input = sys.stdin.readline
m,n,h = map(int,input().split())
box = []
queue = deque([])
for i in range(h):
    box2 = []
    for j in range(n):
        box2.append(list(map(int,input().split())))
    box.append(box2)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                queue.append([k,i,j])
cnt = 0
while queue:
    (c, a, b) = queue.popleft()
    for i in range(6):
        z = c + dh[i]
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and 0 <= z < h and box[z][x][y] == 0:
            queue.append([z, x, y])
            box[z][x][y] = box[c][a][b] + 1

zero = False
for i in range(h):
    for j in range(n):
        if 0 in box[i][j]:
            zero = True
            break
if zero == True:
    print(-1)
else:
    print(box[c][a][b]-1)