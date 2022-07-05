# 220705 / 그래프이론 / 커리큘럼
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
t = [0] * (n+1)
pre = [0] *(n+1)
ft = [0] * (n+1)
for i in range(1,n+1):
    q = list(map(int,input().split()))
    t[i] = q[0]
    for j in q[1:]:
        if j == -1:
            break
        g[j].append(i)
        pre[i] += 1

q = deque([])
res = 0
for i in range(1,n+1):
    if pre[i] == 0:
        q.append(i)
        ft[i] = t[i]

while q:
    now = q.popleft()
    for i in g[now]:
        pre[i] -= 1
        ft[i] = max(ft[i], ft[now])
        if pre[i] == 0:
            q.append(i)
            ft[i] += t[i]

for i in range(1,n+1):
    print(ft[i])

        
