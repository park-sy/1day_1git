# 220117 /정렬 / 11650 / 좌표 정렬하기 

N = int(input())

loc1 = []

for i in range(N):
    [a,b] = map(int, input().split())
    loc1.append([a, b])

for i in range(N):
    print(loc1[i][0], loc1[i][1])