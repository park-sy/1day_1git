# 220527 / 최단경로 / 13549 / 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
pos = [0]*(n+m+1)
visit = [0]*(n+m+1)

def bfs(start):
    q = deque([start])
    visit[start] = 1

    while q:
        now = q.popleft()
        if now == m:
            return pos[now]
        if 0 <= now*2 < n+m+1 and not visit[now*2]:
            pos[now*2] = pos[now]
            visit[now*2] = 1
            q.append(now*2)
        if 0 <= now-1 < n+m+1 and not visit[now-1]:
            pos[now-1] = pos[now] + 1
            visit[now-1] = 1
            q.append(now-1)
        if 0 <= now+1 < n+m+1 and not visit[now+1]:
            pos[now+1] = pos[now] + 1
            visit[now+1] = 1
            q.append(now+1)
        


print(bfs(n))