# 211226 / 기본수학1 단계 3
# 문제번호 1193 / 분수찾기
# [1/1], [2/1, 1/2], [3/1, 2/2, 1/3]


X = int(input())
count = 0
k = 1
for i,j in zip(range(1,k),range(k,1,-1)):
    print(i,j)
    k = k+1
for i in range(X):
    print(i)