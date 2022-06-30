# 211226 / 기본수학1 단계 4
# 문제번호 2869 / 달팽이는 올라가고 싶다

import math

A, B, V = input().split()
A = int(A)
B = int(B)
V = int(V)
a = V-A
b = A-B

if A == V:
    print(1)
elif V-A <= A - B:
    print(2)
else:
    date2 = math.ceil(a/b)+1
    print(int(date2))
