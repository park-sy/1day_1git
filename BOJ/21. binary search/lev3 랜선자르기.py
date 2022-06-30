# 220218 / 이분탐색 / 1654 / 랜선자르기
# 흔히 parametric search라고도 부르는, 이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 테크닉을 배우는 문제
import sys
input = sys.stdin.readline

k, n = map(int,input().split())

wire = []
for i in range(k):
    wire.append(int(input().strip()))

# 457 539 743 802\
left, right = 1, max(wire)
while True:
    middle = (left + right)//2
    if left > right :
        print(middle)
        break
    res = 0
    for i in wire:
        res+= i//middle
        if res > n:
            break
    if res >= n:
        left = middle + 1
    elif res < n:
        right = middle - 1
