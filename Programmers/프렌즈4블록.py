# 220817 / 프렌즈4블록
def solution(m, n, b):
    answer = 0
    dx = [0,0,1,1]
    dy = [0,1,0,1]
    board = []
    for i in b:
        board.append(list(map(str,i)))

    def box(a,b):
        cnt = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[a][b] == board[nx][ny] and board[nx][ny] != "0":
                cnt += 1
        if cnt == 4:
            return True
        
        else: return False
    
    def delbox(a,b):
        cnt = 0
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if board[nx][ny] != '0':
                board[nx][ny] = '0'
                cnt += 1
        return cnt
            
    def sortbox():
        for j in range(n):
            for i in range(m):
                if board[i][j] == '0':
                    k = i
                    while k > 0:
                        board[k][j],board[k-1][j] = board[k-1][j],board[k][j]
                        k -= 1
                            
    while True:
        de = []
        for i in range(m):
            for j in range(n):
                if box(i,j):
                    de.append([i,j])
        if not de:
            break
        for i,j in de:
            answer += delbox(i,j)
        sortbox()
        
    
    return answer

