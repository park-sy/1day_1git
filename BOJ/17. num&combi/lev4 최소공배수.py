# 220207 / 정수론과 조합론 / 1934 / 최소공배수

n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    A,B = a,b
    while A > 0:
        A, B = B%A, A

    print(int(a*b/B))
