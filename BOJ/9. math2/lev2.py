#211231 / 기본수학2 단계 2
# 2581 / 소수

M = int(input())
N = int(input())
data = []
for i in range(M, N+1):
    jud = False
    if i == 1:
        jud = True
    else:
        for j in range(2, i):
            if i % j == 0:
                jud = True
                break
    if jud == False:
        data.append(i)
    
if not data:
    print(-1)
else:
    print(sum(data))
    print(min(data))


