# 220130 / 동적계획법1 / 1463 / 1로 만들기

"""
48
11 0000
 32168421
2 1
3 1
4 2 1 / 4 3 1
5 4 3 1 / 5 4 2 1
28 14 

"""
n = int(input())

arr = [0 for i in range(n+1)]

for i in range(2,n+1):
    arr[i] = arr[i-1]+1
    if i == 2:
        arr[i] = 1
    if i % 3 ==0:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2] + 1)

print(arr[n])