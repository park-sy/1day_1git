# 220706 / 그리디 / 만들 수 없는 금액

n = int(input())
coin = list(map(int,input().split()))

coin.sort()

target = 1

for i in coin:
    if target < i:
        break
    target += i

print(target)