# 220630 / 구현 / 시각
n = int(input())
cnt = 0

for i in range(60):
    if '3' in str(i):
        cnt += 1
cnt2 = 0
for i in range(60):
    if '3' in str(i):
        cnt2 += 60
    else :cnt2 += cnt
cnt3 = 0
for i in range(n+1):
    if '3' in str(i):
        cnt3 += 60*60
    else :cnt3 += cnt2

print(cnt3)
