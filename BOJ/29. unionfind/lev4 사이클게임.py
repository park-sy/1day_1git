# 220327 / 유니온파인드 / 20040 / 사이클 게임
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        return True
    parent[max(x,y)] = min(x,y)

n,m = map(int,input().split())
parent = [i for i in range(n)]

for i in range(1,m+1):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print(i)
        break
    merge(a,b)
else:
    print(0)