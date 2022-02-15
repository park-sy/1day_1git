# 220205 / 그리디 알고리즘 / 11047 / 동전o

n, k = map(int, input().split())
coin = []

for i in range(n):
    coin.append(int(input()))

cnt = 0

for i in range(n-1,-1,-1):
    num = k//coin[i]
    cnt += num
    k -= num*coin[i]

print(cnt)