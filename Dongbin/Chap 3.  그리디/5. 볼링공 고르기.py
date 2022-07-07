# 220707 / 그리디 / 볼링공 고르기

n,m = map(int,input().split())
ball = list(map(int,input().split()))

bcnt = [0]*(m+1)

for i in range(n):
    bcnt[ball[i]] += 1
cnt = 0

for i in range(1,m+1):
    n -= bcnt[i]
    cnt += bcnt[i]*n
print(cnt)
