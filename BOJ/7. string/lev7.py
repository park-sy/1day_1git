# 211223 / 문자열 단계 7
# 문제번호 2608 / 상수

num1, num2 = input().split()
num11 = int(num1[::-1])
num22 = int(num2[::-1])
if num11 > num22:
    print(num11)
else:
    print(num22)
