# 220728 / 어른 상어
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n,m,k = map(int,input().split())

g = [[] for _ in range(n)]
s = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(n):
        g[i].append([temp[j],0,0])
        if temp[j]:
            s.append([temp[j],0,i,j])
s.sort()
direction = list(map(int,input().split()))
for i in range(m):
    s[i][1] = direction[i]

pri = [[[]] for _ in range(m+1)]
for i in range(1,m+1):
    for _ in range(4):
        pri[i].append(list(map(int,input().split())))

isok = [1] *(m+1)

# 상어 냄뿌
def smell():
    for i in range(n):
        for j in range(n):
            if g[i][j][2]:
                g[i][j][2] -= 1
                if not g[i][j][2]:
                    g[i][j][1] = 0

    for i in range(m):
        num, d, x,y = s[i]
        if isok[num]:
            g[x][y][1] = num
            g[x][y][2] = k


# 상어 이동
def move(num, d, x,y):
    for w in pri[num][d]:
        nx = x + dx[w-1]
        ny = y + dy[w-1]
        if 0 <= nx < n and 0 <= ny <n:
            if not g[nx][ny][1]:
                if not g[nx][ny][0]:
                    g[nx][ny][0] = num
                    g[x][y][0] = 0
                    s[num-1] = num,w,nx,ny
                else:
                    g[x][y][0] = 0
                    isok[num] = 0
                return 
    for w in pri[num][d]:
        nx = x + dx[w-1]
        ny = y + dy[w-1]
        if 0 <= nx < n and 0 <= ny <n:
            if g[nx][ny][1] == num:
                g[x][y][0] = 0
                s[num-1] = num,w,nx,ny
                return                 

#상어 체크

res = 0
while True:

    if sum(isok) == 2:
        break
    if res >= 1000:
        res = -1
        break
    smell()
    for i in range(m):
        num, d, x,y = s[i]
        if isok[num]:
            move(num, d, x,y)

    res += 1

print(res)
    

"""
상어 이동
1. 아무 냄새 없는 칸
2. 자기 냄새 칸
3. 이동 후 같이 있으면 작은 숫자 상어남고 탈락"""

