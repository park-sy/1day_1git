# 220830 / 카드 짝 맞추기
from collections import deque
from itertools import permutations
from copy import deepcopy

def solution(board, r, c):
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    global answer
    answer = 10000
    g = [[] for _ in range(7)]
    cards = []
    for i in range(4):
        for j in range(4):
            card = board[i][j]
            if card:
                g[card].append([i,j])
                if card not in cards:
                    cards.append(card)
                
    def bfs(board,start,end):
        x,y = start
        tx,ty = end
        if start == end:
            return 0
        visit = [[0]*4 for _ in range(4)] 
        q = deque([[x,y,0]])
        while q:
            a,b,w = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                cx = a + dx[i]
                cy = b + dy[i]

                while 0 <= cx < 4 and 0 <= cy < 4:
                    if board[cx][cy] :
                        break
                    cx += dx[i]
                    cy += dy[i]
                if not 0 <= cx < 4 or not 0 <= cy < 4:
                    cx -= dx[i]
                    cy -= dy[i]
                if [nx,ny] == [tx,ty] or [cx,cy] == [tx,ty]:
                    return w + 1
                if 0 <= nx < 4 and 0 <= ny < 4 and not visit[nx][ny]:
                    q.append([nx,ny,w+1])
                    visit[nx][ny] = 1
                if not visit[cx][cy]:
                    q.append([cx,cy,w+1])
                    visit[cx][cy] = 1

        return visit[tx][ty]            
    
    def dfs(board,start,now,res):
        global answer
        if now == lc:
            answer = min(answer,res)
            return
        nx,ny = start
        k = t[now]
        
        res1 = (bfs(board,[nx,ny],g[k][0])+ bfs(board,g[k][0],g[k][1])) + 2
        res2 = (bfs(board,[nx,ny],g[k][1])+ bfs(board,g[k][1],g[k][0])) + 2

        a,b = g[k][0]
        c,d = g[k][1]
        nb = deepcopy(board)
        nb[a][b] = 0
        nb[c][d] = 0
        if res1 < res2:
            dfs(nb,g[k][1],now+1,res+res1)
        else:
            dfs(nb,g[k][0],now+1,res+res2)
        
    lc = len(cards)
    for t in permutations(cards):
        dfs(board,[r,c],0,0)

    return answer
  