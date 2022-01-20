# 220120 / 정렬 / 10814 / 나이순 정렬
import sys
input = sys.stdin.readline

N = int(input())
reg = []
for i in range(N):
    a, b = input().split()
    reg.append([int(a), i, b])

reg2 = sorted(reg, key=lambda x:(x[0], x[1]))

for i in range(N):
    print(reg2[i][0], reg2[i][2])