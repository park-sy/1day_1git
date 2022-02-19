# 220219 / 이분탐색 / 2805 / 나무자르기
import sys
input = sys.stdin.readline

k, n = map(int,input().split())

tree = list(map(int,input().split()))
# 457 539 743 802\
left, right = 1, max(tree)
while True:
    middle = (left + right)//2
    if left > right :
        print(middle)
        break
    res = 0
    for i in tree:
        s = i - middle
        if s > 0 :
            res += s
        if res > n:
            break
    if res >= n:
        left = middle + 1
    elif res < n:
        right = middle - 1
