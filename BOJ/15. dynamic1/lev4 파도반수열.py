# 220128 / 동적계획법1 / 9461 / 파도반 수열

"""
p9 = p8 + p2
p(10) = p(9) +p4
p11 = p10 + p7
p12 = p11 + p6

"""

T = int(input())

for i in range(T):
    p = [0,1,1,1,2,2,3,4,5,7,9]
    n = int(input())
    for i in range(1,n+1):
        if i > 10:
            p.append(p[i-1]+p[i-5])

    print(p[n])