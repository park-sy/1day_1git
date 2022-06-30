# 220630 / 그리디 / 1이 될 때까지

n,m = map(int,input().split())

cnt = 0 

while n > 1:
    k = n % m
    if k == 0:
        n //= m
        cnt += 1
    else: 
        n -= k
        cnt += k

if n == 0:
    cnt += 1
print(cnt)