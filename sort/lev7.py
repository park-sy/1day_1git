# 220119 / 정렬 / 11651 / 좌표정렬하기2
import sys
input = sys.stdin.readline
N = int(input())
loc = []
for i in range(N):
    [a, b] = map(int, input().split())
    loc.append([a, b])

loct = sorted(loc, key= lambda x: (x[1], x[0]))

for i in range(N):
    print(loct[i][0], loct[i][1])