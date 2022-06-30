# 220630 / 구현 / 상하좌우
n = int(input())
q = list(map(str, input().split()))

d ={'L':[0,-1], 'R':[0,1], 'U': [-1,0], 'D':[1,0]}
x,y = 1,1

for i in q:
    query = d[i]
    dx = x + query[0]
    dy = y + query[1]
    if 1 <= dx <n and 1 <= dy < n:
        x = dx
        y = dy

print(x,y)
