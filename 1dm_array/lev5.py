# 211219 1차원 배열 단계 4
# 문제번호 1546 / 평균
import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr2 = []
sum = 0
for i in range(N):
    arr2.append(arr[i]/max(arr)*100)
    sum = sum +arr2[i]

print(sum/N)



