#220113 / 브루트포스 / 1018 / 체스판 다시 칠하기

def check(word, W):
    count = 0
    for i in range(8):
        if word[i] != W[i] :
            count+=1

    return count

row, column = map(int, input().split())
board = []
for i in range(row):
    board.append(input())

W = 'WBWBWBWB'
B = 'BWBWBWBW'
sum = []

for i in range(row-7):
    for j in range(column-7):
        sumw = 0
        sumb = 0
        for i1 in range(8):
            if i1 % 2 == 0:
                sumw += check(board[i+i1][j:j+8],W)
                sumb += check(board[i+i1][j:j+8],B)
            else:
                sumw += check(board[i+i1][j:j+8],B)
                sumb += check(board[i+i1][j:j+8],W)
        sum.append(min(sumw,sumb))

print(min(sum))

