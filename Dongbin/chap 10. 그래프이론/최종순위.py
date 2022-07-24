# 220724 / 그래프이론 / 최종순위
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    g = [[0]*(n+1) for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    team = list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            g[team[i][team[j]]] = 1 
            indegree[team[j]] += 1

    
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if g[a][b]:
            g[a][b] = 0
            g[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else:
            g[a][b] = 1
            g[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1
        
        res = []
        q = deque()

        for i in range(1,n+1):
            if indegree[i] == 0:
                q.append(i)
        flag = True
        cycle = False

        for i in range(n):
            if len(q) == 0:
                cycle = True
                break
            if len(q) == 2:
                flag = False
                break
            now = q.popleft()
            res.append(now)
            for j in range(1,n+1):
                if g[now][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
    if cycle or not flag:
        print("IMPOSSIBLE")
    else:
        print(*res)
    print()

            
        
    """
    5 4 3 2 1
    5 
    """