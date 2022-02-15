#220113 / 브루트포스 / 7568 / 덩치

N = int(input())
reg = []
for i in range(N):
    kg, cm = map(int, input().split())
    reg.append([kg, cm, 1])

for i in range(N):
    for j in range(N):
        if reg[i][0] < reg[j][0] and reg[i][1] < reg[j][1]:
            reg[i][2] += 1

for i in range(N):
    print(reg[i][2], end=' ')
