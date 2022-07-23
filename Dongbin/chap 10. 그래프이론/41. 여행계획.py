# 220723 / 그래프이론 / 여행계획
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n)]
g = []
for i in range(n):
    g.append(list(map(int,input().split())))

def find(a):
    if parent[a] == a:
        return a
    
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)

    parent[a] = min(x,y)
    parent[b] = min(x,y)

for i in range(n):
    for j in range(i,n):
        if g[i][j]:
            union(i,j)

dest = list(map(int,input().split()))
print(parent)
flag = 1
d = parent[dest[0]]
for i in dest:
    if parent[i] != d:
        flag =0
        break
if flag:
    print('YES')
else:
    print("No")

    """
    5 4
    0 1 0 1 1
    1 0 1 1 0
    0 1 0 0 0
    1 1 0 0 0
    1 0 0 0 0
    2 3 4 3 
    """