# 211228 / 기본수학1 단계 7
# 2839 / 설탕배달

N = int(input())
if N >= 5:
    num =int(N / 5) 
    count = 0
    for i in range(num,-1,-1):
        if (N - 5*i)%3 == 0:
            count = i +(N - 5*i)/3
            break
elif N == 3:
    count = 1         
else: count = -1
if int(count) == 0:
    print(-1)
else:
    print(int(count))
