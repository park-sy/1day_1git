# 220818 / 경주로건설
from collections import deque
def solution(board):
    n = len(board)

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    
    def bfs(start):
        q = deque([start])
        visit = [[1e9]*n for _ in range(n)]
        visit[0][0] = 0
        while q:
            x,y,c,d= q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                    nc = c + 100
                    if d != i:
                        nc += 500

                    if visit[nx][ny] >= nc:
                        visit[nx][ny] = nc
                        q.append([nx,ny,nc,i])
        return visit[-1][-1]


    return min(bfs([0,0,0,0]), bfs([0,0,0,2]))