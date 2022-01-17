# 220117 /정렬 / 11650 / 좌표 정렬하기 
import sys
N = int(sys.stdin.readline())

loc1 = []

for i in range(N):
    [a,b] = map(int, sys.stdin.readline().split())
    loc1.append([a, b])

loc = sorted(loc1, key=lambda x:(x[0], x[1]))

for i in range(N):
    print(loc[i][0], loc[i][1])