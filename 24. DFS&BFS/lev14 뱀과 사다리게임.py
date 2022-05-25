# 220525 / 그래프 순회 / 16928 / 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
g = [0]*(101)
visit = [0]*(101)
ladder = {}
snake = {}

for _ in range(n):
    a,b = map(int,input().split())
    ladder[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    snake[a] = b

def bfs():
    q = deque([1])
    visit[1] = 1
    while q:
        d = q.popleft()
        if d == 100:
            break
        for i in range(1,7):
            next = d + i
            if next <= 100 and not visit[next]:
                if next in ladder:
                    next = ladder[next]
                if next in snake:
                    next = snake[next]  
                if not visit[next]: 
                    g[next] = g[d] + 1
                    visit[next] = 1
                    q.append(next)

bfs()
print(g[100])