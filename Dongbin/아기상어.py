# 220725 / 아기상어
import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
dx = [0,0,-1,1]
dy = [-1,1,0,0]
n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))

a,b = 0,0
size = 2
for i in range(n):
    for j in range(n):
        if g[i][j] == 9:
            a,b = i,j
            g[i][j] = 0

def find(size):
    global a,b
    q = deque([[a,b]])
    d = [[0]* n for _ in range(n)]
    d[a][b] = 0
    fish = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] <= size:
                if not d[nx][ny]:
                    d[nx][ny] = d[x][y] + 1
                    q.append([nx,ny])
                    if 0 < g[nx][ny] < size:
                        fish.append([d[nx][ny],nx,ny])
    
    if not fish:
        return 0
    fish.sort()

    a,b = fish[0][1], fish[0][2]
    g[a][b] = 0
    return fish[0][0]

cnt = 0
res = 0
while 1:
    t = find(size)
    if not t:
        break
    cnt += 1
    res += t
    if size == cnt:
        size += 1
        cnt = 0

print(res)

"""
5 5 2
0 5 2
1 5 3
2 0 3 
4 1 3
2 1 4
5 0 4
5 2 4

"""