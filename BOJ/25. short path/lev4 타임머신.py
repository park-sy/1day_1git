# 220306 / 최단경로 / 11657 / 타임머신 (벨만포드)
import sys
INF = sys.maxsize
input = sys.stdin.readline

n, m = map(int,input().split())
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


g = []
for i in range(m):
    A,B,C = map(int,input().split())
    g.append([A,C,B])

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if d[i] == INF:
            print("-1")
        else:
            print(d[i])    