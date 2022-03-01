# 220301 / DFS와 BFS / 2206 / 벽 부수고 이동하기
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visit[0][0][1] = 1
    q = deque([(0,0,1)])
    while q:
        (a, b, c) = q.popleft() # c가 1이면 벽을 부술 수 있는 상태, 0이면 부술 수 없는 상태
        if a == n -1 and b == m -1:
            return visit[a][b][c]
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            if 0 <= x < n and 0 <= y < m:
                if w[x][y] == 1 and c == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x,y,0])
                elif w[x][y] == 0 and visit[x][y][c] == 0:
                    visit[x][y][c] = visit[a][b][c] + 1
                    q.append([x,y,c])
    return -1

n,m = map(int,input().split())
w = []
for i in range(n):
    w.append(list(map(int,list(str(input())))))
print(bfs())