# 220714 / dfs bfs / 감시 피하기
from itertools import combinations

n = int(input())
g = []
teachers = []
space = []

for i in range(n):
    g.append(list(input().split()))
    for j in range(n):
        if g[i][j] == "T":
            teachers.append((i,j))
        if g[i][j] == "X":
            space.append((i,j))

def watch(x,y,d):
    if d == 0:
        while y >= 0:
            if g[x][y] == "S":
                return True
            if g[x][y] == "O":
                return False
            y -= 1
    if d == 1:
        while y < n:
            if g[x][y] == "S":
                return True
            if g[x][y] == "O":
                return False
            y += 1
    if d == 2:
        while x >= 0:
            if g[x][y] == "S":
                return True
            if g[x][y] == "O":
                return False
            x -= 1
    if d == 3:
        while x < n:
            if g[x][y] == "S":
                return True
            if g[x][y] == "O":
                return False
            x += 1

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

for data in combinations(space, 3):
    for x,y in data:
        g[x][y] = "O"
    if not process():
        find = True
    for x,y in data:
        g[x][y] = "X"

if find:
    print("YES")
else: print("NO")