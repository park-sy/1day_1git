# 220331 / 최소신장트리 / 1774 / 우주신과의 교감
import sys, heapq
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

n,m = map(int,input().split())
graph = [[]for i in range(n+1)]
pos = [[]]
link = [[]for _ in range(n+1)]
for i in range(n):
    pos.append(list(map(int,input().split())))
for i in range(m):
    n1,n2 = map(int,input().split())
    link[n1].append(n2)
    link[n2].append(n1)
    graph[n1].append([0,n2])
    graph[n2].append([0,n1])

for i in range(1,n+1):
    x1,y1 = pos[i]
    for j in range(1,n+1):
        if i == j: continue
        if j in link[i]: continue
        x2,y2 = pos[j]
        graph[i].append([dist(x1,y1,x2,y2),j])

cnt = 0
res = 0
visit = [False]*(n+1)
hq = [[0,1]]
while cnt < n:
    w, node = heapq.heappop(hq)
    if visit[node]:
        continue
    cnt += 1
    res += w
    visit[node] = True
    for n_w,n_n in graph[node]:
        if visit[n_n]:
            continue
        heapq.heappush(hq,(n_w,n_n))

print("{:.2f}".format(res))