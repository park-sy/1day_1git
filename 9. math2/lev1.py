# 211230 / 기본수학2 단계 1
# 1978 / 소수찾기
# 2 3 5 7 11 13 17 19 23
import sys
N = int(input())
data = list(map(int,sys.stdin.readline().split()))

count = 0
for i in range(N):
    jud = False    
    if data[i] == 1:
        jud = True
    else:
        for j in range(2,data[i]):
            if data[i] % j ==0:
                jud = True
                break

    if jud == False:
        count+=1

print(count)
