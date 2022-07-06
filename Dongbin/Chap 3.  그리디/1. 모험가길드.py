# 220706 / 그리디 / 모험가 길드

n = int(input())
ad = list(map(int,input().split()))

ad.sort()

res = 0
cnt = 0
for i in ad:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)