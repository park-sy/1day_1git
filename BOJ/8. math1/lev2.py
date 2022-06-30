# 211226 / 기본수학1 단계 2
# 문제번호 2292 / 별집

#1 2 3 4 5 6 7 8 9 10 19 37 61
#1 2 2 2 2 2 3 3 3 3 3 
 # 6 12 18 24
N = int(input())
n = 1
for i in range(10000):
    if N > n:
        n = n + 6*i
    if n >= N:
        print(i+1)
        break
