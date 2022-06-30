# 220403 / 트리에서 동적 계획법 / 15681 / 트리워 쿼리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def counttree(start,parent):
    szt[start] = 1
    for node in graph[start]:
        if node != parent:
            counttree(node,start)
            szt[start] += szt[node]

n, r, q = map(int,input().split())
szt = [0]*(n+1)
graph = [[]for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)



counttree(r,-1)
for i in range(q):
    print(szt[int(input())])
