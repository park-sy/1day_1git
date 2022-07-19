# 220719 / 이진탐색 / 두 배열의 합
import sys, bisect
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

suba,subb = [], []
for i in range(n):
    temp = A[i]
    suba.append(temp)
    for j in range(i+1,n):
        temp += A[j]
        suba.append(temp)

for i in range(m):
    temp = B[i]
    subb.append(temp)
    for j in range(i+1,m):
        temp += B[j]
        subb.append(temp)
     
suba.sort()
subb.sort()

cnt = 0
for i in suba:
    l = bisect.bisect_left(subb, T-i)
    r = bisect.bisect_right(subb, T-i)
    cnt += r - l
print(cnt)




