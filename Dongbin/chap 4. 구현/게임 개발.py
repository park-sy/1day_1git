# 220630 / 구현 / 게임 개발
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
a,b,d = map(int,input().split())
g = []
for i in range(n):
    g.append(list(map(int,input().split())))

d = [[0]*m for _ in range(n)]
cnt = 1
d[a][b] = 1
while 1:
    check = 0
    for i in range(m-1,m-5,-1):
        i = i % 4
        x = a + dx[i]
        y = b + dy[i]
        if not d[x][y] and not g[x][y]:
            a,b = x,y
            cnt += 1
            g[x][y] = 2
            check = 1
            m = i
            break
    if not check:
        x = a - dx[m]
        y = b - dy[m]
        if g[x][y] == 1:
            break
        else: a,b = x,y

print(cnt)

