# 220722 / sp / 숨바꼭질
import heapq, sys
n,m = map(int, input().split())
INF = sys.maxsize
g = [[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

q = []
heapq.heappush(q,[0,1])
d = [INF] * (n+1)
d[1] = 0
while q:
    w, now = heapq.heappop(q)
    for next in g[now]:
        if d[next] > w+1:
            d[next] = w + 1
            heapq.heappush(q,[w+1,next])

id = 1
res = 0
cnt = 0
for i in range(2,n+1):
    if d[i] > res:
        id = i
        res = d[i]
        cnt = 0
    if res == d[i]:
        cnt += 1
print(id, res, cnt)
"""
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

"""