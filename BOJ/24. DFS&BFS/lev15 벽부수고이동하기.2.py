# 220526 / 그래프 순회 / 2206 / 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,list(str(input())))))

visit = [[[0]*2 for _ in range(m)]  for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    q = deque([0,0,1])
    visit[0][0][1] = 1

    while q:
        a,b,c = q.popleft()
        if a == n -1 and b == m -1:
            return visit[a][b][c]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if g[x][y] == 1 and c == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x,y,0])
                elif g[x][y] == 0 and visit[x][y][c] == 0:
                    visit[x][y][c] = visit[a][b][c] + 1
                    q.append([x,y,c])

print(bfs())