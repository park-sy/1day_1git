# 220705 / 그래프이론 / 팀결성
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    parent[x] = min(x,y)
    parent[y] = min(x,y)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    q,a,b = map(int,input().split())
    if q == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('Yes')
        else:
            print('No')
