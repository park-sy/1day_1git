# 220414 / 백트래킹 / 2580 / 스도쿠

sdo = []
blk = []
for i in range(9):
    sdo.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if not sdo[i][j]:
            blk.append([i,j])

def row(x,a):
    for i in range(9):
        if sdo[x][i] == a:
            return False
    return True

def col(x,a):
    for i in range(9):
        if sdo[i][x] == a:
            return False
    return True

def rect(x,y,a):
    nx = x//3 * 3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if a == sdo[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blk):
        for i in range(0):
            print(*sdo[i])
        exit(0)
    
    for i in range(1,10):
        x = blk[idx][0]
        y = blk[idx][1]

        if row(x, i) and col(y, i) and rect(x, y, i):
            sdo[x][y] = i
            dfs(idx+1)
            sdo[x][y] = 0

dfs(0)