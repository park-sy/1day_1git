# 211228 / 기본수학1 단계 5
# 문제번호 10250 / 부녀회장이 될테야


import math
T = int(input())

for i in range(T):
    H, W, N = input().split()
    H = int(H)
    W = int(W)
    N = int(N)
    if N % H == 0:
        floor = H
    else:
        floor = N % H
    line = math.ceil(N / H)

    if line < 10:
        print(floor, 0, line, sep='')
    else:
        print(floor, line, sep='')

