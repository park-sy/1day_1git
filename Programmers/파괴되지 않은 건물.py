# 220907 / 파괴되지 않은 건물
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    g = [[0]*(m+1) for _ in range(n+1)]
    for type, r1, c1, r2, c2, degree in skill:
        g[r1][c1] += degree if type == 2 else -degree
        g[r1][c2 + 1] += -degree if type == 2 else degree
        g[r2 + 1][c1] += -degree if type == 2 else degree
        g[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    
    for i in range(n):
        for j in range(m):
            g[i][j+1] += g[i][j]  
            
    for j in range(m):
        for i in range(n):
            g[i+1][j] += g[i][j]
            
    for i in range(n):
        for j in range(m):
            board[i][j] += g[i][j]
            if board[i][j] > 0: answer += 1
    return answer