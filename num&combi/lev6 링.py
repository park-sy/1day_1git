# 220208 / 정수론과 조합론 / 3036 / 링
def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a

n = int(input())
ring = list(map(int, input().split()))

for i in range(1,n):
    a = gcd(ring[0], ring[i])
    print("%d/%d"%(int(ring[0]/a),int(ring[i]/a)))
    