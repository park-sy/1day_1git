# 221010 / Puyo Puyo / 11559
from collections import deque
dx = [0,1,0,-1]
dy = [-1,0,1,0]

g = []

for _ in range(12):
    g.append(list(map(str,input())))

def bfs(x,y,w):
    cnt = 1
    q = deque()
    visit[x][y] = 1
    q.append([x,y])
    v_list = [[x,y]]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny]:
                if g[nx][ny] == w:
                    q.append([nx,ny])
                    cnt += 1
                    visit[nx][ny] = 1
                    v_list.append([nx,ny])
    
    if cnt < 4:
        return 0
    for a,b in v_list:
        g[a][b] = '.'
    return 1

def toFloor():
    for i in range(6):
        for j in range(12):
            if g[11-j][i] != ".":              
                for k in range(11-j+1,12):
                    if g[k][i] != ".": break
                    tmp =  g[k-1][i]
                    g[k][i] = tmp
                    g[k-1][i] = "."

ans = 0
while 1:
    flag = 0
    visit = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if g[i][j] != '.' and not visit[i][j]:
                flag = max(bfs(i,j,g[i][j]), flag)

    if not flag:
        break
    
    ans += 1
    toFloor()

print(ans)



