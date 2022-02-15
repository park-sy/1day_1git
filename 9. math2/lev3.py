# 220101 / 기본수학2 단계 3
# 11653 / 소인수분해

N = int(input())

value = N
if N == 1:
    pass
else:
    while value > 1:
        for i in range(2,value+1):
            if value % i == 0:
                value =int(value / i)
                print(i)
                break
