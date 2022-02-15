# 211219 1차원 배열 단계 4
# 문제번호 3052 / 나머지

arr = []
arr2 = []
for i in range(10):
    arr.append(int(input()))
    arr2.append(arr[i]%42)

print(len(set(arr2)))
