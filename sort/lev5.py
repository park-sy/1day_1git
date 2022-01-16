# 220116 / 정렬 / 1427 / 소트인사이드
import sys

N = list(map(int,input()))

N.sort(reverse=True)

for i in N:
    print(i,end='')