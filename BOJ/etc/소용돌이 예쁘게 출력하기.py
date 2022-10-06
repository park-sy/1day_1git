# 221006 / 소용돌이 예쁘게 출력하기

r1,c1,r2,c2 = map(int,input().split())

g = [[0]* (c2-c1+1) for _ in range(r2-r1+1)]

total = (c2-c1+1)*(r2-r1+1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x,y = 0,0
cnt = 1
m = 0
id = 1
d = 1
while total > 0:
    for i in range(2):
        for j in range(id):
            if r1 <= x <= r2 and c1 <= y <= c2:
                g[x-r1][y-c1] = cnt
                total -= 1
                m = cnt
            x += dx[d]
            y += dy[d]
            cnt += 1
        d = (d-1) % 4
    id += 1
        

ml = len(str(m))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        # tl = len(str(g[i][j]))
        # print(" "*(ml-tl), end = '')
        # print(g[i][j], end = ' ')
        print(str(g[i][j]).rjust(ml), end=" ")
    print()

