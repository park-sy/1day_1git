# 220116 / 정렬 / 10989 / 수 정렬하기 3 / 카운팅 정렬


n = int(input())
num = []

oarr = []
for i in range(n):
    num.append(int(input()))
    oarr.append(-1)

carr = [0]*(max(num)+1)

for i in num:
    carr[i] += 1

for i in range(1,len(carr)):
    carr[i] += carr[i-1]

for i in num:
    oarr[carr[i]-1] = i
    carr[i] -= 1

for i in oarr:
    print(i)