# 220324 / 유니온파인드 / 1717 / 집합의 표현
import sys
input = sys.stdin.readline

def union(a,b):
    if find(a) == find(b):
        return True
    else:
        return False

def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y: return
    graph[y] = a

def find(a):
    if graph[a] == a:
        return a
    graph[a] = find(graph[a])
    return graph[a]

n, m = map(int,input().split())


graph = [i for i in range(n+1)]
for _ in range(m):
    t, n1, n2 = map(int,input().split())
    if t == 0:
        merge(n1,n2)
    else:
        if union(n1,n2):
            print('YES')
        else:
            print('NO')
