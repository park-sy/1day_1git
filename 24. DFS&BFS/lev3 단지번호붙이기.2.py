# 220523 / DFS BFS / 2667 / 단지번호붙이기
import sys
input = sys.stdin.readline

n = int(input())
apt = []
for _ in range(n):
    apt.append(list(map(int,input().rstrip())))

ans = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(g, a, b):
    g[a][b] = 0
    stk = [[a,b]]
    cnt = 1

    while stk:
        a,b = stk.pop()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < n:
                if g[x][y]:
                    g[x][y] = 0
                    stk.append([x,y])
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if apt[i][j]:
            ans.append(dfs(apt,i,j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)