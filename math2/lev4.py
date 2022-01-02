# 220102 / 기본수학 2 레벨 4
# 1929 / 소수 구하기

M, N = map(int, input().split())

for i in range(M, N+1):
    judge = False
    if i == 1:
        judge = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            judge = True
            break
    if judge == False:
        print(i)