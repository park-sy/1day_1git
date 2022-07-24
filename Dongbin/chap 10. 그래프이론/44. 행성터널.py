# 220724 / 그래프이론 / 행성터널
import sys,heapq
input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)
    parent[x] = min(x,y)
    parent[y] = min(x,y)

n = int(input())
c = []
for i in range(n):
    c.append(list(map(int,input().split()))+[i])

cx = sorted(c, key = lambda x : x[0])
cy = sorted(c, key = lambda x : x[1])
cz = sorted(c, key = lambda x : x[2])
temp = []

for i in range(1,n):
    temp.append([abs(cx[i][0]-cx[i-1][0]),cx[i][3],cx[i-1][3]])
    temp.append([abs(cy[i][1]-cy[i-1][1]),cy[i][3],cy[i-1][3]])
    temp.append([abs(cz[i][2]-cz[i-1][2]),cz[i][3],cz[i-1][3]])
    
temp.sort()
parent = [i for i in range(n)]


res = 0
for cost, x,y in temp:
    if find(x) != find(y):
        union(x,y)
        res += cost


print(res)
