# 220208 / 정수론과 조합론 / 9375 / 패션왕 신해빈

n = int(input())

for i in range(n):
    t = int(input())
    c = {}
    for j in range(t):
        a,b = input().split()
        if b in c:
            c[b] += 1
        else:    
            c[b] = 1
    res = 1
    for i in c:
        res *= c[i]+1

    print(res-1)