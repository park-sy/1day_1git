# 220215 / 분할정복 / 11401 / 이항계수3
# 분할 정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제



def power(a,b):
    if b == 1:
        return a

    else:
        temp = power(a,b//2)
        if b % 2 == 0:
            return temp * temp % p
        else:
            return temp * temp * a % p

p = 1000000007

a, b = map(int,input().split())

n, k = map(int,input().split())

factorial = [1]*n

for i in range(1,n+1):
    factorial[i] = factorial[i-1]*i % p

A = factorial[n]
B = (factorial[n-k]*factorial[k]) % p
print((A%p)*(power(B,p-2)%p)%p)