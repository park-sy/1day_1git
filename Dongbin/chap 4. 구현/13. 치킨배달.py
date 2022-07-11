# 220711 / 구현 / 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input().split())))


def check(a,b,r):
    res = INF
    for i in range(m):
        temp = abs(r[i][0]-a) + abs(r[i][1]-b)
        res = min(res, temp)       
    return res

res = INF
store = []
house = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            house.append([i,j])
        if g[i][j] == 2:
            store.append([i,j])

for chik in combinations(store,m):
    temp = 0
    for h in house:
        temp += check(h[0],h[1],chik)
    res = min(temp,res)

print(res)

