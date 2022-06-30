# 220330 / 최소신장트리 / 4386 / 별자리 만들기
import sys, heapq
input = sys.stdin.readline
def dist(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5
n = int(input())
visit = [False]*n
cor = []
for i in range(n):
    cor.append(list(map(float,input().split())))

graph = [[]for _ in range(n)]
for i in range(n):
    x1,y1 = cor[i]
    for j in range(n):
        if i == j: continue
        x2,y2 = cor[j]
        graph[i].append((j,dist(x1,y1,x2,y2)))


heap = [(0,0)]
cnt, ans = 0,0
while cnt < n:
    w, node = heapq.heappop(heap)
    if visit[node]:
        continue

    cnt += 1
    visit[node] = True
    ans += w
    for n_n,n_w in graph[node]:
        if visit[n_n]:
            continue
        heapq.heappush(heap,(n_w,n_n))

print(ans)