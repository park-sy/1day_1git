# 220808 / 크레인 인형뽑기
def solution(board, moves):
    answer = 0
    n = len(board)
    box = [-2,-1]
    def grip(a):
        k = 0
        while k < n:
            if board[k][a]:
                box.append(board[k][a])
                board[k][a] = 0
                return
            k += 1
        return
    
    for i in moves:
        grip(i-1)    
        if box[-1] == box[-2]:
            box.pop()
            box.pop()
            answer += 2

    
    
    return answer