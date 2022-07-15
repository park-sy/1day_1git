# 220715 / dfs bfs / 블록이동하기
from collections import deque
INF = 9

def get_next_pos(pos,board):
    next_pos = []
    pos = list(pos)
    a,b,c,d = pos[0][0],pos[0][1],pos[1][0],pos[1][1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        x1 = a + dx[i]
        y1 = b + dy[i]
        x2 = c + dx[i]
        y2 = d + dy[i]
        if board[x1][y1] == 0 and board[x2][y2] == 0:
            next_pos.append({(x1,y1),(x2,y2)})
    if a == c:
        for i in [-1,1]:
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                next_pos.append({(x1,y1),(x1+i,y1)})
                next_pos.append({(x2,y2),(x2+i,y2)})
    elif b == d:
        for i in [-1,1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                next_pos.append({(x1,y1),(x1,y1+i)})
                next_pos.append({(x2,y2),(x2,y2+i)})
    return next_pos

def solution(g):
    n = len(g)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = g[i][j]
    q = deque()
    visit = []
    pos = {(1,1),(1,2)}
    q.append((pos,0))
    visit.append(pos)

    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        
        for next_pos in get_next_pos(pos,new_board):
            if next_pos not in visit:
                q.append((next_pos, cost+1))
                visit.append(next_pos)
    return 0
