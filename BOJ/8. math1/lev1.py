# 211222 / 기본수학1 단계 1
# 문제번호 1712 / 손익분기점

A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
    

if B - C >= 0:
    print(-1)
else:
    bre = A/(C-B)
    print(int(bre)+1)
