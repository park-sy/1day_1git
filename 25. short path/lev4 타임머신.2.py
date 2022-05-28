# 220528 / 최단경로 / 11657 / 타임머신
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int,input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    A,B,C = map(int,input().split())
    g.append([A,C,B])
d = [INF]*(n+1)

def bellman_ford(start):
    d[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node = g[j][0]
            next_node = g[j][2]
            cost = g[j][1]
            if d[cur_node] != INF and d[next_node] > d[cur_node] + cost:
                d[next_node] = d[cur_node] + cost
                if i ==  m - 1:
                    return True

    return False

if  bellman_ford(1):
    print(-1)
else:
    for i in range(2,n+1):
        if d[i] == INF:
            print(-1)
        else: print(d[i])

