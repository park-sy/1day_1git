# 220326 / 유니온파인드 / 4195 / 친구 네트워크
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

    if x != y:
        print(num[x])
        return
    parent[y] = x
    num[x] += num[y]
    print(num[x])

T = int(input())
for _ in range(T):
    f = int(input())
    parent = {}
    num = {}
    for _ in range(f):
        n1,n2 = input().split()
        if n1 not in parent:
            parent[n1] = n1
            num[n1] = 1
        if n2 not in parent:
            parent[n2] = n2
            num[n2] = 1
        merge(n1,n2)
        
