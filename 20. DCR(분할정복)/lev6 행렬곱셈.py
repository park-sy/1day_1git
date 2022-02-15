# 220215 / 분할정복 / 2740 / 행렬곱셈
import sys
input = sys.stdin.readline

m1, m2, m = [],[],[]
a1, a2 = map(int, input().split())

for i in range(a1):
    m1.append(list(map(int,input().split())))

b1, b2 = map(int, input().split())
for i in range(b1):
    m2.append(list(map(int,input().split())))

for i in range(a1):
    row = []
    for j in range(b2):
        rst = 0
        for k in range(b1):
            rst += m1[i][k]*m2[k][j]

        row.append(rst)
    m.append(row)

for i in range(a1):
    print(*m[i])