# 220705 / 그래프이론 / 도시 분할 계획
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(m):
    a,b,c = map(int,input().split())
    arr.append([c,a,b])
    
arr.sort()
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)
    parent[x] = min(x,y)
    parent[y] = min(x,y)

res = 0
cnt = 0
for cost,a,b in arr:
    x = find(a)
    y = find(b)
    if x == y:
        continue
    union(a,b)
    res += cost
    cnt += 1
    if cnt == n-2:
        break

print(res)