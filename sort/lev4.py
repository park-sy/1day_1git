# 220116 / 정렬 / 2018 / 통계학
import sys

arr = [0] * 8001
n = int(sys.stdin.readline())
com = []
mode = []
import math

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num+4000] += 1
m = max(arr)
for i in range(8001):
    if arr[i] == m:
        mode.append(i-4000)
    if arr[i] != 0:
        for j in range(arr[i]):
            com.append(i-4000)

print(round(sum(com)/n))
print(com[n//2])
if len(mode) == 1:
    print(mode[0])
else: print(mode[1])
print(com[-1]-com[0])

