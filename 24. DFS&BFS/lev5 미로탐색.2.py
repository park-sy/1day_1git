# 220524 / 그래프순회 / 2178 / 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int,input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    visit = [[0]*m for _ in range(n)]
    heap = deque([(0,0)])
    visit[0][0] = 1
    while heap:
        a, b = heap.popleft()
        if a == n-1 and b == m-1:
            break
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<= x < n and 0<= y < m and miro[x][y] and not visit[x][y]:
                miro[x][y] += miro[a][b]
                visit[x][y] = 1
                heap.append([x,y])

bfs()
print(miro[n-1][m-1])