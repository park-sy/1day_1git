# 220724 / 그래프이론 / 어두운길
import sys,heapq
n,m = map(int,input().split())

g = [[]for _ in range(n)]
res = 0
road = []
for _ in range(m):
    a,b,c = map(int,input().split())
    res += c
    heapq.heappush(road,(c,a,b))
    g[a].append([c,b])
    g[b].append([c,a])

print(road)

parent = [i for i in range(n)]
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = find(a)
    y = find(b)
    print(x,y)
    if x == y:
        return 0
    parent[x] = min(x,y)
    parent[y] = min(x,y)
    return 1

cnt = 0
cost = 0
while cnt < n-1:
    w,x,y = heapq.heappop(road)
    if union(x,y):
        cost += w
        cnt += 1
print(parent)
print(res - cost)

"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

"""
