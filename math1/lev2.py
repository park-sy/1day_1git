# 211226 / 기본수학1 단계 2
# 문제번호 2292 / 별집

#1 7 19 37 61
 # 6 12 18 24
N = int(input())
n = 1
for i in range(10000):
    if N > n:
        n = n + 6*i
    if n >= N:
        print(i+1)
        break
