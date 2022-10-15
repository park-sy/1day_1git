# 221015 / 오목 / 2615
import sys
input = sys.stdin.readline

dx = [0,1,-1,1]
dy = [1,0,1,1,]
g = []
for _ in range(19):
    g.append(list(map(int,input().split())))


def dfs(num,cnt,direction,x,y,a,b):
    if cnt == 5 and check(num,d,x,y,a,b):
        print(num)
        print(a+1,b+1)
        exit()
    x += dx[direction]
    y += dy[direction]

    if 0 <= x < 19 and 0 <= y < 19:
        if g[x][y] == num:

            dfs(num,cnt+1,direction,x,y,a,b)

def check(num,d,x,y,a,b):
    x += dx[d]
    y += dy[d]
    a -= dx[d]
    b -= dy[d]
    if 0 <= x < 19 and 0 <= y < 19 and g[x][y] == num:
        return False
    if 0 <= a < 19 and 0 <= b < 19 and g[a][b] == num:
        return False  

    return True

for i in range(19):
    for j in range(19):
        if g[i][j] != 0:
            for d in range(4):
                dfs(g[i][j],1,d,i,j,i,j)

print(0)