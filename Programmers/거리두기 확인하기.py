# 220809 / 거리두기 확인하기
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(places):
    answer = [0]*5
    
    for i in range(5):
        print()
        answer[i] = check(places[i])
        
    return answer

def check(a):
    
    for i in range(5):
        for j in range(5):
            if a[i][j] == "P":
                if not bfs(i,j,a):
                    return 0
                
    return 1

def bfs(a,b,g):
    q = deque([[a,b]])
    d = [[0]*5 for _ in range(5)]
    d[a][b] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not d[nx][ny] and g[nx][ny] != "X":
                    d[nx][ny] = d[x][y] + 1
                    q.append([nx,ny])
                    if g[nx][ny] == "P" and d[nx][ny] <= 3:
                        return False
    return True
                    
                    
    