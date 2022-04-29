# 220429 / 그리디알고리즘 / 1931 / 회의실 배정
import sys
input = sys.stdin.readline

n = int(input())
meet = []
for _ in range(n):
    meet.append(list(map(int,input().split())))


meet = sorted(meet,key = lambda x:x[0])
meet = sorted(meet,key = lambda x:x[1])

cnt = 0
last = 0

for i, j in meet:
    if i >=last:
        cnt+=1
        last = j
print(meet)