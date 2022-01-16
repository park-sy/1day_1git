# 220115 / 정렬/ 2750 / 수정렬하기

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
num2 = num
temp = 0
for i in range(N):
    for j in range(N-1):
        if num[j] > num[j+1]:
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp

for i in range(N):
    print(num[i])