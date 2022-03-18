# 220318 / 트리 / 1167 / 트리의 지름
import sys
input = sys.stdin.readline

n = int(input())
tree = [[]for _ in range(n+1)]
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(1,len(a)-1,2):
        tree[a[0]].append([a[j],a[j+1]])

def dfs(start):
    visit = [-1]*(n+1)
    stk = [start]
    visit[start] = 0
    while stk:
        node = stk.pop()
        for i in tree[node]:
            if visit[i[0]] == -1:
                stk.append(i[0])
                visit[i[0]] = i[1] + visit[node]
    return visit

distance1 = dfs(1)
m_num = 0
id = 0
for i in range(1,n+1):
    if m_num < distance1[i]:
        m_num = distance1[i]
        id = i

print(max(dfs(id)))
