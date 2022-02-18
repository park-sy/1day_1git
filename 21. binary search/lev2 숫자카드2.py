# 220218 / 이분탐색 / 10816 / 숫자카드2
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
ad = {}
for i in A:
    if i not in ad:
        ad[i] = 1
    else:
        ad[i] += 1

A = list(set(A))
A.sort()
# -10 -10 2 3 3 6 10 10 10
for i in B:
    left, right = 0, len(A)-1
    while True:
        middle = (left + right)//2
        if left > right:
            print(0, end=' ')
            break
        if i == A[middle]:
            print(ad[i], end=' ')
            break
        elif i < A[middle]:
            right = middle -1 
        else: left = middle +1