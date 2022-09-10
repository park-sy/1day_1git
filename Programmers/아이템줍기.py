# 220910 / 아이템줍기
from collections import deque
dx = [0,0,1,-1]
dy = [-1,1,0,0]
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    cx = characterX*2
    cy = characterY* 2
    ex = itemX*2
    ey = itemY*2
    
    g = [[0]*101 for _ in range(101)]
    
    for ax,ay,bx,by in rectangle:
        for i in range(ax*2,bx*2+1):
            for j in range(ay*2,by*2+1):
                g[i][j] = 1
    
    for ax,ay,bx,by in rectangle:
        for i in range(ax*2+1,bx*2):
            for j in range(ay*2+1,by*2):
                g[i][j] = 0
    

    q = deque()
    q.append((cx,cy,0))
    visit = [[0]*101 for _ in range(101)]
    visit[cx][cy] = 1
    while q:
        x,y,d = q.popleft()
        if (x,y) == (ex,ey):
            answer = d
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if g[nx][ny] and not visit[nx][ny]:
                q.append((nx,ny,d+1))
                visit[nx][ny] = 1            
        
    return answer//2


        
        