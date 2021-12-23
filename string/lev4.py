# 211222 / 문자열 단계 4
# 문제번호 2675 / 문자열 반복

num = int(input())
for i in range(num):
    N, P = input().split()
    for j in P:
         print(j*int(N),end='')
    print("")