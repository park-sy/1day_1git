# 220218 / 이분탐색 / 1920 / 수찾기
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
B = list(map(int, input().split()))

# 1 2 3 4 5
for i in B:
    left, right = 0, n-1, 
    while True:
        middle = (left + right)//2
        if left > right:
            print(0)
            break
        if i == A[middle]:
            print(1)
            break
        elif i < A[middle]:
            right = middle -1 
        else: left = middle +1