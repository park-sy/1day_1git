# 220207 / 정수론과 조합론 / 2609 / 최대공약수와 최소공배수

a, b = map(int, input().split())

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a


if a > b:
    g = gcd(a,b)
else:
    g = gcd(b,a)

print(g)
print(int(a*b/g))