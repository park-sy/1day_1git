# 220428 / 분할정복 / 1629 / 곱셈

a,b,c = map(int,input().split())

def dimul(n,d):
    if d == 1:
        return n%c
    
    tmp = dimul(n,d//2)
    if d % 2 == 0:
        return tmp * tmp % c
    else:
        return tmp * tmp * n % c

print(dimul(a,b))