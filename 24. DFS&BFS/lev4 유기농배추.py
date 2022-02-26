# 220226 / DFS와BFS / 1012 / 유기농배추

def dfs(graph, a,b):
    stk = [(a,b)]
    graph[a][b] = 0
    while stk:
        x,y = stk.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    stk.append((nx,ny))
    return 1            

dx = [-1,1,0,0]
dy = [0,0,-1,1]

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())

    cbg = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        cbg[b][a] = 1
    cnt = 0
    
    for i in range(n):
        for j in range(m):
            if cbg[i][j] == 1:
                cnt += dfs(cbg, i,j)
    
    print(cnt)

