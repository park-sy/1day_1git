# 220612 / 트리 / 4803 / 트리
import sys
input = sys.stdin.readline
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        cycle.append(x)
        return
    parent[max(x,y)] = min(x,y)


cnt = 1
while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0: break
    parent = [i for i in range(n+1)]
    group = set()
    cycle = []
    for _ in range(m):
        n1, n2 = map(int,input().split())
        merge(n1,n2)

    for i in range(n+1):
        find( i)
    for cycle_vertex in cycle:
        group.add(parent[cycle_vertex])
    sum = 0
    for i in range(1, n+1):
        if parent[i] in group:
            continue
        sum += 1
        group.add(parent[i])


    if sum == 0:
        print("Case %d: No trees."%(cnt))
    elif sum == 1:
        print("Case %d: There is one tree."%(cnt))
    else:
        print("Case %d: A forest of %d trees."%(cnt, sum))
    cnt += 1
    