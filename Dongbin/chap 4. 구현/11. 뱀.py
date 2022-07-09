# 220709 / 구현 / 뱀
from collections import deque
n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(int(input())):
    a,b = map(int,input().split())
    g[a][b] = 2

q = [0]*10000
for _ in range(int(input())):
    x,c = map(str,input().split())
    q[int(x)] = c

sec = 0
d = 0

hx,hy = 1,1
que = deque([[1,1]])
g[1][1] = 1
while True:
    sec += 1
    hx += dx[d%4]
    hy += dy[d%4]
    
    if 1 <= hx <= n and 1<= hy <= n and g[hx][hy] != 1:
        que.append([hx,hy])
        if g[hx][hy] != 2:
            tx,ty = que.popleft()
            g[tx][ty] = 0
        g[hx][hy] = 1
        if q[sec] == "L":
            d -= 1
        elif q[sec] == "D":
            d += 1   
    else:
        break

print(sec)


    





