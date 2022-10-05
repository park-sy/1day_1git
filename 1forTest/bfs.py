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


    # 220828 / 동굴 탐험
from collections import deque

def solution(n, path, order):

    g = [[] for _ in range(n)]
    for a,b in path:
        g[a].append(b)
        g[b].append(a)
    
    visit = [0] *(n)
    pre = [0] * n
    for a,b in order:
        pre[b] = a
    q = deque([0])
    after = {}
    cnt = 0
    while q:
        now = q.popleft()
        
        if pre[now] and not visit[pre[now]]:
            after[pre[now]] = now
            continue
        visit[now] = 1
        cnt += 1
        
        for next in g[now]:
            if not visit[next]:
                q.append(next)
                
        if now in after:
            q.append(after[now])
            
    return n == cnt


# 블록이동하기

from collections import deque
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def solution(board):
    n = len(board)
    new_board = [[1]*(n+2)]
    for i in board:
        new_board.append([1]+i+[1])
    new_board.append([1]*(n+2))
    

    q = deque()
    pos = {(1,1),(1,2)}
    q.append((pos,0))
    visit = []
    while q:
        pos,w = q.popleft()
        if (n,n) in pos:
            return w
        
        for next_pos in get_next(new_board,pos):
            if next_pos not in visit:
                visit.append(next_pos)
                q.append((next_pos,w+1))           
    return 0

def get_next(board, pos):
    
    arr = []
    pos = list(pos)
    ax,ay,bx,by = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    
    for i in range(4):
        nax = ax + dx[i]
        nay = ay + dy[i]
        nbx = bx + dx[i]
        nby = by + dy[i]
    
        if not board[nax][nay] and not board[nbx][nby]: 
            arr.append({(nax,nay),(nbx,nby)})
    
    if ax == bx:
        for i in [-1,1]:
            if not board[ax+i][ay] and not board[bx+i][by]:
                arr.append({(ax,ay),(ax+i,ay)})
                arr.append({(bx+i,by),(bx,by)})
    else:
        for i in [-1,1]:
            if not board[ax][ay+i] and not board[bx][by+i]:
                arr.append({(ax,ay),(bx,by+i)})
                arr.append({(ax,ay+i),(bx,by)})
            
    return arr