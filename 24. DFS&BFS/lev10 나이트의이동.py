# 220302 / DFS와BFS / 7562 / 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
for _ in range(t):
    n = int(input())
    chs = [[0 for _ in range(n)]for _ in range(n)]
    x1, y1 = map(int,input().split())
    x2, y2 = map(int,input().split())
    chs[x1][y1] = 1
    q = deque([(x1,y1)])

    while q:
        a, b = q.popleft()
        if a == x2 and b == y2:
            break
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < chs[x][y] == 0:
                chs[x][y] = chs[a][b] + 1
                q.append([x,y])
    print(chs[x2][y2]-1)