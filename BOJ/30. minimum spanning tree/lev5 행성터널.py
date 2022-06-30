# 220401 / 최소신장트리 / 2887 / 행성 터널
import sys,heapq
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    x = parent[a]
    y = parent[b]
    parent[min(x,y)] = max(x,y)

n = int(input())
pos = []
for i in range(n):
    pos.append([i] + list(map(int,input().split())))

graph = []
g_x = sorted(pos, key = lambda x:x[1])
g_y = sorted(pos, key = lambda x:x[2])
g_z = sorted(pos, key = lambda x:x[3])

for i in range(n-1):
    graph.append([abs(g_x[i][1]-g_x[i+1][1]), g_x[i][0], g_x[i+1][0]])
    graph.append([abs(g_y[i][2]-g_y[i+1][2]), g_x[i][0], g_y[i+1][0]])
    graph.append([abs(g_z[i][3]-g_z[i+1][3]), g_x[i][0], g_z[i+1][0]])

graph.sort()

parent = [i for i in range(n)]
res = 0
for node in graph:
    distance, a, b = node
    if find(a) != find(b):
        union(a,b)
        res += distance

print(res)