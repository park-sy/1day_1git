# 220615 / 최소신장트리 / 4386 / 별자리만들기
import sys, heapq
input = sys.stdin.readline

def distance(a,b):
    x = a[0]-b[0]
    y = a[1]-b[1]
    return (x**2 + y**2)**0.5

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(float,input().split())))

visit = [0]*n
res = 0

def makestar(root):
    visit[root] = 1
    star = []
    res = 0
    for i in range(n):
        if visit[i] : continue
        cost = distance(g[i],g[root])
        heapq.heappush(star,(cost,i))
    while star:
        wei, next = heapq.heappop(star)
        if not visit[next]:
            res += wei
            res += makestar(next)
            
    return res

print("%0.2f"%makestar(0))