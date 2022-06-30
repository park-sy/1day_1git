# 211219 1차원 배열 단계 2
# 문제번호 2562 / 최대값

a = []
for i in range(9):
    a.append(int(input()))

n = 1
for i in range(9):
    if a[i] == max(a):
        print(a[i])
        print(n)
    else: n = n + 1