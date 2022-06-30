# 220625 / dp in tree / 2533 / 사회망서비스
import sys

n = int(input())
g = [[]for _ in range(n+1)]
sns = [[0,0] for _ in range(n+1)]
for _ in range(n-1):
    n1,n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)

visit = [0] *(n+1)

def dfs(start):
    visit[start] = 1
    sns[start][0] = 1
    for i in g[start]:
        if not visit[i]:
            dfs(i)
            sns[start][0] += min(sns[i][0],sns[i][1])
            sns[start][1] += sns[i][0]

dfs(1)
print(sns)
