# 220803 / 1946 / 신입사원
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    p = []
    for _ in range(n):
        p.append(list(map(int,input().split())))
    p.sort()
    print(p)
    Max = p[0][1]
    cnt = 1
    for i in range(1,n):
        print(p[i],Max)
        if Max > p[i][1]:
            cnt += 1
            Max = p[i][1]

    print(cnt)


