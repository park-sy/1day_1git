# 220208 / 정수론과 조합론 / 11050 / 이항계수 1

a, b = map(int, input().split())
if b == 0:
    print(1)
else:
    A = a
    B = 1
    for i in range(1,b):
        a -= 1
        A *= a
        B *= i+1

    print(int(A/B))