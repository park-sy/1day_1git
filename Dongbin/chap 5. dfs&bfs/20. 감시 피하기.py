# 220714 / dfs bfs / 감시피하기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = []
teacher = []
temp = [[0]*n for _ in range(n)]
for i in range(n):
    g.append(list(map(str,input().split())))
    for j in range(n):
        if g[i][j] == "T":
            teacher.append([i,j])
            
dx = [0,0,1,-1]
dy = [1,-1,0,0]
res = 0

def check():
    q = deque(teacher)
    while q:
        x,y = q.popleft()
        for i in range(4):
            for j in range(1,n):
                nx = x + j*dx[i]
                ny = y + j*dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if temp[nx][ny] != "O": break
                    if temp[nx][ny] == "S":
                        temp[nx][ny] == "X"
                    
def cnt_stu(arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "S":
                cnt += 1
    return cnt

def dfs(cnt):
    global res
    if cnt == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = g[i][j]
        check()
        res = max(res, cnt_stu(temp))
        return
    for i in range(n):
        for j in range(n):
            if g[i][j] == "X":
                g[i][j] == "O"
                cnt += 1
                dfs(cnt)
                cnt -= 1
                g[i][j] == "X"

dfs(0)
if res == cnt_stu(g):
    print("YES")
else: print("NO")

