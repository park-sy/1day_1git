# 211219 1차원 배열 단계 6
# 문제번호 8958 / OX퀴즈

N = int(input())
result = []
for i in range(N):
    arr = list(input())
    sum = 0
    score = 0
    for j in range(len(arr)):
        if arr[j] == "O":
            score = score + 1
            sum = sum + score
        else: score = 0
    result.append(sum)

for i in range(N):
    print(result[i])
