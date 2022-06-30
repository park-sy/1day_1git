# 220325 / 유니온파인드 / 1976 / 여행가자
import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)
n = int(input())
m = int(input())
city = [i for i in range(n+1)]
def find(node):
    if city[node] == node:
        return node
    city[node] = find(city[node])
    return city[node]

def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    city[y] = x


for i in range(n):
    arr = list(map(int,input().split()))
    for j in range(n):
        if arr[j] == 1:
            merge(i+1,j+1) 

plan = list(map(int,input().split()))
parent = [find(plan[i]) for i in range(m)]
tmp = True
for i in range(1,m):
    if parent[i-1] != parent[i]:
        tmp = False
        break

print('YES' if tmp == True else 'NO')
