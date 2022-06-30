# 220630 / 구현 / 왕실의 나이트

n = input()
dx = [1,-1,2,-2,1,-1,2,-2]
dy = [2,-2,1,-1,-2,2,-1,1]

a,b = ord(n[0]) - ord('a')+1 ,int(n[1])
cnt = 0
for i in range(8):
    x = a + dx[i]
    y = b + dy[i]
    if 1<=x<=8 and 1<=y<=8:
        cnt += 1

print(cnt)
