# 211219 1차원 배열 단계 2
# 문제번호 2577 / 숫자의 개수

n = []
for i in range(3):
    n.append(int(input()))

num = n[0]*n[1]*n[2]


arr = list(map(int,list(str(num))))
count = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    for j in range(len(arr)):
        if arr[j] == i:
            count[i] += 1
    print(count[i])