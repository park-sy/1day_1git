# 220723 / 그래프이론 / 탑승구
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
cnt = 0
flag = 0
g = []
for i in range(m):
    g.append(int(input()))


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)

    parent[a] = min(x,y)
    parent[b] = min(x,y)

res = 0
for _ in range(m):
    k = find(int(input()))
    
    if k == 0:
        break
    union(k,k-1)
    res += 1

print(res)
