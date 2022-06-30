# 220506 / 분할정복 / 11401 / 이항계수3
n,k = map(int,input().split())
p = 1000000007

def power(a,b):
    if b == 1:
        return a
    temp = power(a,b//2)
    if b % 2 == 0:
        return temp * temp % p
    else:
        return temp * temp * a % p


fac = [1]*(n+1)
for i in range(1,n+1):
    fac[i] = fac[i-1]*n%p

a = fac[i]
b = (fac[n-k]*fac[k]) % p
print((a%p)*(power(b,p-2)%p)%p)

